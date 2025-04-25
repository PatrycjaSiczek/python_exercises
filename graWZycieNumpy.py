import curses
import numpy as np

def initialize_grid(height, width):
    """
    Tworzy losową planszę do gry jako macierz NumPy.
    1 = żywa komórka, 0 = martwa.
    """
    return np.random.randint(2, size=(height, width), dtype=np.uint8)

def count_neighbors(grid):
    """
    Zlicza liczbę żywych sąsiadów każdej komórki w siatce za pomocą przesunięć macierzy.
    """
    neighbors = sum(np.roll(np.roll(grid, i, 0), j, 1)
                    for i in (-1, 0, 1)
                    for j in (-1, 0, 1)
                    if not (i == 0 and j == 0))
    return neighbors

def compute_next_generation(grid):
    """
    Zwraca nową generację komórek zgodnie z zasadami Conwaya.
    """
    neighbors = count_neighbors(grid)
    return np.where((grid == 1) & ((neighbors == 2) | (neighbors == 3)) |
                    (grid == 0) & (neighbors == 3), 1, 0).astype(np.uint8)

def draw_grid(stdscr, grid):
    """
    Rysuje planszę w terminalu. '#' dla żywej komórki, spacja dla martwej.
    """
    stdscr.clear()
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            stdscr.addch(y, x, "#" if grid[y, x] else " ")
    stdscr.refresh()

def game_loop(stdscr):
    """
    Główna pętla gry: rysowanie, wejście użytkownika, aktualizacja generacji.
    """
    curses.curs_set(0)
    stdscr.nodelay(False)
    stdscr.clear()
    
    height, width = stdscr.getmaxyx()
    height, width = height - 1, width - 1
    grid = initialize_grid(height, width)
    
    while True:
        draw_grid(stdscr, grid)
        key = stdscr.getch()
        if key == ord('q'):
            break
        grid = compute_next_generation(grid)

if __name__ == "__main__":
    curses.wrapper(game_loop)
