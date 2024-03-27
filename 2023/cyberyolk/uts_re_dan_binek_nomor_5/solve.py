def calculate_value():
    rbp = [0] * 20  # Simulating memory (rbp-4, rbp-8, rbp-12, rbp-16)

    rbp[-4] = 20
    rbp[-8] = 10
    rbp[-12] = 20

    eax = rbp[-4] * rbp[-8] + 2
    ecx = eax + (rbp[-12] - (rbp[-12] << 2))
    rbp[-16] = ecx << 20

    if rbp[-16] > 100000000:
        if rbp[-16] <= 500000000:
            rbp[-16] = (rbp[-16] + 7) >> 3
    else:
        rbp[-16] = (rbp[-16] + (rbp[-16] >> 31)) >> 1

    return rbp[-16]

result = calculate_value()
print(result)
