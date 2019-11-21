from missionaries_and_cannibals import MissionariesAndCannibals
from search import iterative_deepening_search


def main():
    problem = MissionariesAndCannibals()
    result = iterative_deepening_search(problem)
    list_arr = []
    for node in result.path():
        list_arr.append(node.state.value)
    return list_arr


if __name__ == '__main__':
    main()
