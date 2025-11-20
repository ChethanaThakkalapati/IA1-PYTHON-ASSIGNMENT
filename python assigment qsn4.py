# Program to record and analyze speeds over 12 hours

speeds = [12]   

print("Enter the speed of vehicles for each of the 12 hours:")

for i in range(12):
    speed = int(input(f"Hour {i+1} speed: "))
    speeds.append(speed)


average_speed = int(sum(speeds) / 12)


if average_speed < 40:
    flow = "Slow"
elif 40 <= average_speed <= 80:
    flow = "Normal"
else:
    flow = "Fast"


print("Traffic Report ")
print("Average Speed:", average_speed)
print("Traffic Flow:", flow)
