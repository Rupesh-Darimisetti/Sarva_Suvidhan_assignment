from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import BogieChecksheet, BogieChecksheet
from .forms import BogieChecksheetForm, WheelSpecificationForm
# from rest_framework.filters import SearchFilter
# from django_filters.rest_framework import DjangoFilterBackend

# class WheelSpecificationFormCreateView(generics.ListCreateAPIView):
#     queryset = WheelSpecificationForm.objects.all()
#     serializer_class = WheelSpecificationForm
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['formNumber', 'submittedBy', 'submittedDate']

# class BogieChecksheetFormCreateView(generics.CreateAPIView):
#     queryset = BogieChecksheetForm.objects.all()
#     serializer_class = BogieChecksheetForm
# @api_view(['POST'])
# def create_bogie_checksheet(request):
#     serializer = BogieChecksheetSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def create_bogie_checksheet(request):
    if request.method == 'POST':
        form = BogieChecksheetForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            form = BogieChecksheetForm()
        return render(request,'create.html',{'form':form})
    
# list view
def bogie_checksheet_list(request):
    bogie_checksheet = BogieChecksheet.objects.all()
    return render(request,'list.html',{'bogie_checksheet':bogie_checksheet})

# update view
def update_bogie_checksheet(request,pk):
    bogie_checksheet = BogieChecksheet.get(id=pk)
    if(request.method == 'POST'):
        form = BogieChecksheetForm(request.POST,instance=bogie_checksheet)
        
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = BogieChecksheetForm(instance = bogie_checksheet)
    return render(request,'update.html',{'form':form})

# delete view
def delete_bogie_checksheet(request,pk):
    bogie_checksheet = BogieChecksheet.objects.get(id=pk)
    if request.method == "POST":
        bogie_checksheet.delete()
        return redirect('list')