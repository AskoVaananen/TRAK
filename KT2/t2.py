
l = [
    50, 70, 30, 2, 40, 24, 19, 60
    ]
n = len(l)-1
def insertionsort(s):
    for i in range(1, len(s)):
        val = s[i]
        j = i - 1
        while (j >= 0) and (s[j] > val):
            s[j+1] = s[j]
            j = j - 1
        s[j+1] = val
    return s

print insertionsort(l)

#http://www.pythontutor.com/visualize.html#mode=display how this works
