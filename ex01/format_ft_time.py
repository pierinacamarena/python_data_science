import time
from datetime import datetime

date_today_str = datetime.now().strftime('%b %d %Y')

seconds_since_epoch = time.time()

print(f"Seconds since January 1, 1970: {seconds_since_epoch:.4f} or {seconds_since_epoch:.2e} in scientific notation")
print(date_today_str)