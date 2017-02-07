a = [5,2,4,5,8,5,46,1,22,5,99]



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

