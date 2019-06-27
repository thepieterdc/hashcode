from sys import stdout

import numpy as np
import os


class Car:
    def __init__(self, id, startCoord: tuple, finishCoord: tuple, startTime: int):
        self.id = id
        self.startCoord = startCoord
        self.finishCoord = finishCoord
        self.startTime = startTime

    def isAvailable(self, currentTime: int):
        return distance(self.startCoord, self.finishCoord) <= (currentTime - self.startTime)

    def distanceTo(self, coord: tuple):
        return distance(self.finishCoord, coord)


def distance(start: tuple, end: tuple):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


def get_hotspots(rows, cols, ritten):
    hotspots = np.zeros((rows, cols), dtype=int)

    for rit in ritten:
        hotspots[rit[2], rit[3]] += 1

    return None


def main(input, output):
    ritten = np.loadtxt(input, dtype=int)

    # R: rows van grid    -- < 10000
    # C: columns van grid || < 10000
    # F: aantal vehicles < 1000
    # N: aantal rides < 10000
    # B: per-ride bonus die je krijgt om ride op tijd te starten < 10000
    # T: aantal steps in simulatie < 1000000000000
    R, C, F, N, B, T = tuple(ritten[0])

    ritten = ritten[1:]

    autoLijst = [Car(x, (0, 0), (0, 0), 0) for x in range(F)]

    result = [[] for x in autoLijst]

    time = 0

    def assign(startCoord: tuple, eindCoord: tuple, time):
        availableCars = []
        for car in autoLijst:
            if car.isAvailable(time):
                availableCars.append((car, car.distanceTo(startCoord)))

        if availableCars:
            bestCar, bestDist = availableCars[0]
            for car in availableCars:
                if car[1] < bestDist:
                    bestCar = car[0]
                    bestDist = car[1]
            bestCar.startCoord = bestCar.finishCoord
            bestCar.finishCoord = eindCoord
            bestCar.startTime = time
            return bestCar
        return None

    for i, rit in enumerate(ritten):
        ritStart = (rit[0], rit[1])
        ritEind = (rit[2], rit[3])
        assgn = assign(ritStart, ritEind, time)
        while not assgn:
            time += 1
            assgn = assign(ritStart, ritEind, time)

        result[assgn.id].append(i)

    for id, ritten in enumerate(result):
        print("{} {}".format(id + 1, " ".join(str(x) for x in ritten)), file=output)


def runAll():
    for file in ["a_example.in", "b_should_be_easy.in", "c_no_hurry.in", "d_metropolis.in", "e_high_bonus.in"]:
        try:
            os.remove("{}.out".format(file))
        except:
            pass

    for file in ["a_example.in", "b_should_be_easy.in", "c_no_hurry.in", "d_metropolis.in", "e_high_bonus.in"]:
        main(file, open("{}.out".format(file), "w"))
        print("{} OK".format(file))

runAll()