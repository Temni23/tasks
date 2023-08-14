from typing import List


def day_serch(days: List, price: int, left, right) -> int:
    if right <= left:
        return -1
    middlle = (left + right) // 2
    if days[middlle] >= price > days[middlle - 1] or middlle == 0:
        return middlle + 1
    elif days[middlle] >= price:
        return day_serch(days, price, left, middlle)
    else:
        return day_serch(days, price, middlle + 1, right)


if __name__ == "__main__":
    days_count = int(input())
    days_total_money = [int(x) for x in input().split()]
    price_of_bike = int(input())
    print(day_serch(days_total_money, price_of_bike, 0, len(days_total_money)), end=' ')
    print(day_serch(days_total_money, price_of_bike * 2, 0, len(days_total_money)))
