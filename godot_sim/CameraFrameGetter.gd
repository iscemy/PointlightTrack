extends Node

var index = 0
var timePassed = 0

var cam1ImageArray : Array[Image]  = []
var numOfImages = 500
var isFramesSavedOnce = 0
# Called when the node enters the scene tree for the first time.
func _ready():
	cam1ImageArray.resize(2000)
	pass

func save_frames():
	for index in numOfImages:
		cam1ImageArray[index].save_png("../sim_export/cam1_" + str(index) + ".png")

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):

	var cam1 : SubViewport = %cam1
	var cam2 : SubViewport = %cam2
	var cam3 : SubViewport = %cam3
	var cam4 : SubViewport = %cam4
	
	var im1 = cam1.get_texture().get_image()
	var im2 = cam2.get_texture().get_image()
	var im3 = cam3.get_texture().get_image()
	var im4 = cam4.get_texture().get_image()
	
	if(index < numOfImages):
		cam1ImageArray[index] = (im1)
	else:
		print(timePassed)
		if(isFramesSavedOnce == 0):
			save_frames()
			isFramesSavedOnce = 1
		return
	
	index += 1
	timePassed += delta
	return

