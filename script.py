import sys, os
sys.path.append('/Users/mystis/projects/freebie')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "freebie.settings")
from django.conf import settings

from fcompany.models import Company
from foffer.models import Offer



