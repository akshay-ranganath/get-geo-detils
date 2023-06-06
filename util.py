import reverse_geocoder as rg
import re

pattern = '(\d+)deg(\d+)\'([0-9.]+)\"([EWNS])'

def split_coords(coords):
    deg, mins, sec, dir = (0, 0, 0, 'N')    
    coords = coords.replace(' ','')

    res = re.match(pattern, coords)
    if res.groups() and len(res.groups()) == 4:
        deg, mins, sec, dir = res.groups()
    return (deg, mins, sec, dir)

def get_direction(deg, mins, sec, dir):
    value = int(deg) + (float(mins) / 60) + (float(sec) / 3600)
    if dir in ['S','W']:
        value = -1 * value
    return value    

def convert_coords(coords):
    deg, mins, sec, dir = split_coords(coords)
    return get_direction(deg, mins, sec, dir)    

def get_location(coords):
    lat, long = coords.split(':')
    lat = convert_coords(lat)
    long = convert_coords(long)
    res = rg.get((long,lat))
    return res