from django.urls import path
from .views import bogie_checksheet_list,create_bogie_checksheet,delete_bogie_checksheet,update_bogie_checksheet

urlpatterns = [
    # path('wheel-specifications', WheelSpecificationFormCreateView.as_view(), name='wheel-specifications'),
    path('bogie-checksheet', bogie_checksheet_list, name='list'),
    path('bogie-checksheet/create', create_bogie_checksheet, name='create'),
    path('bogie-checksheet/<int:pk>',update_bogie_checksheet,name="update"),
    path('bogie-checksheet/<int:pk>', delete_bogie_checksheet, name='delete'),  
    
]
# path('bogie-checksheet', BogieChecksheetFormCreateView.as_view(), name='bogie-checksheet'),
    