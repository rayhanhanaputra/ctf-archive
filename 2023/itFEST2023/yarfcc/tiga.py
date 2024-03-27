# import itertools
# import string

# # Define the characters to be used
# characters = string.ascii_letters + string.digits + "_{}"

# # Generate combinations of length 4
# combinations = itertools.product(characters, repeat=4)

# # Write combinations to a text file
# with open('combinations.txt', 'w') as file:
#     for comb in combinations:
#         file.write(''.join(comb) + '\n')

# with open('combinations.txt', 'r') as file:
#     combinations_array = file.read().splitlines()

flag_yang_aseli_dan_nyata_sekali = [
    2956318005, 1748181433, 2290686289, 1746470217, 1747544497,
    3632858473, 1482229169, 4036035961, 410634617, 1483277617,
    2294905193, 1476762057, 672741721, 274313477, 1076433193,
]
# idx=0
# result = []
# for group in combinations_array:
#         value = 0
#         for j, char in enumerate(group):
#             value |= ord(char) << (8 * j)
#         v15 = 0
#         m = 0
#         while value:
#             v15 |= ((value & 1) == 0) << m
#             value >>= 1
#             m += 1
#         v16 = 0
#         for m in range(32):
#             v16 |= (v15 & (1 << m)) >> m << (31 - m)
#         v18 = ((v16 >> 8) | (v16 << (32 - 8))) & 0xFFFFFFFF  # Simulating __ROR4__ function
#         # print(v18,flag_yang_aseli_dan_nyata_sekali[idx])
#         result.append(v18)
    
# with open('results.txt', 'w') as file:
#     for integer in result:
#         file.write(str(integer) + '\n')

with open('results.txt', 'r') as file:
    combinations_array = file.read().splitlines()

flag=[]
for val in flag_yang_aseli_dan_nyata_sekali:
    index = combinations_array.index(str(val))
    flag.append(index)

print(flag)

with open('combinations.txt', 'r') as file:
    combinations_array = file.read().splitlines()

for c in flag:
    print(combinations_array[c],end="")

