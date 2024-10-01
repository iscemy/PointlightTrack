
extends CSGSphere3D


var frequency = 0
var duty_cycle = 0
var sim_step_ms = 0

# Called when the node enters the scene tree for the first time.
func _ready():
	duty_cycle = get_meta("blink_duty_cycle")
	frequency = get_meta("blink_frequency")
	material = get_material()

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	sim_step_ms = sim_step_ms + (1.0/60.0) * 1000.0
	var period_ms = (1.0/frequency * 1000.0)
	var sim_step_ms_d = sim_step_ms / period_ms
	
	var sim_step_ms_ = sim_step_ms - (floor(sim_step_ms_d)) * period_ms
	
	if(sim_step_ms_ > (1.0/frequency * 1000.0 / 2.0)):
		material.albedo_color = Color(0.5, 0.5, 0.5, 1)
	else:
		material.albedo_color = Color(0.5, 0.5, 0.5, 0)
