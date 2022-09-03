class IP:
    raw: str
    outsides: list[str]
    hypernets: list[str]

    def __init__(self, raw_input):
        self.raw = raw_input
        self.outsides = self.extract_outsides()
        self.hypernets = self.extract_hypernets()

    def extract_outsides(self):
        pieces = []
        start = 0
        end = -1
        for i, c in enumerate(self.raw):
            if c == '[':
                end = i
            if end != -1:
                pieces.append(self.raw[start:end])
                end = -1
            if c == "]":
                start = i + 1
                end = -1

        pieces.append(self.raw[start:])
        return pieces

    def extract_hypernets(self):
        pieces = []
        start = 0
        end = -1
        for i, c in enumerate(self.raw):

            if end != -1:
                pieces.append(self.raw[start:end])
                end = -1
            if c == "[":
                start = i +1
                end = -1
            if c == ']':
                end = i

        # pieces.append(self.raw[start:])
        return pieces

    @staticmethod
    def extract_pieces(net_to_check: str) -> list[str]:
        pieces = []
        for i in range(len(net_to_check)+1):
            if i >= 4:
                sequence = net_to_check[i - 4:i]
                pieces.append(sequence)
        return pieces

    @staticmethod
    def check_for_abba(list_of_seq: list[str]) -> bool:
        for seq in list_of_seq:
            a, b, c, d = seq
            if a == d and b == c and a != b:
                return True
        return False

    def supports_tls(self):
        if self.check_ABBAs(self.outsides) and not self.check_ABBAs(self.hypernets):
            return True
        return False

    @staticmethod
    def check_ABBAs(nets_to_check):
        for net in nets_to_check:
            pieces = IP.extract_pieces(net)
            if IP.check_for_abba(pieces):
                return True
        return False


class InputHandler:
    ips: list[IP]

    def __init__(self):
        self.ips = []

    def handle_raw_input(self, raw_input):
        lines = raw_input.split("\n")
        for line in lines:
            self.ips.append(IP(line))

class OutputHandler:
    inputHandler: InputHandler
    output: int

    def __init__(self, i):
        self.inputHandler = i
        self.output = 0
        self.build_output()

    def build_output(self):
        for ip in self.inputHandler.ips:
            if ip.supports_tls():
                self.output += 1

    def get_output(self):
        return self.output


if __name__ == "__main__":
    ip = IP("abba[mnop]qrst")
    # print(ip.hypernets)
    # print(ip.outsides)
    a = IP.check_ABBAs(ip.outsides)
    b = IP.check_ABBAs(ip.hypernets)
    print(a,b)
    print(ip.supports_tls())
