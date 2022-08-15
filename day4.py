import threading
import multiprocessing
import hashlib
import os
import queue

"""
--- Day 4: The Ideal Stocking Stuffer ---

Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically 
forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 
hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must
 find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes 
(000001dbbfa...), and it is the lowest such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is
 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
Your puzzle answer was 346386.
"""

PUZZ = "iwrupvqb"


def get_hash(_n):
    m = hashlib.md5()
    m.update(f"{PUZZ}{_n}".encode())
    check = m.hexdigest()
    digits = 6
    # print(check)
    if check[0:digits] == "0" * digits:
        print(digits, PUZZ, _n, check)


def work(q):
    while not q.empty():
        n = q.get()
        get_hash(n)
        q.task_done()


def split_tasks(_proc_number, _min, _max):
    jobs = queue.Queue()
    # print(_proc_number, _min, _max)
    for i in range(_min, _max):
        jobs.put(i)

    # print(_proc_number, "loaded all jobs")
    for i in range(100):
        worker = threading.Thread(target=work, args=(jobs,))
        worker.start()
    jobs.join()


if __name__ == "__main__":
    start = 0
    end = 10000000
    while end % os.cpu_count() != 0:
        end += 1
    step = end // os.cpu_count()
    procs = []
    k = 0
    for i in range(start, end, step):
        proc = multiprocessing.Process(target=split_tasks, args=(k, i, i + step))
        k += 1
        procs.append(proc)
    for proc in procs:
        proc.start()
