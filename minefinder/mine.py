import pygame
import sys

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
