from utils.point_generator import PointGenerator
from algorithm.traditional import DistanceAlgorithm
import time
import heapq
from algorithm import s2

if __name__ == '__main__':
    algo = DistanceAlgorithm()

    print(algo.spherical_distance(90, 13, 79, 45))

    gen = PointGenerator(count=1000000)
    point_list = gen.generate()

    # Traditional Algorithm
    start = time.clock()

    distance_list = list()
    distance_list.append(-1)

    for x in point_list[1:]:
        distance_list.append(algo.spherical_distance(point_list[0]["lat"], point_list[0]["long"], x["lat"], x["long"]))

    min_num_index_list = map(distance_list.index, heapq.nsmallest(5, distance_list))
    print(list(min_num_index_list))

    print("spherical_distance Time used:", time.clock() - start)

    # S2
    start = time.clock()

    hilbert_list = list()

    i = 0

    for x in point_list:
        hilbert = s2.point_to_hilbert(x["long"], x["lat"])
        hilbert_list.append(dict(index=i, hilbert=hilbert))
        i = i + 1

    print("s2 hilbertTime used:", time.clock() - start)

    hilbert_list_sorted = sorted(hilbert_list, key=lambda e: e.__getitem__("hilbert"))

    for index in range(len(hilbert_list_sorted)):
        if hilbert_list_sorted[index]["index"] == 0:
            print(hilbert_list_sorted[index - 1]["index"])
            print(hilbert_list_sorted[index - 2]["index"])
            print(hilbert_list_sorted[index]["index"])
            print(hilbert_list_sorted[index + 1]["index"])
            print(hilbert_list_sorted[index + 2]["index"])

    print("s2 Time used:", time.clock() - start)



