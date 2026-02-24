from datetime import datetime
date1 = datetime(2025, 2, 20, 10, 0, 0)
date2 = datetime(2025, 2, 23, 12, 30, 0)
difference = date2 - date1
seconds = difference.total_seconds()
print("Difference in seconds:", seconds)