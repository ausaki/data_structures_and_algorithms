# modular inverse

def modiv(a, b):
    # import sys
    # if sys.version_info[:2] >= (3, 8):
    #     return pow(x, -1, m)
    
    def egcd(a, b):
        if b == 0:
            return a, 1, 0
        q, r = divmod(a, b)
        g, s, t = egcd(b, r)
        return g, t, s - t * q
    
    g, s, t = egcd(a, b)
    return s % b if g == 1 else 0

print(modiv(10, 20))