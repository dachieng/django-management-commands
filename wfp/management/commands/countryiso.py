from django.core.management.base import BaseCommand
from django.shortcuts import get_object_or_404
from wfp.models import Country, Intervention
import datetime


class Command(BaseCommand):
    help = "Command to convert Iso Code given start_date = 2021"
    year = 2021

    # get the iso_code as an argument
    def add_arguments(self, parser):
        parser.add_argument('iso', type=str)

    def handle(self, *args, **kwargs):
        iso = kwargs['iso']

        # filter coutry by iso code

        country = get_object_or_404(Country, Iso_code=iso)

        # get the interventions associated with the given country

        interventions = country.intervention_set.all()

        for elem in interventions:
            print(elem.Start_date.strftime('%Y'))
            if elem.Start_date.strftime('%Y') == self.year:
                elem.Code_name = "SCOPE2021"
                elem.save()
                print(elem.Code_name)
            else:
                print(f"The given startd date is not {self.year}")
                print(elem.Code_name)
