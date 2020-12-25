def decrypt(sn, pub):
    loop = 0
    v = 1
    while v != pub:
        v *= sn
        v %= 20201227
        loop += 1
    return loop

def encrypt(sn, loop):
    v= 1
    for i in range(loop):
        v *= sn
        v %= 20201227
    return v

a = decrypt(7, 18499292)
b = decrypt(7, 8790390)
print(encrypt(18499292, b))