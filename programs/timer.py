import time

t = int(input("how long should the timer be? (seconds):\n"))
for x in reversed(range(0, t + 1)):
    secs = x % 60
    mins = (x // 60) % 60
    hrs = (x // 3600) 
    print(f"\r{hrs:02}:{mins:02}:{secs:02}", end="", flush=True)
    time.sleep(1)

print("\nbeep beep beep!")
