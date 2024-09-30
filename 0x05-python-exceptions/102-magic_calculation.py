def magic_calculation(a, b):
    result = 0
    for i in range(1, 4):  # Loop from 1 to 3 (inclusive)
        try:
            if i > a:
                raise Exception("Too far")
            result += (a ** b) / i
        except Exception as e:
            result = a + b  # if an exception occurs, sum a and b
            break  # exit the loop
    return result
