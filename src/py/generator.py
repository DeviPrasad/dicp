from collections import Counter


## 'g' is the generator, and 'p' is the prime modulus.
def subgroup(g, p):
    sub_grp = []
    for i in range(1, p):
        a = pow(g, i, p)
        sub_grp.append(a)
    return sub_grp


## 'g' is the generator, and 'p' is the prime modulus.
def subgroup_reduced(g, p):
    cl = Counter(subgroup(g, p))
    return list(cl.keys())


## list of subgroups for a given prime modulus 'p'
def subgroups(p):
    sub_grpoups = []
    for g in range(1, p):
        sub_grpoups.append((g, subgroup_reduced(g, p)))
    return sub_grpoups


def print_subgroups(p):
    print("  Sln      Order     Group")
    for a, sg in subgroups(p):
        print("%4d      %4d       %s" % (a, len(sg), sg))


def is_generator_group(g, p):
    return len(set(subgroup(g, p))) == p - 1


def is_generator(g, p):
    return pow(g, p - 1, p) == 1 and pow(g, (p - 1) // 2, p) == p - 1


def generators(p):
    lg = []
    for g in range(1, p):
        if is_generator(g, p):
            lg.append(g)
    return lg


#### chapter 21. Is -1 a Square Modulo p?
## is 'a' a quadratic residue? if so, list the solutions.
##
def quadratic_residues(p):
    lqr = []
    for a in range(2, p):
        (_, lr) = quadratic_residues_of(a, p)
        if len(lr) > 0:
            lqr.append((a, lr))
    return lqr


def quadratic_residues_of(a, p):
    lr = []
    for x in range(1, p):
        if pow(x, 2, p) == a:
            lr.append(x)
    return (len(lr) > 0, lr)


def is_qr(g, p):
    return quadratic_residues_of(g, p)[0]


# is -1 a quadratic residue? if so, list the solutions.
def qr_of_minus_1(p):
    return quadratic_residues_of(p - 1, p)


def legendre_symbol(a, p):
    (s, _) = quadratic_residues_of(a, p)
    return 1 if s else -1


def legendre_symbol_mod_p(a, p):
    return legendre_symbol(a, p) % p


def sqrt(a, p):
    return pow(a, (p - 1) // 2, p)


## helper function to cast the sqrt value as legendre symbol.
## more specifically, returns -1 when sqrt produced (p-1).
## 'p' must be a prime number.
def sqrt_legendre_symbol(a, p):
    return legendre_symbol_mod_p((sqrt(a, p)), p)


def test_generators():
    assert is_generator(2, 19)
    assert is_generator(3, 19)
    assert not (is_generator(4, 19))


def test_subgroup():
    assert subgroup_reduced(8, 19) == [8, 7, 18, 11, 12, 1]


def test_quadratic_residues():
    ## page 150
    assert quadratic_residues_of(3, 11) == (True, [5, 6])
    assert quadratic_residues_of(7, 31) == (True, [10, 21])
    assert quadratic_residues_of(10, 47) == (False, [])
    assert quadratic_residues_of(15, 97) == (False, [])
    assert quadratic_residues_of(33, 173) == (True, [44, 129])
    assert quadratic_residues_of(222, 941) == (True, [242, 699])
    assert quadratic_residues_of(78, 409) == (False, [])
    assert quadratic_residues_of(33, 499) == (True, [136, 363])
    assert quadratic_residues_of(57, 601) == (False, [])
    assert quadratic_residues_of(222, 941) == (True, [242, 699])
    assert quadratic_residues_of(129, 1223) == (True, [313, 910])


def test_sqrt():
    assert sqrt(3, 11) == legendre_symbol_mod_p(3, 11)
    assert sqrt(7, 31) == legendre_symbol_mod_p(7, 31)
    assert sqrt(10, 47) == legendre_symbol_mod_p(10, 47)
    assert sqrt(15, 97) == legendre_symbol_mod_p(15, 97)
    assert sqrt(33, 173) == legendre_symbol_mod_p(33, 173)
    assert sqrt(222, 941) == legendre_symbol_mod_p(222, 941)
    assert sqrt(78, 409) == legendre_symbol_mod_p(78, 409)
    assert sqrt(33, 499) == legendre_symbol_mod_p(33, 499)
    assert sqrt(57, 601) == legendre_symbol_mod_p(57, 601)


## page 148
def test_qr_of_minus_1():
    assert qr_of_minus_1(3) == (False, [])
    assert qr_of_minus_1(5) == (True, [2, 3])
    assert qr_of_minus_1(7) == (False, [])
    assert qr_of_minus_1(11) == (False, [])
    assert qr_of_minus_1(13) == (True, [5, 8])
    assert qr_of_minus_1(17) == (True, [4, 13])
    assert qr_of_minus_1(19) == (False, [])
    assert qr_of_minus_1(23) == (False, [])
    assert qr_of_minus_1(29) == (True, [12, 17])
    assert qr_of_minus_1(31) == (False, [])
    assert qr_of_minus_1(37) == (True, [6, 31])
    assert qr_of_minus_1(39) == (False, [])


test_quadratic_residues()
test_qr_of_minus_1()
test_generators()
test_sqrt()

test_subgroup()

print_subgroups(25)
