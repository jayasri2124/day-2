def ASCII(x):
    if type(x)==str:
        return ord(x)
    return (x)
l=["A",-20,"a",94,66]
l.sort(key=ASCII)
print(l)
