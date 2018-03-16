import random

import numpy as np


class Rit:
    # klasse met rit in
    def __init__(self, a, b, x, y, s, laatstestart, number):
        self.start = (a, b)
        self.end = (x, y)
        self.earlyeststart = s
        self.laststart = laatstestart
        self.number = number


class Car:
    def __init__(self, readytime, endlocation, number):
        self.readytime = readytime
        self.endlocation = endlocation
        self.number = number


def distance(start: tuple, end: tuple):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


def main(inp, outp):
    # R: rows van grid    -- < 10000
    # C: columns van grid || < 10000
    # F: aantal vehicles < 1000
    # N: aantal rides < 10000
    # B: per-ride bonus die je krijgt om ride op tijd te starten < 10000
    # T: aantal steps in simulatie < 1000000000000
    input = np.loadtxt(inp, dtype=int)
    rows_in_grid, colums_in_grid, number_of_vehicles, number_of_rides, bonus, T = map(int, input[0])

    ritten = list()
    for ni in range(number_of_rides):
        # a: rij van startkruispunt < R
        # b: kolom van startkruispunt < C
        # x: rij van eindkruispunt < R
        # y: kolom van eindkruispunt < C
        # s: vroegste start < T
        # f: laatste finish < T
        a, b, x, y, s, f = map(int, input[ni + 1])
        laatstestart = f - distance((a, b), (x, y))

        ritten.append(Rit(a, b, x, y, s, laatstestart, ni))
    fill_score_stuff(rows_in_grid, colums_in_grid, ritten)

    algoritme(ritten, number_of_vehicles, bonus, outp)


def eindscore(result, ritten, bonus):
    score = 0
    for carindex, carrides in enumerate(result):
        vorigeplaats = (0, 0)
        tijd = 0
        for ride in carrides:
            score += distance(ritten[ride].start, ritten[ride].end)
            if tijd + distance(vorigeplaats, ritten[ride].start) <= ritten[ride].earlyeststart:
                score += bonus
            tijd += distance(vorigeplaats, ritten[ride].start) + distance(ritten[ride].start, ritten[ride].end)
            vorigeplaats = ritten[ride].end
    return score


# SCORE STUFF
hotspots = None
grid_size = None
heatmap = None
row_amt = None
col_amt = None


def fill_score_stuff(rows, cols, ritten):
    global hotspots
    global row_amt
    global col_amt
    global grid_size
    global heatmap

    grid_size = min(rows, cols, 100)
    grid_size += grid_size & 1

    hotspots = np.zeros((rows + 2 * grid_size, cols + 2 * grid_size), dtype=int)

    heatmap = np.zeros((grid_size, grid_size), dtype=int)
    half = grid_size // 2
    for i in range(half):
        heatmap[i, :half] = np.arange(i, half + i)
        heatmap[i, half:] = np.arange(half + i - 1, i - 1, -1)

    heatmap += np.flip(heatmap, axis=0)

    row_amt = rows
    col_amt = cols

    for rit in ritten:
        hotspots[rit.end[0] + grid_size, rit.end[1] + grid_size] += 1

    print("SCORE_STUFF")


def score(ride: Rit, car: Car, bonus):
    global hotspots
    global row_amt
    global col_amt
    global grid_size
    global heatmap

    r, c = car.endlocation

    half = grid_size // 2
    # ret = distance(ride.start, ride.end)
    # if distance(car.endlocation, ride.start) + car.readytime < ride.earlyeststart:
    #     ret += bonus
    #     ret -= (ride.earlyeststart - distance(car.endlocation, ride.start) - car.readytime)
    ret = 0
    ret += np.sum(hotspots[r + half:r + half + grid_size, c + half:c + half + grid_size] * heatmap)
    return ret


## END SCORE STUFF


def insert(cars, car):
    cars.append(None)

    key = lambda x: x
    find = key(car)

    cars_len = len(cars) - 1
    first = 0
    last = cars_len
    midpoint = last // 2

    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if key(cars[midpoint]) == find:
            found = True
        else:
            if key(cars[midpoint]) > find:
                last = midpoint - 1
            else:
                first = midpoint + 1

    cars[midpoint + 1:] = cars[midpoint:cars_len]
    cars[midpoint] = car


def algoritme(ritten, number_of_vehicles, bonus, outp):
    global hotspots

    bestscore = 8179753
    while True:
        driven = []
        ongesort = ritten.copy()

        ritten = sorted(ritten, key=lambda rit: rit.earlyeststart)
        cars = []
        for i in range(number_of_vehicles):
            cars.append(Car(0, (0, 0), i))
            driven.append([])
        while len(ritten) > 0:
            ride = ritten[0]
            hotspots[ride.end[0] + grid_size, ride.end[1] + grid_size] -= 1

            optimalecarindex = random.randrange(0, len(cars))
            # optimalescore = -1
            # for carindex, car in enumerate(cars):
            #     if distance(car.endlocation, ride.start) + car.readytime <= ride.laststart:
            #         current_score = score(ride, car, bonus)
            #         if current_score > optimalescore:
            #             optimalescore = current_score
            #             optimalecarindex = carindex
            if optimalecarindex != -1:
                driven[cars[optimalecarindex].number].append(ride.number)
                starttijd = max(ride.earlyeststart,
                                cars[optimalecarindex].readytime + distance(cars[optimalecarindex].endlocation,
                                                                            ride.start))
                cars[optimalecarindex].readytime = starttijd + distance(ride.start, ride.end)
                cars[optimalecarindex].endlocation = ride.end
                cars.sort(key=lambda car: car.readytime)
            del ritten[0]
        if eindscore(driven, ongesort, bonus) > bestscore:
            f = outp
            for row in driven:
                print(len(row), end=" ", file=f)
                for r in row:
                    print(r, end=" ", file=f)
                print(file=f)
            print("score moet %s zijn" % eindscore(driven, ongesort, bonus))
            exit()


main("c_no_hurry.in", open("c_no_hurry.out", "w"))

# print("score moet 4 zijn \n\
# a_example.in OK\n\
# score moet 123381 zijn\n\
# b_should_be_easy.in OK\n\
# score moet 8056275 zijn\n\
# c_no_hurry.in OK\n\
# score moet 3963138 zijn\n\
# d_metropolis.in OK\n\
# score moet 12795330 zijn\n\
# e_high_bonus.in OK")
