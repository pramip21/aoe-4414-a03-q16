# sez_to_ecef.py
# Usage: python3 script_name.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Pramil Patel
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
# e.g., import math # math module
import sys # argv
import math
import subprocess
import os
import numpy

# "constants"
# e.g., R_E_KM = 6378.137
# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
# arg1 = '' # description of argument 1
# arg2 = '' # description of argument 2

# parse script arguments
# if len(sys.argv)==3:
#   arg1 = sys.argv[1]
#   arg2 = sys.argv[2]
#   ...
# else:
#   print(\
#    'Usage: '\
#    'python3 arg1 arg2 ...'\
#   )
#   exit()
o_lat_deg = float('nan')
o_lon_deg = float('nan')
o_hae_km = float('nan')
s_km = float('nan')
e_km = float('nan')
z_km = float('nan')

if len(sys.argv)==7:
    o_lat_deg = float(sys.argv[1])
    o_lon_deg = float(sys.argv[2])
    o_hae_km = float(sys.argv[3])
    s_km = float(sys.argv[4])
    e_km = float(sys.argv[5])
    z_km = float(sys.argv[6])
else:
    print("Usage: python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km")
    

# write script below this line
o_lat_rad = o_lat_deg*(math.pi/180)
o_lon_rad = o_lon_deg*(math.pi/180)
hae_km = o_hae_km
lat_deg = o_lat_deg
lon_deg = o_lon_deg
lat_rad = o_lat_rad
lon_rad = o_lon_rad

r_ECEF = numpy.array([[(math.cos(o_lon_rad)*math.sin(o_lat_rad)*s_km) + (math.cos(o_lon_rad)*math.cos(o_lat_rad)*z_km) - (math.sin(o_lon_rad)*e_km)],
          [(math.sin(o_lon_rad)*math.sin(o_lat_rad)*s_km) + (math.sin(o_lon_rad)*math.cos(o_lat_rad)*z_km) + (math.cos(o_lon_rad)*e_km)],
          [(-math.cos(o_lat_rad)*s_km) + (math.sin(o_lat_rad)*z_km)]])

R_E_KM = 6378.1363
e_E = 0.081819221456

def calc_denom(ecc, lat_rad):
    return math.sqrt(1.0-(ecc**2)*(math.sin(lat_rad))**2)

denom = calc_denom(e_E,lat_rad)
C_E = R_E_KM/denom
S_E = (R_E_KM*(1-(e_E**2)))/denom

r_x_km=(C_E+hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
r_y_km=(C_E+hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
r_z_km=(S_E+hae_km)*math.sin(lat_rad)

r_km_array = numpy.array([[r_x_km], [r_y_km], [r_z_km]])

ecef_km = r_ECEF + r_km_array

print(ecef_km[0])
print(ecef_km[1])
print(ecef_km[2])
