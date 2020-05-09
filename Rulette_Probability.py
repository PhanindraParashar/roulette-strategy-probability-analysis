import numpy as np

Odd = set(np.arange(1,37,2))
Even = set(np.arange(2,37,2))
Zero = {0}
All_EZ = set(np.arange(1,37,1))
All = set(np.arange(0,37,1))

Red = {1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36}
black = []
for i in All_EZ:
    if i not in Red:
        black.append(i)
Black = set(black)

R1 = set(np.arange(3,37,3))
R2 = set(np.arange(2,36,3))
R3 = set(np.arange(1,35,3))

C1 = set(np.arange(1,13,1))
C2 = set(np.arange(13,25,1)) 
C3 = set(np.arange(25,37,1))       


    