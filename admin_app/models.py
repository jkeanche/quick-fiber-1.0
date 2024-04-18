from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from django.contrib.auth.models import User


from utils.UserManagerUtil import CustomUserManager


class County(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Constituency(models.Model):
    name = models.CharField(max_length=100, unique=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name='constituencies')

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    constituency = models.ForeignKey(Constituency, on_delete=models.CASCADE, related_name='locations')

    def __str__(self):
        return self.name


class Estate(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='estates')

    def __str__(self):
        return self.name


class Role(models.Model):
    """
    Model representing a role that can be assigned to users.
    """
    name = models.CharField(max_length=100, unique=True)
    permissions = models.ManyToManyField('Permission', blank=True)

    def __str__(self):
        return self.name


class Permission(models.Model):
    """
    Model representing a permission that can be assigned to roles.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Users(models.Model):
    acc = models.TextField(primary_key=True)
    name = models.TextField()
    phone = models.TextField()
    package = models.IntegerField()
    username = models.TextField()
    password = models.TextField()
    install_date = models.TextField()
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'hotspotAccounts'
        #managed = False


class Station(models.Model):
    name = models.CharField(max_length=100)
    location = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    payment_methods = models.ManyToManyField(PaymentMethod, related_name='stations', null=True, blank=True)
    users = models.ManyToManyField(Users, related_name='stations', null=True, blank=True)  # Changed to ManyToManyField
    default_payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True,
                                               related_name='default_stations', blank=True)
    status = models.BooleanField(default=True)  # is_active

    def count_users(self):
        return self.users.count()

    def get_payment_methods_str(self):
        # Get all payment methods associated with the station
        payment_methods = self.payment_methods.all()
        if payment_methods:
            return ", ".join(payment_method.name for payment_method in payment_methods)
        else:
            # If no payment methods are available, return "Not Specified"
            return "Not Specified"

    def __str__(self):
        return self.name


class Router(models.Model):
    STATUS_CHOICES = [
        ('online', 'Online'),
        ('offline', 'Offline'),
    ]

    host = models.CharField(max_length=255, unique=True, help_text="IP address or domain name")
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    port = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)

    def __str__(self):
        return self.host


class IPPool(models.Model):
    name = models.CharField(max_length=255, unique=True)
    start_ip = models.GenericIPAddressField(protocol='IPv4')
    end_ip = models.GenericIPAddressField(protocol='IPv4')
    router = models.ForeignKey(Router, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Payment(models.Model):
    pid = models.AutoField(primary_key=True)
    acc = models.TextField()
    code = models.TextField()
    amount = models.IntegerField()
    source = models.TextField()
    date = models.TextField()
    time = models.TextField()

    class Meta:
        db_table = 'payments'
        #managed = False


class Sessions(models.Model):
    sid = models.AutoField(primary_key=True)
    acc = models.TextField()
    profile = models.TextField()
    startDate = models.TextField(db_column='start date')
    startTime = models.TextField(db_column='start time')
    endDate = models.TextField(db_column='end date')
    endTime = models.TextField(db_column='end time')
    status = models.TextField()
    creation_date = models.TextField(db_column='creation date')

    class Meta:
        db_table = 'sessions'
        #managed = False


class Contacts(models.Model):
    cid = models.AutoField(primary_key=True)
    account = models.TextField()
    contact = models.TextField()
    apartment_name = models.TextField(null=True, blank=True)
    unit_number = models.TextField(null=True, blank=True)
    device_mac = models.TextField(null=True, blank=True)
    device_serial_number = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'contacts'
        #managed = False


class Finances(models.Model):
    fid = models.AutoField(primary_key=True)
    acc = models.TextField()
    moneyIn = models.IntegerField(db_column='money in')
    moneyOut = models.IntegerField(db_column='money out')
    description = models.TextField()
    date = models.TextField()

    class Meta:
        db_table = 'finance'
        #managed = False


class Pkgs(models.Model):
    pno = models.AutoField(primary_key=True)
    name = models.TextField()
    speed = models.IntegerField()
    days = models.IntegerField()
    max_users = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    pkg_type = models.TextField(db_column='type')

    class Meta:
        db_table = 'packages'
        #managed = False


class Logs(models.Model):
    lid = models.AutoField(primary_key=True)
    topic = models.TextField()
    date = models.TextField()
    time = models.TextField()
    desc = models.TextField()

    class Meta:
        db_table = 'logs'
        #managed = False


class Notifications(models.Model):
    id = models.AutoField(primary_key=True)
    topic = models.TextField()
    category = models.TextField()
    to = models.TextField()
    dateTime = models.TextField()
    notification = models.TextField()
    read = models.BooleanField()

    class Meta:
        db_table = 'notifications'
        #managed = False\


class Messages(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.TextField()
    to = models.TextField()
    dateTime = models.TextField()
    message = models.TextField()
    read = models.BooleanField()

    class Meta:
        db_table = 'messages'
        #managed = False


class pppoe(models.Model):
    acc = models.TextField(primary_key=True)
    phone = models.TextField()
    location = models.TextField()
    ip = models.TextField()
    username = models.TextField()
    password = models.TextField()
    install_date = models.TextField(db_column='install date')
    name = models.TextField()
    package = models.IntegerField()
    balance = models.IntegerField()

    class Meta:
        db_table = 'pppoeAccounts'
    # managed = False


class Invoice(models.Model):
    TERMS = [
        ('0 days', '0 days'),
        ('14 days', '14 days'),
        ('30 days', '30 days'),
        ('60 days', '60 days'),
    ]

    STATUS = [
        ('CURRENT', 'CURRENT'),
        ('EMAIL_SENT', 'EMAIL_SENT'),
        ('OVERDUE', 'OVERDUE'),
        ('PAID', 'PAID'),
    ]

    title = models.CharField(null=True, blank=True, max_length=100)
    number = models.CharField(null=True, blank=True, max_length=100)
    dueDate = models.DateField(null=True, blank=True)
    paymentTerms = models.CharField(choices=TERMS, default='30 days', max_length=100)
    status = models.CharField(choices=STATUS, default='CURRENT', max_length=100)
    notes = models.TextField(null=True, blank=True)

    #RELATED fields
    client = models.ForeignKey(Users, blank=True, null=True, on_delete=models.SET_NULL)

    #Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.number, self.uniqueId)

    def get_absolute_url(self):
        return reverse('invoice-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.number, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.number, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Invoice, self).save(*args, **kwargs)


'''class adminAccounts(models.Model):
    id =models.TextField(primary_key=True)
    password=models.CharField(max_length=128)
    last_login=models.DateTimeField()
    is_superuser=models.BooleanField()
    username=models.TextField(max_length=150)
    last_name=models.TextField(max_length=150)
    email=models.TextField(max_length=254)
    is_staff=models.BooleanField()
    is_active=models.BooleanField()
    date_joined=models.DateTimeField()
    first_name=models.TextField(max_length=150)

    class Meta:
        db_table = 'auth_user'
       # managed = False     '''

#seeders

def seed_counties_and_locations():
    kenyan_counties = {
        "Baringo": ["Kabarnet", "Eldama Ravine"],
        "Bomet": ["Bomet", "Longisa"],
        "Bungoma": ["Bungoma", "Webuye"],
        "Busia": ["Busia", "Malaba"],
        "Elgeyo Marakwet": ["Iten", "Eldoret"],
        "Embu": ["Embu", "Runyenjes"],
        "Garissa": ["Garissa", "Modogashe"],
        "Homa Bay": ["Homa Bay", "Oyugis"],
        "Isiolo": ["Isiolo", "Moyale"],
        "Kajiado": ["Kajiado", "Namanga"],
        "Kakamega": ["Kakamega", "Lugari"],
        "Kericho": ["Kericho", "Litein"],
        "Kiambu": ["Kiambu", "Thika"],
        "Kilifi": ["Kilifi", "Malindi"],
        "Kirinyaga": ["Kerugoya", "Sagana"],
        "Kisii": ["Kisii", "Ogembo"],
        "Kisumu": ["Kisumu", "Muhoroni"],
        "Kitui": ["Kitui", "Mwingi"],
        "Kwale": ["Kwale", "Msambweni"],
        "Laikipia": ["Nanyuki", "Rumuruti"],
        "Lamu": ["Lamu", "Mpeketoni"],
        "Machakos": ["Machakos", "Kangundo"],
        "Makueni": ["Wote", "Sultan Hamud"],
        "Mandera": ["Mandera", "Banisa"],
        "Marsabit": ["Marsabit", "Laisamis"],
        "Meru": ["Meru", "Chuka"],
        "Migori": ["Migori", "Kehancha"],
        "Mombasa": ["Mombasa", "Likoni"],
        "Murang'a": ["Murang'a", "Maragua"],
        "Nairobi": ["Nairobi", "Kibera"],
        "Nakuru": ["Nakuru", "Naivasha"],
        "Nandi": ["Kapsabet", "Nandi Hills"],
        "Narok": ["Narok", "Mai Mahiu"],
        "Nyamira": ["Nyamira", "Nyansiongo"],
        "Nyandarua": ["Ol Kalou", "Nyahururu"],
        "Nyeri": ["Nyeri", "Othaya"],
        "Samburu": ["Maralal", "Wamba"],
        "Siaya": ["Siaya", "Yala"],
        "Taita Taveta": ["Voi", "Taveta"],
        "Tana River": ["Hola", "Garsen"],
        "Tharaka-Nithi": ["Chuka", "Kathwana"],
        "Trans Nzoia": ["Kitale", "Kiminini"],
        "Turkana": ["Lodwar", "Kakuma"],
        "Uasin Gishu": ["Eldoret", "Soy"],
        "Vihiga": ["Vihiga", "Hamisi"],
        "Wajir": ["Wajir", "Buna"],
        "West Pokot": ["Kapenguria", "Lokichar"]
    }

    for county_name, locations in kenyan_counties.items():
        county = County.objects.create(name=county_name)
        for location_name in locations:
            Location.objects.create(name=location_name, constituency=None, county=county)

# seed_counties_and_locations()
