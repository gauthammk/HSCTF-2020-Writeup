# Pythagorean Tree Fractal 1

Points: 100

## Solution

A very basic recursive algorithm. Each level has two times the number of squares in the previous level and one additional square as the base.

```python
def numberOfSquares(level):
    if level == 1:
        return 1
    else:
        return 1 + 2*numberOfSquares(level - 1)


print(numberOfSquares(50))
```

Flag : `flag{1125899906842623}`
