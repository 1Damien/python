for i in range(151):

    print(i)

for i in range(5, 1001, 5):

    print(i)

for i in range(1, 101):

    if i % 10 == 0:

        print("Coding Dojo")

    elif i % 5 == 0:

        print("Coding")

    else:

        print(i)

sum_of_odds = 0

for i in range(1, 500001, 2):

    sum_of_odds += i

print("The sum of odd integers from 0 to 500,000 is:", sum_of_odds)


for i in range(2018, 0, -4):

    print(i)

low_num = 2

high_num = 9

mult = 3


for i in range(low_num, high_num + 1):

    if i % mult == 0:

        print(i)