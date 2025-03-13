from math import cbrt


def f(x):
    return x ** 3 - 10 * x + 2


def df(x):
    return 3 * x ** 2 - 10


def ddf(x):
    return 6 * x


# 1 Подпрограмма для нахождение интервала (a,b), который  содержит один и только один корень уравнения ближайший к 0
def interval(step=0.1, max_search=50):
    interspace = None
    distance = float('inf')

    x = -max_search
    while x < max_search:
        if f(x) * f(x + step) < 0:
            mid = (x + (x + step)) / 2
            dist = abs(mid)
            if dist < distance:
                distance = dist
                interspace = [x, x + step]
        x += step

    return interspace


# 2 Методы вычисления

# 2.1 - Метод диохотомии
def dichotomy_method(a, b, eps):
    left, right = a, b
    x = left

    while abs(f(x)) > eps:
        x = (left + right) / 2
        if f(x) * f(left) < 0:
            right = x
        else:
            left = x
    return x


# 2.2 - Метод порпорциональных частей (хорд)
def chord_method(a, b, eps):
    left, right = a, b

    if f(left) * ddf(left) > 0:
        X = left
        x = right
    else:
        X = right
        x = left
    while abs(f(x)) > eps:
        x = x - f(x) * (X - x) / (f(X) - f(x))

    return x


# 2.3 - Метод касательных (Ньютона)
def tangent_method(a, b, eps):
    left, right = a, b

    if f(left) * ddf(left) > 0:
        x0 = left
    else:
        x0 = right

    x = x0
    while abs(f(x)) > eps:
        x = x - f(x) / df(x)
    return x


# 2.4 - Модифицированный метод Ньютона
def mod_newton_method(a, b, eps):
    left, right = a, b

    if f(left) * ddf(left) > 0:
        x0 = left
    else:
        x0 = right

    x = x0
    while abs(f(x)) > eps:
        x = x - f(x) / df(x0)

    return x


# 2.5 - Комбинированный метод
def combined_method(a, b, eps):
    left, right = a, b

    if f(left) * ddf(left) > 0:
        x0 = left
        y0 = right
    else:
        x0 = right
        y0 = left

    x = x0
    y = y0
    while abs(y - x) > eps:
        x = x - f(x) / df(x)
        y = y - f(y) * (x - y) / (f(x) - f(y))

    return y


# 2.6 - Метод итераций


def iteration_method(a, b, eps):
    def phi(x):
        return cbrt(10 * x - 2)

    def alpha(x):
        return (x ** 3 + 2) / 10

    def phi2(x):
        return (5 * cbrt(2)) / (3 * cbrt((5 * x - 1) ** 2))

    left, right = a, b
    x = right
    if phi2(x) > 1:
        phi = alpha
    while True:
        x_new = phi(x)
        if abs(f(x_new)) < eps:
            return x_new
        x = x_new
