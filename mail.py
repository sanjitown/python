import time
def time():
    t=0
    import time
    a=time.asctime( time.localtime(time.time()) )
    b=[]
    b.append(a[11])
    b.append(a[12])
    c=int(b[0])*10 +int(b[1])
    if c>=6:
        if c<=23:
         t=1
    print(c)
    return t
print(time())
