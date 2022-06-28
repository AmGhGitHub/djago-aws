# Django command to wait for the db to be available

import time
from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for the DB.")
        db_up = False
        while not db_up:
            try:
                self.check(databases=["default"])
                db_up = True
            except (OperationalError, Psycopg2Error):
                self.stdout.write("DB is unavialable. Try again in 1 second.")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("DB is ready."))

