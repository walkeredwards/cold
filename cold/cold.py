"""Kattis cold puter problem.
"""


__author__ = "Walker Edwards"
__date__ = "October 10, 2023"


def answer(temps: str) -> int:
    """Finds and returns the number of negative numbers

    Args:
        temps (str): temps seperated by a space
    Returns:
        int: number of negative numbers
    """
    return temps.count('-')


def solve() -> None:
    """_summary_
    """
    # n = input()
    data = input()
    print(answer(data))


if __name__ == "__main__":
    solve()
