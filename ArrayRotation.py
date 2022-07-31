c = 3 #rotations
n = int(input("enter number of ele- "))
a = [int(i) for i in input().split(" ", n-1)]

for i in range(1,c+1):
    b.append(a[-i])
    b.insert(0,b.pop())
    print(b + list(set(a)-set(b)))
