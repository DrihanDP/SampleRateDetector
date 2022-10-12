file_type = ''

print("Please input a directory")
file = input(">")


f = open(file, 'r')
line = f.readline()

if file.endswith(".asc"):
    file_type = "asc"
elif file.endswith(".trc"):
    file_type = "trc"

first_bit = []
first_bit_count = 0

while line:
    splitLine = [x for x in line.split(" ") if x != ""]
    if "Rx" not in splitLine:
        line = f.readline()
    elif first_bit_count == 101:
        print(line[1:11])
        if line[3:4] == "1":
            print("Sample rate is 100Hz")
        elif line[3:4] == "2":
            print("Sample rate is 50Hz")
        elif line[3:4] == "3" or line[3:4] == "4":
            print("Smaple rate is 25Hz")
        elif line[3:4] == "5":
            print("Sample rate is 20Hz")
        elif line[2:4] == "10":
            print("Sample rate is 10Hz")
        elif line[2:4] == "19" or line[2:4] == "20":
            print("Sample rate is 5Hz")
        elif line[2:4] == "99" or line[1:4] == "100":
            print("Sample rate is 1Hz")
        else:
            print("Unknown sample rate")
        break
    else:
        if "Rx" in line:
            if "301" in line[13:20]:
                first_bit_count += 1
                if first_bit_count == 0:
                    first_301_time = line[3:11]
                    line = f.readline()
                else:
                    line = f.readline()
            else:
                line = f.readline()
        else: 
            line = f.readline()