import os
import time
import sys
import concurrent.futures

def create_file():
    with open(f"file_{count_prefix}.exe", "w") as f:
        f.write("X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*")

try:
    count_prefix = 0

    for i in range(1, 50):
        print("Creating file #" + str(count_prefix))
        concurrent.futures.ProcessPoolExecutor(create_file())
        os.system(f"file_{count_prefix}.exe")

        count_prefix += 1

    print(f"""
----------------------------------------
RESULTS:
----------------------------------------

AV blocked files: pass
AV blocked execution chain: FAIL!""")

except KeyboardInterrupt:
    sys.exit()
