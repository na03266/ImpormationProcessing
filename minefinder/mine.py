import pygame
import sys
import random

# Pygame 초기화
pygame.init()

# 창 크기 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# 창 타이틀 설정
pygame.display.set_caption("지뢰찾기")

# 그리드 설정
ROWS, COLS = 10, 10 # 10행 10열
CELL_SIZE = 50 #50px

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 그리드 그리기
def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    draw_grid()

    pygame.display.update()


# 지뢰 개수 설정
    NUM_MINES = 10

# 지뢰 랜덤 배치
    def place_mines():
        mines = random.sample(range(ROWS * COLS), NUM_MINES)
        grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        for mine in mines:
            row, col = divmod(mine, COLS)
            grid[row][col] = 1

        return grid

    grid = place_mines()
    print(grid)  # 지뢰가 있는 위치는 1로 표시됩니다.
