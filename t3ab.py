a = [9, 3, 11, 2]



def bubblesort(a):

    
    changes = True
    # Toistetaan niin kauan, kuin vaihtoja tulee
    while changes:
        changes = False
        
        for i in xrange(1, len(a)):
            
            if a[i] < a[i - 1]:
               
                a[i], a[i - 1] = a[i - 1], a[i]
              
                changes = True
  
    return a
print bubblesort(a)

# kaydaan lavitse kahta perakkkaista indexia ja vaihdetaan niitten paikkaa
# jos entinen on suurempi, toistetaan aina viimeiseen indexiin asti vertailu
# kaydaan niin monta kierrosta lavitse kunnes indexit on oikeassa jarjestyksessa

# esim 9 3 11 2 first round 3 9 2 11 --> 11 suurin
# round 2: 3 2 9 11 --> 9 ja 2 vaihtaa paikkaa
# round 3: 2 3 9 11 ---> 3 ja 2 vaihtaa paikkaa --> suurusjarjestys ja vertailu loppuu




#3B = n^2 = 50^2 = 2500 worst case

