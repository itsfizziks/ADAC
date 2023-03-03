import subprocess, sys
import tkinter as tk
from tkinter import simpledialog;


root = tk.Tk()
root.title("Active Directory - QOL dlc")
root.geometry("700x350")
tk.Label(root,text="Active directory fancy search engine").pack()

input = tk.Entry()
input.insert(0,"B or K number")
input.pack()



def group_of():
    #p = subprocess.Popen('powershell.exe -ExecutionPolicy RemoteSigned -file "AD_GROUP_PW.ps1"', stdout=sys.stdout)
    #p.communicate()
    ps_command = 'Get-ADUser -Identity "{}" -Properties MemberOf | Select-Object -ExpandProperty MemberOf | Get-ADGroup |Select-Object Name | Sort-Object Name'.format(input.get())
    ps_output = subprocess.check_output(["powershell.exe", "-Command", ps_command])
    rez = (ps_output.decode("utf-8"))
    newWindow = tk.Toplevel()
    newWindow.title("Member of group")
    newWindow.geometry("500x800")
    tk.Label(newWindow,text =rez).pack()

def passwrd_exp():
    ps_command = 'Get-ADUser -identity "{}" -properties PasswordLastSet, PasswordExpired, PasswordNeverExpires | ft Name, PasswordLastSet, PasswordExpired, PasswordNeverExpires'.format(input.get())
    ps_output = subprocess.check_output(["powershell.exe", "-Command", ps_command])

    # Print the output
    rez = (ps_output.decode("utf-8"))
    newWindow = tk.Toplevel()
    newWindow.title("Password look-up results")
    newWindow.geometry("500x200")
    tk.Label(newWindow,text =rez).pack()

def update():
    newWindow = tk.Toplevel()
    newWindow.title("update")
    newWindow.geometry("500x200")
    tk.Label(newWindow,text =input.get()).pack()



# Buttons
button_Group = tk.Button(root, text="Group search", command=group_of)
button_Group.pack()

button_Passwrd = tk.Button(root, text="Password check-up", command=passwrd_exp)
button_Passwrd.pack()

button_Update = tk.Button(root,text="check", command=update)
button_Update.pack()

# Start the event loop
root.mainloop()