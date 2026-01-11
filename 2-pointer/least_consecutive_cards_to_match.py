from collections import defaultdict
import math

def least_consecutive_cards_to_match(cards: list[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    window = set()
    minl = math.inf
    left = 0
    for right in range(len(cards)):
        while cards[right] in window:
            window.remove(cards[left])
            minl = min(minl, right - left + 1)
            left += 1
        window.add(cards[right])

    return minl if minl != math.inf else -1
