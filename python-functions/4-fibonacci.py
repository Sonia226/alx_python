def fibonacci_sequence(n):
    if n <= 0:
            return[]
    elif n == 1:
         return[0]
    elif n == 2:
         return [0, 1]

    fibo_numbers = [0, 1]
    for i in range (2, n):
        next_fibo = fibo_numbers[-1] + fibo_numbers[-2]
        fibo_numbers.append(next_fibo)
    return fibo_numbers
