import random
from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from brokers.models import Broker
from invoices.models import Status, Invoice
from brokers.models import Broker

class Command(BaseCommand):
    help = 'Populate Invoice model with dummy data'

    def handle(self, *args, **options):
        # get the list of status and broker instances
        status = Status.objects.get(name='Missing paperwork')
        brokers = Broker.objects.all()


        # Populate Invoice model with dummy data
        for _ in range(100):
            Invoice.objects.create(
                invoice_number=random.randint(1000, 9999),
                reference=f'Ref-{random.randint(1, 100)}',
                broker=random.choice(brokers),
                pick_up=timezone.now() - timedelta(days=random.randint(1, 30)),
                delivery=timezone.now() + timedelta(days=random.randint(1, 30)),
                amount=random.uniform(100.0, 1000.0),
                status=status,
                comment=f'Comment-{random.randint(1, 10)}',
                last_update=timezone.now(),
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Invoice model with dummy data.'))
