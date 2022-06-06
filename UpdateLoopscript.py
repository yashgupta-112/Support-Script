from subprocess import check_output

status =  check_output("app-plex upgrade",   shell=True)

print(status)