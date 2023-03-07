import subprocess, sys
import tkinter as tk
from tkinter import simpledialog;

startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
startupinfo.wShowWindow = subprocess.SW_HIDE

root = tk.Tk()
root.title("Active Directory - QOL dlc")
root.geometry("350x350")
tk.Label(root,text="Active directory fancy search engine").pack(side=tk.TOP)

input = tk.Entry()
input.insert(0,"B or K number")
input.pack() 



def group_of():
    ps_command = 'Get-ADUser -Identity "{}" -Properties MemberOf | Select-Object -ExpandProperty MemberOf | Get-ADGroup |Select-Object Name | Sort-Object Name'.format(input.get())
    ps_output = subprocess.check_output(["powershell.exe", "-Command", ps_command], startupinfo=startupinfo)
    rez = (ps_output.decode("utf-8"))
    newWindow = tk.Toplevel()
    newWindow.title("Member of group")
    newWindow.geometry("500x800")
    tk.Label(newWindow,text =rez).pack()

def passwrd_exp():
    ps_command = 'Get-ADUser -identity "{}" -properties PasswordLastSet, PasswordExpired, PasswordNeverExpires | ft Name, PasswordLastSet, PasswordExpired, PasswordNeverExpires'.format(input.get())
    ps_output = subprocess.check_output(["powershell.exe", "-Command", ps_command], startupinfo=startupinfo)

    # Print the output
    rez = (ps_output.decode("utf-8"))
    newWindow = tk.Toplevel()
    newWindow.title("Password look-up results")
    newWindow.geometry("500x200")
    tk.Label(newWindow,text =rez).pack()

def get_Username():
    def run_userfinder():
        ps_command = 'Get-ADUser -Filter {{Surname -eq "{}"}} | Select-Object -Property SamAccountName'.format(input.get())
        ps_output = subprocess.check_output(["powershell.exe", "-Command", ps_command], startupinfo=startupinfo)
        rez = (ps_output.decode("utf-8"))
        tk.Label(newWindow,text=rez).pack()
        
    newWindow = tk.Toplevel()
    newWindow.title("Whats the username?")
    newWindow.geometry("500x200")
    tk.Label(newWindow,text ="Username Finder (only from last name - BETA)").pack()
    input = tk.Entry(newWindow)
    input.insert(0,"enter user's last name")
    input.pack()
    button_run = tk.Button(newWindow,text="run",command=run_userfinder,fg="green")
    button_run.pack()
   
    

#def update():
    #newWindow = tk.Toplevel()
    #newWindow.title("update")
    #newWindow.geometry("500x200")
    #tk.Label(newWindow,text =input.get()).pack()

def exit():
    root.quit()

# Buttons
button_Group = tk.Button(root, text="Group search", command=group_of)
button_Group.pack()

button_Passwrd = tk.Button(root, text="Password check-up", command=passwrd_exp)
button_Passwrd.pack()

button_Userfinder = tk.Button(root,text="Username finder - BETA", command=get_Username)
button_Userfinder.pack()

#button_Update = tk.Button(root,text="", command=update)
#button_Update.pack()

button_Exit = tk.Button(root,text="Exit",command=exit,fg="red")
button_Exit.pack(side=tk.BOTTOM)

# Start the event loop
root.mainloop()