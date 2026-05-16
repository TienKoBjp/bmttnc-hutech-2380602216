import itertools

danh_sach = [1, 2, 3]
hoan_vi = itertools.permutations(danh_sach)

for p in hoan_vi:
    print(p)