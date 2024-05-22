import year_checker as yc
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

def check_year():
    value = year_entry.get()
    result_statement = "Ar įvesti metai " + value + " yra keliamieji? "
    
    if not value.isnumeric() or int(value) < 0:
        messagebox.showerror("Klaida", "Neteisingai įvesti duomenys.")
        return
    if yc.is_leap_year(int(value)):
        result_statement = result_statement + "Taip"
    else:
        result_statement = result_statement + "Ne"
    result_text_box.insert(INSERT, result_statement)
    result_text_box.insert(END, "\n")
    
def check_year_range():
    value_from = year_entry_from.get()
    value_to = year_entry_to.get()
    
    if not value_from.isnumeric() or \
        int(value_from) < 0 or \
        not value_to.isnumeric() or \
        int(value_to) < 0 or \
        int(value_from) > int(value_to):
            
        messagebox.showerror("Klaida", "Neteisingai įvesti duomenys.")
        return
   
    result = yc.leap_year_list(int(value_from), int(value_to) + 1)
    for year in result:
        result_text_box.insert(INSERT, year)
        result_text_box.insert(END, "\n")

window = Tk()
window.geometry("900x500")
window.title("Keliamųjų metų skaičiuoklė")
window.resizable(width=False, height=False)

leap_year_frame = Frame(window, highlightbackground="black", highlightthickness=1)
leap_year_frame.pack(pady=10)
year_label = Label(leap_year_frame, text="Metai: ")
year_label.grid(row=0, column=0, pady=15, padx=20)

year_entry = Entry(leap_year_frame, width=6, justify=CENTER)
year_entry.grid(row=0, column=1, padx=50)

year_submit_button = Button(leap_year_frame, text="Tikrinti", command=check_year)
year_submit_button.grid(row=0, column=2, padx=15)
result = Label(leap_year_frame, justify=LEFT)
result.grid(row=1, column=0, columnspan=3)



leap_year_range_frame = Frame(window, highlightbackground="black", highlightthickness=1)
leap_year_range_frame.pack(pady=10)

year_label_from = Label(leap_year_range_frame, text="Metai: ")
year_label_from.grid(row=0, column=0, pady=15, padx=5)

year_entry_from = Entry(leap_year_range_frame, width=6, justify=CENTER)
year_entry_from.grid(row=0, column=1, padx=15)

year_label_to = Label(leap_year_range_frame, text=" - ")
year_label_to.grid(row=0, column=2, pady=15)

year_entry_to = Entry(leap_year_range_frame,width=6, justify=CENTER)
year_entry_to.grid(row=0, column=3, padx=15)


year_submit_range_button = Button(leap_year_range_frame, text="Tikrinti", command=check_year_range)
year_submit_range_button.grid(row=0, column=4, padx=15)
result_range = Label(leap_year_range_frame, justify=LEFT)
result_range.grid(row=1, column=0, columnspan=3)




result_text_box = ScrolledText(window, width=45, height=15)
result_text_box.pack()



window.mainloop()