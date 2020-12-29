import subprocess

console = subprocess.Popen(['dir'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
output, error = console.communicate()
print(output, error)