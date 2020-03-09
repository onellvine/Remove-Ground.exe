import os, subprocess
import plyer.platforms.win.notification
from plyer import notification
import admincheck


if not admincheck.isUserAdmin():
    admincheck.runAsAdmin()

#use everything cli to scan the computer for Ground.exe virus
cli = subprocess.check_output("es.exe \"Ground.exe\"", shell=True)

#clean the search results
output = cli.decode()
files = output.split("\r\n")

del files[-1] #deletes the last entry "" from the list

#notification = ToastNotifier()

removed = False
try:
    for file in files:
        if "Ground.exe" in file:
            os.remove(file)
            removed = True
except PermissionError: #In case prompted for administrator password and one gets it wrong
    removed = None

if removed == True:
    notification.notify('Notification', 'Successfully removed Ground.exe')
elif removed == False:
    notification.notify('Notification', 'Ground.exe was not found in your computer')
elif removed == None:
    notification.notify('Notification', 'Permission denied - can\'t remove ground.exe')