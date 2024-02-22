import tkinter

window = tkinter.Tk()
window.title("My First GUI Project")
window.minsize(width=500, height=500)
window.config(padx=20,pady=20)
#Label
my_label = tkinter.Label(text='I am a Label', font=("Arial",24,"bold"))
my_label.grid(column=0, row=0)

#Button

def button_clicked():
    my_label['text'] = my_entry.get()

my_button = tkinter.Button(text='Click Me', command=button_clicked)
my_button.grid(column=1, row=1)

my_button2 = tkinter.Button(text='New Button')
my_button2.grid(column=2, row=0)

#Entry
my_entry = tkinter.Entry(width=20)
my_entry.grid(column=3, row=2)

window.mainloop()