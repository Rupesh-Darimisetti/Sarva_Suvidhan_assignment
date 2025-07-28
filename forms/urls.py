from django.urls import path
from .views import WheelSpecificationFormCreateView, BogieChecksheetFormCreateView

urlpatterns = [
    path('wheel-specifications', WheelSpecificationFormCreateView.as_view(), name='wheel-specifications'),
    path('bogie-checksheet', BogieChecksheetFormCreateView.as_view(), name='bogie-checksheet'),
]
