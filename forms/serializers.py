from rest_framework import serializers
from .models import WheelSpecificationForm, BogieChecksheetForm

class WheelSpecificationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelSpecificationForm
        fields = '__all__'

class BogieChecksheetFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieChecksheetForm
        fields = '__all__'
