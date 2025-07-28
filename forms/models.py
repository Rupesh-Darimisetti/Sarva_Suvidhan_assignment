from django.db import models
from django.contrib.postgres.fields import JSONField

class WheelSpecificationForm(models.Model):
    # formNumber= models.TextField(max_length=100, unique=True, name="Form Number")
    # submittedBy= models.TextField(max_length=100, name="Submitted By")
    # submittedDate= models.DateField(auto_created=True,auto_now_add=True)
    treadDiameterNew= models.TextField(max_length=100, name="Tread Diameter (New)")
    lastShopIssueSize= models.TextField(max_length=100, name="Last Shop Issue Size")
    condemningDia= models.TextField(max_length=100, name="Condemning Dia.")
    wheelGauge= models.TextField(max_length=100, name="Wheel Gauge")
    variationSameAxle= models.IntegerField(default=5, name="Variation Same Axle")
    variationSameBogie= models.IntegerField(default=10, name="Variation Same Bogie")
    variationSameCoach= models.IntegerField(default=15, name="Variation Same Coach")
    wheelProfile= models.TextField(max_length=100, name="Wheel Profile")
    intermediateWWP= models.TextField(max_length=100, name="Intermediate WWP")
    bearingSeatDiameter= models.TextField(max_length=100, name="Bearing Seat Diameter")
    rollerBearingOuterDia= models.TextField
    rollerBearingBoreDia= models.CharField(max_length=100, name="Roller Bearing Bore Dia.")
    rollerBearingWidth= models.TextField(max_length=100, name="Roller Bearing Width")
    axleBoxHousingBoreDia= models.TextField(max_length=100, name="Axle Box Housing Bore Dia.")
    wheelDiscWidth= models.TextField(max_length=100, name="Wheel Disc Width")
            
    # threadDiameter = models.TextField(max_length=100, name="Thread Diameter (New)")
    # lastShopIssueSize = models.TextField(max_length=100, name="Last Shop Issue Size")
    # condemningDia = models.TextField(max_length=100, name="Condemning Dia.")
    # permissibleVariation = models.TextField(max_length=100, name="Permissible Variation")
    # formNumber = models.CharField(max_length=100, unique=True)
    # submittedBy = models.CharField(max_length=100)
    # submittedDate = models.DateField()
    # fields = models.JSONField()

    def __str__(self):
        return self.formNumber

class BogieChecksheetForm(models.Model):
    BogieNumber = models.CharField(max_length=100, unique="Truename=Bogie No")
    MakerYearBuilt = models.CharField(max_length=100, name="Malker & Year Built")
    IncomingDivDate = models.DateField(name="Incoming Div. & Date")
    DeflictOfComponents = models.JSONField( name="Deflict of Components (if any)")
    DateofIOH = models.DateField(name="Date of IOH")
    inspectionBy = models.CharField(max_length=100)
    inspectionDate = models.DateField()
    bogieDetails = models.JSONField()
    bogieChecksheet = models.JSONField()
    bmbcChecksheet = models.JSONField()

    def __str__(self):
        return self.formNumber
