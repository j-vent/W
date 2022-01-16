from socket import fromshare

from django import forms 

FILTER_CHOICES =[('Food provided', 'Food provided'), 
('LGBTQ2S+ friendly', 'LGBTQ2S+ friendly'), 
('Public transit accessible', 'Public transit accessible'), 
('Showers provided', 'Showers provided'), 
('Women only', 'Women only'),]


class FilterForms(forms.Form):
    filters = forms.MultipleChoiceField(
        required=False, 
        widget = forms.CheckboxSelectMultiple, 
        choices = FILTER_CHOICES,
    )