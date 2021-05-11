def out(arr):
    for i in (arr):
        for j in (i):
            print(j, end=" | ")
        print()

def makeEggDropArray(e, f):
    arrEggDrop = [[-1 for j in range(f+1)] for i in range(e)]
    for i in range(f+1):
        arrEggDrop[0][i] = i
    for i in range(len(arrEggDrop)):
        arrEggDrop[i][0] = 0
        arrEggDrop[i][1] = 1
    return arrEggDrop

def eggDrop(e, f, arrEggDrop):
    if (arrEggDrop[e-1][f] != -1):
        return arrEggDrop[e-1][f]
    res = max(eggDrop(e-1,0, arrEggDrop), eggDrop(e, f-1, arrEggDrop))
    min = res
    for i in range(2, f+1):
        res = max(eggDrop(e-1,i-1, arrEggDrop), eggDrop(e, f-i, arrEggDrop))
        if (res < min):
            min = res
    answer = 1 + min
    arrEggDrop[e-1][f] = answer
    return answer

def solveEggDrop(e,f):
    arrEggDrop = makeEggDropArray(e,f)
    return eggDrop(e,f,arrEggDrop)

#main
e = int(input("Enter the amount of eggs: "))
f = int(input("Enter the number of floors: "))

ans = "The minimum amount of trials for "
ans += str(e)
ans += " number of eggs and "
ans += str(f)
ans += " number of floors is "
ans += str(solveEggDrop(e,f))
ans += " trials"
print(ans)

