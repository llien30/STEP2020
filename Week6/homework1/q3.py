def foo(b):
    b = 2
    print("id(b): %#08x" % id(b))


a = 1
print("id(a): %#08x" % id(a))
foo(a)
print("id(a): %#08x" % id(a))
print("a:", a)
