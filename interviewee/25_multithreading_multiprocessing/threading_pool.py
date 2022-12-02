import time
import concurrent.futures

start = time.perf_counter()


def do_someting(seconds):
    print(f"Sleeping {seconds} second(s) ....")
    time.sleep(seconds)
    return f"Done sleeping .... {seconds} second(s)."

with concurrent.futures.ThreadPoolExecutor() as executor:
#     f1 = executor.submit(do_someting, 1)
#     print(f1.result())
    results = [executor.submit(do_someting, i) for i in range(9,-1,-1)]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

# threads = []

# for i in range(10):
#     t = threading.Thread(target=do_someting, args=[i])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} second(s).")
