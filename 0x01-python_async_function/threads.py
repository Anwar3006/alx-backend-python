import threading
import time

def alice():
    while True:
        time.sleep(1)
        print("Hello this is Alice")

def bob():
    while True:
        time.sleep(0.8)
        print("Hi there; this is Bob")

threading.Thread(target=alice).start()
threading.Thread(target=bob).start()
