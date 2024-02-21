from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import random


def do_something(x):
    time.sleep(3)
    return f"Task {x} completed."

# ThreadPoolExecutorを使用して非同期タスクを実行
with ThreadPoolExecutor(max_workers=2) as executor:    
    # 3つのタスクを非同期に実行
    start = time.time()
    futures = [executor.submit(do_something, i) for i in range(3)]
    results = []

    # as_completedを使用して各タスクの完了を待つ
    for future in as_completed(futures):
        results.append(future.result())
    print(results)
    end = time.time()
    print(f"Elapsed time: {end - start} sec")    
