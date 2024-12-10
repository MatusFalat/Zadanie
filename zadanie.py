import tkinter as tk
from tkinter import messagebox

def process_names():
    # Pole 10 krstných mien
    names = ["julia", "adam", "matej", "zuzana", "peter", "katarina", "lucia", "martin", "jan", "eva"]

    # Zoradenie podľa abecedy
    names.sort()

    # Výber prvého, piateho a desiateho mena
    first_name = names[0]
    fifth_name = names[4]
    tenth_name = names[9]

    # Prevod všetkých mien na veľké písmená a pridanie poradových čísel
    names_upper = [f"{i+1}. {name.upper()}" for i, name in enumerate(names)]

    # Zobrazenie výsledkov v GUI
    result = (
        f"Zoradzované mená: {', '.join(names)}\n"
        f"\nPrvé meno: {first_name}\n"
        f"Piate meno: {fifth_name}\n"
        f"Desiate meno: {tenth_name}\n\n"
        f"Mená veľkými písmenami + poradové čísla:\n" + "\n".join(names_upper)
    )

    messagebox.showinfo("Výsledok", result)

# Vytvorenie hlavného okna
root = tk.Tk()
root.title("Python Zadanie 2024/2025 Matúš Falat")
root.geometry("850x350")

# Nastavenie vlastného pozadia
background_image = tk.PhotoImage(file="")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Názov aplikácie
label_title = tk.Label(root, text="Programovacie techniky", font=("Arial", 16), bg="lightblue")
label_title.pack(pady=10)

# Meno a priezvisko
label_name = tk.Label(root, text="Matúš Falat", font=("Arial", 14), bg="lightblue")
label_name.pack(pady=5)

# Zadanie úlohy
label_task = tk.Label(root, text="Zadanie úlohy: Vytvorte pole 10 krstných mien z malých písmen (manuálne), zoraďte ich podľa abecedy,\n vypíšte prvé, piate a 10 meno, zmeňte všetky písmená na veľké a vypíšte celý zoznam aj s poradovými číslami.", font=("Arial", 10), bg="lightblue")
label_task.pack(pady=5)

# Tlačidlo na spustenie programu
task_button = tk.Button(root, text="Spustiť program", font=("Arial", 14), command=process_names, bg="lightblue")
task_button.pack(pady=20)

# Spustenie hlavnej slučky
root.mainloop()
