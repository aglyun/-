def demo(a):
    return a+1


lb = ['hello', 'xxx', 'world']
a = map(demo, lb)

print(''.join(lb))

for i in range(100):
    print(i+1,end='')

