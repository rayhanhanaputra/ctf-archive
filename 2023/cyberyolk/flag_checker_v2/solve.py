from z3 import *

# Create Z3 integer variables for a1[i]

a1 = [Int(f'a1_{i}') for i in range(0, 40)]  # Index from 1 to 40

# Create a Z3 solver
solver = Solver()

for i in a1:
    solver.add(i>0)
    solver.add(i<128)

print("base input")

# Encode the constraints
solver.add(a1[7] + a1[3] * a1[17] - a1[2] + a1[25] - a1[11] * a1[6] - a1[35] == 5913)
solver.add(a1[7] * a1[20] == 10450)
solver.add(a1[16] + a1[10] * a1[29] * a1[4] - a1[28] - a1[36] - a1[13] - a1[27] == 757856)
solver.add(a1[24] * a1[9] == 5035)
solver.add(a1[26] + a1[14] - a1[1] * a1[22] - a1[32] - a1[33] + a1[0] * a1[9] == 390)
solver.add(a1[0] * a1[23] == 7638)
solver.add(a1[21] + a1[12] + a1[31] * a1[15] + a1[19] - a1[24] * a1[38] + a1[30] == -3673)
solver.add(a1[35] * a1[38] == 6460)
solver.add(a1[18] + a1[20] + a1[5] - a1[37] - a1[34] + a1[23] * a1[8] * a1[39] == 1524896)
solver.add(a1[36] * a1[16] == 6264)
solver.add(a1[16] + a1[3] * a1[28] - a1[2] + a1[9] - a1[7] * a1[14] - a1[21] == -2562)
solver.add(a1[15] * a1[31] == 2448)
solver.add(a1[20] + a1[39] * a1[8] * a1[35] - a1[12] - a1[30] - a1[27] - a1[5] == 1270376)
solver.add(a1[6] * a1[29] == 4940)
solver.add(a1[34] + a1[36] - a1[25] * a1[22] - a1[19] - a1[0] + a1[1] == -4296)
solver.add(a1[22] * a1[30] == 4992)
solver.add(a1[33] + a1[31] + a1[26] * a1[6] + a1[11] - a1[23] * a1[15] + a1[10] == -2660)
solver.add(a1[5] * a1[3] == 8856)
solver.add(a1[13] + a1[32] + a1[37] - a1[17] - a1[24] + a1[4] * a1[2] * a1[38] * a1[29] == 48294989)
solver.add(a1[13] * a1[1] == 6270)
solver.add(a1[21] + a1[36] * a1[19] - a1[11] + a1[10] - a1[5] * a1[24] - a1[34] == -186)
solver.add(a1[33] * a1[2] == 7120)
solver.add(a1[14] + a1[4] * a1[8] * a1[32] - a1[7] - a1[31] - a1[28] - a1[30] == 682856)
solver.add(a1[37] * a1[14] == 4485)
solver.add(a1[33] + a1[17] - a1[20] * a1[23] - a1[1] - a1[16] + a1[3] * a1[27] == 3553)
solver.add(a1[4] * a1[11] == 7560)
solver.add(a1[0] + a1[25] + a1[9] * a1[12] + a1[35] - a1[26] * a1[22] + a1[2] == 739)
solver.add(a1[10] * a1[21] == 6650)
solver.add(a1[29] + a1[37] + a1[15] - a1[6] - a1[18] + a1[39] * a1[13] * a1[38] == 807579)
solver.add(a1[32] * a1[12] == 3876)
solver.add(a1[37] + a1[21] * a1[3] - a1[1] + a1[30] - a1[18] * a1[9] - a1[24] == 5889)
solver.add(a1[18] * a1[26] == 2448)
solver.add(a1[27] + a1[26] * a1[12] * a1[38] - a1[20] - a1[17] - a1[16] - a1[19] == 166178)
solver.add(a1[25] * a1[19] == 10146)
solver.add(a1[5] + a1[35] - a1[32] * a1[15] - a1[6] - a1[13] + a1[29] * a1[4] == 4352)
solver.add(a1[28] * a1[34] == 2706)
solver.add(a1[25] + a1[31] + a1[22] * a1[8] + a1[10] - a1[33] * a1[0] + a1[11] == 101)
solver.add(a1[27] * a1[8] == 12519)
solver.add(a1[14] + a1[28] + a1[36] - a1[7] - a1[2] + a1[34] * a1[23] * a1[39] == 470306)
solver.add(a1[17] * a1[39] == 10750)
solver.add(a1[19] + a1[25] * a1[37] - a1[10] + a1[21] - a1[4] * a1[33] - a1[6] == -3212)
solver.add(a1[24] + a1[35] * a1[11] * a1[26] - a1[8] - a1[15] - a1[28] - a1[38] == 410190)
solver.add(a1[12] + a1[14] - a1[18] * a1[3] - a1[7] - a1[2] + a1[20] * a1[9] == -1271)
solver.add(a1[22] + a1[30] + a1[0] * a1[31] + a1[36] - a1[17] * a1[29] + a1[23] == -4429)
solver.add(a1[32] + a1[16] + a1[27] - a1[1] - a1[5] + a1[39] * a1[13] * a1[34] == 392038)

# Check for satisfiability and find a model
if solver.check() == sat:
    print("tes")
    model = solver.model()
    # Print the model
    print("Solution:")
    for i in range(0, 40):
        # print(f"a1_{i} =", model[a1[i-1]])
        print(model[a1[i-1]])
else:
    print("No solution found.")

flag = [125, 67, 66, 89, 123, 84, 72, 52, 110, 107, 53, 95, 90, 51, 95, 115, 48, 108, 86, 51, 114, 95, 70, 48, 114, 95, 89, 48, 117, 82, 95, 104, 51, 76, 80, 33, 95, 58, 39, 68]

for c in flag:
    print(chr(c),end="")
