
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


def main():
    # R: rows van grid    -- < 10000
    # C: columns van grid || < 10000
    # F: aantal vehicles < 1000
    # N: aantal rides < 10000
    # B: per-ride bonus die je krijgt om ride op tijd te starten < 10000
    # T: aantal steps in simulatie < 1000000000000
    input = np.loadtxt('e_high_bonus.in', dtype=int)
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
    algoritme(ritten, number_of_vehicles)


def algoritme(ritten, number_of_vehicles):
    driven = []

    ritten = sorted(ritten, key=lambda rit: rit.earlyeststart)
    cars = []
    for i in range(number_of_vehicles):
        cars.append(Car(0, (0, 0), i))
        driven.append([])
    while len(ritten) > 0:
        car = cars[0]
        ride = ritten[0]
        if distance(car.endlocation, ride.start) + car.readytime < ride.laststart:
            driven[car.number].append(ride.number)
            car.endlocation = ride.end
            starttijd = min(ride.earlyeststart, car.readytime + distance(car.endlocation, ride.start))
            car.readytime = starttijd + distance(ride.start, ride.end)
            cars.sort(key=lambda car: car.readytime)
        del ritten[0]
    f = open("e_example.out",'w')
    for row in driven:
        print(len(row), end=" ",file=f)
        for r in row:
            print(r, end=" ",file=f)
        print(file=f)


main()
