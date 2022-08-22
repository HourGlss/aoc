def part1():
    fin = open('day8.text', 'rb')
    after = 0
    before = 0
    while True:
        line = fin.readline()
        if line == b"":
            break
        after += len(eval(line[:-2]))
        before += len(line[:-2].decode('utf-8'))
    return before - after

def part2():
    fin = open('day8.text', 'rb')
    after = 0
    before = 0
    while True:
        line = fin.readline()
        if line == b"":
            break
        before += len(line[:-2].decode())
        new = b''
        for i in range(0,len(line[:-2])):
            if chr(line[i]) == '"':
                new += b'\\' + b'"'
            elif chr(line[i]) == '\\':
                new += b'\\' + b'\\'
            else:
                new += chr(line[1]).encode()
        new = b'"' + new + b'"'
        after += len(new.decode())
    return after - before


if __name__ == "__main__":
    print(part2())
