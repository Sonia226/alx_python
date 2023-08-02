def is_prime(number):
    if number <= 1:
     return False
    elif number % 2 == 0:
       return False
    elif number % 3 == 0:
        return False
    else:
       return True
