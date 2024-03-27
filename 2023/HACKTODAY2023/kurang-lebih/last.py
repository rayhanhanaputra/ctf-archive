spl = '''
    >+++>
    [-]
'''

spl2 = '''
            >>
            [-]
            >
            [-]
'''

a = open("parse.bf").read()
hsl = a.split(spl)
val=[0]*58
for b in hsl:
    c=b.split(spl2)
    del c[0]
    for i in range(len(c)):
        val[i]+=len(c[i].split('\n')[0].replace("\t",""))
del val[-1]
print("".join([chr(i) for i in val]))