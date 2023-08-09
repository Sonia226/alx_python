def no_c(my_string):
    list = ""
    a = 'c'
    b = 'C'
    for i in my_string:
        if i != a and i != b:
            list += i
    return list