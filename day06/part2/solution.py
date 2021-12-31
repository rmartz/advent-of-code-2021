from functools import lru_cache
import sys

GROWTH_INTERVAL=7
START_INTERVAL=2+GROWTH_INTERVAL


@lru_cache
def fish_growth(days):
    if days < GROWTH_INTERVAL:
        return 1
    return (
        fish_growth(days - GROWTH_INTERVAL) +
        fish_growth(days - START_INTERVAL)
    )

days = 256
input = next(sys.stdin)
initial_cooldown = (int(val) for val in input.split(','))

fish_growths = (fish_growth(days - cooldown + 6) for cooldown in initial_cooldown)

print(sum(fish_growths))
