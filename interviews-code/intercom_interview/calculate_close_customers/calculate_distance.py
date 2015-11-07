import math
 

def calculate_distance(latitude_a, longitude_a, latitude_b, longitude_b):
    """
    This function takes the latitude and longitude of 2 points, calculate
    the distance between the 2 points and return the result value in
    Kilometers

    It raise a ValueError Exception in case one of the parameters are not
    numbers
    """
    if (not isinstance(latitude_a, (int, long, float, complex)) or
            not isinstance(longitude_a, (int, long, float, complex)) or
            not isinstance(latitude_b, (int, long, float, complex)) or
            not isinstance(longitude_b, (int, long, float, complex))):
        raise ValueError(
            "The latitude and longitude parameters need to be numbers.")

    EARTH_RADIUS = 6371000 / 1000 # radius in Kilometers

    latitude_distance = math.radians(latitude_b - latitude_a)
    longitude_distance = math.radians(longitude_b - longitude_a)

    a = (math.sin(latitude_distance / 2) * math.sin(latitude_distance / 2) +
         math.cos(math.radians(latitude_a)) *
         math.cos(math.radians(latitude_b)) *
         math.sin(longitude_distance / 2) * math.sin(longitude_distance / 2))

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = EARTH_RADIUS * c
    
    return round(distance, 2)
