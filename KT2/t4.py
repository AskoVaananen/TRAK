def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = [60,170,30,2,11,19,24,50,60,3,100]
mergeSort(alist)
print(alist)

# alussa jaetaan taulukko osa taulukoihin keskelta
# jaetaan yha pienempiin osataulukoihin
# kun taulukoissa on jaljella 1 indeksi
# jarjestetaan ne seuraavalle tasolle vertailemalla kahta perakkaista taulukkoa keskenaan laittamalla pienempi indexi ensimmaiseksi
# nyt on kahden alkion taulukko jarjestyksessa
# verrataan naita seuraaviin alkioihin jotka on jarjestetty samalla tasolla ja yhdistetaan ne.
# jatketaan kunnes kaikki osa taulukot on yhdistetty.
