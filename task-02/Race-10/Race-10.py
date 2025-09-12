def bob_can_win(a, x, y):
    if x > y:
        x, y = y, x
    if a <= x or a >= y:
        print("YES")
    else:
        print("NO")

t = int(input())
for i in range(t):
    a, x, y = map(int, input().split())
    bob_can_win(a, x, y)
