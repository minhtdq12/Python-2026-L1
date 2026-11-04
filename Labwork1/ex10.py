def get_divisors(n):
    result = []

    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)

    return result

n = int(input("Enter a number: "))
print("Divisors: ", get_divisors(n))
