BIN_FORMAT = '05b'
for i in range(0, 2 ** 5):
    j = i ^ (i >> 1)
    print(i, format(i, BIN_FORMAT), format(j, BIN_FORMAT))
    for k in range(0, 5):
        print((j >> k) & 1)

for k in range(4, -1, -1):
    print(k, '>>>>>>>>>>>>>>>>>>>>>>>>>>')
    for i in range(0, 2 ** 5):
        print((((i ^ (i >> 1)) >> k) & 1))
