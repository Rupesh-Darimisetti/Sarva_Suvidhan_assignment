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
    id = models.CharField(max_length=20,primary_key=True)
    BogieNumber = models.CharField(max_length=100, unique="Truename=Bogie No")
    MakerYearBuilt = models.CharField(max_length=100, name="Malker & Year Built")
    IncomingDivDate = models.DateField(name="Incoming Div. & Date")
    DeflictOfComponents = models.JSONField( name="Deflict of Components (if any)")
    DateofIOH = models.DateField(name="Date of IOH")
    BogieFieldCodition= models.CharField(
        max_length=100, choices=BogieFieldCodition, default='Good', name="Bogie Field Condition"
    )
    Blaster = models.CharField(max_length=100, name="Blaster",choices=BlasterChoices, default='Good')
    BlasterSuspensionBracket = models.CharField(max_length=100, name="Blaster Suspension Bracket", choices=BlasterChoices, default='Good')
    LowerSpringSeat = models.CharField(max_length=100, name="Lower Spring Seat", choices=BlasterChoices, default='Good')
    AxleGuide = models.CharField(max_length=100, name="Axle Guide", choices=BlasterChoices, default='Good')
    AxleGuideAssembly = models.CharField(max_length=100, name="Axle Guide Assembly", choices=BlasterChoices, default='Good')
    ProtectiveTubes = models.CharField(max_length=100, name="Protective Tubes", choices=BlasterChoices, default='Good')
    AnchorLink = models.CharField(max_length=100, name="Anchor Link", choices=BlasterChoices, default='Good')
    SideBearer = models.CharField(max_length=100, name="Side Bearer", choices=BlasterChoices, default='Good')
    BMBCChecksheetChoices = [
        ('Good', 'Good'),
        ('Worn out', 'Worn out'),
        ('Damaged', 'Damaged'),
        ('OtherBMBCChecksheet', 'Other'),
    ]
    CylinderBodyDomeCover = models.CharField(max_length=100, name="Cylinder Body & Dome Cover", choices=BMBCChecksheetChoices, default='Good')
    PistonTrunnionBody = models.CharField(max_length=100, name="Piston Trunnion Body", choices=BMBCChecksheetChoices, default='Good')
    AdjustingTubeandScrew = models.CharField(max_length=100, name="Adjusting Tube and Screw", choices=BMBCChecksheetChoices, default='Good')
    PlungerSpring = models.CharField(max_length=100, name="Plunger Spring", choices=BMBCChecksheetChoices, default='Good')
    TreeBoltHexNut = models.CharField(max_length=100, name="Tree Bolt Hex Nut", choices=BMBCChecksheetChoices, default='Good')
    PawlandPawlSpring = models.CharField(max_length=100, name="Pawl and Pawl Spring", choices=BMBCChecksheetChoices, default='Good')
    DustExcluder = models.CharField(max_length=100, name="Dust Excluder", choices=BMBCChecksheetChoices, default='Good')
        
    

    def __str__(self):
        return self.BogieNumber
