import random
from datetime import datetime, timedelta

def random_past_datetime(months_back):
    days = random.randint(0, months_back * 30)
    return datetime.now() - timedelta(days=days)

def random_past_date(months_back):
    return random_past_datetime(months_back).date()

def random_future_date(start_datetime):
    return (start_datetime + timedelta(days=random.randint(3, 60))).date()
