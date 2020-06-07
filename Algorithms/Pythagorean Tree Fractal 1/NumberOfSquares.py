def numberOfSquares(level):
    if level == 1:
        return 1
    else:
        return 1 + 2*numberOfSquares(level - 1)


print(numberOfSquares(50))
