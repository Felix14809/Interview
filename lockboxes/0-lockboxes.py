#!/usr/bin/python3


def canUnlockAll(boxes):
    keys = [0]
    unlocked = []
    prev_unlocked = -1
    while prev_unlocked != len(unlocked):
        prev_unlocked = len(unlocked)
        for box in range(len(boxes)):
            if box in keys and box not in unlocked:
                for key in boxes[box]:
                    keys.append(key)
                unlocked.append(box)
    return len(unlocked) == len(boxes)
