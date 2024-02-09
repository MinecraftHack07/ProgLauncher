import minecraft_launcher_lib as mll
import subprocess
import customtkinter as CTk
from PIL import Image



# current_max = 0


# def set_status(status: str):
#     print(status)


# def set_progress(progress: int):
#     if current_max != 0:
#         print(f"{progress}/{current_max}")


# def set_max(new_max: int):
#     global current_max
#     current_max = new_max





class App(CTk.CTk):
    def __init__(self):
        super().__init__()
        CTk.set_default_color_theme("blue")
        self.geometry("934x525")
        self.title("Launcher")
        
        self.resizable(False, False)
        self.bg = CTk.CTkImage(dark_image=Image.open('images/bg.png'),size=(934,525))
        self.img = CTk.CTkImage(dark_image=Image.open('images/Prog.jpg'),size=(100,100))
        self.bg_label = CTk.CTkLabel(master=self, text="", image=self.bg)
        self.bg_label.grid(row=0,column=0)
        CTk.set_appearance_mode("Dark")
        


        


        self.frame = CTk.CTkFrame(master=self, fg_color="transparent",width=330, height=934)
        self.frame.place(x=0,y=0)


        self.moon = CTk.CTkImage(dark_image=Image.open('images/moon.png'),size=(50,50))
        self.dark_button = CTk.CTkButton(master=self.frame, hover_color="#202020", text="",bg_color="transparent", fg_color="transparent", width=50, height=50,font=("Comic Sans MS",30), image=self.moon, command=self.Light)
        self.dark_button.place(x=10, y=14)
        
        self.sun = CTk.CTkImage(dark_image=Image.open('images/sun.png'), size=(50,50))
        self.light_button = CTk.CTkButton(master=self.frame, hover_color="#E0E0E0", text="", bg_color="transparent", fg_color="transparent", width=50, height=50,font=("Comic Sans MS",30), image=self.sun, command=self.Dark)
        self.light_button.place(x=10, y=14)
        self.light_button.place_forget()
        




        self.theame = CTk.CTkButton(master=self, text="🌙")



        self.error = CTk.CTkLabel(master=self.frame, text="ERROR: Username is incorrect!", font=("Comic Sans Ms", 15), text_color="#FF0000")


        self.img_label = CTk.CTkLabel(master=self.frame, text="", image=self.img)

        self.username = CTk.CTkEntry(master=self.frame, font=("Comic Sans MS",15), placeholder_text="Username",placeholder_text_color="#90AAF2",width=290,height=50, text_color="#90AAF2",border_color="#5D87F7")
        self.username.place(x=19, y=220)
        
        self.enter = CTk.CTkButton(master=self.frame, text="Играть", width=230, height=70,font=("Comic Sans MS",30), command=command)
        self.enter.place(x=48,y=400)
        self.img_label.place(x=114,y=70)
 
        # self.version = CTk.CTkOptionMenu(master=self.frame, dynamic_resizing=True, values=["1.0","1.1","1.2.1","1.2.2","1.2.3","1.2.4","1.2.5","1.3.1","1.3.2","1.4.2","1.4.3","1.4.4","1.4.5","1.4.5","1.4.6","1.4.7","1.5.2","1.5.1","1.6.1","1.6.2","1.6.4","1.7.2","1.7.3","1.7.4","1.7.5","1.7.6","1.7.7","1.7.8","1.7.9","1.7.9","","",""])
        # self.version.place(x=18, y=300)
        self.version = CTk.CTkEntry(master=self.frame, font=("Comic Sans MS",15), placeholder_text="Version",placeholder_text_color="#90AAF2",width=90,height=50, text_color="#90AAF2",border_color="#5D87F7")
        self.version.place(x=19, y=300)
        self.forge = CTk.CTkCheckBox(master=self.frame, border_color="#5D87F7", text_color="#90AAF2", text="Forge", fg_color="#5D87F7", font=("Comic Suns MS", 15))
        self.forge.place(x=130,y=315)
        self.fabric = CTk.CTkCheckBox(master=self.frame, border_color="#5D87F7", text_color="#90AAF2", text="Fabric", fg_color="#5D87F7", font=("Comic Suns MS", 15))
        self.fabric.place(x=225,y=315)
        # self.v_label = CTk.CTkLabel(master=self.frame, text="Version:", font=("Comic Sans Ms", 37), text_color="#5D87F7")
        # self.v_label.place(x=30, y=293)
        self.error2 = CTk.CTkLabel(master=self.frame, text="ERROR: Version is incorrect!", font=("Comic Sans MS", 15), text_color="#FF0000")
        self.error3 = CTk.CTkLabel(master=self.frame, text="ERROR: Choose one thing!", font=("Comic Sans MS", 15), text_color="#FF0000")
        self.error4 = CTk.CTkLabel(master=self.frame, text="ERROR: This version doesn't support fabric!", font=("Comic Sans MS", 15), text_color="#FF0000")










    def Dark(self):
        self.light_button.place_forget()
        CTk.set_appearance_mode("Dark")
        self.dark_button.place(x=10, y=14)
        
    def Light(self):
        self.dark_button.place_forget()
        CTk.set_appearance_mode("light")
        self.light_button.place(x=10, y=14)




def command(): 
    app.error.place_forget()
    app.error2.place_forget()
    app.error3.place_forget()
    app.error4.place_forget()
    NIKNAME = app.username.get()
    VERSION = app.version.get()
    if NIKNAME == "":
        app.error.place(x=50, y=350)
    elif VERSION == "":
        app.error2.place(x=50, y=350)
    elif app.forge.get() == 1 and app.fabric.get() == 1:
        app.error3.place(x=60, y=350)
    elif app.forge.get() == 1:
    #     callback = {
    # "setStatus": set_status,
    # "setProgress": set_progress,
    # "setMax": set_max
    #     }
        app.destroy()
        options = {
            'username' : NIKNAME,
            'uuid' : '',
            'token' : ''
        }
        forge_version = mll.forge.find_forge_version(VERSION)
        
        
        mll.forge.install_forge_version(forge_version, '.mjnlauncher')
        v = forge_version.split("-")
        print(v)
        VERSION = v[0] + "-forge-" + v[1] 
        
        subprocess.call(mll.command.get_minecraft_command(version=VERSION, minecraft_directory='.mjnlauncher', options=options))
    elif app.fabric.get() == 1:
        version_fabric_true = mll.fabric.is_minecraft_version_supported(VERSION)
        if version_fabric_true == False:
            app.error4.place(x=10,y=350)
        else:
            app.destroy()
    #         callback = {
    # "setStatus": set_status,
    # "setProgress": set_progress,
    # "setMax": set_max
            # }
            options = {
                'username' : NIKNAME,
                'uuid' : '',
                'token' : ''
            }
            loader = "0.15.6"
            print(loader)
            mll.fabric.install_fabric(VERSION, ".mjnlauncher", loader)
            subprocess.call(mll.command.get_minecraft_command(version=f"fabric-loader-{loader}-{VERSION}", minecraft_directory='.mjnlauncher', options=options))



        
    else:
        app.destroy()
    #     callback = {
    # "setStatus": set_status,
    # "setProgress": set_progress,
    # "setMax": set_max
    #     }
        
        # mll.install.install_minecraft_version(versionid=VERSION, minecraft_directory='.mjnlauncher')
        mll.install.install_minecraft_version(versionid=VERSION, minecraft_directory='.mjnlauncher')
        options = {
            'username' : NIKNAME,
            'uuid' : '',
            'token' : ''
        }

        

        subprocess.call(mll.command.get_minecraft_command(version=VERSION, minecraft_directory='.mjnlauncher', options=options))
        



app = App()
app.mainloop()


