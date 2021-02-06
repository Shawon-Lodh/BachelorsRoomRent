from tkinter import *
from tkinter import messagebox


def statechange(condition):
    if condition == 0:
        Shawon_field.config(state="disable")
        Arup_field.config(state="disable")
        Rafsan_field.config(state="disable")
        Shanto_field.config(state="disable")
    elif condition == 1:
        Shawon_field.config(state="normal")
        Arup_field.config(state="normal")
        Rafsan_field.config(state="normal")
        Shanto_field.config(state="normal")


def clearall():
    statechange(1)
    Houserent_field.delete(0, END)
    Bua_field.delete(0, END)
    Internet_field.delete(0, END)
    MoylaBill_field.delete(0, END)
    GasBill_field.delete(0, END)
    Extra_field.delete(0, END)

    Shawon_field.delete(0, END)
    Arup_field.delete(0, END)
    Rafsan_field.delete(0, END)
    Shanto_field.delete(0, END)

    Bua_field.insert(10, str(2200))
    Internet_field.insert(10, str(800))
    MoylaBill_field.insert(10, str(100))
    GasBill_field.insert(10, str(0))
    Extra_field.insert(10, str(0))

    statechange(0)


def checkerror():
    if (Houserent_field.get() == "" or
            Bua_field.get() == "" or
            Internet_field.get() == "" or
            MoylaBill_field.get() == "" or
            GasBill_field.get() == "" or
            Extra_field.get() == ""):
        # show the error message
        messagebox.showerror("Input Error,Please check all the input box")
        return -1
    if (any(c.isalpha() for c in Houserent_field.get()) == True or
            any(c.isalpha() for c in Bua_field.get()) == True or
            any(c.isalpha() for c in Internet_field.get()) == True or
            any(c.isalpha() for c in MoylaBill_field.get()) == True or
            any(c.isalpha() for c in GasBill_field.get()) == True or
            any(c.isalpha() for c in Extra_field.get()) == True):
        # show the error message
        messagebox.showerror("Input Error,Please check That you give all the inpot like a number")
        return -1


def calcualte_result():
    value = checkerror()
    if value == -1:
        return
    else:
        pani_current = int(Houserent_field.get()) - 13000
        bua = int(Bua_field.get())
        internet = int(Internet_field.get())
        moyla = int(MoylaBill_field.get())
        gass = int(GasBill_field.get())
        extra = int(Extra_field.get())

        per_person_rent_without_vhara = (pani_current + bua + internet + moyla + gass + extra) / 4
        Takar_amount_for_shawon = 2500 + per_person_rent_without_vhara
        Takar_amount_for_arup = 3500 + per_person_rent_without_vhara
        Takar_amount_for_rafsan = 3500 + per_person_rent_without_vhara
        Takar_amount_for_shanto = 3500 + per_person_rent_without_vhara

        statechange(1)
        Shawon_field.insert(10, str(Takar_amount_for_shawon))
        Arup_field.insert(10, str(Takar_amount_for_arup))
        Rafsan_field.insert(10, str(Takar_amount_for_rafsan))
        Shanto_field.insert(10, str(Takar_amount_for_shanto))
        statechange(0)


if __name__ == "__main__":
    # Create a GUI window
    gui = Tk()

    # Set the background colour of GUI window
    gui.configure(background="light green")

    # set the name of tkinter GUI window
    gui.title("House Rent")

    # Set the configuration of GUI window
    gui.geometry("300x350")

    # heading Label
    Heading1 = Label(gui, text="Total House Rent Bill", bg="blue", font=16)
    Heading2 = Label(gui, text="Per Person Bill", bg="blue", font=16)

    # Heading Label position
    Heading1.grid(row=0, column=1)
    Heading2.grid(row=8, column=1)

    # gap label
    gap = Label(gui, bg="light green")

    # gap Label position
    gap.grid(row=13, column=1)

    # All label
    Houserent = Label(gui, text="Houserent : ", bg="light green", font=16)
    Bua = Label(gui, text="Bua : ", bg="light green", font=16)
    Internet = Label(gui, text="Internet : ", bg="light green", font=16)
    MoylaBill = Label(gui, text="Moyla : ", bg="light green", font=16)
    GasBill = Label(gui, text="Gass : ", bg="light green", font=16)
    Extra = Label(gui, text="Extra : ", bg="light green", font=16)
    Shawon = Label(gui, text="Shawon's bill : ", bg="light green", font=16)
    Arup = Label(gui, text="Arup's bill : ", bg="light green", font=16)
    Rafsan = Label(gui, text="Rafsan's bill : ", bg="light green", font=16)
    Shanto = Label(gui, text="Shanto's bill : ", bg="light green", font=16)

    # All label position
    Houserent.grid(row=2, column=1)
    Bua.grid(row=3, column=1)
    Internet.grid(row=4, column=1)
    MoylaBill.grid(row=5, column=1)
    GasBill.grid(row=6, column=1)
    Extra.grid(row=7, column=1)

    Shawon.grid(row=9, column=1)
    Arup.grid(row=10, column=1)
    Rafsan.grid(row=11, column=1)
    Shanto.grid(row=12, column=1)

    # All entry field
    Houserent_field = Entry(gui)
    Bua_field = Entry(gui, textvariable=StringVar(gui, value='2200'))
    Internet_field = Entry(gui, textvariable=StringVar(gui, value='800'))
    MoylaBill_field = Entry(gui, textvariable=StringVar(gui, value='100'))
    GasBill_field = Entry(gui, textvariable=StringVar(gui, value='0'))
    Extra_field = Entry(gui, textvariable=StringVar(gui, value='0'))

    Shawon_field = Entry(gui, state="disable")
    Arup_field = Entry(gui, state="disable")
    Rafsan_field = Entry(gui, state="disable")
    Shanto_field = Entry(gui, state="disable")

    # All entry field position
    Houserent_field.grid(row=2, column=2)
    Bua_field.grid(row=3, column=2)
    Internet_field.grid(row=4, column=2)
    MoylaBill_field.grid(row=5, column=2)
    GasBill_field.grid(row=6, column=2)
    Extra_field.grid(row=7, column=2)

    Shawon_field.grid(row=9, column=2)
    Arup_field.grid(row=10, column=2)
    Rafsan_field.grid(row=11, column=2)
    Shanto_field.grid(row=12, column=2)

    # all button field
    FindResult = Button(gui, text="Find Amount", fg="Black", bg="Red", command=calcualte_result)
    ClearAll = Button(gui, text="Clear All", fg="Black", bg="Red", command=clearall)
    # all button position
    FindResult.grid(row=14, column=1)
    ClearAll.grid(row=14, column=2)
    # Start the GUI
    gui.mainloop()
