from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    if len(temperatures) == 1:
        return 1
    count = 0
    yesterday = None
    today = temperatures[0]
    tomorrow = temperatures[1]
    if today > tomorrow:
        count += 1
    yesterday = today
    for i in range(1, len(temperatures)-1):
        today = temperatures[i]
        tomorrow = temperatures[i + 1]
        if today > yesterday and today > tomorrow:
            count += 1
        yesterday = today
    if temperatures[-1] > temperatures[-2]:
        count += 1
    return count


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))
