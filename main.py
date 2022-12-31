from tkinter import *


def button_clicked():
    miles = input.get()
    result = float(miles) * 1.609344
    converted_num.config(text=result)

window = Tk()
window.title("Mike to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

input = Entry(width=10)
input.grid(column=2, row=1)

input_label = Label(text="Miles", font=("Arial", 18))
input_label.grid(column=3, row=1)

equals_label = Label(text="is equal to", font=("Arial", 18))
equals_label.grid(column=1, row=2)

converted_num = Label(text=0, font=("Arial", 18))
converted_num.grid(column=2, row=2)

km_label = Label(text="Km", font=("Arial", 18))
km_label.grid(column=3, row=2)

button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)




window.mainloop()