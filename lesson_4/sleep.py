from time import sleep

n = 10  # a number of times 
dt = 1  # time delta [sec]
t = n * dt  # current time [sec]

while True:
    print(f'\rtime left: {t:02d} sec', end='')
    if t > 0:
        sleep(dt)
    else:
        print()
        break
    t -= dt
