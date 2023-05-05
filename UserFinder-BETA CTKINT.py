import subprocess, sys
import tkinter
import customtkinter as CTk
from PIL import Image



class MainApplication(CTk.CTkFrame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.master.title("ADAC - Launcher")
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
        #self.master.withdraw()


class MenuWindowApplication(CTk.CTkFrame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.master.title("ADAC - Active Directory Automated Commands")
        self.master.geometry(f"{1120}x{510}")
        
        ####################### SIDE BAR MENU #######################
        
        #sidebar with widgets
        self.sidebar_frame = CTk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = CTk.CTkLabel(self.sidebar_frame, text="ADAC Menu")
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        #btn Group_lookup
        self.optionmenu_var = CTk.StringVar(value="Groups Query")  # set initial value
        self.group_option = CTk.CTkOptionMenu(self.sidebar_frame,values=["Mirror", "Simple lookup"],command=self.menu_group,variable=self.optionmenu_var)
        self.group_option.grid(row=1, column=0, padx=20, pady=10)
        #btn Password_lookup
        self.sidebar_password = CTk.CTkButton(self.sidebar_frame, text="Password Info", command=self.menu_password)
        self.sidebar_password.grid(row=2, column=0, padx=20, pady=10)
        #btn tbd
        self.sidebar_button_3 = CTk.CTkButton(self.sidebar_frame, text="Username Finder",command=self.menu_finder)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        #customization
        self.appearance_mode_label = CTk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = CTk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        
        ####################### OPTION BOX FOR GROUPS #######################
        
        #create option box
        self.option_frame = CTk.CTkFrame(self, width=140, corner_radius=0)
        self.option_frame.grid(row=4, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        #options for mirror ID group
        self.label_source_from = CTk.CTkLabel(self.option_frame, text="Source to copy : ")
        self.source_from = CTk.CTkEntry(self.option_frame, text_color=("gray10", "#DCE4EE"))
        
        self.label_source_to = CTk.CTkLabel(self.option_frame, text="The recipient : ")
        self.source_to = CTk.CTkEntry(self.option_frame, text_color=("gray10", "#DCE4EE"))
        
        self.runMID = CTk.CTkButton(self.option_frame, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Compare", command=self.running_MID)
        
        #options for Simple lookup
        self.label_simplelook = CTk.CTkLabel(self.option_frame, text="Username here : ")
        self.username_getter = CTk.CTkEntry(self.option_frame, text_color=("gray10", "#DCE4EE"))
        self.runSL = CTk.CTkButton(self.option_frame, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="RUN", command=self.running_SL)
        
        ####################### OPTION BOX FOR PSSWRD #######################
        
        #option box already created
        
        #options
        self.label_password = CTk.CTkLabel(self.option_frame, text="Username here : ")
        self.username_getter = CTk.CTkEntry(self.option_frame, text_color=("gray10", "#DCE4EE"))
        self.runPSSWRD = CTk.CTkButton(self.option_frame, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="RUN", command=self.running_PSSWRD)
        
        ####################### OPTION BOX FOR USERFINDER #######################

        #option box already created
        
        #options for mirror ID group
        self.label_first_name = CTk.CTkLabel(self.option_frame, text="First name : ")
        self.first_name = CTk.CTkEntry(self.option_frame, text_color=("gray10", "#DCE4EE"))
        
        self.label_last_name = CTk.CTkLabel(self.option_frame, text="Last name : ")
        self.last_name = CTk.CTkEntry(self.option_frame, text_color=("gray10", "#DCE4EE"))
        
        self.runFIND = CTk.CTkButton(self.option_frame, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Search", command=self.running_FIND)

         ####################### STATIC ASSETS #######################
        
        raw_ascii_art = '''
 ____ ____ ____ ____                
||A |||D |||A |||C ||               
||__|||__|||__|||__||               
|/__\|/__\|/__\|/__\|               
 ____ ____ ____ ____ ____ ____ ____ 
||c |||o |||n |||s |||o |||l |||e ||
||__|||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|/__\|                                                                                                                                                                                                                                                
'''
        # create textbox
        self.textbox = CTk.CTkTextbox(self, width=750, font=("Courier", 15))
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert(CTk.END, raw_ascii_art)
        self.pack()
        
        # create main entry and button
        self.main_entry = CTk.CTkEntry(self, placeholder_text="Username", text_color=("gray10", "#DCE4EE"))
        self.main_entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_RUN = CTk.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Admin Checker" + "\n" + "(may cause lag)", command=self.running_main)
        self.main_button_RUN.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        ####################### FONC. GROUPS #######################
    
    def menu_group(self,*args):
        selected_value = self.optionmenu_var.get()
        print(selected_value)
        
        if selected_value == "Mirror":
            #remove previous if it was the case
            frame_widgets = self.option_frame.winfo_children()
            for widget in frame_widgets:
                widget.grid_remove()  
            
            self.label_source_from.grid(row=0, column=0)
            self.source_from.grid(row=1, column=0, padx=(20, 0), pady=(20, 20), sticky="nsew")
            self.label_source_to.grid(row=0, column=1)
            self.source_to.grid(row=1, column=1)
            self.runMID.grid(row=2, column=0)
        
        elif selected_value == "Simple lookup":
            #remove previous if it was the case
            frame_widgets = self.option_frame.winfo_children()
            for widget in frame_widgets:
                widget.grid_remove()
            
            self.label_simplelook.grid(row=0, column=0)
            self.username_getter.grid(row=1, column=0)
            self.runSL.grid(row=2, column=0)
    
    def running_SL(self):
        inserted_input = self.username_getter.get()
        if not inserted_input:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert("0.0" , "Please enter a username for a simple lookup")
        else :
            ps_command = 'Get-ADUser -Identity "{}" -Properties MemberOf | Select-Object -ExpandProperty MemberOf | Get-ADGroup |Select-Object Name | Sort-Object Name'.format(self.username_getter.get())
            ps_output = subprocess.check_output(["powershell.exe", "-Command", ps_command], creationflags=subprocess.CREATE_NO_WINDOW)
            rez = (ps_output.decode("utf-8"))
            self.textbox.delete('1.0', 'end')
            self.textbox.insert("0.0", "Current user selected : " + inserted_input + "\n\n" + "All member of group : " + rez)
             
   
    def running_MID(self):
        inserted_input_from = format(self.source_from.get())
        inserted_input_to = format(self.source_to.get())
        if not inserted_input_from and inserted_input_to :
            self.textbox.delete('1.0', 'end')
            self.textbox.insert("0.0" , "Please specify a source user")
        elif not inserted_input_to and inserted_input_from :
            self.textbox.delete('1.0', 'end')
            self.textbox.insert("0.0" , "Please specify the clone user")
        elif not inserted_input_to and not inserted_input_from:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert("0.0" , "Please specify the source user to copy from and a user to paste to")
        
        else:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert("0.0", "Finding missing groups : \n\n" + "Source : " + inserted_input_from + "  -  " + "Real name here" + "\n\n" + "Clone : " + inserted_input_to + "  -  " + "Real name here")
            #creating pws script
            # PowerShell command to compare group memberships
            ps_command = f'''
            $groups_user_1 = Get-ADUser {inserted_input_to} -Properties MemberOf | ForEach-Object {{ $_.MemberOf | Get-ADGroup | Select-Object -ExpandProperty Name }};
            $groups_user_2 = Get-ADUser {inserted_input_from} -Properties MemberOf | ForEach-Object {{ $_.MemberOf | Get-ADGroup | Select-Object -ExpandProperty Name }};
            $missing_groups = Compare-Object $groups_user_1 $groups_user_2 | Where-Object {{ $_.SideIndicator -eq '=>' }} | Select-Object -ExpandProperty InputObject;
            $missing_groups
            '''
            #running
            try:
                #ps_output = subprocess.check_output(["powershell.exe", "-Command", ps_command], creationflags=subprocess.CREATE_NO_WINDOW)
                #ps_output = ps_command.communicate()[0].decode().strip()
                ps_process = subprocess.Popen(['powershell.exe', '-Command', ps_command], creationflags=subprocess.CREATE_NO_WINDOW, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                ps_output, ps_error = ps_process.communicate()
                ps_output = ps_output.decode().strip()
                #group_list = ps_output.split('\n')

                #rez = (ps_output.decode("utf-8"))
                self.textbox.delete('1.0', 'end')
                self.textbox.insert("0.0", inserted_input_to + " is missing all of these groups from " + inserted_input_from  + "\n\n" + ps_output)
            except subprocess.CalledProcessError as e:
                self.textbox.delete('1.0', 'end')
                self.textbox.insert("0.0" , "error try again")
                sys.exit(1)
        
        ####################### FONC. PASSWORD #######################
    
    def menu_password(self):
        #remove previous if it was the case
        frame_widgets = self.option_frame.winfo_children()
        for widget in frame_widgets:
            widget.grid_remove() 
            
        self.label_password.grid(row=0, column=0)    
        self.username_getter.grid(row=1, column=0)
        self.runPSSWRD.grid(row=2, column=0)
    
    def running_PSSWRD(self):
        inserted_input_pass = self.username_getter.get()
        if not inserted_input_pass:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert("0.0" , "Please specify a user to get the password info")
        else:
            ps_command = 'Get-ADUser -identity "{}" -properties PasswordLastSet, PasswordExpired, PasswordNeverExpires | ft Name, PasswordLastSet, PasswordExpired, PasswordNeverExpires'.format(inserted_input_pass)
            ps_output = subprocess.check_output(["powershell.exe", "-Command", ps_command], creationflags=subprocess.CREATE_NO_WINDOW)

            #Print the output
            rez = (ps_output.decode("utf-8"))
            self.textbox.delete('1.0', 'end')
            self.textbox.insert("0.0" ,rez)
   
        ####################### FONC. USER FINDER #######################

    def menu_finder(self):
        #remove previous if it was the case
        frame_widgets = self.option_frame.winfo_children()
        for widget in frame_widgets:
            widget.grid_remove() 
        
        self.label_first_name.grid(row=0, column=0)
        self.first_name.grid(row=1, column=0, padx=(20, 0), pady=(20, 20), sticky="nsew")
        self.label_last_name.grid(row=0, column=1)
        self.last_name.grid(row=1, column=1)
        self.runFIND.grid(row=2, column=0)
   
    def running_FIND(self):
        inserted_input_first_name = self.first_name.get()
        inserted_input_last_name = self.last_name.get()

        if not inserted_input_first_name and inserted_input_last_name:
            ps_command = 'Get-ADUser -Filter {{Surname -eq "{}"}} | Select-Object -Property SamAccountName'.format(inserted_input_last_name)
            ps_output = subprocess.check_output(["powershell.exe", "-Command", ps_command], creationflags=subprocess.CREATE_NO_WINDOW)
            rez = (ps_output.decode("utf-8"))
            self.textbox.delete('1.0', 'end')
            self.textbox.insert("0.0" ,rez)
        
        elif not inserted_input_last_name and inserted_input_first_name:
            ps_command = 'Get-ADUser -Filter {{ GivenName -eq "{}"}} | Select-Object -Property SamAccountName'.format(inserted_input_first_name)
            ps_output = subprocess.check_output(["powershell.exe", "-Command", ps_command], creationflags=subprocess.CREATE_NO_WINDOW)
            rez = (ps_output.decode("utf-8"))
            self.textbox.delete('1.0', 'end')
            self.textbox.insert("0.0" ,rez)
        
        elif not inserted_input_first_name and not inserted_input_last_name:
            self.textbox.delete('1.0', 'end')
            self.textbox.insert("0.0" , "Please enter either the first or last name of the user you are looking for")
    
        else:
            name = inserted_input_first_name + " " + inserted_input_last_name
            powershell_script = f"$searchString = '*{name}*'; $user = Get-ADUser -Filter {{ DisplayName -like $searchString }} | Select-Object -ExpandProperty SamAccountName; if ($user) {{ Write-Output \"The SamAccountName for {name} is: $user\" }} else {{ Write-Output \"No user found with the name {name}\" }}"
            process = subprocess.run(["powershell", "-Command", powershell_script], capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW)

            if process.returncode == 0:
                rez = (process.stdout.strip())
                self.textbox.delete('1.0', 'end')
                self.textbox.insert("0.0" ,rez)
            else:
                rez = (f"An error occurred: {process.stderr.strip()}")
                self.textbox.delete('1.0', 'end')
                self.textbox.insert("0.0" ,rez)
        
        ####################### FONC. MAIN LIST ALL #######################

    def running_main(self):
        main_input = self.main_entry.get()
        if not main_input :
            self.textbox.delete('1.0', 'end')
            self.textbox.insert("0.0" , "No user was found in the main entry.")
        else:
            # Set execution policy to bypass
            execution_policy = "-ExecutionPolicy Bypass"

            # PowerShell script to execute
            ps_script = f'''powershell.exe -ExecutionPolicy Bypass -Command "$Username = \\"{main_input}\\"; $UserObj = Get-ADUser -Filter {{SamAccountName -eq $Username}} -Properties *; if (!$UserObj) {{ Write-Host \\"User '{main_input}' not found in Active Directory\\"; exit }}; $PasswordLastSet = $UserObj.PasswordLastSet; $PasswordExpired = $UserObj.PasswordExpired; $LogonEvents = Get-WinEvent -FilterHashtable @{{Logname='Security';ID=4624;ProviderName='Microsoft-Windows-Security-Auditing';StartTime=(Get-Date).AddDays(-30);}} -ComputerName $env:COMPUTERNAME -MaxEvents 1000; $LastLogon = $LogonEvents | Where-Object {{$_.Properties[5].Value -eq $Username}} | Select-Object -First 1 | ForEach-Object {{$_.TimeCreated}}; $LastLogon = [DateTime]::Parse($LastLogon); $FullName = $UserObj.Name; $Computer = $LogonEvents | Where-Object {{$_.Properties[5].Value -eq $Username}} | Select-Object -First 1 | ForEach-Object {{$_.Properties[1].Value}}; Write-Output \\"User: $Username\\"; Write-Output \\"Password last set: $PasswordLastSet\\"; Write-Output \\"Password expired: $PasswordExpired\\"; Write-Output \\"Last logon: $LastLogon\\"; Write-Output \\"Full name: $FullName\\"; Write-Output \\"Last computer logged in to: $Computer\\";"'''


            # Use subprocess to execute the PowerShell script with execution policy set to bypass
            try:
                output = subprocess.check_output(ps_script, stderr=subprocess.STDOUT, creationflags=subprocess.CREATE_NO_WINDOW, shell=True)
                rez = output.decode()
                self.textbox.delete('1.0', 'end')
                self.textbox.insert("0.0" ,rez)
            except subprocess.CalledProcessError as e:
                rez = e.output.decode()
                self.textbox.delete('1.0', 'end')
                self.textbox.insert("0.0" ,"shit just hit the fan" + "\n\n" + rez)


            # Get the output and error message (if any) of the PowerShell script
            #output, error = process.communicate()

            # Print the output and error message (if any) of the PowerShell script
            #fuck = (error.decode())
                #self.textbox.delete('1.0', 'end')
            #self.textbox.insert("0.0" ,"shit just hit the fan" + "\n\n" + fuck)
            #rez = output.decode()
            #self.textbox.delete('1.0', 'end')
            ##elf.textbox.insert("0.0" ,rez)
            

    def change_appearance_mode_event(self, new_appearance_mode: str):
        CTk.set_appearance_mode(new_appearance_mode)   
        
root = CTk.CTk()
app = MainApplication(root)
app.pack()
root.mainloop()