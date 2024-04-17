from django.db import models
from django.contrib.auth.models import User


class LeadSource(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    cid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, unique=True)
    last_name = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class SupportStaff(models.Model):
    first_name = models.CharField(max_length=20, unique=True)
    last_name = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=20, unique=True)
    phone_number = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class PipeLineStage(models.Model):
    name = models.CharField(max_length=20, unique=True)
    position = models.IntegerField(unique=True)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.position


class Customer(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    support_staff = models.ForeignKey(SupportStaff, on_delete=models.CASCADE)
    pipeline_stage = models.ForeignKey(PipeLineStage, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contact.first_name


class Company(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=100)
    size = models.IntegerField()
    website = models.URLField()

    def __str__(self):
        return self.name


class CustomField(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CustomFieldCustomer(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pipeline_stage = models.ForeignKey(PipeLineStage, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField(max_length=255, null=True, blank=True)
    support_staff = models.OneToOneField(SupportStaff, on_delete=models.CASCADE)

    def __str__(self):
        return self.notes


class CompanyCustomField(models.Model):
    company = models.OneToOneField(Company, on_delete=models.CASCADE)
    custom_field = models.OneToOneField(CustomField, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.company.name


class Document(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    file_path = models.FileField(upload_to="uploads/documents/")
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.file_path


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    color = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=True, blank=True)
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class CustomerPipelineStage(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    pipeline_stage = models.ForeignKey(PipeLineStage, on_delete=models.CASCADE)
    notes = models.CharField(max_length=255, null=True, blank=True)
    support_staff = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.first_name
