from cache.SolutionCache import SolutionCache


def score_comparator(old: int, new: int):
    return new > old


if __name__ == '__main__':
    cache = SolutionCache("1", score_comparator)

    # Algoritme bepaalt deze 2 lists:
    mysolution = ["solution1", "solution2"]
    myscores = [8, 1]

    cache.save(mysolution, myscores)
