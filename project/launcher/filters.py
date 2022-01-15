from cgitb import lookup
from django import forms
from django.contrib.auth.models import User, Group
from .models import Housing
import django_filters

class HousingFilter(django_filters.FilterSet):
    # first_name = django_filters.CharFilter(lookup_expr='icontains')
    # year_joined = django_filters.NumberFilter(name='date_joined', lookup_expr='year')
    # groups = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all(),
    #     widget=forms.CheckboxSelectMultiple)
    
    
    organization = django_filters.CharFilter(lookup_expr='icontains')
    # distance = django_filters.RangeFilter()
    # class Meta:
    #     model = User
    #     fields = ['username', 'first_name', 'last_name', 'year_joined', 'groups']