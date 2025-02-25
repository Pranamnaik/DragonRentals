from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Property
from .forms import PropertySearchForm

from .forms import PropertyForm

def home(request):
    search_form = PropertySearchForm(request.GET or None)
    properties = Property.objects.all()

    if search_form.is_valid():
        title = search_form.cleaned_data.get('title')
        location = search_form.cleaned_data.get('location')
        property_type = search_form.cleaned_data.get('property_type')
        min_rent = search_form.cleaned_data.get('min_rent')
        max_rent = search_form.cleaned_data.get('max_rent')
        available_from = search_form.cleaned_data.get('available_from')

        if title:
            properties = properties.filter(title__icontains=title)
        if location:
            properties = properties.filter(location__icontains=location)
        if property_type:
            properties = properties.filter(property_type=property_type)
        if min_rent:
            properties = properties.filter(rent__gte=min_rent)
        if max_rent:
            properties = properties.filter(rent__lte=max_rent)
        if available_from:
            properties = properties.filter(available_from__gte=available_from)

    properties = properties.order_by('-created_at')[:5]

    return render(request, 'home.html', {'properties': properties, 'search_form': search_form})


@login_required
def create_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.landlord = request.user
            property.save()
            return redirect('home')
    else:
        form = PropertyForm()
    return render(request, 'listings/create_property.html', {'form': form})

@login_required
def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'listings/property_detail.html', {'property': property})

@login_required
def edit_property(request, pk):
    property = get_object_or_404(Property, pk=pk, landlord=request.user)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property_detail', pk=property.pk)
    else:
        form = PropertyForm(instance=property)
    return render(request, 'listings/edit_property.html', {'form': form})

@login_required
def delete_property(request, pk):
    property = get_object_or_404(Property, pk=pk, landlord=request.user)
    if request.method == 'POST':
        property.delete()
        return redirect('home')
    return render(request, 'listings/confirm_delete.html', {'property': property})
