import os, time, sys
# python3 cron.py 4 // 4 hours
hourly_cron = int(sys.argv[-1]) if len(sys.argv) > 1 else 4

rate = 60*60*hourly_cron

while True:
    os.system("make run")
    time.sleep(rate)