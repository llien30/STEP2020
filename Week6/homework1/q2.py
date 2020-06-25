a = [1]
print("id(a): %#08x" % id(a))
b = a
print("id(b): %#08x" % id(b))
b.append(2)
print("id(b): %#08x" % id(b))

print("a:", a)
print("b:", b)
