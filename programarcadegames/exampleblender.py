# Import Blender Game Engine
import bge
# Get a reference to the blue object
cont = bge.logic.getCurrentController()
blueObject = cont.owner
# Print the x,y coordinates where the blue object is
print(blueObject.position[0], blueObject.position[1] )
# Change x,y coordinates according to x_change and
# y_change. x_change and y_change are game properties
# associated with the blue object.
blueObject.position[0] += blueObject["x_change"]
blueObject.position[1] += blueObject["y_change"]
# Check to see of the object has gone to the edge.
# If so reverse direction. Do so with all 4 edges.
if blueObject.position[0] > 6 and blueObject["x_change"] > 0:
    blueObject["x_change"] *= -1
if blueObject.position[0] < -6 and blueObject["x_change"] < 0:
    blueObject["x_change"] *= -1
if blueObject.position[1] > 6 and blueObject["y_change"] > 0:
    blueObject["y_change"] *= -1
if blueObject.position[1] < -6 and blueObject["y_change"] < 0:
    blueObject["y_change"] *= -1
