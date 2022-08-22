def look_and_say(raw_input:str)->str:
    current = None
    current_count = 0
    return_string = ""
    for c in raw_input:
        if current is None:
            current = c
            current_count += 1
        else:
            if c != current:
                return_string += f"{current_count}{current}"
                current = c
                current_count = 1
            else:
                current_count += 1
    return_string += f"{current_count}{current}"
    return return_string


if __name__ == "__main__":
    test = "1113122113"
    for i in range(50):
        test = look_and_say(test)
    print(len(test))