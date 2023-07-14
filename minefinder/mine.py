import pygame
import sys
import random

# Pygame 초기화
pygame.init()

# 창 크기 설정
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 50

ROWS, COLS = 10, 10  # 10행 10열

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
RED = (255, 0, 0)

# 게임 보드 초기화
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
mines = set(random.sample(range(ROWS * COLS), 10))

for mine in mines:
    row, col = divmod(mine, COLS)
    board[row][col] = "M"

# 주변에 있는 지뢰 개수를 계산하여 셀에 표시하는 함수
def calculate_mine_counts():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] != "M":
                count = sum(1 for i in range(-1, 2) for j in range(-1, 2)
                            if 0 <= row + i < ROWS and 0 <= col + j < COLS and board[row + i][col + j] == "M")
                board[row][col] = count

# 셀을 열어서 지뢰를 확인하는 함수
def open_cell(row, col):
    if 0 <= row < ROWS and 0 <= col < COLS and board[row][col] != "M" and board[row][col] != -1:
        board[row][col] = -1  # -1은 셀이 열렸음을 표시

        if board[row][col] == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    open_cell(row + i, col + j)

        return True

    return False

# 게임 보드를 그리는 함수
def draw_board(screen):
    for row in range(ROWS):
        for col in range(COLS):
            x, y = col * CELL_SIZE, row * CELL_SIZE
            cell = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

            if board[row][col] == 0:
                pygame.draw.rect(screen, GRAY, cell)
            else:
                pygame.draw.rect(screen, WHITE, cell)

                if board[row][col] == "M":
                    pygame.draw.circle(screen, RED, (x + CELL_SIZE // 2, y + CELL_SIZE // 2), CELL_SIZE // 4)
                else:
                    font = pygame.font.Font(None, 30)
                    text = font.render(str(board[row][col]), True, BLACK)
                    text_rect = text.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                    screen.blit(text, text_rect)

            pygame.draw.rect(screen, BLACK, cell, 1)

# 게임 루프
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("지뢰찾기")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # 마우스 왼쪽 버튼 클릭
                    x, y = event.pos
                    col, row = x // CELL_SIZE, y // CELL_SIZE
                    if board[row][col] == "M":
                        print("Game Over!")
                        pygame.quit()
                        sys.exit()
                    else:
                        if open_cell(row, col):
                            calculate_mine_counts()

        screen.fill(BLACK)
        draw_board(screen)

        pygame.display.update()

if __name__ == "__main__":
    main()
