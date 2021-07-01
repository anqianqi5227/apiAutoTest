# import functools as f
import random
# a = lambda x :x%2==1
# b = lambda y :y*y-4

# f1 = filter(a,range(10))
# f2 = filter(b,range(10))

# m1 = map(a,range(10))
# m2 = map(b,range(10))

# print(list(f1),list(f2),list(m1),list(m2))

# print(f.reduce(lambda x,y:x+y,range(5)))

# s = 'ashdfjasdashdfhasjfhkasdf'
# l = list(set(s))
# l.sort()
#
# print(l)

# print ([ (x, y) for x in range(10) if x % 2 if x > 3 for y in range(10) if y > 7 if y != 8 ])
# 生成随机字典

# print([lambda i,j: for i in range(100) for j in range(100)])

d ={x:random.randint(1,100) for x in 'hyjkdln'}
print(dict(sorted(d.items(),key= lambda x:x[1])))
# sorted(d.items())


z = zip(d.keys(),d.values())
print(dict(sorted(z)))