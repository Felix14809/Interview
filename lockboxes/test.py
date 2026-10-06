#!/usr/bin/python3


def canUnlockAll(boxes):
    print(f"boxes:{len(boxes)}")

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

    print(f"Unlocked: {len(unlocked)} keys {keys}")
    return len(unlocked) == len(boxes)

boxes = [[4], [], [1], [2], [3]]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
