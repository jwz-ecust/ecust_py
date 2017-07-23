import queue


def task(name, work_queue):
    if work_queue.empty():
        print("Task {} nothing to do".format(name))
    else:
        while not work_queue.empty():
            count = work_queue.get()
            total = 0
            for x in range(count):
                print("Task {} running".format(name))
                total += 1
            print("Task {} total: {}".format(name, total))


def main():
    work_queue = queue.Queue()

    for work in [15, 10, 5, 2]:
        work_queue.put(work)


    tasks = [
        (task, 'one', work_queue),
        (task, 'two', work_queue)
    ]
    for t, n, q  in tasks:
        t(n, q)


if __name__ == "__main__":
    # main()
    zjw = queue.Queue()
    zjw.put("zjw")
    zjw.put('cbb')
    print(zjw.get())
    print(zjw.empty())
    print(zjw.get())
    print(zjw.empty())
