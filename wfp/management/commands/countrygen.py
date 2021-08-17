from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from wfp.models import Country, Intervention
import string
from datetime import datetime
import random
from django.shortcuts import get_object_or_404


# function to generate random dates

def random_date(first_date, second_date):
    first_timestamp = int(first_date.timestamp())
    second_timestamp = int(second_date.timestamp())
    random_timestamp = random.randint(first_timestamp, second_timestamp)
    return datetime.fromtimestamp(random_timestamp)


class Command(BaseCommand):
    help = "Generator for 32 counties each with 32 intevetions"
    d1 = datetime.strptime("1/1/2018", "%d/%m/%Y")
    d2 = datetime.strptime("31/12/2022", "%d/%m/%Y")

    d3 = datetime.strptime("1/1/2023", "%d/%m/%Y")
    d4 = datetime.strptime("31/12/2025", "%d/%m/%Y")

    def add_arguments(self, parser):
        parser.add_argument('total', nargs='?', type=int, default=32)
        parser.add_argument('-c', '--country_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        total = options['total']

        for i in range(total):
            country = Country(Name=get_random_string(
                length=7, allowed_chars=string.ascii_uppercase), Iso_code=get_random_string(length=7, allowed_chars=string.ascii_uppercase + string.digits))
            country.save()

        for i in range(total):

            for country_id in options['country_ids']:

                country = get_object_or_404(Country, pk=country_id)

                for i in range(total):
                    country.intervention_set.create(Name=get_random_string(
                        length=7, allowed_chars=string.ascii_uppercase), Code_name=get_random_string(length=7, allowed_chars=string.ascii_uppercase + string.digits), Start_date=random_date(self.d1, self.d2), End_date=random_date(self.d3, self.d4))
                    country.Id += 1
