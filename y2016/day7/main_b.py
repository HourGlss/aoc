class IP:
    raw: str
    supernets: list[str]
    hypernets: list[str]

    def __init__(self, raw_input):
        self.raw = raw_input
        self.supernets = self.extract_outsides()
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
                start = i + 1
                end = -1
            if c == ']':
                end = i

        # pieces.append(self.raw[start:])
        return pieces

    @staticmethod
    def extract_aba_pieces(net_to_check: str) -> list[str]:
        pieces = []
        for i in range(len(net_to_check) + 1):
            if i >= 3:
                sequence = net_to_check[i - 3:i]
                pieces.append(sequence)
        return pieces

    @staticmethod
    def check_for_aba(list_of_seq: list[str]) -> list[str]:
        abas = []
        for seq in list_of_seq:
            a, b, c = seq
            if a == c and b != a:
                abas.append(f"{a}{b}{c}")
        return abas

    @staticmethod
    def convert_abas_to_babs(list_of_seq: list[str]) -> list[str]:
        babs_out = []
        for seq in list_of_seq:
            a,b,c = seq
            babs_out.append(f"{b}{a}{b}")
        return babs_out

    def supports_ssl(self):
        valid_supernet_abas = []
        for net in self.supernets:
            pieces = IP.extract_aba_pieces(net)
            aba_check = IP.check_for_aba(pieces)
            for check in aba_check:
                valid_supernet_abas.append(check)
        valid_hypernet_babs = []
        for net in self.hypernets:
            pieces = IP.extract_aba_pieces(net)
            aba_check = IP.check_for_aba(pieces)
            for check in aba_check:
                valid_hypernet_babs.append(check)
        valid_supernet_babs = IP.convert_abas_to_babs(valid_supernet_abas)
        for aba in valid_supernet_babs:
            for bab in valid_hypernet_babs:
                if aba == bab:
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
            if ip.supports_ssl():
                self.output += 1

    def get_output(self):
        return self.output
