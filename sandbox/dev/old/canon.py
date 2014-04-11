from Blender import *
from Blender.Registry import *
from math import *

# returns the location of the shell relative to the tip of the cannon
def getInitLoc(cannon, L, alphapitch, gammayaw):
    cLocX, cLocY, cLocZ = cannon.getLocation()
    sLocX  = cLocX + ( L * cos(pi/2.0 - alphapitch) * cos(gammayaw) )
    sLocY  = cLocY + ( L * cos(pi/2.0 - alphapitch) * sin(gammayaw)	)
    sLocZ  = cLocZ + ( L * cos(alphapitch) )
    return (sLocX, sLocY, sLocZ)

# get handles to objects
cannon   =  Object.Get('cannon')
shell    =  Object.Get('shell')
rotator  =  Object.Get('MCRotator')
elevator =  Object.Get('MCElevator')

# get a pointer to the objects function
cprop = cannon.getProperty

# get properties of the object
scale  = cprop('scale').data
timescale  = cprop('timescale').data
L      = cprop('L').data * scale
Vm     = cprop('Vm').data * scale
g      = cprop('g').data * scale
Yb     = cannon.getLocation()[2] * scale
hit    = cprop('hit').data

# get the current time
time   = (Get('curtime') - 1.0) * scale

# get the pitch and yaw angles of the cannon
#euler = cannon.getEuler()
#alphapitch = euler[1]
#gammayaw = euler[2]

# get the pitch and yaw angles from the rotator and elevator
# rotator is rotated about the vertical Z-Axis
# elevator is rotated about Y-Axis
alphapitch  = elevator.getEuler()[1] * scale
gammayaw    = rotator.getEuler()[2] * scale

# start simulation
if time == 0:
	cprop('hit').data = 0
        shell.LocX, shell.LocY, shell.LocZ = getInitLoc(L, alphapitch, gammayaw)	
	Redraw()
elif hit == 0:
       	oldX, oldY, oldZ = getInitLoc(L, alphapitch, gammayaw)
        
        # 'b' is the projection of the cannon (of length 'L') on the X-Y plane
	b = L * cos(pi/2.0 - alphapitch)

        # the components of the cannon along the 3 axes
	Lx = b * cos(gammayaw)
	Ly = b * sin(gammayaw)
	Lz = L * cos(alphapitch)
	
        # the directional cosines of the cannon
	cosX = Lx / L
	cosY = Ly / L
	cosZ = Lz / L 
		
	# calculate the instantneous displacement of the shell
	instX = Vm * cosX * time
	instY = Vm * cosY * time				
	instZ = Yb + (L * cos(alphapitch)) + (Vm * cosZ * time) + (0.5 * g * time * time)
	
        # calculate the total displacement of the shell
	shell.LocX = oldX + instX
	shell.LocY = oldY + instY
	shell.LocZ = oldZ + instZ

        # if the shell hit the ground, rewind simulation
	if shell.LocZ < 0.0:
	    shell.LocZ = 0.0
	    cprop('hit').data = 1
	    # we hit the floor. create a new object here.
	    obj = Object.New("Mesh", "ShellDead")
	    data = NMesh.GetRaw('shellmesh')
	    obj.link(data)
	    obj.setLocation(shell.getLocation())
	    Scene.GetCurrent().link(obj)
            Set('curframe', 1)
