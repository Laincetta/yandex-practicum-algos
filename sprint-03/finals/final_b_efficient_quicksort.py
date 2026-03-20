from random import randint


Participant = tuple[str, int, int]  # (login, solved problems, fine)

def p1_equal_p2(p1: Participant, p2: Participant) -> bool:
    return p1 == p2


def p1_more_p2(p1: Participant, p2: Participant) -> bool:
    if p1[1] != p2[1]:
        return p1[1] > p2[1]  # -Pi
    elif p1[2] != p2[2]:
        return p1[2] < p2[2]  # Fi
    else:
        return p1[0] < p2[0]  # login


def efficient_quick_sort(participants: list[Participant]) -> list[Participant]:
    if len(participants) <= 1:
        return participants

    pivot = participants[randint(0, len(participants) - 1)]
    mid = []
    left = []
    right = []
    for participant in participants:
        if p1_equal_p2(participant, pivot):
            mid.append(participant)
        elif p1_more_p2(participant, pivot):
            left.append(participant)
        else:
            right.append(participant)
    return efficient_quick_sort(left) + mid + efficient_quick_sort(right)


if __name__ == '__main__':
    n = int(input())
    participants = [(login, int(p), int(f)) for login, p, f in (input().split() for _ in range(n))]
    for login, _, _ in efficient_quick_sort(participants):
        print(login)