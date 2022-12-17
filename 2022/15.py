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

row = 10
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

    for y in range(s_y-manhattan_distance, s_y+manhattan_distance):
        if y < 0 and y > 20:
            continue
        for x in range(s_x-manhattan_distance, s_x+ manhattan_distance):
            if x < 0 and x > 20:
                continue
            new_pos = (x,y)
            if abs(new_pos[0] - s_x) + abs(new_pos[1] - s_y) <= manhattan_distance:
                if new_pos not in set_sensor and new_pos not in set_beacon:
                    clear.add(new_pos)

                

count = len([x for x in clear if x[1] == row])
print(count)
count = count + len([x for x in set_sensor if x[1] == row])
#print(count)

possible_location = []
def print_matrix(min_x, max_x, min_y, max_y):
    for y in range(min_y, max_y+1):
        for x in range(min_x, max_x+1):
            current_tup = (x,y)
            if current_tup in sensor:
                print("S", end="")
                pass
            elif current_tup in beacon:
                print("B", end="")
                pass
            elif current_tup in clear:
                print("#", end="")
                pass
            else:
                possible_location.append((x,y))

                print(".", end="")
        print(y)

#print_matrix(-2, 26, -2, 26)
print_matrix(0, 20, 0, 20)
print(possible_location)
x, y = possible_location[0]
print(x*4000000 + y)
