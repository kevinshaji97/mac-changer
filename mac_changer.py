import subprocess

interface = input("Enter the interface to change >")
new_mac = input ("Enter the mac to change >")

print("Changing MAC for "+ interface )
subprocess.call("ifconfig",shell="true")