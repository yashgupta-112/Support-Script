import os
import sys
from subprocess import check_output, check_call



try:
    import halo
except ImportError:
    FNULL = open(os.devnull, 'w')
    check_call([sys.executable, "-m", "pip", "install", 'halo'], stdout=FNULL)

#App Upgrade
finally:
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
            