v11 = [0]*44
v12 = [0]*500
v11[0] = 117
v11[1] = 103
v11[2] = -110
v11[3] = 123
v11[4] = 97
v11[5] = -99
v11[6] = 5
v11[7] = 110
v11[8] = -118
v11[9] = 358
v11[10] = 92
v11[11] = -117
v11[12] = 472
v11[13] = 103
v11[14] = -78
v11[15] = 815
v11[16] = 34
v11[17] = -70
v11[18] = 1257
v11[19] = 55
v11[20] = -1
v11[21] = 1554
v11[22] = 7
v11[23] = -31
v11[24] = 2411
v11[25] = 74
v11[26] = -34
v11[27] = 2941
v11[28] = 214
v11[29] = -50
v11[30] = 3795
v11[31] = 206
v11[32] = -93
v11[33] = 4485
v11[34] = 208
v11[35] = -72
v11[36] = 5754
v11[37] = 151
v11[38] = -241
v11[39] = 6697
v11[40] = 234
v11[41] = -231
v11[42] = 8034
v11[43] = 145

v10 = 44
v4 = 0
for i in range(2,1001):  
    v6 = 0
    for j in range(1,i+1):
      if (i%j==0):
        v6+=1
    if ( v6 == 2 ):
        v12[v4] = i
        v4+=1
v8 = 0
flag=""
for k in range(0,v10):
    if ( k % 3 ):
      if ( k % 3 == 1 ):
        flag += chr((v12[k]+k)^v11[k])  
      elif ( k % 3 == 2):
        flag += chr(((k - v12[k])) ^ v11[k])
    else:
      flag += chr( (k * v12[k]) ^ v11[k])

print(flag)
      
