import os
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk
from backend.backend import calculate_values, get_index_price


def calculate(entry_multiplier=None, target_multiplier=None, stop_loss_multiplier=None):
    entry_price = entry_var.get()
    entry, target, stop_loss = calculate_values(entry_price, entry_multiplier, target_multiplier, stop_loss_multiplier)
    entry_result_var.set("{:.2f}".format(entry))
    target_result_var.set("{:.2f}".format(target))
    stop_loss_result_var.set("{:.2f}".format(stop_loss))


def update_indices():
    x = nifty_price_var.get()
    y = sensex_price_var.get()
    if x == '':
        x = '0'
        y = '0'
    previous_nifty_price = float(x)
    previous_sensex_price = float(y)

    nifty_price, sensex_price = get_index_price()
    nifty_price_var.set("{:.2f}".format(nifty_price))
    sensex_price_var.set("{:.2f}".format(sensex_price))

    update_logos(previous_nifty_price, previous_sensex_price, nifty_price, sensex_price)

    root.after(3000, update_indices)


def close():
    root.destroy()


def update_logos(previous_nifty_price, previous_sensex_price, new_nifty_price, new_sensex_price):
    if new_nifty_price > previous_nifty_price:
        up_nifty_logo_label.grid(row=1, column=6, padx=5, pady=5, sticky=tk.W)
        down_nifty_logo_label.grid_forget()
    elif new_nifty_price < previous_nifty_price:
        down_nifty_logo_label.grid(row=1, column=6, padx=5, pady=5, sticky=tk.W)
        up_nifty_logo_label.grid_forget()
    # else:
    #     up_nifty_logo_label.grid_forget()
    #     down_nifty_logo_label.grid_forget()

    if new_sensex_price > previous_sensex_price:
        up_sensex_logo_label.grid(row=2, column=6, padx=5, pady=5, sticky=tk.W)
        down_sensex_logo_label.grid_forget()
    elif new_sensex_price < previous_sensex_price:
        down_sensex_logo_label.grid(row=2, column=6, padx=5, pady=5, sticky=tk.W)
        up_sensex_logo_label.grid_forget()
    # else:
    #     up_sensex_logo_label.grid_forget()
    #     down_sensex_logo_label.grid_forget()


root = tk.Tk()
root.title('BankNifty')
root.configure(bg='#f0f0f0')

style = ThemedStyle(root)
style.set_theme('breeze')

style.configure('TButton', font=('Arial', 12))
style.configure('TEntry', font=('Arial', 12))

frame = ttk.Frame(root, padding=20)
frame.grid(row=0, column=0, sticky="news")

entry_var = tk.StringVar()
entry_label = ttk.Label(frame, text="Current Market Price:")
entry_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
entry_entry = ttk.Entry(frame, textvariable=entry_var)
entry_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

button_frame = ttk.Frame(frame)
button_frame.grid(row=1, column=0, columnspan=2, pady=10)

button_style = {'padding': (10, 5)}

B1 = ttk.Button(button_frame, text="Monday", command=lambda: calculate(1.3, 1.14, 0.85), **button_style)
B1.grid(row=0, column=0, padx=5)

B2 = ttk.Button(button_frame, text="Tuesday", command=lambda: calculate(1.3, 1.15, 0.85), **button_style)
B2.grid(row=0, column=1, padx=5)

b3 = ttk.Button(button_frame, text="Wednesday", command=lambda: calculate(1.4, 1.2, 0.8), **button_style)
b3.grid(row=0, column=2, padx=5)

B4 = ttk.Button(button_frame, text="Thursday", command=lambda: calculate(1.5, 1.25, 0.75), **button_style)
B4.grid(row=0, column=3, padx=5)

B5 = ttk.Button(button_frame, text="Friday", command=lambda: calculate(1.2, 1.1, 0.9), **button_style)
B5.grid(row=0, column=4, padx=5)

B6 = ttk.Button(button_frame, text="Exit", command=close, **button_style)
B6.grid(row=0, column=6, padx=5)

result_frame = ttk.Frame(frame)
result_frame.grid(row=2, column=0, columnspan=2, pady=10)

entry_result_var = tk.StringVar()
entry_result_label = ttk.Label(result_frame, text="Entry:")
entry_result_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
entry_result_entry = ttk.Entry(result_frame, textvariable=entry_result_var, state='readonly')
entry_result_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

target_result_var = tk.StringVar()
target_result_label = ttk.Label(result_frame, text="Target:")
target_result_label.grid(row=0, column=2, padx=5, pady=5, sticky=tk.E)
target_result_entry = ttk.Entry(result_frame, textvariable=target_result_var, state='readonly')
target_result_entry.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)

stop_loss_result_var = tk.StringVar()
stop_loss_result_label = ttk.Label(result_frame, text="Stop Loss:")
stop_loss_result_label.grid(row=0, column=4, padx=5, pady=5, sticky=tk.E)
stop_loss_result_entry = ttk.Entry(result_frame, textvariable=stop_loss_result_var, state='readonly')
stop_loss_result_entry.grid(row=0, column=5, padx=5, pady=5, sticky=tk.W)

nifty_frame = ttk.Frame(frame)
nifty_frame.grid(row=3, column=0, columnspan=1, pady=10)

nifty_price_var = tk.StringVar()
nifty_price_label = ttk.Label(nifty_frame, text="Nifty 50 Price:")
nifty_price_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
nifty_price_entry = ttk.Entry(nifty_frame, textvariable=nifty_price_var, state='readonly')
nifty_price_entry.grid(row=1, column=1, columnspan=5, padx=5, pady=5, sticky=tk.W)

sensex_price_label = ttk.Label(nifty_frame, text="Sensex Price:")
sensex_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.E)
sensex_price_var = tk.StringVar()
sensex_price_entry = ttk.Entry(nifty_frame, textvariable=sensex_price_var, state='readonly')
sensex_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)


up_image = Image.open(os.path.dirname(os.getcwd())+"\\resources\\up.png")
width, height = 20, 20
resized_image = up_image.resize((width, height))
tk_up_image = ImageTk.PhotoImage(resized_image)

down_image = Image.open(os.path.dirname(os.getcwd())+"\\resources\\down.png")
width, height = 20, 20
resized_image = down_image.resize((width, height))
tk_down_image = ImageTk.PhotoImage(resized_image)

up_nifty_logo_label = ttk.Label(nifty_frame, image=tk_up_image)
down_nifty_logo_label = ttk.Label(nifty_frame, image=tk_down_image)
up_sensex_logo_label = ttk.Label(nifty_frame, image=tk_up_image)
down_sensex_logo_label = ttk.Label(nifty_frame, image=tk_down_image)
update_indices()

root.mainloop()
