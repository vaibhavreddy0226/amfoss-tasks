t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    total_ones = 0
    ones_in_original = s.count('1')

    for i in range(n):
        if s[i] == '1':
            total_ones += (ones_in_original - 1) #when i flip a number if its 1 change to 0 so the no of ones reduce by 1 
        else:
            total_ones += (ones_in_original + 1)

    print(total_ones)

