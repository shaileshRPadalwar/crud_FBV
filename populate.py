import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crudFBV.settings')
import django
django.setup()
from random import randint
from empdetails.models import Employee
from faker import Faker

faker=Faker()
def populate(n):
    for i in range(10):
        feno=randint(1001,9999)
        fename=faker.name()
        fesal=randint(1000,10000)
        feaddr=faker.city()
        emp_record=Employee.objects.get_or_create(eno=feno,ename=fename,esal=fesal,eaddr=feaddr)

populate(10)
