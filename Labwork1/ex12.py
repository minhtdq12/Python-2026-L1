def print_pattern(m, n):
    for i in range(m):
        if i == 0 or i == m - 1:
            print("* " *n)
        else:
            print("* " + " " * (n - 2) + "*")

m = int(input("Enter number of rows: "))
n = int(input("Enter numbet of columns: "))

print_pattern(m, n)
