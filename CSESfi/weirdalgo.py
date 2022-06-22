input_1 = int(input())
print(int(input_1), end =" ")
while input_1 != 1:
    if input_1 % 2 == 0:
        input_1 /= 2
        print(int(input_1), end =" ")
    else:
        input_1 = 3*input_1 + 1
        print(int(input_1), end =" ")