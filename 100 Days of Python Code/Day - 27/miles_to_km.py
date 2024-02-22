import tkinter

window = tkinter.Tk()
window.title("My First GUI Project")
window.minsize(width=200, height=50)
window.config(padx=20,pady=20)

#Entry
miles_entry = tkinter.Entry(width=10)
miles_entry.insert(tkinter.END, string="0")
miles_entry.grid(column=1, row=0)

#Label1
label1 = tkinter.Label(text='Miles')
label1.grid(column=2, row=0)

#Label2
label2 = tkinter.Label(text='is equal to')
label2.grid(column=0, row=1)

#KM_Label
km_label = tkinter.Label(text='0')
km_label.grid(column=1, row=1)

#Label3
label3 = tkinter.Label(text='Km')
label3.grid(column=2, row=1)

def convert():
    miles = miles_entry.get()
    kms = int(miles) * 1.609
    km_label['text'] = round(kms)

#Calculate_button

calculate = tkinter.Button(text='Calculate', command=convert)
calculate.grid(column=1, row=2)
window.mainloop()