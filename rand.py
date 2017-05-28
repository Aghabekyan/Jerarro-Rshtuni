import random
from homepage.models import *


for lp in range(100):
    get_id = random.randint(13, 18)
    obj = Catalog.objects.get(pk=get_id)
    obj.id = None
    obj.save()
    print 5555555555555


print 11111111
