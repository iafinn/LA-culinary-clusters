from math import radians, cos, sin, asin, sqrt


def haver(lon_list, lat_list, lon2, lat2):
    """
    this very useful function is from: 
    https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
    Calculate the great circle distance between two points in kilometers
    on the earth (specified in decimal degrees)
    """
    d_list = []
    for lon1, lat1 in zip(lon_list, lat_list):
        # convert decimal degrees to radians 
        lon1, lat1, lon2a, lat2a = map(radians, [lon1, lat1, lon2, lat2])

        # haversine formula 
        dlon = lon2a - lon1 
        dlat = lat2a - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2a) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 6371 # Radius of earth in kilometers. Use 3956 for miles
        d_list.append(c * r)
    return d_list