hex = [0x28, 0xCC, 0x28, 0x0D5, 0x2C, 0x0C9, 0x2C, 0x0C4, 0x2A, 0x0C3, 0x2F, 0x0D5, 0x34, 0x0C1, 0x2F, 0x0D7]


for i in range(len(hex)):
    if(i % 2 == 1):
        hex[i] = hex[i] ^ 0xBA ^ 0x1D
    else:
        hex[i] = hex[i] ^ 0x5E ^ 0x1D


for i in range (8):
    hex[i], hex[15 - i] = hex[15 - i], hex[i]
    
for i in range(len(hex)):
    print(chr(hex[i]), end='')
