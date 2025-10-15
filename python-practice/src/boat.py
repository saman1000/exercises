def can_travel_to(game_matrix, from_row, from_column, to_row, to_column):
    result = False
    max_row = len(game_matrix)
    max_column = len(game_matrix[0])
    if 0 <= from_row < max_row and 0 <= to_row < max_row and 0 <= from_column < max_column and 0 <= to_column < max_column:
        # check if from or to located on land

        if game_matrix[to_row][to_column] == False or game_matrix[from_row][from_column] == False:
            return False
        blocking_rows = set()
        blocking_columns = {}
        for row in range(from_row, to_row):
            for column in range(from_column, to_column):
                if column in blocking_columns[column] and game_matrix[row][column]:
                    pass
                else:
                    blocking_columns[column] = True
                if game_matrix[row][column]:
                    break
                elif column == to_column - 1:
                    # all row grids are land
                    blocking_rows.add(row)

    return result

if __name__ == "__main__":
    game_matrix = [
        [False, True,  True,  False, False, False],
        [True,  True,  True,  False, False, False],
        [True,  True,  True,  True,  True,  True],
        [False, True,  True,  False, True,  True],
        [False, True,  True,  True,  False, True],
        [False, False, False, False, False, False],
    ]

    print(can_travel_to(game_matrix, 3, 2, 2, 2)) # True, Valid move
    print(can_travel_to(game_matrix, 3, 2, 3, 4)) # False, Can't travel through land
    print(can_travel_to(game_matrix, 3, 2, 6, 2)) # False, Out of bounds