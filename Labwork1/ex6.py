range1 = list(range(0, 7))
#print("range1:", *range1, sep=", ")

range2 = list(range(1, 11, 3))
#print("range2:", *range2, sep=", ")

range3 = list(range(5, 0, -1))
#print("range3:", *range3, sep=", ")

range4 = list(range(6, -3, -2))
#print("range4:", *range4, sep=", ")

print("range1:", ", ".join(map(str, range1)))
print("range2:", ", ".join(map(str, range2)))
print("range3:", ", ".join(map(str, range3)))
print("range4:", ", ".join(map(str, range4)))