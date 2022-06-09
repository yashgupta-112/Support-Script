import os
import sys
import subprocess
from subprocess import check_output, check_call

#install halo package if it's not there
def package_install(package):
    subprocess.call(["/usr/bin/pip3", "install", "--user", "-q", "--no-cache-dir", "--disable-pip-version-check", "halo"])

def check_halo():
    os.system("pip list | grep halo")

def app_upgrade():
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


#check halo package for spinner
try:
    if check_halo == '':
        package_install('halo')
        import halo
        app_upgrade()
    else:
        import halo
        app_upgrade()

except:
    print("Unable to install Halo module, try to run 'pip3 install halo' and then script again.")