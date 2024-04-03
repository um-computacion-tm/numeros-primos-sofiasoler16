

# def is_primo(numero):
#     n = list(range(1,numero+1,1))
#     print(n)
#     for g in n:
#         if g == 1 or numero:
#             l = True
#             if numero%g == 0:
#                 l = False
#     l = True
#     return l

def is_primo(value):
    divisor=value-1
    while divisor>1:
        if value%divisor==0:
            return False
        divisor=divisor-1

    return True



