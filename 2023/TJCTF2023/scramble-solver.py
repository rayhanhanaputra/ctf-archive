#first 3 lines are given
import random
seed = 1000
random.seed(seed)

#unscramble the rest
flag_length = 31
inp = [1]*flag_length
n = len(inp)
mod = 256
l = []
l2 = [0]*n
l3 =[0]*n

def main():
    for i in range(n):
        l.append(random.randint(6, 420))

    assert(len(l)==n)

    print("flag is:", decrypt(inp))
    

def recur(lst):
    if(len(lst)==1):
        assert(lst[0]>0)
        return lst[0]
    return recur(lst[::2])/recur(lst[1::2]) 

def decrypt(inp):
    for i in range(1, n):
        l2[i] = (l[i]*5+(l2[i]+n)*l[i])%l[i]
        l2[i] += inp[i] 
    
    l2[0] += int(recur(l2[1:])*50)
    l3[0] = l2[0]%mod

    print(l2)

    for i in range(1, n):
        l3[i] = (l2[i]^((l[i]&l3[i-1]+(l3[i-1]*l[i])%mod)//2))%mod
        

    l4 = [70, 123, 100, 53, 123, 58, 105, 109, 2, 108, 116, 21, 67, 69, 238, 47, 102, 110, 114, 84, 83, 68, 113, 72, 112, 54, 121, 104, 103, 41, 124]
    flag = ""
    for i in range(n):
        flag+=chr((l4[i]^l3[i]))    
    return flag
    


main()

