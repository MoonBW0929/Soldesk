
from datetime import datetime, timedelta


date = datetime(2015,1,1)
date += timedelta(1)

if date == datetime(2015,1,2):
    print(True)
else:
    print(False)