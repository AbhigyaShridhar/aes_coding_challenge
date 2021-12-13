from datetime import time, datetime
from .models import Transaction

def set_tn_number():
    tn_number = "TRN"
    year = datetime.now().year
    count = Transaction.objects.filter(tn_time__year=year).count() + 1
    tn_number = tn_number + "/" + str(year) + "/" + str(count)
    return tn_number
