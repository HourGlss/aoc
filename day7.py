class Wire:
    uid: str
    value: int | None

    def __init__(self, _uid):
        self.uid = _uid
        self.value = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        ret = ""
        if self.value is not None:
            ret += "("
        ret += f"{self.uid}"
        if self.value is not None:
            ret += f" {self.value})"
        return ret


class Element:
    number_of_inputs: int
    inputs: list['Wire']
    outputs: list['Wire']
    type_of_element: str
    done: bool
    uid: str

    def __init__(self, _toe, debug):
        self.type_of_element = _toe
        self.number_of_inputs = 0
        self.inputs = []
        self.outputs = []
        self.done = False
        self.debug = debug

    def add_input(self, _e: "Wire") -> bool:
        if self.number_of_inputs < 2:
            self.number_of_inputs += 1
            self.inputs.append(_e)
            return True
        return False

    def add_output(self, _e: "Wire"):
        self.outputs.append(_e)

    def go(self):
        pass

        if self.debug:
            print(str(self))

    def set_uid(self):
        self.uid = str(self)


class ELShift(Element):
    amount_to_shift_by: int

    def __init__(self, _amount_to_shift_by, debug):
        super().__init__("lshift", debug)
        self.amount_to_shift_by = _amount_to_shift_by

    def go(self):
        if not self.done:
            for _ in self.inputs:
                if _.value is None:
                    return
            temp = self.inputs[0].value << self.amount_to_shift_by
            if temp < 0:
                temp += 2 ** 16
            for _ in self.outputs:
                _.value = temp
            self.done = True
            super().go()

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.inputs[0]} {self.type_of_element} {self.amount_to_shift_by} -> {self.outputs[0]}"


class ERShift(Element):
    amount_to_shift_by: int

    def __init__(self, _amount_to_shift_by,debug):
        super().__init__("rshift",debug)
        self.amount_to_shift_by = _amount_to_shift_by

    def go(self):
        if not self.done:
            for _ in self.inputs:
                if _.value is None:
                    return
            temp = self.inputs[0].value >> self.amount_to_shift_by
            if temp < 0:
                temp += 2 ** 16
            for _ in self.outputs:
                _.value = temp
            self.done = True
            super().go()

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.inputs[0]} {self.type_of_element} {self.amount_to_shift_by} -> {self.outputs[0]}"


class ESignal(Element):
    output_value: int

    def __init__(self, _value, debug):
        super().__init__("signal", debug)
        self.output_value = _value

    def go(self):
        if not self.done:
            for _ in self.outputs:
                _.value = self.output_value
            self.done = True
            super().go()

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.output_value} -> {self.outputs[0]}"


class ENot(Element):
    def __init__(self,debug):
        super().__init__("not",debug)

    def go(self):
        if not self.done:
            for _ in self.inputs:
                if _.value is None:
                    return
            temp = ~self.inputs[0].value
            if temp < 0:
                temp += 2 ** 16
            for _ in self.outputs:
                _.value = temp
            self.done = True
            super().go()

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.type_of_element} {self.inputs[0]} -> {self.outputs[0]}"


class EAnd(Element):

    def __init__(self,debug):
        super().__init__("and",debug)

    def go(self):
        if not self.done:
            for _ in self.inputs:
                if _.value is None:
                    return
            temp = self.inputs[0].value & self.inputs[1].value
            if temp < 0:
                temp += 2 ** 16
            for _ in self.outputs:
                _.value = temp
            self.done = True
            super().go()

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.inputs[0]} {self.type_of_element} {self.inputs[1]} -> {self.outputs[0]}"


class EOr(Element):

    def __init__(self,debug):
        super().__init__("or",debug)

    def go(self):
        if not self.done:
            for _ in self.inputs:
                if _.value is None:
                    return
            temp = self.inputs[0].value | self.inputs[1].value
            if temp < 0:
                temp += 2 ** 16
            for _ in self.outputs:
                _.value = temp
            self.done = True
            super().go()

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.inputs[0]} {self.type_of_element} {self.inputs[1]} -> {self.outputs[0]}"


def get_element(raw_input_line: str, _wires: dict[str, Wire], _elements: dict[str, Element], debug):
    pieces = raw_input_line.split(" ")
    if "AND" in raw_input_line:
        _ = create_and_gate(_elements, _wires, debug, pieces)
    elif "OR" in raw_input_line:
        _ = create_or_gate(_wires, debug, pieces)
    elif "LSHIFT" in raw_input_line:
        _ = create_lshift_gate(_wires, debug, pieces)
    elif "RSHIFT" in raw_input_line:
        _ = create_rshift_gate(_wires, debug, pieces)
    elif "NOT" in raw_input_line:
        _ = create_not_gate(_wires, debug, pieces)
    else:
        _ = create_signal_gate(_wires, debug, pieces)
    _.set_uid()
    if _.uid not in _elements:
        _elements[_.uid] = _


def create_signal_gate(_wires, debug, pieces):
    _ = ESignal(int(pieces[0]), debug)
    _.add_output(_wires[pieces[2]])
    return _


def create_not_gate(_wires, debug, pieces):
    _ = ENot(debug)
    _.add_input(_wires[pieces[1]])
    _.add_output(_wires[pieces[3]])
    return _


def create_rshift_gate(_wires, debug, pieces):
    _ = ERShift(int(pieces[2]), debug)
    _.add_input(_wires[pieces[0]])
    _.add_output(_wires[pieces[4]])
    return _


def create_lshift_gate(_wires, debug, pieces):
    _ = ELShift(int(pieces[2]), debug)
    _.add_input(_wires[pieces[0]])
    _.add_output(_wires[pieces[4]])
    return _


def create_or_gate(_wires, debug, pieces):
    _ = EOr(debug)
    _.add_input(_wires[pieces[0]])
    _.add_input(_wires[pieces[2]])
    _.add_output(_wires[pieces[4]])
    return _


def create_and_gate(_elements, _wires, debug, pieces):
    _ = EAnd(debug)
    temp = None
    try:
        check = int(pieces[0])
        wtemp = None
        if "1 -> one" not in _elements.keys():
            temp = ESignal(1, debug)
            if "one" not in _wires.keys():
                wtemp = Wire("one")
                _wires['one'] = wtemp
                temp.add_output(wtemp)
                temp.set_uid()
                _elements[temp.uid] = temp
        else:
            wtemp = _wires['one']
        _.add_input(wtemp)
    except:
        _.add_input(_wires[pieces[0]])
    _.add_input(_wires[pieces[2]])
    _.add_output(_wires[pieces[4]])
    return _


def identify_wires(line_of_raw_input: str) -> dict[str, Wire]:
    _wires = dict()
    for line in line_of_raw_input.split("\n"):
        pieces_of_line = line.split(" ")
        for piece in [_.strip() for _ in pieces_of_line]:
            if piece.islower():
                if piece not in _wires.keys():
                    _wires[piece] = Wire(piece)

    return _wires


def part1(raw_input_string, debug: bool = False):
    wires = identify_wires(raw_input_string)
    elements = populate_elements(debug, raw_input_string, wires)
    if debug:
        c = 0
    while True:
        for wire in wires.values():
            if wire.value is not None:
                pass
            else:
                break
        else:
            break
        if debug:
            print(c)
            c += 1
        run_all_elements(elements)
    for wire_name, wire in wires.items():
        if wire_name == "lx":
            return wire.value, wires, elements


def populate_elements(debug, raw_input_string, wires):
    elements = dict()
    temp = raw_input_string.split("\n")
    temp.sort()
    for _ in temp:
        get_element(_, wires, elements, debug)
    return elements


def run_all_elements(elements):
    for element in elements.values():
        element.go()


def part2(_wires, _elements, debug=False):
    for element in _elements.values():
        element.done = False
    for wire in _wires.values():
        wire.value = None
    temp = _wires['b']
    for element in _elements.values():
        for output in element.outputs:
            if output == temp:
                element.output_value = answer
    if debug:
        c = 0
    while True:
        for wire in wires.values():
            if wire.value is not None:
                pass
            else:
                break
        else:
            break
        if debug:
            print(c)
            c += 1
        for element in elements.values():
            element.go()
    for wire_name, wire in wires.items():
        if wire_name == "lx":
            return wire.value, wires, elements


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
iy AND ja -> jb
NOT bb -> bc
ha OR gz -> hb
1 AND cx -> cy
NOT ax -> ay
ev OR ew -> ex
bn RSHIFT 2 -> bo
er OR es -> et
eu OR fa -> fb
jp OR ka -> kb
ea AND eb -> ed
k AND m -> n
et RSHIFT 3 -> ev
et RSHIFT 5 -> ew
hz RSHIFT 1 -> is
ki OR kj -> kk
NOT h -> i
lv LSHIFT 15 -> lz
as RSHIFT 1 -> bl
hu LSHIFT 15 -> hy
iw AND ix -> iz
lf RSHIFT 1 -> ly
fp OR fv -> fw
1 AND am -> an
ap LSHIFT 1 -> bj
u LSHIFT 1 -> ao
b RSHIFT 5 -> f
jq AND jw -> jy
iu RSHIFT 3 -> iw
ih AND ij -> ik
NOT iz -> ja
de OR dk -> dl
iu OR jf -> jg
as AND bd -> bf
b RSHIFT 3 -> e
jq OR jw -> jx
iv AND jb -> jd
cg OR ch -> ci
iu AND jf -> jh
1 AND cc -> cd
ly OR lz -> ma
NOT el -> em
1 AND bh -> bi
fb AND fd -> fe
lf OR lq -> lr
bn RSHIFT 3 -> bp
bn AND by -> ca
af AND ah -> ai
cf LSHIFT 1 -> cz
dw OR dx -> dy
gj AND gu -> gw
jg AND ji -> jj
jr OR js -> jt
bl OR bm -> bn
gj RSHIFT 2 -> gk
cj OR cp -> cq
gj OR gu -> gv
b OR n -> o
o AND q -> r
bi LSHIFT 15 -> bm
dy RSHIFT 1 -> er
cu AND cw -> cx
iw OR ix -> iy
hc OR hd -> he
0 -> c
db OR dc -> dd
kk RSHIFT 2 -> kl
eq LSHIFT 1 -> fk
dz OR ef -> eg
NOT ed -> ee
lw OR lv -> lx
fw AND fy -> fz
dz AND ef -> eh
jp RSHIFT 3 -> jr
lg AND lm -> lo
ci RSHIFT 2 -> cj
be AND bg -> bh
lc LSHIFT 1 -> lw
hm AND ho -> hp
jr AND js -> ju
1 AND io -> ip
cm AND co -> cp
ib OR ic -> id
NOT bf -> bg
fo RSHIFT 5 -> fr
ip LSHIFT 15 -> it
jt AND jv -> jw
jc AND je -> jf
du OR dt -> dv
NOT fx -> fy
aw AND ay -> az
ge LSHIFT 15 -> gi
NOT ak -> al
fm OR fn -> fo
ff AND fh -> fi
ci RSHIFT 5 -> cl
cz OR cy -> da
NOT ey -> ez
NOT ju -> jv
NOT ls -> lt
kk AND kv -> kx
NOT ii -> ij
kl AND kr -> kt
jk LSHIFT 15 -> jo
e OR f -> g
NOT bs -> bt
hi AND hk -> hl
hz OR ik -> il
ek AND em -> en
ao OR an -> ap
dv LSHIFT 1 -> ep
an LSHIFT 15 -> ar
fo RSHIFT 1 -> gh
NOT im -> in
kk RSHIFT 1 -> ld
hw LSHIFT 1 -> iq
ec AND ee -> ef
hb LSHIFT 1 -> hv
kb AND kd -> ke
x AND ai -> ak
dd AND do -> dq
aq OR ar -> as
iq OR ip -> ir
dl AND dn -> do
iu RSHIFT 5 -> ix
as OR bd -> be
NOT go -> gp
fk OR fj -> fl
jm LSHIFT 1 -> kg
NOT cv -> cw
dp AND dr -> ds
dt LSHIFT 15 -> dx
et RSHIFT 1 -> fm
dy RSHIFT 3 -> ea
fp AND fv -> fx
NOT p -> q
dd RSHIFT 2 -> de
eu AND fa -> fc
ba AND bc -> bd
dh AND dj -> dk
lr AND lt -> lu
he RSHIFT 1 -> hx
ex AND ez -> fa
df OR dg -> dh
fj LSHIFT 15 -> fn
NOT kx -> ky
gk OR gq -> gr
dy RSHIFT 2 -> dz
gh OR gi -> gj
lj AND ll -> lm
x OR ai -> aj
bz AND cb -> cc
1 AND lu -> lv
as RSHIFT 3 -> au
ce OR cd -> cf
il AND in -> io
dd RSHIFT 1 -> dw
NOT lo -> lp
c LSHIFT 1 -> t
dd RSHIFT 3 -> df
dd RSHIFT 5 -> dg
lh AND li -> lk
lf RSHIFT 5 -> li
dy RSHIFT 5 -> eb
NOT kt -> ku
at OR az -> ba
x RSHIFT 3 -> z
NOT lk -> ll
lb OR la -> lc
1 AND r -> s
lh OR li -> lj
ln AND lp -> lq
kk RSHIFT 5 -> kn
ea OR eb -> ec
ci AND ct -> cv
b RSHIFT 2 -> d
jp RSHIFT 1 -> ki
NOT cr -> cs
NOT jd -> je
jp RSHIFT 2 -> jq
jn OR jo -> jp
lf RSHIFT 3 -> lh
1 AND ds -> dt
lf AND lq -> ls
la LSHIFT 15 -> le
NOT fg -> fh
at AND az -> bb
au AND av -> ax
kw AND ky -> kz
v OR w -> x
kk OR kv -> kw
ks AND ku -> kv
kh LSHIFT 1 -> lb
1 AND kz -> la
NOT kc -> kd
x RSHIFT 2 -> y
et OR fe -> ff
et AND fe -> fg
NOT ac -> ad
jl OR jk -> jm
1 AND jj -> jk
bn RSHIFT 1 -> cg
NOT kp -> kq
ci RSHIFT 3 -> ck
ev AND ew -> ey
1 AND ke -> kf
cj AND cp -> cr
ir LSHIFT 1 -> jl
NOT gw -> gx
as RSHIFT 2 -> at
iu RSHIFT 1 -> jn
cy LSHIFT 15 -> dc
hg OR hh -> hi
ci RSHIFT 1 -> db
au OR av -> aw
km AND kn -> kp
gj RSHIFT 1 -> hc
iu RSHIFT 2 -> iv
ab AND ad -> ae
da LSHIFT 1 -> du
NOT bw -> bx
km OR kn -> ko
ko AND kq -> kr
bv AND bx -> by
kl OR kr -> ks
1 AND ht -> hu
df AND dg -> di
NOT ag -> ah
d OR j -> k
d AND j -> l
b AND n -> p
gf OR ge -> gg
gg LSHIFT 1 -> ha
bn RSHIFT 5 -> bq
bo OR bu -> bv
1 AND gy -> gz
s LSHIFT 15 -> w
NOT ie -> if
as RSHIFT 5 -> av
bo AND bu -> bw
hz AND ik -> im
bp AND bq -> bs
b RSHIFT 1 -> v
NOT l -> m
bp OR bq -> br
g AND i -> j
br AND bt -> bu
t OR s -> u
hz RSHIFT 5 -> ic
gk AND gq -> gs
fl LSHIFT 1 -> gf
he RSHIFT 3 -> hg
gz LSHIFT 15 -> hd
hf OR hl -> hm
1 AND gd -> ge
fo OR fz -> ga
id AND if -> ig
fo AND fz -> gb
gr AND gt -> gu
he OR hp -> hq
fq AND fr -> ft
ga AND gc -> gd
fo RSHIFT 2 -> fp
gl OR gm -> gn
hg AND hh -> hj
NOT hn -> ho
gl AND gm -> go
he RSHIFT 5 -> hh
NOT gb -> gc
hq AND hs -> ht
hz RSHIFT 3 -> ib
hz RSHIFT 2 -> ia
fq OR fr -> fs
hx OR hy -> hz
he AND hp -> hr
gj RSHIFT 5 -> gm
hf AND hl -> hn
hv OR hu -> hw
NOT hj -> hk
gj RSHIFT 3 -> gl
fo RSHIFT 3 -> fq
he RSHIFT 2 -> hf"""
    answer, wires, elements = part1(raw_samples,True)
    print(f"Part1 {answer}")
    # answer, wires, elements = part2(wires, elements)
    # print(f"Part2 {answer}")
