import time

setTime = int(input("Ketikkan Jumlah Waktu yang Ingin Anda Atur Timer-nya: "))

for x in range(setTime, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

print("GET OUT!")
