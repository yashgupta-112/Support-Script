from subprocess import check_output

while True:
    status =  check_output("app-plex upgrade",   shell=True)
    status = status.decode("utf-8")
    if "true" in status:
        print("succes")
        break
    elif "false" in status:
        status =  check_output("app-plex upgrade",   shell=True)
        print("fail")