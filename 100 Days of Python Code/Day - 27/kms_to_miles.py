import tkinter

window = tkinter.Tk()
window.title("My First GUI Project")
window.minsize(width=200, height=50)
window.config(padx=20,pady=20)

#Entry
kms_entry = tkinter.Entry(width=10)
kms_entry.insert(tkinter.END, string="0")
kms_entry.grid(column=1, row=0)

#Label1
label1 = tkinter.Label(text='Kms')
label1.grid(column=2, row=0)

#Label2
label2 = tkinter.Label(text='is equal to')
label2.grid(column=0, row=1)

#KM_Label
miles_label = tkinter.Label(text='0')
miles_label.grid(column=1, row=1)

#Label3
label3 = tkinter.Label(text='Miles')
label3.grid(column=2, row=1)

def convert():
    kms = kms_entry.get()
    miles = int(kms) / 1.609
    miles_label['text'] = round(miles)

#Calculate_button

calculate = tkinter.Button(text='Calculate', command=convert)
calculate.grid(column=1, row=2)
window.mainloop()