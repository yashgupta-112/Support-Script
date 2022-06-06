from subprocess import check_output

status =  check_output("app-plex upgrade",   shell=True)

if "true" in status:
    print("success")
elif "false" in status:
    print("failure")