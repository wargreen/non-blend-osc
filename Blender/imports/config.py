from subprocess import check_output


################## Static configuration // Edit here ###################
conf = {
	"osc_client_addr" : "127.0.0.1",
	"osc_client_port" : 1337,
	# full OSC path = osc_base_path + ObjectName + osc_[angle, radius, elevation]_path
	"osc_base_path": "Non-Mixer.nXEUB/strip/",
	"osc_angle_path": "/Spatializer/Azimuth",
	"osc_radius_path": "/Spatializer/Radius",
	"osc_elevation_path": "/Spatializer/Elevation"
	}



##### Look for the "random" OSC port of non-mixer
def non_port():
	portlist = check_output("netstat -ulpn -W | grep non-mixer | cut -d: -f2 | cut -d ' ' -f1 | tail -n1", shell=True)
	return portlist
	
non_portlist = int(non_port())

if non_portlist :
	conf["osc_client_port"] = non_portlist
	print("Found Non-mixer port : " + str(non_portlist))
