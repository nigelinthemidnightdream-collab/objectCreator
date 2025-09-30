import maya.cmds as cmds

def createObjects(obj):
	if obj == 'cone':
		cmds.polyCone()
	elif obj == 'cube':
		cmds.polyCube()
	elif obj == 'sphere':
		cmds.polySphere()
	elif obj == 'torus':
		cmds.polyTorus()
	elif obj == 'cylinder':
		cmds.polyCylinder()
