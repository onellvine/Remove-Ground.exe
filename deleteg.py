import os, subprocess
from win10toast import ToastNotifier
import admincheck


if not admincheck.isUserAdmin():
    admincheck.runAsAdmin()

#use everything cli to scan the computer for Ground.exe virus
cli = subprocess.check_output("es.exe \"Ground.exe\"", shell=True)

#clean the search results
output = cli.decode()
files = output.split("\r\n")

del files[-1] #deletes the last entry "" from the list

notification = ToastNotifier()

removed = False
try:
    for file in files:
        if "Ground.exe" in file:
            os.remove(file)
            removed = True
except PermissionError: #In case prompted for administrator password and one gets it wrong
    removed = None

if removed == True:
    notification.show_toast(title='Notification', msg='Successfully removed Ground.exe',duration=5, threaded=False)
elif removed == False:
    notification.show_toast(title='Notification', msg='Ground.exe was not found in your computer',duration=5, threaded=False)
elif removed == None:
    notification.show_toast(title='Notification', msg='Permission denied - can\'t remove ground.exe',duration=5, threaded=False)