import math
from typing import List


class SolutionCache:
    def __init__(self, file: str, comparator: callable):
        self.__comparator = comparator
        self.__file = file
        self.__scores = {}
        self.__solutions = {}

        self.__load()

    def __load(self):
        try:
            with open("outputs/{}.scores.txt".format(self.__file, 'r')) as fh:
                self.__scores = {idx: int(score) for idx, score in enumerate(fh.readlines())}

            with open("outputs/{}.output.txt".format(self.__file, 'r')) as fh:
                self.__solutions = {idx: solution.strip() for idx, solution in enumerate(fh.readlines())}
        except FileNotFoundError:
            pass

    def save(self, new_solutions: List[str], new_scores: List[int]):
        total_score = sum(self.__scores.values())

        for idx, solution in enumerate(new_solutions):
            try:
                old_score = self.__scores[idx]
            except KeyError:
                old_score = -float("inf")

            if math.isinf(old_score) or self.__comparator(old_score, new_scores[idx]):
                self.__scores[idx] = new_scores[idx]
                self.__solutions[idx] = new_solutions[idx]

        total_new_score = sum(self.__scores.values())

        print("New score: {} | Old score: {}".format(total_new_score, total_score))

        if self.__comparator(total_score, total_new_score):
            print("Improved! Good job =)")

            with open("outputs/{}.output.txt".format(self.__file), "w") as fh:
                output_solutions = [self.__solutions[idx] for idx in range(len(self.__solutions))]
                fh.write("\n".join(output_solutions))

            with open("outputs/{}.scores.txt".format(self.__file), "w") as fh:
                output_scores = [str(self.__scores[idx]) for idx in range(len(self.__scores))]
                fh.write("\n".join(output_scores))
        elif total_score == total_new_score:
            print("Equally good :/")
        else:
            print("Nooo :(")
