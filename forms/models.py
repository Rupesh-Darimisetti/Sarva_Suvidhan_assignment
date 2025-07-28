from django.db import models

class WheelSpecification(models.Model):
    # formNumber= models.TextField(max_length=100, unique=True, name="Form Number")
    # submittedBy= models.TextField(max_length=100, name="Submitted By")
    # submittedDate= models.DateField(auto_created=True,auto_now_add=True)
    treadDiameterNew= models.CharField(max_length=100, name="Tread Diameter (New)")
    lastShopIssueSize= models.CharField(max_length=100, name="Last Shop Issue Size")
    condemningDia= models.CharField(max_length=100, name="Condemning Dia.")
    wheelGauge= models.CharField(max_length=100, name="Wheel Gauge")
    variationSameAxle= models.IntegerField(default=5, name="Variation Same Axle")
    variationSameBogie= models.IntegerField(default=10, name="Variation Same Bogie")
    variationSameCoach= models.IntegerField(default=15, name="Variation Same Coach")
    wheelProfile= models.CharField(max_length=100, name="Wheel Profile")
    intermediateWWP= models.CharField(max_length=100, name="Intermediate WWP")
    bearingSeatDiameter= models.CharField(max_length=100, name="Bearing Seat Diameter")
    rollerBearingOuterDia= models.CharField(max_length=100,name="Roller Bearing Diameter")
    rollerBearingBoreDia= models.CharField(max_length=100, name="Roller Bearing Bore Dia.")
    rollerBearingWidth= models.TextField(max_length=100, name="Roller Bearing Width")
    axleBoxHousingBoreDia= models.TextField(max_length=100, name="Axle Box Housing Bore Dia.")
    wheelDiscWidth= models.TextField(max_length=100, name="Wheel Disc Width")

    def __str__(self):
        return self.treadDiameterNew

class BogieChecksheet(models.Model):
    BogieFieldCodition = [
        ('Overaged', 'Overaged'),
        ('Cracked', 'Cracked'),
        ('Worn  out', 'Worn out'),
        ('Good', 'Good'),
        ('OtherBogieField', 'Other'),
    ]
    BlasterChoices = [
        ('Cracked', 'Cracked'),
        ('Worn  out', 'Worn out'),
        ('Good', 'Good'),
        ('otherBlaster', 'Other'),
    ]
    # id = models.CharField(max_length=20,primary_key=True, auto_created=True)
    bogie_number = models.CharField(max_length=100, unique="Truename=Bogie No")
    maker_year_built = models.CharField(max_length=100)
    incoming_div_date = models.DateField()
    deflict_of_components = models.JSONField( )
    date_of_IOH = models.DateField()
    bogie_field_codition= models.CharField(max_length=100, choices=BogieFieldCodition, default='Good'    )
    blaster = models.CharField(max_length=100,choices=BlasterChoices, default='Good')
    blaster_suspension_bracket = models.CharField(max_length=100, choices=BlasterChoices, default='Good')
    lower_spring_seat = models.CharField(max_length=100, choices=BlasterChoices, default='Good')
    axle_guide = models.CharField(max_length=100,  choices=BlasterChoices, default='Good')
    axle_guide_assembly = models.CharField(max_length=100, choices=BlasterChoices, default='Good')
    protective_tubes = models.CharField(max_length=100, choices=BlasterChoices, default='Good')
    anchor_link = models.CharField(max_length=100,  choices=BlasterChoices, default='Good')
    side_bearer = models.CharField(max_length=100,  choices=BlasterChoices, default='Good')
    BMBCChecksheetChoices = [
        ('Good', 'Good'),
        ('Worn out', 'Worn out'),
        ('Damaged', 'Damaged'),
        ('OtherBMBCChecksheet', 'Other'),
    ]
    cylinder_body_dome_cover = models.CharField(max_length=100,  choices=BMBCChecksheetChoices, default='Good')
    piston_trunnion_body = models.CharField(max_length=100,  choices=BMBCChecksheetChoices, default='Good')
    adjusting_tubeand_screw = models.CharField(max_length=100, choices=BMBCChecksheetChoices, default='Good')
    plunger_spring = models.CharField(max_length=100,  choices=BMBCChecksheetChoices, default='Good')
    tree_bolt_hexNut = models.CharField(max_length=100,  choices=BMBCChecksheetChoices, default='Good')
    pawl_pawl_spring = models.CharField(max_length=100,  choices=BMBCChecksheetChoices, default='Good')
    dust_excluder = models.CharField(max_length=100, choices=BMBCChecksheetChoices, default='Good')
        
    

    def __str__(self):
        return self.BogieNumber
