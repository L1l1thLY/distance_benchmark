import numpy as np
import json
import os
import random

class PointGenerator(object):
    def __init__(self, count, min_long=-180.0, max_long=180.0, min_lat=-90.0, max_lat=90.0):
        self.count = count
        self.min_long = min_long
        self.max_long = max_long
        self.min_lat = min_lat
        self.max_lat = max_lat
        self._point_list = list()

    def generate(self):
        for x in range(self.count):
            new_lat = random.uniform(self.min_lat, self.max_lat)
            new_long = random.uniform(self.min_long, self.max_long)
            new_point = dict(index=x, lat=new_lat, long=new_long)
            self._point_list.append(new_point)

        return self._point_list

    def save_to_file(self):
        if len(self._point_list) == 0:
            print("Error: No point generated!")
            return
        else:
            if os.path.exists("point_data"):
                pass
            else:
                os.mkdir("point_data")
            with open("point_data/point_list.json", mode="w") as json_file:
                json.dump(self._point_list, json_file, indent=2)
            print("Done: point list saved!")

