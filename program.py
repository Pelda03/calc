import tkinter as tk

def pridat():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result.set(num1 + num2)
    except ValueError:
        result.set("Nespravny vstup")

def odcitat():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result.set(num1 - num2)
    except ValueError:
        result.set("Nespravny vstup")

def nasobit():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result.set(num1 * num2)
    except ValueError:
        result.set("Nespravny vstup")

def delit():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            result.set("Nelze delit nulou")
        else:
            result.set(num1 / num2)
    except ValueError:
        result.set("Nespravny vstup")

# Vytvoření hlavního okna
root = tk.Tk()
root.title("Kalkulačka")

# Vytvoření vstupních polí pro čísla
label_num1 = tk.Label(root, text="Prvni cislo:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Druhe cislo:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Vytvoření tlačítek pro operace
button_pridat = tk.Button(root, text="Přidat", command=pridat)
button_pridat.pack()

button_odcitat = tk.Button(root, text="Odčítat", command=odcitat)
button_odcitat.pack()

button_nasobit = tk.Button(root, text="Násobit", command=nasobit)
button_nasobit.pack()

button_delit = tk.Button(root, text="Dělit", command=delit)
button_delit.pack()

# Vytvoření proměnné pro výsledek
result = tk.StringVar()
result.set("Výsledek: ")
label_result = tk.Label(root, textvariable=result)
label_result.pack()

# Spuštění hlavní smyčky Tkinter
root.mainloop()
