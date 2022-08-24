from django.core.management.base import BaseCommand
import pandas as pd



class Command(BaseCommand):
    help = "Adding authod from command"

    def handle(self, *args, **options):
        # return super().handle(*args, **options)
        print("Adding data...!")

        excel_file = 'test.xlsx'
        df = pd.read_excel(excel_file)