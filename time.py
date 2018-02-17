def time1():
    t=0
    import time
    a=time.asctime( time.localtime(time.time()) )
    b=[]
    print(a)
    c=int(a[11])*10 +int(a[12])
    print(c)
    if c>5:
        if c<23:
         t=1
    return t
#a=time3()
#print(a)
def time3():
    t=0
    import time
    a=time.asctime( time.localtime(time.time()) )
    b=[]
    print(a)
    time.sleep(5)
    d=time.asctime( time.localtime(time.time()) )
    print(b)
    c=int(a[11])*10 +int(a[12])
    print(c)
    if c>5:
        if c<23:
         t=1
time3()
