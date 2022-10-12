file_type = ''

print("Please input a directory")
file = input(">")


f = open(file, 'r')
line = f.readline()

if file.endswith(".asc"):
    time = 1
    position = 0
    id_position = 2
    lower_bound = 0.999
    upper_bound = 1.001
elif file.endswith(".trc"):
    time = 100
    position = 1
    id_position = 3
    lower_bound = 999.9
    upper_bound = 1000.1

first_id = ''
first_bit_count = 0

while line:
    splitLine = [x for x in line.split(" ") if x != ""]
    if "Rx" not in splitLine:
        line = f.readline()
    else:
        if "Rx" in splitLine:
            if first_id in splitLine[id_position]:
                first_bit_count += 1
                if first_id == '':
                    first_id = splitLine[id_position]
                    line = f.readline()
                elif lower_bound < float(splitLine[position]) < upper_bound:
                    if first_bit_count == 101:
                        print("Sample rate is 100Hz")
                    elif first_bit_count == 51:
                        print("Sample rate is 50Hz")
                    elif first_bit_count == 26:
                        print("Smaple rate is 25Hz")
                    elif first_bit_count == 21:
                        print("Sample rate is 20Hz")
                    elif first_bit_count == 11:
                        print("Sample rate is 10Hz")
                    elif first_bit_count == 6:
                        print("Sample rate is 5Hz")
                    elif first_bit_count == 2:
                        print("Sample rate is 1Hz")
                    else:
                        print("Unknown sample rate")
                    break
                else:
                    line = f.readline()
            else:
                line = f.readline()
        else: 
            line = f.readline()