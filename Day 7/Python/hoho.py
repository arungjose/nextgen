t =input("Enter check-in time (12 Hr Std)    :    ")

time =  t.split(" ")

if time[1] == "pm":
        x = time[0].split(":")
        if int(x[0]) >= 2:
            print("Sorry! No Attendence. You were late.")
        else:
            print("Attendence marked!")
else:
    print("Attendence marked!")
