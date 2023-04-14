import subprocess, sys
import tkinter
import customtkinter as CTk
from PIL import Image



class MainApplication(CTk.CTkFrame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.widgets()
    
    def widgets(self):
        #getter
        logo_img = CTk.CTkImage(light_image=Image.open("assets/adac-logo.png"),size=(800, 500))
        #loaders
        self.menu_window_button = CTk.CTkButton(master=self, command=self.open_new_window, image=logo_img, text="", fg_color="transparent", hover=False)
        self.credits_line1 = CTk.CTkLabel(master=self,text="Made by Liam Poulson")
        self.credits_line2 = CTk.CTkLabel(master=self,text="v1.0")
        #framing
        self.menu_window_button.pack()
        self.credits_line1.pack()
        self.credits_line2.pack()
        
    def open_new_window(self):
        menu_window = CTk.CTkToplevel(self.master)
        new_app = MenuWindowApplication(menu_window)
        self.master.withdraw()


class MenuWindowApplication(CTk.CTkFrame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.master.title("ADAC - Main menu")
        self.master.geometry(f"{1100}x{580}")
        
        #sidebar with widgets
        self.sidebar_frame = CTk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=5, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = CTk.CTkLabel(self.sidebar_frame, text="ADAC Menu")
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        #btn Group_lookup
        self.sidebar_button_1 = CTk.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        #btn Password_lookup
        self.sidebar_button_2 = CTk.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        #btn tbd
        self.sidebar_button_3 = CTk.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        #customization
        self.appearance_mode_label = CTk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = CTk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        
        # create main entry and button
        self.entry = CTk.CTkEntry(self, placeholder_text="Username", text_color=("gray10", "#DCE4EE"))
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        
        self.pack()
        
    def sidebar_button_event(self):
        print("sidebar_button click")
    
    def change_appearance_mode_event(self, new_appearance_mode: str):
        CTk.set_appearance_mode(new_appearance_mode)   
        
"""
    
main_frame = customtkinter.CTkFrame(master=root)
main_frame.pack(pady=20, padx=60, fill="both", expand=True)
root.title("ADAC v1.0 CTKINTER update")


def launching():
    menu_frame = customtkinter.CTkFrame(master=root, width=800, height=500)
    main_frame.quit
    menu_frame(pady=20, padx=60, fill="both", expand=True)
    
    



label_credits = customtkinter.CTkLabel(main_frame, text="Made by Liam Poulson")
label_credits.pack()
label_credits2 = customtkinter.CTkLabel(main_frame, text="v1.0 version")
label_credits2.pack()




    


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

def get_Username():
    def run_userfinder():
        ps_command = 'Get-ADUser -Filter {{Surname -eq "{}"}} | Select-Object -Property SamAccountName'.format(input.get())
        ps_output = subprocess.check_output(["powershell.exe", "-Command", ps_command])
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

"""

root = CTk.CTk()
app = MainApplication(root)
app.pack()
root.mainloop()