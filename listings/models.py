from django.db import models
from django.core.validators import MinValueValidator
from accounts.models import CustomUser

class Property(models.Model):
    PROPERTY_TYPES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('dojo', 'Dojo'),
        ('shop', 'Shop'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    location = models.CharField(max_length=200)
    rent = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    deposit = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    distance_to_noodle_shop = models.DecimalField(max_digits=5, decimal_places=2, help_text="Distance in km")
    available_from = models.DateField()
    landlord = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='properties')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.get_property_type_display()}"

    class Meta:
        verbose_name_plural = "Properties"
        ordering = ['-created_at']
