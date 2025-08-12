from datetime import datetime

a = datetime.strftime(datetime(2025, 6, 4), "%Y%m%d")
today = datetime.strftime(datetime.now(), "%Y%m%d")
print(a == today)
