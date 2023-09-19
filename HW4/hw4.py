from typing import List
from math import sqrt
import numpy as np


def pearson_correlation(numbers_1: List[float], numbers_2: List[float]) -> float:
    if len(numbers_1) != len(numbers_2):
        raise ValueError("Длина массивов должна быть одинаковой")

    n = len(numbers_1)

    # Расчет среднего значения для каждого массива
    numb_1 = sum(numbers_1) / n
    numb_2 = sum(numbers_2) / n

    # Вычисление ковариации и дисперсии для массивов numbers_1 и numbers_2
    covariance = sum((numbers_1[i] - numb_1) *
                     (numbers_2[i] - numb_2) for i in range(n))
    variance_numbers_1 = sum((x - numb_1) ** 2 for x in numbers_1)
    variance_numbers_2 = sum((y - numb_2) ** 2 for y in numbers_2)

    # Расчет корреляции Пирсона
    correlation = covariance / \
        (sqrt(variance_numbers_1) * sqrt(variance_numbers_2))

    return round(correlation)


mass_1 = np.random.randint(0, 100, size=5)
mass_2 = np.random.randint(0, 100, size=5)
print(f"Сгенирированные массивы: {mass_1} & {mass_2}")

correlation = pearson_correlation(mass_1, mass_2)
print(f"Корреляция Пирсона: {correlation}")
