#!/usr/bin/python3
"""
program that calculates the least amount of coins 
needed to reach the total
"""

def makeChange(coins, total):
    if total < 0:
        return 0
    total_coins = 0
    scoins = sorted(coins, reverse=True)
    for coin in scoins:
        if coin < total:
            total_coins += total // coin
            total = total % coin
        if total == 0:
            return total_coins
    return -1
