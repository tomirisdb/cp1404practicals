for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a)
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b)
for i in range(20, 0, -1):
    print(i, end=' ')
print()
# c)
number = int(input("Enter number of stars: "))
stars = ""
for i in range(number):
    stars += '*'
print(stars)
# d)
lines = int(input("Enter the number of lines: "))
for i in range(1, lines + 1):
    print('*' * i)
