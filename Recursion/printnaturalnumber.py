def printnaturalnumber(n):
    if n == 1:
        print(n)
        return
    else:
        printnaturalnumber(n-1)
    print(n)

def printnaturalnumber_reverse(n):
    if n == 1:
        print(n)
        return
    else:
        print(n)
        printnaturalnumber_reverse(n-1)

printnaturalnumber(8)
print('----------------------------------------')
printnaturalnumber_reverse(8)