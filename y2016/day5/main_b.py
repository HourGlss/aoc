import hashlib


class PasswordBuilder:
    password: str

    def __init__(self, door_id):
        self.password = PasswordBuilder.build_password(door_id)

    @staticmethod
    def build_password(door_id:str) -> str:
        ret = []
        for i in range(8):
            ret.append(None)
        _ = -1
        while None in ret:
            while True:
                m = hashlib.md5()
                m.update(f"{door_id}{_}".encode())
                hex_digest = m.hexdigest()
                _ += 1
                if PasswordBuilder.check_hash(hex_digest, 5):
                    position = int(hex_digest[5:6],16)
                    char = hex_digest[6:7]
                    try:
                        if ret[position] is None:
                            ret[position] = char
                        break
                    except:
                        pass
        return "".join(ret)

    @staticmethod
    def check_hash(hash_to_check: str, number_of_zeroes: int) -> bool:
        check_section = hash_to_check[:number_of_zeroes]
        check_set = set(check_section)
        if check_set == {'0'}:
            return True
        return False

