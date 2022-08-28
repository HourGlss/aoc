from day19_data import replacement_string_input, molecule_input
import multiprocessing


def break_string(input_str: str, break_start: int, break_end: int) -> tuple[str, str]:
    start = ""
    end = ""
    for i in range(len(input_str)):
        if i < break_start:
            start += input_str[i]
        if i > break_end:
            end += input_str[i]
    return start, end


def build_replacements(replacement_input: str):
    replacements_to_return = {}
    for replacement_line in [_.strip() for _ in replacement_input.split("\n")]:
        pieces = replacement_line.split(" ")
        if pieces[0] not in replacements_to_return.keys():
            replacements_to_return[pieces[0]] = []
        replacements_to_return[pieces[0]].append(pieces[2])
    return replacements_to_return


def branch_combobulate_results(
        replacements_to_use: dict[str, list],
        molecule: str,
        current_path: list,
        tx_con: multiprocessing.Pipe,
        answer_q: multiprocessing.Queue
):
    if molecule == molecule_input:
        answer_queue.put(current_path)
        return
    for replacement in replacements_to_use.keys():
        lp = len(replacement)
        for i in range(0, len(molecule)):
            if i + lp > len(molecule):
                break
            current = molecule[i:i + lp]
            if current == replacement:
                for replace in replacements_to_use[replacement]:
                    s, e = break_string(molecule, i, i + lp - 1)
                    test = f"{s}{replace}{e}"
                    print(molecule,test,current_path, flush=True)
                    next_replacement = f"{replacement} => {replace}"
                    if len(current_path)>=1:
                        if next_replacement != current_path[-1]:
                            current_path.append(next_replacement)
                            nextp = multiprocessing.Process(target=branch_combobulate_results,
                                                            args=(replacements_to_use, test, current_path, tx_con, answer_q))
                            nextp.start()
                            tx_con.send(nextp)
                    else:
                        current_path.append(next_replacement)
                        nextp = multiprocessing.Process(target=branch_combobulate_results,
                                                        args=(
                                                        replacements_to_use, test, current_path, tx_con, answer_q))
                        nextp.start()
                        tx_con.send(nextp)

def handle_attempts(answer_q: multiprocessing.Queue, rx_con: multiprocessing.Pipe):
    answers = []
    processes = []
    while True:
        while not answer_q.empty():
            answers.append(answer_q.get(block=False))
        while rx_con.poll(timeout=.001):
            data = rx_con.recv()
            processes.append(data)
        if len(answers) > 0:
            break
    for process in processes:
        process.kill()
    for answer in answers:
        print(answer)


if __name__ == "__main__":
    answer_queue = multiprocessing.Queue()
    rx_pipe, tx_pipe = multiprocessing.Pipe()
    churn = multiprocessing.Process(target=branch_combobulate_results,
                                    args=(build_replacements(replacement_string_input), "e", [], tx_pipe, answer_queue))
    receive_data = multiprocessing.Process(target=handle_attempts, args=(answer_queue, rx_pipe))
    receive_data.start()
    churn.start()

    churn.join()
    receive_data.join()
    print("maybe done?")
