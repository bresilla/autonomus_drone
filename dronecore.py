import time
import dronekit
from pymavlink import mavutil

def status_info(vehicle):
    print "---------------------------------------------------"
    print " GPS: %s" % vehicle.gps_0
    print " Battery: %s" % vehicle.battery
    print " Last Heartbeat: %s" % vehicle.last_heartbeat
    print " Is Armable?: %s" % vehicle.is_armable
    print " System status: %s" % vehicle.system_status.state
    print " Mode: %s" % vehicle.mode.name    # settable
    print "---------------------------------------------------"
def check_n_arm(vehicle):
    print "Basic pre-arm checks"
    if not vehicle.armed:
        # Don't let the user try to arm until autopilot is ready
        while not vehicle.is_armable:
            print " Waiting for vehicle to initialise..."
            time.sleep(1)
        print "Arming motors"
        # Copter should arm in GUIDED mode
        vehicle.mode    = dronekit.VehicleMode("GUIDED")
        vehicle.armed   = True
        while not vehicle.armed:
            print " Waiting for arming..."
            time.sleep(1)
    else:
        print "Vehicle already armed"
def take_off(vehicle, z=2):
    vehicle.simple_takeoff(z) # Take off to target altitude
    while True:
        print " Altitude: ", vehicle.location.global_relative_frame.alt 
        if vehicle.location.global_relative_frame.alt>=z*0.95:
            break
        time.sleep(1)
def move_up(vehicle, z=0.25):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
        0,                                  # time_boot_ms (not used)
        0, 0,                               # target system, target component
        mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
        0b0000111111000111,                 # type_mask
        0, 0, 0,                            # x, y, z positions (not used)
        0, 0, -1*z,                          # m/s
        0, 0, 0,                            # x, y, z acceleration
        0, 0)
    vehicle.send_mavlink(msg)
    vehicle.flush()
def move_down(vehicle, z=0.25):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
        0,                                  # time_boot_ms (not used)
        0, 0,                               # target system, target component
        mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
        0b0000111111000111,                 # type_mask
        0, 0, 0,                            # x, y, z positions (not used)
        0, 0, z,                          # m/s
        0, 0, 0,                            # x, y, z acceleration
        0, 0)
    vehicle.send_mavlink(msg)
    vehicle.flush()
def move_left(vehicle, y=0.25):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
        0,                                  # time_boot_ms (not used)
        0, 0,                               # target system, target component
        mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
        0b0000111111000111,                 # type_mask
        0, 0, 0,                            # x, y, z positions (not used)
        0, -1*y, 0,                          # m/s
        0, 0, 0,                            # x, y, z acceleration
        0, 0)
    vehicle.send_mavlink(msg)
    vehicle.flush()
def move_right(vehicle, y=0.25):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
        0,                                  # time_boot_ms (not used)
        0, 0,                               # target system, target component
        mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
        0b0000111111000111,                 # type_mask
        0, 0, 0,                            # x, y, z positions (not used)
        0, y, 0,                          # m/s
        0, 0, 0,                            # x, y, z acceleration
        0, 0)
    vehicle.send_mavlink(msg)
    vehicle.flush()
def move_forward(vehicle, x=0.25):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
        0,                                  # time_boot_ms (not used)
        0, 0,                               # target system, target component
        mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
        0b0000111111000111,                 # type_mask
        0, 0, 0,                            # x, y, z positions (not used)
        x, 0, 0,                          # m/s
        0, 0, 0,                            # x, y, z acceleration
        0, 0)
    vehicle.send_mavlink(msg)
    vehicle.flush()
def move_backward(vehicle, x=0.25):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
        0,                                  # time_boot_ms (not used)
        0, 0,                               # target system, target component
        mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED, 
        0b0000111111000111,                 # type_mask
        0, 0, 0,                            # x, y, z positions (not used)
        -1*x, 0, 0,                       # m/s
        0, 0, 0,                            # x, y, z acceleration
        0, 0)
    vehicle.send_mavlink(msg)
    vehicle.flush()
