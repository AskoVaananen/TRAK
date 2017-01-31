

def luvut(b):
    k = 0
    a = []
    a.append(1)
    
    while a[k] <= 13:
        k = k + 1
        a.append((a[k-1])*2)
    return a
print luvut(13)

    

