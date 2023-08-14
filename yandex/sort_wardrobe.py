def sort_wardrobe(data: str) -> str:
    result = [0] * 3
    cash = ""
    for num in data:
        result[int(num)] += 1
    for i in range(len(result)):
        cash += str(i) * result[i]
    return " ".join(cash)


if __name__ == '__main__':
    n = int(input())
    example = input().replace(" ", "")
    print(sort_wardrobe(example))
