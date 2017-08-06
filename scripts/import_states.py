#!/usr/bin/env python


import csv
import os
import sys


sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE","project.settings")

from app.models import State, StateCapital

states = State.objects.all()



states_csv =  os.path.join(os.path.dirname(os.path.abspath(__file__)),"states.csv")

csv_file = open(states_csv,'r')
reader = csv.DictReader(csv_file)

for row in reader:


    new_state, created = State.objects.get_or_create(name = row['state'])
    new_state.abbreviation = row['abbrev']
    new_state.save()
    print created


    new_capital, created = StateCapital.objects.get_or_create(name=row['capital'])
    new_capital.state = new_state
    new_capital.latitude = row['latitude']
    new_capital.longitude= row['longitude']
    new_capital.population = row['population']
    new_capital.save()
    print created


csv_file.close()










