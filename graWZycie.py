import random
import curses

def initialize_grid(height, width):
    """Tworzy losową planszę do gry."""
    return [[random.choice([0, 1]) for _ in range(width)] for _ in range(height)]

def count_neighbors(grid, x, y):
    """Zlicza liczbę żywych sąsiadów dla komórki (x, y)."""
    height = len(grid)
    width = len(grid[0])
    count = 0

    # Przeszukujemy 8 sąsiednich komórek
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue  # Pomijamy samą komórkę

            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                count += grid[ny][nx]  # Dodajemy wartość sąsiada

    return count

def count(board ,x,y):
    count = 0
    width = len(board[0])
    height = len(board)
    neighbor = [(-1,-1), (-1,0),(-1,1),(0,-1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for i, j in neighbor:
        ii = ii + x
        jj = j + y
        if ii >= 0 and ii < height and jj >= 0 and jj < width:
            count = count + board[ii][jj]
    return count

def next_generation(board):
    newBoard = []
    for _ in range(height):
        newBoard.append([0] * width)
        #albo 
    newBoard = [[0] * width for _ in range(height)]
    return newBoard
def compute_next_generation(grid):
    """Oblicza następną generację komórek zgodnie z regułami Gry w Życie."""
    height = len(grid)
    width = len(grid[0])
    new_grid = [[0] * width for _ in range(height)]

    for y in range(height):
        for x in range(width):
            neighbors = count_neighbors(grid, x, y)
            if grid[y][x] == 1:
                new_grid[y][x] = 1 if neighbors in [2, 3] else 0  # Żywa komórka
            else:
                new_grid[y][x] = 1 if neighbors == 3 else 0  # Martwa komórka

    return new_grid

def draw_grid(stdscr, grid):
    """Wyświetla siatkę komórek na ekranie terminala."""
    stdscr.clear()
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            stdscr.addch(y, x, "#" if cell else " ")
    stdscr.refresh()

def game_loop(stdscr):
    """Główna pętla gry obsługująca wyświetlanie i aktualizację stanu planszy."""
    curses.curs_set(0)  # Ukrywa kursor
    stdscr.nodelay(False)  # Program czeka na wejście użytkownika

    # Pobranie rozmiaru terminala i dostosowanie planszy do jego wielkości
    height, width = stdscr.getmaxyx()
    height, width = height - 1, width - 1  # Uniknięcie problemów z krawędziami
    grid = initialize_grid(height, width)

    while True:
        draw_grid(stdscr, grid)
        key = stdscr.getch()

        if key == ord('q'):
            break  # Wyjście z programu po naciśnięciu 'q'

        grid = compute_next_generation(grid)  # Aktualizacja stanu gry

if __name__ == "__main__":
    curses.wrapper(game_loop)
