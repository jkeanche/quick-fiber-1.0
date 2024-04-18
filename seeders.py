from django_seeding import seeders
from django_seeding.seeder_registry import SeederRegistry

from crm_app.models import LeadSource, PipeLineStage, CustomField, Tag
from admin_app.models import County, Location


from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# CRM Stuff
@SeederRegistry.register
class LeadSourceSeeder(seeders.JSONFileModelSeeder):
    id = 'LeadSourceSeeder'
    priority = 1
    model = LeadSource
    json_file_path = [BASE_DIR / 'seeders/lead_sources.json']


@SeederRegistry.register
class PipeLineStageSeeder(seeders.JSONFileModelSeeder):
    id = 'PipeLineStageSeeder'
    priority = 2
    model = PipeLineStage
    json_file_path = [BASE_DIR / 'seeders/pipeline_stages.json']


@SeederRegistry.register
class CustomFieldSeeder(seeders.JSONFileModelSeeder):
    id = 'CustomFieldSeeder'
    priority = 3
    model = CustomField
    json_file_path = [BASE_DIR / 'seeders/custom_fields.json']


@SeederRegistry.register
class TagFieldSeeder(seeders.JSONFileModelSeeder):
    id = 'TagSeeder'
    priority = 4
    model = Tag
    json_file_path = [BASE_DIR / 'seeders/tags.json']








