def foo(b):
    print("id(b-1): %#08x" % id(b))
    b.append(2)
    print("id(b-2): %#08x" % id(b))
    b = b + [3]
    print("id(b-3): %#08x" % id(b))
    b.append(4)
    print("id(b-4): %#08x" % id(b))
    print("b:", b)


a = [1]
print("id(a-1): %#08x" % id(a))
foo(a)
print("id(a-2): %#08x" % id(a))
print("a:", a)
