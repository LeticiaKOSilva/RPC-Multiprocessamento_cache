def check_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        i = 5
        w = 2
        is_prime = True
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += w
            w = 6 - w
        return is_prime
