import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
from methods import diagonal, expanded_matrix, inverse_matrix, norm, make_diagonally_dominant

def solve_slae():
    try:
        system = np.array([[1.7, -1.8, 1.9, -57.4],
                           [1.1, -4.3, 1.5, -1.7],
                           [1.2, 1.4, 1.6, 1.8],
                           [7.1, -1.3, -4.1, 5.2]])
        b = np.array([10, 19, 20, 10])
        E = np.eye(len(system))

        system_copy1 = np.copy(system)
        system_copy2 = np.copy(system)
        E_copy = np.copy(E)

        expand = expanded_matrix(system_copy1, E_copy)
        det_system, LU_matrix = diagonal(expand)
        cond = norm(system_copy2) * norm(inverse_matrix(LU_matrix))

        new_system, new_b = make_diagonally_dominant(system, b)
        X = np.copy(new_b)
        X_new = np.copy(new_b)

        max_iterations = 500
        tolerance = 0.001

        for iteration in range(max_iterations):
            for i in range(len(X)):
                s = sum(new_system[i, j] * X[j] for j in range(len(X)) if i != j)
                X_new[i] = (new_b[i] - s) / new_system[i, i]

            if np.sum(np.abs(X_new - X)) < tolerance:
                break
            X = X_new.copy()

        result_text.set(f"Определитель: {round(det_system, 4)}\n" +
                        f"Число обусловленности: {round(cond, 4)}\n" +
                        f"Решение: {X}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")

app = tk.Tk()
app.title("Решение СЛАУ")
app.geometry("600x450")
app.resizable(False, False)
app.configure(bg='#f0f0f0')

frame = tk.Frame(app, bg='#f0f0f0')
frame.pack(pady=20)

image = Image.open("image.png")
image = image.resize((400, 100), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(frame, image=photo, bg='#f0f0f0')
image_label.grid(row=0, column=0, pady=10)

tk.Label(frame, text="Решение СЛАУ для заданной системы", font=("Arial", 14, "bold"), bg='#f0f0f0').grid(row=1, column=0, pady=10)

solve_button = tk.Button(frame, text="Решить", command=solve_slae, font=("Arial", 12, "bold"), bg='#4caf50', fg='white', padx=15, pady=8, relief="raised", borderwidth=3)
solve_button.grid(row=2, column=0, pady=10)

result_frame = tk.Frame(frame, bg='#ffffff', bd=2, relief="groove")
result_frame.grid(row=3, column=0, pady=10, padx=10, ipadx=10, ipady=5)

result_text = tk.StringVar()
result_label = tk.Label(result_frame, textvariable=result_text, justify="left", font=("Arial", 12), bg='#ffffff', fg='#333')
result_label.pack(pady=5, padx=5)

tk.Label(app, text="Разработано с ❤️", font=("Arial", 10, "italic"), bg='#f0f0f0', fg='#555').pack(side="bottom", pady=5)

app.mainloop()
