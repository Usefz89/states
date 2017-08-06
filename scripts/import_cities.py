#!/usr/bin/env python


import csv
import os
import sys


sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE","project.settings")

from app.models import State, City

states = State.objects.all()
city = City.objects.all()




states_csv =  os.path.join(os.path.dirname(os.path.abspath(__file__)),"zip_codes_states.csv")

csv_file = open(states_csv,'r')
reader = csv.DictReader(csv_file)

for row in reader:
    try:
        state, created = State.objects.get_or_create(abbreviation=row['state'])
        state.save()
    except:
        print state
    try:

        new_city, created = City.objects.get_or_create(name=row['city'])
        new_city.zip_code = row['zip_code']
        new_city.latitude = row['latitude']
        new_city.longitude = row['longitude']
        new_city.state = state
        new_city.county = row['county']
        new_city.save()
    except:
        print new_city










csv_file.close()










