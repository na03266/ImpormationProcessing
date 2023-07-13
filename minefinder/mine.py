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
ROWS, COLS = 10, 10  # 10행 10열
CELL_SIZE = 50  # 50px

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
RED = (255, 0, 0)

# 그리드 그리기
def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            cell_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, cell_rect, 1)

# 지뢰 개수 설정
NUM_MINES = 10

# 지뢰 랜덤 배치
def place_mines():
    mines = random.sample(range(ROWS * COLS), NUM_MINES)
    grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

    for mine in mines:
        row, col = divmod(mine, COLS)
        grid[row][col] = 9  # 9는 지뢰를 의미

    return grid

grid = place_mines()

# 게임 상태 변수
revealed = [[False for _ in range(COLS)] for _ in range(ROWS)]
flagged = [[False for _ in range(COLS)] for _ in range(ROWS)]

# 주변에 있는 지뢰의 개수를 계산하는 함수
def count_surrounding_mines(row, col):
    if grid[row][col] == 9:
        return 9  # 현재 셀이 지뢰인 경우

    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr != 0 or dc != 0:
                r, c = row + dr, col + dc
                if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 9:
                    count += 1

    return count

# 그리드 내부의 셀 열기 (재귀적으로 주변 셀을 열도록 구현)
def reveal_cells(row, col):
    if row < 0 or row >= ROWS or col < 0 or col >= COLS or revealed[row][col] or flagged[row][col]:
        return

    revealed[row][col] = True

    if grid[row][col] == 0:  # 주변 셀 열기
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr != 0 or dc != 0:
                    reveal_cells(row + dr, col + dc)

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 마우스 왼쪽 버튼 클릭
                x, y = event.pos
                col, row = x // CELL_SIZE, y // CELL_SIZE

                if flagged[row][col]:
                    continue

                if grid[row][col] == 9:  # 클릭한 셀이 지뢰인 경우
                    # 모든 지뢰를 표시하고 게임 종료
                    for r in range(ROWS):
                        for c in range(COLS):
                            if grid[r][c] == 9:
                                revealed[r][c] = True
                else:
                    reveal_cells(row, col)  # 클릭한 셀 주변의 빈 셀을 열기

            elif event.button == 3:  # 마우스 오른쪽 버튼 클릭
                x, y = event.pos
                col, row = x // CELL_SIZE, y // CELL_SIZE

                if revealed[row][col]:
                    continue

                flagged[row][col] = not flagged[row][col]

    screen.fill(BLACK)
    draw_grid()

    # 그리드 내부의 셀 표시
    for row in range(ROWS):
        for col in range(COLS):
            cell_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if revealed[row][col]:
                if grid[row][col] == 9:  # 지뢰인 경우 빨간색으로 표시
                    pygame.draw.rect(screen, RED, cell_rect)
                else:  # 빈 셀인 경우 회색으로 표시
                    pygame.draw.rect(screen, GRAY, cell_rect)
                    if grid[row][col] > 0:  # 주변 지뢰 개수를 표시
                        font = pygame.font.SysFont(None, 30)
                        num_mines = count_surrounding_mines(row, col)
                        text_surface = font.render(str(num_mines), True, WHITE)
                        text_rect = text_surface.get_rect(center=cell_rect.center)
                        screen.blit(text_surface, text_rect)
            elif flagged[row][col]:
                pygame.draw.rect(screen, WHITE, cell_rect)
                font = pygame.font.SysFont(None, 30)
                flag_text = "F"
                text_surface = font.render(flag_text, True, BLACK)
                text_rect = text_surface.get_rect(center=cell_rect.center)
                screen.blit(text_surface, text_rect)
            else:
                pygame.draw.rect(screen, WHITE, cell_rect, 1)  # 미열린 셀은 흰색 테두리로 표시

    pygame.display.update()
