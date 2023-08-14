# ID 87867532

class Competitor:
    def __init__(self, name: str, tasks: str, penaltys: str):
        self.name = name
        self.tasks = int(tasks)
        self.penaltys = int(penaltys)

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return (self.tasks, other.penaltys, other.name) < (
            other.tasks, self.penaltys, self.name)


def quicksort(example: list, left_border: int, right_border: int) -> None:
    if left_border >= right_border:
        return

    left, right = left_border, right_border
    pivot = example[left_border]

    while left <= right:
        while example[left] < pivot:
            left += 1
        while pivot < example[right]:
            right -= 1
        if left <= right:
            example[left], example[right] = example[right], example[left]
            left += 1
            right -= 1

    quicksort(example, left_border, right)
    quicksort(example, left, right_border)


if __name__ == '__main__':
    users_count = int(input())
    users_achievements = [Competitor(*input().split()) for _ in range(users_count)]
    quicksort(users_achievements, left_border=0,
              right_border=len(users_achievements) - 1)
    print(*users_achievements[::-1], sep='\n')
