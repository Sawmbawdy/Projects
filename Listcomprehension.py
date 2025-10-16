Number = int(input("Enter a number:\n"))
Odd = []
for i in range(Number + 1):
    if i % 2 != 0:
        Odd.append(i)
print(Odd)

fruits = ['apple', 'banana', 'mango', 'watermelon']

fruits2 = []

for i in range(len(fruits)):
    fruits2.append(str(fruits[i]).capitalize())
print(fruits2)