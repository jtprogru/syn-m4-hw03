from django.http import HttpResponse
import random


def game_view(request):
    numbers = [random.randint(0, 3) for _ in range(3)]  # Генерация трех случайных чисел
    if numbers[0] == numbers[1] == numbers[2]:  # Проверка, равны ли все числа
        message = f"Победа, все 3 числа равны! Числа: {numbers}"
    else:
        message = f"Повезет в следующий раз! Числа: {numbers}"
    return HttpResponse(message)
