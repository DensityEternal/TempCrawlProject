
import time
from threadingTest import WeLearn
from concurrent.futures import ThreadPoolExecutor
import psutil
start_time = time.time()
with ThreadPoolExecutor(6)as t:
    # for i in range(1,7):
    #     t.submit(WeLearn,i)
    t.submit(WeLearn,1)
    t.submit(WeLearn, 2)
    t.submit(WeLearn, 3)
    t.submit(WeLearn, 4)
    t.submit(WeLearn, 5)
    t.submit(WeLearn, 6)
end_time = time.time()
print(psutil.cpu_percent())
print("Elapsed time:", end_time - start_time)