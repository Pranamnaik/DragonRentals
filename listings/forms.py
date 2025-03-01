from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'title', 'description', 'property_type', 'location', 
            'rent', 'deposit', 'distance_to_noodle_shop', 
            'available_from', 'image'
        ]
        widgets = {
            'available_from': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class PropertySearchForm(forms.Form):
    title = forms.CharField(required=False)
    location = forms.CharField(required=False)
    property_type = forms.ChoiceField(choices=Property.PROPERTY_TYPES, required=False)
    min_rent = forms.DecimalField(required=False, min_value=0)
    max_rent = forms.DecimalField(required=False, min_value=0)
    available_from = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
