#!/usr/bin/python3
"""
program that calculates the least amount of coins
needed to reach the total
"""


def makeChange(coins, total):
    if total < 0:
        return 0
    if not coins:
        return -1
    scoins = sorted(coins, reverse=True)
    total_coins = 0
    temp_total = 0
    for coin in scoins:
        temp = 0
        temp_total = total
        for coin in scoins:
            if coin <= temp_total:
                temp += temp_total // coin
                temp_total = temp_total % coin
        if total_coins == 0 or temp < total_coins:
            total_coins = temp
        scoins.pop(0)
    if temp_total == 0:
        return total_coins
    return -1
