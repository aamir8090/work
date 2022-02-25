from .models import advrt
from django import forms


class advrtForm(forms.ModelForm):
    class Meta:
        model = advrt

        fields = ['description', 'distance', 'Categories', 'till_date', 'remark', 'address']
