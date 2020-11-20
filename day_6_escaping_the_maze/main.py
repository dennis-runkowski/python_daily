"""Escaping the maze."""

import pandas as pd

maze = [
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 0, 0, 1],
    [1, 0, 1, 1],
    [1, 0, 0, 100],
]


def main(maze):
    """Escape the maze game

    Get to the value 100. you can only move in 0s
    """
    df = pd.DataFrame(maze)
    df[0][0] = '*'
    move = 0
    print(f"Move {move}")
    print("")
    print(df)
    print("###############################")
    position = (0, 0)
    while True:
        move += 1
        moves = [1, -1]
        next_move = False
        for x in range(0, 2):
            test = (position[0] + moves[x], position[1])
            value = df[test[0]][test[1]]
            if value == 100:
                print("You have excaped the maze!")
                return
            elif value == 0:
                position = test
                df[test[0]][test[1]] = '*'
                next_move = True
                break
            else:
                for y in range(0, 2):
                    test = (position[0], position[1] + moves[x])
                    value = df[test[0]][test[1]]
                    if value == 100:
                        print("You have excaped the maze!")
                        return
                    elif value == 0:
                        position = test
                        df[test[0]][test[1]] = '*'
                        next_move = True
                        break
            if next_move:
                break
        if not next_move:
            print("Could not solve maze!")
            return
        print(f"Move {move}")
        print("")
        print(df)
        print("###############################")

if __name__ == "__main__":
    main(maze)
