import math
print("Приветствую тебя, введи положительное чилсо")

while True:
    try:
        num = int(input("Введите положительное число: "))
    except ValueError:
        print("Ошибка! Введите полное число.")
        continue

    if num < 0:
        print("Положительное число")
        continue
        break
    def factorial_calculation(num):
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

    def main():
        if num == 0:
            print(factorial_calculation(int(num)))
    # Вычисление факториал без оптимизации
    factorial_calculation = factorial_calculation(num)
    print(f"Факториал числа {num} равен {factorial_calculation} ")
        
    def optimized_factorial(num):
        return math.factorial(num)
        print(optimized_factorial(int(num)))
    # Вычисление факториала с оптимизацией
    optimized_factorial = optimized_factorial(num)
    print(f"Оптимизированный факториал числа {num} равен {optimized_factorial} ")

    if __name__ == '__main__':
        main()
