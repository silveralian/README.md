start = int(input("Count from: "))
end = int(input("Count to  : "))
step = int(input("Count by  : "))

for n in range(start, end + 1, step):
    print(n, end=" ")
