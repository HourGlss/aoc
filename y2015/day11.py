chars = [chr(_) for _ in range(97, 97 + 26)]
def check_increasing_straight(pswd) -> bool:
    global chars
    good = False
    last = -1
    in_a_row = 0
    for i, c in enumerate(pswd):
        # print(i,c,last,in_a_row)
        if last == -1:
            # print("\t1")
            last = chars.index(c)
        else:
            # print("\t2")
            if chars.index(c) == last + 1:
                # print("\t3")
                last = chars.index(c)
                in_a_row += 1
                if in_a_row == 3:
                    # print("\t4")
                    good = True
                    break
            else:
                # print("\t5")
                last = chars.index(c)
                in_a_row = 1
    return good


def check_banned_characters(pswd: str) -> bool:
    for c in pswd:
        if c == "i":
            return False
        if c == "o":
            return False
        if c == "l":
            return False
    return True


def check_non_overlapping_pairs(pswd: str) -> bool:
    last = -1
    pairs = []
    for i, c in enumerate(pswd):
        if last == -1:
            last = c
        else:
            if last == c:
                pairs.append(f"{c}{c}")
                last = -1
            else:
                last = c
    return len(pairs) >= 2


def check_password(pswd) -> bool:
    return check_non_overlapping_pairs(pswd) and check_banned_characters(pswd) and check_increasing_straight(pswd)


def increment_password(pswd, carry, return_password) -> str:
    global chars
    if pswd == "":
        return return_password
    else:
        current_character = pswd[len(pswd) - 1]
        pswd_to_forward = pswd[:len(pswd) - 1]
        if len(return_password) == 0 or carry:
            carry, return_password = increment_password_carry(current_character, return_password)
            return increment_password(pswd_to_forward, carry, return_password)
        else:
            return_password = current_character + return_password
            # print("-", pswd_to_forward, carry, return_password)
            return increment_password(pswd_to_forward, carry, return_password)


def increment_password_carry(current_character, return_password):
    global chars
    if current_character == "z":
        return_password = "a" + return_password
        carry = True
    else:
        current_character = chars[chars.index(current_character) + 1]
        return_password = current_character + return_password
        carry = False
    return carry, return_password


def get_next_password(pswd: str) -> str:
    password = pswd
    while True:
        password = increment_password(password, False, "")
        if check_password(password):
            break
    return password


if __name__ =="__main__":
    print(get_next_password("vzbxkghb"))
    print(get_next_password("vzbxxyzz"))
