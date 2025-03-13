from methods import interval, dichotomy_method, chord_method, tangent_method, mod_newton_method, combined_method, iteration_method, f

from tkinter.font import Font
from tkinter import Tk, Frame, Label, Entry, StringVar, OptionMenu, Button, SOLID

from matplotlib.pyplot import subplots
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.widgets import Cursor

from numpy import linspace

a, b = interval()
eps = 0.0001
print(dichotomy_method(a, b, eps))
print(chord_method(a, b, eps))
print(tangent_method(a, b, eps))
print(mod_newton_method(a, b, eps))
print(combined_method(a, b, eps))
print(iteration_method(a, b, eps))


def solve():
    eps = float(eps_entry.get())
    method = method_var.get()
    a, b = interval()

    if method == "Метод итераций":
        root = iteration_method(a, b, eps)
    elif method == "Метод диохотомии":
        root = dichotomy_method(a, b, eps)
    elif method == "Метод пропорциональных частей (хорд)":
        root = chord_method(a, b, eps)
    elif method == "Метод касательных (Ньютона)":
        root = tangent_method(a, b, eps)
    elif method == "Модифицированный метод Ньютона":
        root = mod_newton_method(a, b, eps)
    elif method == "Комбинированный метод":
        root = combined_method(a, b, eps)

    result_label.config(text=f"Найденный корень: {root:.6f}")
    ax.clear()
    x = linspace(-10, 10, 1000)
    ax.plot(x, f(x), label="x³ - 10x + 2", color='blue')
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)
    ax.plot(root, f(root), 'ro')
    ax.legend()
    canvas.draw()


def solve():
    eps = float(eps_entry.get())
    method = method_var.get()
    a, b = interval()

    if method == "Метод итераций":
        root_value = iteration_method(a, b, eps)
    elif method == "Метод диохотомии":
        root_value = dichotomy_method(a, b, eps)
    elif method == "Метод пропорциональных частей (хорд)":
        root_value = chord_method(a, b, eps)
    elif method == "Метод касательных (Ньютона)":
        root_value = tangent_method(a, b, eps)
    elif method == "Модифицированный метод Ньютона":
        root_value = mod_newton_method(a, b, eps)
    elif method == "Комбинированный метод":
        root_value = combined_method(a, b, eps)

    result_label.config(text=f"Найденный корень: {root_value:.8f}")
    ax.clear()
    x = linspace(-10, 10, 1000)
    ax.plot(x, f(x), label="x³ - 10x + 2", color='blue')
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)
    ax.plot(root_value, f(root_value), 'ro')
    ax.legend()
    canvas.draw()

root = Tk()
root.title("Решение уравнения")
root.configure(bg="#eaeaea")  # светлый серый фон
root.geometry("1000x800")
root.resizable(False, False)

frame = Frame(root, bg="#f3f3f3", padx=40, pady=40)  # светло-серый фон для фрейма
frame.pack(pady=20)

# Установка красивого шрифта
font_style = Font(family="Helvetica", size=12, weight="bold")

fig, ax = subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack()



cursor = Cursor(ax, useblit=True, color='gray', linewidth=1)

Label(frame, text="Погрешность:", bg="#f3f3f3", font=font_style).pack()
eps_entry = Entry(frame, font=font_style)
eps_entry.pack()
eps_entry.insert(0, "0.0001")

Label(frame, text="Метод:", bg="#f3f3f3", font=font_style).pack()
method_var = StringVar(root)
method_var.set("Метод итераций")
method_menu = OptionMenu(frame, method_var, "Метод диохотомии", "Метод пропорциональных частей (хорд)", "Метод касательных (Ньютона)", "Модифицированный метод Ньютона", "Комбинированный метод", "Метод итераций")
method_menu.config(font=font_style)
method_menu.pack()

Button(frame, text="Решить", command=solve, font=font_style, bg="#4CAF50", fg="white", relief=SOLID).pack(pady=10)
result_label = Label(frame, text="", bg="#f3f3f3", font=font_style)
result_label.pack()

x = linspace(-10, 10, 1000)
ax.plot(x, f(x), label="x³ - 10x + 2", color='blue')
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.legend()
canvas.draw()

toolbar = NavigationToolbar2Tk(canvas, frame)
toolbar.update()
root.mainloop()
