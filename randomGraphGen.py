import random as r
import matplotlib.pyplot as plt
import os
from datetime import datetime
from tqdm import tqdm
import cv2
import os

# Define the graph size (axis range)
axRang = 50

# Define the min and max number of nodes (n >= 1) and the jump size
start = 2
nodes = 250
jump = 1

# Define a new directory in which to save the graph images
try:
	imDir = "perc/"+str(nodes)+"_"+str(jump)+"_"+str(datetime.today().date())
	os.makedirs(imDir)
except:
	imDir = "perc/"+str(nodes)+"_"+str(jump)+"_"+str(datetime.today().date())+str(1)
	os.makedirs(imDir)

# Set the seed for the random number generator
seedNum = r.randint(0,100)

# Generate the random 3D graph the specified amount of times
# Use tqdm to add a progress meter in the terminal
for n in tqdm(range(start,nodes,jump), desc = "Processing", unit = "iteration"):
	x = []
	y = []
	z = []
	graphSize = n
	r.seed(seedNum)
	
	# Generate the coordinates for each node
	for i in range(graphSize):
		x.append(r.randint(0,axRang))
		y.append(r.randint(0,axRang))
		z.append(r.randint(0,axRang))

	# Plot nodes on the graph
	fig = plt.figure(figsize = (8, 8))
	ax = fig.add_subplot(111, projection = "3d")
	scatter= ax.scatter(x, y, z, s = 1, color = "black")
	ax.set_xlim(0,axRang)
	ax.set_ylim(0,axRang)
	ax.set_zlim(0,axRang)
	plt.axis("off")
	plt.grid(False)

	# Define the boundary for joining nodes (side length of box / 2)
	rang = 10
	
	# Connect the nodes
	for i in range(graphSize):
		for j in range(i + 1, graphSize):
				if x[i] in range(x[j] - rang, x[j] + rang) and y[i] in range(y[j] - rang, y[j] + rang) and z[i] in range(z[j] - rang, z[j] + rang):
					ax.plot([x[i], x[j]], [y[i], y[j]], [z[i], z[j]], color = "red", linewidth = 0.5)
	
	# Save the plot to a specified folder
	plt.savefig(imDir + "/" + str(n) + ".png", dpi = 100)
	#plt.show()
	plt.close()

# Create a video of the evolution of the graph from the plots
image_folder = imDir
video_name = 'VIDEO.avi'
images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
images = sorted(images, key=lambda x: int(x.split('.')[0]))
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape
video = cv2.VideoWriter(video_name, 0, 1, (width, height))
for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))
cv2.destroyAllWindows()
video.release()
