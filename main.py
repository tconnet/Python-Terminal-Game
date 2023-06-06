def close_flaps(numbers_to_replace, flaps):
    for num in numbers_to_replace:
        if num in flaps:
            flaps[flaps.index(num)] = '*'
    return flaps

def open_flaps(numbers_to_replace, flaps):
    for num in numbers_to_replace:
        if '*' in flaps:
            flaps[flaps.index('*')] = num
    return flaps

def draw_flaps(flaps):
    return f"""
---+---+---+---+---+---+---+---+---
 {' | '.join(map(str, flaps))} 
---+---+---+---+---+---+---+---+---
"""

flaps = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(draw_flaps(close_flaps([6, 4, 2], flaps[:])))

print(draw_flaps(open_flaps([6, 4, 2], flaps[:])))


