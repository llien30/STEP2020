a = 1
print("id(a-1): %#08x" % id(a))
b = a
print("id(a-1): %#08x" % id(b))
b = 3
print("id(a-1): %#08x" % id(b))
print("id(a-1): %#08x" % id(a))
print(a)
