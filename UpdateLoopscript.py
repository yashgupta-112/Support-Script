from subprocess import check_output

status =  check_output("app-plex upgrade",   shell=True)
status = status.decode("utf-8")
if "true" in status:
    print("success")
elif "false" in status:
    print("failure")