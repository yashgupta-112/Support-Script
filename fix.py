import os
import sys
from subprocess import check_output, check_call
from pip._internal import main 
import importlib
#install halo package if it's not there

#check halo package for spinner
try:
    importlib.import_module('halo')
except ImportError:
    main(['install', 'halo'])
    os.system("clear")
    
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