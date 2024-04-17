from django.contrib import admin

from crm_app.models import LeadSource, PipeLineStage, CustomerPipelineStage, Contact, Company, CustomField, \
    CustomFieldCustomer, CompanyCustomField, Tag, Document, Task

admin.site.register(LeadSource)
admin.site.register(PipeLineStage)
admin.site.register(CustomerPipelineStage)
admin.site.register(Contact)
admin.site.register(Company)
admin.site.register(CustomField)
admin.site.register(CustomFieldCustomer)
admin.site.register(CompanyCustomField)
admin.site.register(Tag)
admin.site.register(Document)
admin.site.register(Task)
