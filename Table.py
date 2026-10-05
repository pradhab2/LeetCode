
def table(inp):
    a=list(range(inp,inp*10+1, inp))
    print("_"*39)
    print("\t".join(map(str, a)))
    b=list(range(1, 11))
    print("\t".join(map(str, b)))
    c=[str(inp)] * 10
    print("\t".join(c))
    print("_" * 39)





