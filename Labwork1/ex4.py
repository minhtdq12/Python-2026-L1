n = int(input("enter a number: "))
sum_divisors = 0 

for i in range(1, n):
    if n % i == 0:
        sum_divisors += i

if sum_divisors == n:
    print(n, "is a perfect number")
else:
    print(n, "is not a perfect number")
    
