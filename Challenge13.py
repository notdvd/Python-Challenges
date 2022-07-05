stations = ["s1", "s2", "s3", "s4", "s5"]
stations = ["s1"]

message = "This train is for "+stations[-1]+" and will be calling at: "

if len(stations) == 1:
    message += stations[0]
else:
    for station in stations:
        string = station + ", "
        message += string

print(message)
