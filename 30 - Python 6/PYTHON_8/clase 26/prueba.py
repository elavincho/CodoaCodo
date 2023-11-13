a = list(range(5))
print(a) # [0, 1, 2, 3, 4]

b = a
print(b) #[0, 1, 2, 3, 4]

b.append(5)
print(a) #[0, 1, 2, 3, 4, 5]
del a[2]
print(b) #[0, 1, 3, 4, 5]
print(a is b) #True