import re

with open("15.txt", 'r') as file:
    lines = [i.rstrip() for i in file.readlines()]

sensor = []
beacon = []
min_x = 1e10
max_x = -1e10
min_y = 1e10
max_y = -1e10
for line in lines:
    numbers = list(map(int, re.findall("-*[0-9]+", line)))
    min_x = min(numbers[0], min_x)
    min_x = min(numbers[2], min_x)
    min_y = min(numbers[1], min_y)
    min_y = min(numbers[3], min_y)

    max_x = max(numbers[0], max_x)
    max_x = max(numbers[2], max_x)
    max_y = max(numbers[1], max_y)
    max_y = max(numbers[3], max_y)


    sensor.append((numbers[0], numbers[1]))
    beacon.append((numbers[2], numbers[3]))
sensor_distance = []
clear = set()
set_sensor = set(sensor.copy())
set_beacon = set(beacon.copy())
for sensor_zip, beacon_zip in zip(sensor, beacon):
    #if sensor_zip != (8,7):
    #    continue
    s_x, s_y = sensor_zip
    b_x, b_y = beacon_zip

    delta_x = abs(s_x - b_x)
    delta_y = abs(s_y - b_y)
    manhattan_distance = delta_x + delta_y
    sensor_distance.append((s_x, s_y, manhattan_distance))

    for y in range(manhattan_distance+1):
        x = manhattan_distance+1 - y
        for dir_x, dir_y in [(-1,-1), (-1,1), (1,-1), (1,1)]:
            new_x = s_x + x*dir_x
            new_y = s_y + y*dir_y
            if not(0<=x<=4000000 and 0<=y<=4000000):
                continue
            clear.add((new_x, new_y))

for x, y in list(clear):
    for s_x, s_y, md in sensor_distance:
        if abs(x-s_x) + abs(y-s_y) <= md:
            clear.remove((x,y))
            break

res = [(x,y) for x,y in clear if 0<= x <= 4000000 and 0<= y <= 4000000][0]
print(res[0] * 4000000 + res[1])


