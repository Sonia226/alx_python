def safe_print_division(a, b):
    solution = None
    try:
        solution = a / b
    except ZeroDivisionError:
        return None
    except Exception as e:
        print(" an error occured:", e)
        return None
    finally:
        print("Inside result: {}".format(solution))

    return solution