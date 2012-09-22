
import datetime
import random

from django.contrib.auth.models import User


def get_choices(length, n=2, l=[]):
    if n >= length:
        n = length
    if n <= 0:
        return l
    
    num = random.randint(0,length-1)
    while num in l:
        num = random.randint(0,length-1)

    l.append(num)
    return get_choices(length, n-1, l)

def choose_foodman(n=2):
    random.seed(datetime.datetime.now())

    qs = User.objects.filter(is_active=True)
    length = qs.count()
    ch = get_choices(length, n, [])
    return [qs[i] for i in ch]
