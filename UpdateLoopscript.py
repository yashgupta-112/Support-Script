import os
import sys
from subprocess import check_output, check_call
import time
os.popen("pip install halo").read()
time.sleep(3)

import halo
spinner = halo.Halo(text='In-Progress', text_color='magenta', spinner='bouncingBar')
appname = input("Enter AppName to upgrade: ")

spinner.start()
count = 1
while True:
    status = check_output(f"app-{appname} upgrade".format(appname=appname), shell=True)
    status = status.decode("utf-8")
    if "true" in status:
        spinner.stop()
        print("[SUCCESS] Upgrade Count:", count)
        break
    elif "false" in status:
        count +=1
        