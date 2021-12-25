from datetime import datetime

dates = [datetime.now(), datetime.now()]

print(*map(str, dates))
