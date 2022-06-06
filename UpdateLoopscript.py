from subprocess import check_output
appname = input("Please application name you want to upgrade: ")

while True:
    status =  check_output("app-{app} upgrade",   shell=True).format(appname)
    status = status.decode("utf-8")
    if "true" in status:
        print("succes")
        break
    elif "false" in status:
        status =  check_output("app-plex upgrade",   shell=True)
        print("fail")

