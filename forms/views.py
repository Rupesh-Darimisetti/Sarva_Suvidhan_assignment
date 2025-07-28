from rest_framework import generics
from .models import WheelSpecificationForm, BogieChecksheetForm
from .serializers import WheelSpecificationFormSerializer, BogieChecksheetFormSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

class WheelSpecificationFormCreateView(generics.ListCreateAPIView):
    queryset = WheelSpecificationForm.objects.all()
    serializer_class = WheelSpecificationFormSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['formNumber', 'submittedBy', 'submittedDate']

class BogieChecksheetFormCreateView(generics.CreateAPIView):
    queryset = BogieChecksheetForm.objects.all()
    serializer_class = BogieChecksheetFormSerializer
