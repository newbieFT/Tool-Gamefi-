import subprocess
import time
import requests
import json
def cmd():
    process_1 = subprocess.Popen(['py', 'fish_1.py'])
    process_2 = subprocess.Popen(['py', 'fish_2.py'])
    process_3 = subprocess.Popen(['py', 'fish_3.py'])
    process_4 = subprocess.Popen(['py', 'fish_4.py'])
    process_5 = subprocess.Popen(['py', 'fish_5.py'])
    process_6 = subprocess.Popen(['py', 'fish_6.py'])
    time.sleep(50)
    process_1.kill()
    process_2.kill()
    process_3.kill()
    process_4.kill()
    process_5.kill()
    process_6.kill()
def tatcmd():
    for xzz in range (1,20):
        cmd()
        time.sleep(5)
    exit()
tatcmd()