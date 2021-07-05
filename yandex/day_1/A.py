temps = list(map(int, input().split()))
room = temps[0]
cond = temps[1]
mode = input()
if mode == "heat":
    if cond >= room:
        print(cond)
    else:
        print(room)
elif mode == "freeze":
    if cond <= room:
        print(cond)
    else:
        print(room)
elif mode == "auto":
    print(cond)
else:
    print(room)
