import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from SerialCommunication import *

FFMPEG_BIN="ffmpeg"

ser = sensorInit()
num_rows = 7
num_cols = 4
toggle = 0
Matrix = np.zeros((num_rows, num_cols))
for i in range (4):
	Array = readSensors(ser, 28)
Matrix[0,0] = 255

Array = bytearray(num_rows*num_cols)
sensor_num = 28


def generate_data():
	Array = readSensors(ser, sensor_num)
	Matrix = matrixConvert(Array, num_rows, num_cols)
	return Matrix

def update(data):
	mat.set_data(data)
	#print("Doing update")
	return mat 

def data_gen():
	while True:
	    #print("Doing Data_gen")
	    yield generate_data()       

fig, ax = plt.subplots()
mat = ax.matshow(Matrix, interpolation='bicubic')
plt.colorbar(mat)
ani = animation.FuncAnimation(fig, update, data_gen, interval=3, save_count=150, 
blit=False)
ani.save('blah.mp4', writer="ffmpeg", fps=15)

plt.show()
