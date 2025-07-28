from django import forms
from .models import WheelSpecification, BogieChecksheet

class WheelSpecificationForm(forms.ModelForm):
    class Meta:
        model = WheelSpecification
        fields = '__all__'

class BogieChecksheetForm(forms.ModelForm):
    # other_bogie_condition = forms.CharField(required=False, label="Specify Other (Bogie Field Condition)")
    # DateofIOH = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = BogieChecksheet
        fields = '__all__'
        widgets = {
            'IncomingDivDate': forms.SelectDateWidget(),
            'DateofIOH':forms.SelectDateWidget()
        }
