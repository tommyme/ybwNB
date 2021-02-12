def Xor(a: bytes, b: bytes):
    res = b''
    def func(x): return 1 if x == 0 else 0
    data, lens = [a, b], [len(a), len(b)]
    idx = lens.index(min(lens))
    print(idx, func(idx))
    mini = data[idx]
    big = data[func(idx)]
    for i in range(len(big)):
        res += bytes(chr(big[i] ^ mini[i % len(mini)]), encoding='gb2312')

    return res

class sb():
    def __init__(self,inp):
        if isinstance(inp,str):
            self.str = inp
            self.btar = bytearray(inp,encoding='utf-8')
        elif isinstance(inp,bytearray):
            self.str = inp.decode('utf-8')
            self.btar = inp
        elif isinstance(inp,list):
            self.btar = bytearray(inp) 
            self.str = self.btar.decode('utf-8')

abc = b'qwertyuiopasdfghjklzxcvbnm'

ABC = b'QWERTYUIOPASDFGHJKLZXCVBNM'

num = b'1234567890'

chSet = range(32, 128)
