v = [
    79,
    73,
    75,
    69,
    65
]
avain = [
    1,
    3,
    0,
    4,
    2
]
def sekoita(v, avain):
    tulos = [0] * len(v) # valiaikaiseen tulos taulukkoon 0 * len(v)
    for i in range(0, len(v)): # 0 - 4
       tulos[avain[i]] = v[i] # otetaan indexit avain taulukosta v taulukkoa vastaamaan
    
    return tulos

print sekoita(v, avain)

       


             

        

        
