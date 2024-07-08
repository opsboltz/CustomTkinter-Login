import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox


def Main_Menu():
    login.withdraw()  # Hide the login frame
    new_frame = ctk.CTk()
    new_frame.title("Main Menu")
    new_frame.geometry("800x600")

    label = ctk.CTkLabel(new_frame, text="Welcome Admin", font=("Times New Roman", 32))
    label.pack(pady=20, padx=10)

    new_frame.mainloop()

##Login
def Login():
    Username = entry1.get()
    Password = entry2.get()
    if Username == "admin" and Password == "pass":
        messagebox.showinfo("Login Successful", "You have logged in successfully!")
        Main_Menu()
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password")


login = ctk.CTk()
login.title("Login")
login.geometry("580x350")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Middle Frame
frame = ctk.CTkFrame(login)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Label in frame
label = ctk.CTkLabel(frame, text="Login System", font=("Cosmic", 26))
label.pack(pady=14, padx=10)

# Entry Widgets in frame
entry1 = ctk.CTkEntry(frame, placeholder_text="Username", corner_radius=10, width=180)
entry1.pack(pady=14, padx=10)
entry2 = ctk.CTkEntry(frame, placeholder_text="Password", show="*", corner_radius=10, width=180)
entry2.pack(pady=14, padx=10)


# Login Button
button = ctk.CTkButton(frame, text="Login", command=Login, corner_radius=10)
button.pack(pady=12, padx=10)

##END OF LOGIN


login.mainloop()