import time

start = time.perf_counter()


def do_someting():
    print("Sleeping 1 second ....")
    time.sleep(1)
    print("Done sleeping ....")


do_someting()
do_someting()
do_someting()
do_someting()
do_someting()

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} second(s).")
