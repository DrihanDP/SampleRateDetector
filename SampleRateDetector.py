file = input(">")

f = open(file, 'r')
line = f.readline()

_301count = 0
bit_ID = []
first_bit = []

while line:
    if "Rx" not in line:
        line = f.readline()
    elif _301count == 101:
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
                _301count += 1
                if _301count == 0:
                    first_301_time = line[3:11]
                    line = f.readline()
                else:
                    line = f.readline()
            else:
                line = f.readline()
        else: 
            line = f.readline()