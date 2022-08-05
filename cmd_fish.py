import subprocess
import time
import os
def cmd():
    print("Run Cmd")
    os.system("start cmd /c py run_fish.py")
    time.sleep(1150)
    print("=================================")
    cmd()
cmd()