import os
import time
import multiprocessing as mp
import subprocess


def main():
    prev_time = time.time()
    # launch firefox in a subprocess
    p = subprocess.Popen(["firefox", "index.html", "--kiosk"])

    while True:
        now_time = time.time()
        if now_time - prev_time > 30:
            break

        print(now_time - prev_time)

    # terminate the subprocess if it's still running

    p.terminate()
    quit()


if __name__ == "__main__":
    main()
