from gpiozero import CPUTemperature
from time import strftime, time
import matplotlib.pyplot as plt

plt.ion()
x = []
y = []

cpu = CPUTemperature()
# type cpu.temperature in terminal to get a temp in C

stop_program = False

#create figure
fig = plt.figure()

def key_to_stop(event):
    global stop_program
    if event.key == 'q': # press 'q' in the plot window
        stop_program = True

fig.canvas.mpl_connect('key_press_event', key_to_stop)
        
print("Press 'q' to stop program")

with open("/home/matt_foord/cpu_temp.csv", "a") as log:
    while not stop_program:
        temp = cpu.temperature
        y.append(temp)
        x.append(len(x))
        plt.clf()
        plt.xlabel("Time (seconds)")
        plt.ylabel("Temperature (°C)")
        plt.title("CPU Temperature")
        plt.scatter(x,y)
        plt.plot(x,y)
        log.write("{0},{1}\n".format(strftime("%d-%m-%Y %H:%M:%S"), str(temp)))
        plt.pause(1)
        plt.draw()
