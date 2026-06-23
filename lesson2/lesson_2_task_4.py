def fizz_buzz(n):
    """Печатает числа от 1 до n, заменяя их на Fizz,
      Buzz или FizzBuzz по правилам"""
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# Пример вызова функции
fizz_buzz(17)
