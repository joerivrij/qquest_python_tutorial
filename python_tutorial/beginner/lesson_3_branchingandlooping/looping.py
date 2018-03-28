numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for statement
for x in range(0, 10):
    print(numbers[x])

# foreach
for num in numbers:
    print(num)

# while
x = 0
while x < 10:
    print(numbers[x])
    x += 1

while x in range(0, 10):
    print(numbers[x])