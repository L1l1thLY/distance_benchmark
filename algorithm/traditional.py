import math
import numpy as np


class DistanceAlgorithm(object):
    def __init__(self):
        pass

    # spherical_distance Time used: 1.6785420000000002
    @staticmethod
    def spherical_distance(a_lat, a_long, b_lat, b_long):
        a_rad_lat = math.radians(a_lat)
        b_rad_lat = math.radians(b_lat)
        lat_delta = a_rad_lat - b_rad_lat
        long_delta = math.radians(a_long) - math.radians(b_long)

        distance = 2 * math.asin(
            math.sqrt(
                math.pow(math.sin(lat_delta / 2), 2) + \
                math.cos(a_rad_lat) * math.cos(b_rad_lat) * \
                math.pow(math.sin(long_delta / 2), 2)
            )) * 6378.137

        return distance

    # Time used: 6.774689
    @staticmethod
    def relative_distance(a_lat, a_long, b_lat, b_long):
        point_a = np.array([a_lat, a_long]).reshape((2, 1))
        point_b = np.array([b_lat, b_long]).reshape((2, 1))

        return np.linalg.norm(point_a - point_b)

    # Time used: 0.7238929999999999
    @staticmethod
    def relative_distance_2(a_lat, a_long, b_lat, b_long):
        return math.sqrt(math.pow((a_lat - b_lat), 2) + math.pow((a_long - b_long), 2))

    # Time used: 3.221544
    @staticmethod
    def relative_distance_3(a_lat, a_long, b_lat, b_long):
        return np.sqrt(np.square(a_lat - b_lat) + np.square(a_long - b_long))
