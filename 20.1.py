import tkinter as tk


def convert_temperature():
    celsius = float(celsius_entry.get())
    fahrenheit = (celsius * 9 / 5) + 32
    fahrenheit_label.config(text=f"{fahrenheit:.2f} °F")


root = tk.Tk()
root.title("перетворювач темепратури ")

# Віджет для введення температури в Цельсіях
tk.Label(root, text="температура в цельсіях :").pack()
celsius_entry = tk.Entry(root)
celsius_entry.pack()

# Кнопка для конвертації
convert_button = tk.Button(root, text="перетворення", command=convert_temperature)
convert_button.pack()

# Віджет для відображення результату
fahrenheit_label = tk.Label(root, text="темепратура в ференгейтах : ")
fahrenheit_label.pack()

root.mainloop()
