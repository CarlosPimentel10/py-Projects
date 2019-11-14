# working with datetime objects
from datetime import datetime, timedelta
import time


dt1 = datetime(2018, 1, 1) + timedelta(1)
print(dt1)
dt2 = datetime.now()
dt = datetime.strptime('2019/09/04', '%Y/%m/%d')
dt = datetime.fromtimestamp(time.time())

print(f'{dt.year}/{dt.month}')
print('days', dt1.days)
