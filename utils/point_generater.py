import numpy as np


class PointGenerator(object):
    def __init__(self, count, min_long=-180.0, max_long=180.0, min_lat=-90.0, max_lat=90.0):
        self.count = count
        self.min_long = min_long
        self.max_long = max_long
        self.min_lat = min_lat
        self.max_lat = max_lat

