def is_valid(board, visited, row, col):
    nrows, ncols = len(board), len(board[0])
    return 0 <= row < nrows and 0 <= col < ncols and not visited[row][col]


def dfs(board, word, row, col, index, visited):
    # If all letters matched
    if index == len(word):
        return True

    # Check bounds and match
    if not is_valid(board, visited, row, col) or board[row][col] != word[index]:
        return False

    # Mark as visited
    visited[row][col] = True

    # Explore all 8 neighbors
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            if dfs(board, word, row + dr, col + dc, index + 1, visited):
                return True

    # Backtrack
    visited[row][col] = False
    return False


def find_word(board, word):
    nrows, ncols = len(board), len(board[0])
    for row in range(nrows):
        for col in range(ncols):
            visited = [[False for col in range(ncols)] for row in range(nrows)]
            if dfs(board, word, row, col, 0, visited):
                return True
    return False


if __name__ == "__main__":
    boggle_board = [
        ['S', 'T', 'R'],
        ['E', 'N', 'O'],
        ['L', 'P', 'K']
    ]

    test_words = ["STONE", "STOP", "TEN", "PEN", "NOPE", "RANK"]

    for word in test_words:
        result = find_word(boggle_board, word)
        print(f"Word '{word}' found on board? {result}")
