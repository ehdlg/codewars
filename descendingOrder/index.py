def descendingOrder(n: int):
    n = [x for x in str(n)]

    n.sort(reverse=True)

    return "".join(n)


print(descendingOrder(23324162346))
