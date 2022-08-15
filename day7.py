# Left shift
a = 8
b = a << 2
print(b)

# Right shift
a = 8
b = a >> 2
print(b)

# bitwise and
c = 5
d = 4
e = c & d
print(e)

# bitwise OR
c = 5
d = 4
e = c | d
print(e)

# NOT
f = 16
k = ~f
print(k)


# BASE
class Element:
    uid: str
    number_of_inputs: int
    inputs: list
    outputs: list
    type_of_element: str

    def __init__(self, _uid, _number_of_inputs, _toe):
        self.uid = _uid
        self.number_of_inputs = _number_of_inputs
        self.type_of_element = _toe


# 'LSHIFT', 'AND', 'NOT', 'RSHIFT', 'OR'

class LShift(Element):
    amount_to_shift_by: int

    def __init__(self, _uid, _number_of_inputs, _toe, _amount_to_shift_by):
        super().__init__(_uid, 1, "lshift")
        self.amount_to_shift_by = _amount_to_shift_by


class RShift(Element):
    amount_to_shift_by: int

    def __init__(self, _uid, _number_of_inputs, _toe, _amount_to_shift_by):
        super().__init__(_uid, 1, "rshift")
        self.amount_to_shift_by = _amount_to_shift_by



if __name__ == "__main__":
    raw_samples = """NOT dq -> dr
kg OR kf -> kh
ep OR eo -> eq
44430 -> b
NOT gs -> gt
dd OR do -> dp
eg AND ei -> ej
y AND ae -> ag
jx AND jz -> ka
lf RSHIFT 2 -> lg
z AND aa -> ac
dy AND ej -> el
bj OR bi -> bk
kk RSHIFT 3 -> km
NOT cn -> co
gn AND gp -> gq
cq AND cs -> ct
eo LSHIFT 15 -> es
lg OR lm -> ln
dy OR ej -> ek
NOT di -> dj
1 AND fi -> fj
kf LSHIFT 15 -> kj
NOT jy -> jz
NOT ft -> fu
fs AND fu -> fv
NOT hr -> hs
ck OR cl -> cm
jp RSHIFT 5 -> js
iv OR jb -> jc
is OR it -> iu
ld OR le -> lf
NOT fc -> fd
NOT dm -> dn
bn OR by -> bz
aj AND al -> am
cd LSHIFT 15 -> ch
jp AND ka -> kc
ci OR ct -> cu
gv AND gx -> gy
de AND dk -> dm
x RSHIFT 5 -> aa
et RSHIFT 2 -> eu
x RSHIFT 1 -> aq
ia OR ig -> ih
bk LSHIFT 1 -> ce
y OR ae -> af
NOT ca -> cb
e AND f -> h
ia AND ig -> ii
ck AND cl -> cn
NOT jh -> ji
z OR aa -> ab
1 AND en -> eo
ib AND ic -> ie
NOT eh -> ei
iy AND ja -> jb"""
    types_to_deal_with = set()
    samples = raw_samples.split("\n")
    for sample in samples:
        pieces = sample.split(" ")
        for piece in pieces:
            if piece.isupper():
                types_to_deal_with.add(piece)
    print(types_to_deal_with)
