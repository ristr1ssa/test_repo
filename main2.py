import tkinter as tk
import numpy as np
from scipy.integrate import solve_ivp


def lorenz(t, state, sigma, rho, beta):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]


def solve_lorenz(sigma, rho, beta, t_span, y0, num_points):
    t_eval = np.linspace(t_span[0], t_span[1], num_points)
    solution = solve_ivp(lorenz, t_span, y0, args=(sigma, rho, beta), t_eval=t_eval)
    return solution


root = tk.Tk()
root.title("Аттрактор Лоренца")
canvas = tk.Canvas(root, width=800, height=600, bg='white')
canvas.pack()


sigma = 10
rho = 28
beta = 8/3
y0 = [0.0, 0.0, 1.0]  # Начальное положение точки
t_span = (0, 100)  # Временной интервал
num_points = 10000  # Количество точек для численного решения


solution = solve_lorenz(sigma, rho, beta, t_span, y0, num_points)
x_points, y_points, z_points = solution.y


def update_point(i):
    x = int(400 + x_points[i] * 10)  # Масштабируем координаты для отображения
    y = int(300 + y_points[i] * 10)
    canvas.delete("point")  # Удаляем предыдущую точку
    canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="red", tags="point")  # Рисуем точку
    root.after(10, update_point, (i + 1) % num_points)  # Обновляем точку с заданной задержкой


update_point(1)
root.mainloop()
