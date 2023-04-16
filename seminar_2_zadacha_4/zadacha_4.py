
def spicok():
    num = []
    n = int(input("Введите число: "))
    for i in range(-n,n+1):
        num.append(i)
    nym = num[-2:]+num[:-2]
    print(nym)
spicok()