from django import forms
from .models import WheelSpecification, BogieChecksheet

class WheelSpecificationForm(forms.ModelForm):
    class Meta:
        model = WheelSpecification
        fields = '__all__'

class BogieChecksheetForm(forms.ModelForm):
    # other_bogie_condition = forms.CharField(required=False, label="Specify Other (Bogie Field Condition)")
    class Meta:
        model = BogieChecksheet
        fields = '__all__'
