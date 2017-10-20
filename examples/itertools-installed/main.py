from itertools import chain

a = [1, 2, 3]
b = [4, 5, 6]

print("chaining lists:")
print("  a: ", a)
print("  b: ", b)

print("here we go...")
for val in chain(a, b):
    print("  ", val)
