from customtkinter import *

app = CTk()

app.geometry('500x400')
set_appearance_mode('dark')

btn = CTkButton(master=app, text='click me', corner_radius=32, fg_color='#C850C0', hover_color='#4158D0')

btn.place(relx=0.5, rely=0.5, anchor='center')

app.mainloop()