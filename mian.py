import tkinter as tk
from tkinter import ttk, font

window = tk.Tk()
window.title('window')
window.geometry('400x300')

#print(font.families())

style = ttk.Style()
#style.theme_use('clam')

#style.configure('string', background='green')
style.configure('new.TButton', foreground='cyan', font=('System', 20))
style.map('new.TButton',
          foreground=[('pressed', 'red'), ('disabled', 'yellow')],
          background=[('pressed', 'green'), ('active', 'blue')])

label = ttk.Label(window,
                  text='a label\nsecond line',
                  background='cyan',
                  foreground='blue',
                  font=('System', 20),
                  justify='center'
                  )
label.pack()

button = ttk.Button(window, text='button', style='new.TButton')
button.pack()

window.mainloop()