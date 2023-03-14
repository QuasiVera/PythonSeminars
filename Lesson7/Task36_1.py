def func(f, i=1):
    x = i+1
    y =i+2
    a = (f(x,y))
    print(a)

func(lambda x, y: x+y, 3)