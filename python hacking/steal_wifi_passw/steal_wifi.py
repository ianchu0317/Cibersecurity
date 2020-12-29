import subprocess
from time import asctime

console = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode("utf-8").split("\n")
wifis = [item.strip("All User Profile").strip("\r").strip(":").strip(" ") for item in console if "All User Profile" in item]
time = asctime()
for wifi in wifis:
    console = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', wifi, "key=clear"]).decode("utf-8")
    with open(str(f"{time.replace(':', '_')}_WIFI.txt"), "a") as file:
        file.write(console)
        for i in range(2):
            file.write("\n")