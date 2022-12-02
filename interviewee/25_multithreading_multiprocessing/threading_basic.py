import time
import threading

start = time.perf_counter()


def do_someting(seconds):
    print(f"Sleeping {seconds} second(s) ....")
    time.sleep(seconds)
    print("Done sleeping ....")

threads = []

for i in range(10):
    t = threading.Thread(target=do_someting, args=[i])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} second(s).")
