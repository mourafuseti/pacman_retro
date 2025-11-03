# --------------------------------------------------------------
#  PAC-MAN – Leonardo de Moura Fuseti – 2025
#  FANTASMAS ALEATÓRIOS + HIGHSCORE + VIDAS DIREITA + SOM
# --------------------------------------------------------------

import pygame
import random
import sys
import math
import os

# ---------------------- INICIALIZAÇÃO ----------------------
pygame.init()
pygame.mixer.init()

# ---------------------- CONFIGURAÇÕES ----------------------
CELL_SIZE = 20
GRID_WIDTH = 50
GRID_HEIGHT = 30

# Cores
BLACK   = (0, 0, 0)
BLUE    = (0, 0, 255)
YELLOW  = (255, 255, 0)
WHITE   = (255, 255, 255)
RED     = (255, 0, 0)
PINK    = (255, 192, 203)
CYAN    = (0, 255, 255)
ORANGE  = (255, 165, 0)

# Arquivo de highscore
HIGHSCORE_FILE = "highscore.txt"

# Banner
BANNER = [
    "╔═══════════════════════════════════════════════════════════════════════════════╗",
    "║                                  Jogo pacman                                  ║",
    "║                             Aplicação  Python                                 ║",
    "║                       Criado por Leonardo de Moura Fuseti                     ║",
    "║                      Copyright 2025 - All Rights Reserved                     ║",
    "╚═══════════════════════════════════════════════════════════════════════════════╝"
]

# Mapa com POWER PELLETS
LEVEL = [
"111111111111111111111111111111111111111111111111",
"100000000000000000000000000000000000000000000001",
"101111012110111101011111011011011111011110111101",
"100000000000000000000000000000000000000000000001",
"101111011112111101011111011211011211011110111101",
"100000000000000000000000000000000000000000000001",
"101111011110111101011111011011211111011110111101",
"100000000000000000000000000000000000000000000001",
"101111011110111101011111011011111111011110111101",
"100000000000000000000000000000000000000000000001",
"101111011110111101011111011111011111011110111101",
"100000000000000000000000000000000000000000000001",
"101111011110111101011211011011111111011110111101",
"100000000000000000000000000000000000000000000001",
"101111011110111101011111011011211111011110111101",
"100000000000000000000000000000000000000000000001",
"101111011110111101011111011011011111011110111101",
"100000000000000000000000000000000000000002000001",
"101111011110111101011111011111011111011110111101",
"100000000000000000000000000000000000000000000001",
"101110011110111101011111011011111111011110111101",
"100000000000000000000000000000000000000000000001",
"101111011110111101011111011111011111011110111101",
"100000000000000000000000000000000000000000000001",
"101111011112111101011111011011111111011110111101",
"100000000000000000000000000000000000000000000001",
"101111011110112101011111011011011111011110111101",
"100000000000000000000200000000000000000000000001",
"101111011110111101011111011011111111011110111101",
"100000000000000000000000000000000000000000000001",
"111111111111111111111111111111111111111111111111"
]

# Fontes
font = pygame.font.SysFont("consolas", 24)
big_font = pygame.font.SysFont("consolas", 48)
title_font = pygame.font.SysFont("consolas", 72, bold=True)
input_font = pygame.font.SysFont("consolas", 40)

# Sons
SOUND_PATH = "sounds"
def load_sound(name):
    path = os.path.join(SOUND_PATH, name)
    if not os.path.exists(path):
        print(f"[AVISO] Som não encontrado: {path}")
        return None
    return pygame.mixer.Sound(path)

SOUNDS = {
    "chomp": load_sound("chomp.wav"),
    "power": load_sound("power.wav"),
    "death": load_sound("death.wav"),
    "ghost_eat": load_sound("ghost_eat.wav"),
    "start": load_sound("start.wav")
}

# ---------------------- HIGHSCORE ----------------------
def load_highscore():
    if not os.path.exists(HIGHSCORE_FILE):
        return 0, "Ninguém"
    try:
        with open(HIGHSCORE_FILE, "r", encoding="utf-8") as f:
            score = int(f.readline().strip())
            name = f.readline().strip()
            return score, name
    except:
        return 0, "Ninguém"

def save_highscore(score, name):
    with open(HIGHSCORE_FILE, "w", encoding="utf-8") as f:
        f.write(f"{score}\n{name}")

# ---------------------- TELA DE ENTRADA ----------------------
def show_start_screen(highscore_score, highscore_name):
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("PAC-MAN – Tela Inicial")
    clock = pygame.time.Clock()

    if SOUNDS["start"]:
        SOUNDS["start"].play()

    while True:
        screen.fill(BLACK)
        sw, sh = screen.get_size()

        y = sh // 2 - 220
        for line in BANNER:
            txt = font.render(line, True, WHITE)
            screen.blit(txt, (sw//2 - txt.get_width()//2, y))
            y += 30

        title = title_font.render("PAC-MAN", True, YELLOW)
        screen.blit(title, (sw//2 - title.get_width()//2, y + 40))

        inst = big_font.render("Aperte ENTER para jogar", True, WHITE)
        screen.blit(inst, (sw//2 - inst.get_width()//2, y + 160))

        hs_text = big_font.render(f"RECORD: {highscore_score:,} - {highscore_name}", True, CYAN)
        screen.blit(hs_text, (sw//2 - hs_text.get_width()//2, y + 240))

        pygame.display.flip()
        clock.tick(60)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    return screen
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# ---------------------- TELA DE INPUT NOME ----------------------
def input_name(screen, score):
    input_box = pygame.Rect(0, 0, 300, 50)
    color = YELLOW
    text = ''
    active = True
    clock = pygame.time.Clock()

    sw, sh = screen.get_size()
    input_box.center = (sw // 2, sh // 2)

    while active:
        screen.fill(BLACK)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN and text.strip():
                    active = False
                elif e.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif len(text) < 12:
                    text += e.unicode

        txt_surface = input_font.render(text, True, color)
        width = max(300, txt_surface.get_width() + 20)
        input_box.w = width
        input_box.centerx = sw // 2

        prompt = big_font.render("PARABÉNS! Digite seu nome:", True, YELLOW)
        score_text = big_font.render(f"Pontuação: {score:,}", True, WHITE)
        screen.blit(prompt, (sw//2 - prompt.get_width()//2, sh//2 - 120))
        screen.blit(score_text, (sw//2 - score_text.get_width()//2, sh//2 - 60))
        pygame.draw.rect(screen, color, input_box, 3)
        screen.blit(txt_surface, (input_box.x + 15, input_box.y + 10))

        pygame.display.flip()
        clock.tick(60)

    return text.strip() or "Anônimo"

# ---------------------- POSIÇÃO ALEATÓRIA ----------------------
def get_random_position(grid, offset_x, offset_y):
    while True:
        gx = random.randint(1, GRID_WIDTH - 2)
        gy = random.randint(1, GRID_HEIGHT - 2)
        if grid[gy][gx] in '0 ':
            x = offset_x + gx * CELL_SIZE + CELL_SIZE // 2
            y = offset_y + gy * CELL_SIZE + CELL_SIZE // 2
            return x, y

# ---------------------- CLASSES ----------------------
class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dir = 0
        self.next_dir = 0
        self.speed = 2
        self.radius = CELL_SIZE // 2 - 2
        self.mouth = 0
        self.mouth_speed = 10
        self.alive = True
        self.lives = 3

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:   self.next_dir = 2
        if keys[pygame.K_RIGHT]:  self.next_dir = 0
        if keys[pygame.K_UP]:     self.next_dir = 1
        if keys[pygame.K_DOWN]:   self.next_dir = 3

    def move(self, grid, offset_x, offset_y):
        if not self.alive: return
        nx, ny = self.x, self.y
        dx = [self.speed, 0, -self.speed, 0][self.next_dir]
        dy = [0, -self.speed, 0, self.speed][self.next_dir]
        nx += dx
        ny += dy

        if not self._wall(nx, ny, grid, offset_x, offset_y):
            self.dir = self.next_dir
            self.x, self.y = nx, ny
        else:
            dx = [self.speed, 0, -self.speed, 0][self.dir]
            dy = [0, -self.speed, 0, self.speed][self.dir]
            nx = self.x + dx
            ny = self.y + dy
            if not self._wall(nx, ny, grid, offset_x, offset_y):
                self.x, self.y = nx, ny

        left_edge = offset_x
        right_edge = offset_x + GRID_WIDTH * CELL_SIZE
        if self.x < left_edge:
            self.x = right_edge - CELL_SIZE
        if self.x >= right_edge:
            self.x = left_edge

    def _wall(self, x, y, grid, offset_x, offset_y):
        gx = int((x - offset_x) // CELL_SIZE)
        gy = int((y - offset_y) // CELL_SIZE)
        if gx < 0 or gx >= GRID_WIDTH or gy < 0 or gy >= GRID_HEIGHT:
            return True
        return grid[gy][gx] == '1'

    def eat(self, grid, offset_x, offset_y, score):
        gx = int((self.x - offset_x) // CELL_SIZE)
        gy = int((self.y - offset_y) // CELL_SIZE)
        if 0 <= gy < GRID_HEIGHT and 0 <= gx < GRID_WIDTH:
            cell = grid[gy][gx]
            if cell == '2':
                if SOUNDS["power"]: SOUNDS["power"].play()
                score[0] += 50
                grid[gy][gx] = ' '
                return True, 50
            if cell == '0':
                if SOUNDS["chomp"]: SOUNDS["chomp"].play()
                score[0] += 10
                grid[gy][gx] = ' '
        return False, 0

    def draw(self, screen, offset_x, offset_y):
        if not self.alive: return
        cx = int(self.x)
        cy = int(self.y)
        pygame.draw.circle(screen, YELLOW, (cx, cy), self.radius)

        self.mouth = (self.mouth + self.mouth_speed) % 90
        start = {0: self.mouth, 1: 90 + self.mouth, 2: 180 + self.mouth, 3: 270 + self.mouth}[self.dir]
        end = start + 360 - 2 * self.mouth

        points = [(cx, cy)]
        for a in range(int(start), int(end), 5):
            rad = math.radians(a)
            px = cx + self.radius * math.cos(rad)
            py = cy + self.radius * math.sin(rad)
            points.append((px, py))
        points.append((cx, cy))
        if len(points) > 2:
            pygame.draw.polygon(screen, BLACK, points)

    def draw_lives(self, screen, offset_x, offset_y, sw):
        for i in range(self.lives):
            cx = sw - 80 - i * 40
            cy = offset_y - 40
            pygame.draw.circle(screen, YELLOW, (cx, cy), 15)
            pygame.draw.arc(screen, BLACK, (cx-10, cy-10, 20, 20), 0.3, 2.8, 3)

class Ghost:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.dir = random.randint(0, 3)
        self.speed = 1.5
        self.radius = CELL_SIZE // 2 - 2
        self.vulnerable = False

    def move(self, grid, pacman, offset_x, offset_y):
        dirs = [(1,0), (0,-1), (-1,0), (0,1)]  # CORRIGIDO
        valid = []
        for i, (dx, dy) in enumerate(dirs):
            nx = self.x + dx * self.speed
            ny = self.y + dy * self.speed
            if not self._wall(nx, ny, grid, offset_x, offset_y):
                valid.append((i, nx, ny))

        if valid:
            if random.random() < 0.7 and pacman.alive and not self.vulnerable:
                best = min(valid, key=lambda v: (v[1]-pacman.x)**2 + (v[2]-pacman.y)**2)
                self.dir, self.x, self.y = best
            else:
                self.dir, self.x, self.y = random.choice(valid)

    def _wall(self, x, y, grid, offset_x, offset_y):
        gx = int((x - offset_x) // CELL_SIZE)
        gy = int((y - offset_y) // CELL_SIZE)
        if gx < 0 or gx >= GRID_WIDTH or gy < 0 or gy >= GRID_HEIGHT:
            return True
        return grid[gy][gx] == '1'

    def draw(self, screen, offset_x, offset_y, power_mode, blink_timer):
        cx = int(self.x)
        cy = int(self.y)
        color = (0, 0, 255) if power_mode else self.color
        if power_mode and blink_timer % 20 >= 10:
            color = WHITE
        pygame.draw.circle(screen, color, (cx, cy), self.radius)
        eye = self.radius // 2
        pygame.draw.circle(screen, WHITE, (cx - eye//2, cy - eye//2), 5)
        pygame.draw.circle(screen, WHITE, (cx + eye//2, cy - eye//2), 5)
        pygame.draw.circle(screen, BLACK, (cx - eye//2 + 1, cy - eye//2), 2)
        pygame.draw.circle(screen, BLACK, (cx + eye//2 + 1, cy - eye//2), 2)

# ---------------------- FUNÇÕES DO JOGO ----------------------
def draw_grid(grid, screen, offset_x, offset_y, blink_timer):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            cx = offset_x + x * CELL_SIZE
            cy = offset_y + y * CELL_SIZE
            if cell == '1':
                pygame.draw.rect(screen, BLUE, (cx, cy, CELL_SIZE, CELL_SIZE))
            elif cell == '0':
                pygame.draw.circle(screen, WHITE, (cx + CELL_SIZE//2, cy + CELL_SIZE//2), 3)
            elif cell == '2':
                color = YELLOW if blink_timer % 30 < 15 else WHITE
                pygame.draw.circle(screen, color, (cx + CELL_SIZE//2, cy + CELL_SIZE//2), 7)

def collision(pacman, ghosts):
    for g in ghosts:
        if (pacman.x - g.x)**2 + (pacman.y - g.y)**2 < (CELL_SIZE*0.7)**2:
            return g
    return None

# ---------------------- LOOP PRINCIPAL ----------------------
def main():
    highscore_score, highscore_name = load_highscore()
    screen = show_start_screen(highscore_score, highscore_name)
    pygame.display.set_caption("PAC-MAN – Jogo")
    clock = pygame.time.Clock()

    sw, sh = screen.get_size()
    game_width = GRID_WIDTH * CELL_SIZE
    game_height = GRID_HEIGHT * CELL_SIZE
    offset_x = max(0, (sw - game_width) // 2)
    offset_y = max(0, (sh - game_height) // 2)

    grid = [list(row) for row in LEVEL]

    pac_x = offset_x + (GRID_WIDTH // 2) * CELL_SIZE + CELL_SIZE // 2
    pac_y = offset_y + (GRID_HEIGHT // 2) * CELL_SIZE + CELL_SIZE // 2
    pac = Pacman(pac_x, pac_y)

    ghost_colors = [RED, PINK, CYAN, ORANGE]
    ghosts = []
    for color in ghost_colors:
        gx, gy = get_random_position(grid, offset_x, offset_y)
        ghosts.append(Ghost(gx, gy, color))

    score = [0]
    power = False
    power_timer = 0
    blink_timer = 0
    running = True

    while running:
        screen.fill(BLACK)
        blink_timer += 1

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r and pac.lives <= 0:
                    return main()
                if e.key == pygame.K_ESCAPE:
                    running = False

        if pac.alive:
            pac.handle_input()
            pac.move(grid, offset_x, offset_y)
            ate, pts = pac.eat(grid, offset_x, offset_y, score)
            if ate:
                power = True
                power_timer = 600
                for g in ghosts:
                    g.vulnerable = True
            if power:
                power_timer -= 1
                if power_timer <= 0:
                    power = False
                    for g in ghosts:
                        g.vulnerable = False

            for g in ghosts:
                g.move(grid, pac, offset_x, offset_y)

            collided = collision(pac, ghosts)
            if collided:
                if power and collided.vulnerable:
                    if SOUNDS["ghost_eat"]: SOUNDS["ghost_eat"].play()
                    score[0] += 200
                    gx, gy = get_random_position(grid, offset_x, offset_y)
                    collided.x, collided.y = gx, gy
                else:
                    if SOUNDS["death"]: SOUNDS["death"].play()
                    pac.alive = False
                    pac.lives -= 1
                    pygame.time.wait(1500)
                    if pac.lives > 0:
                        pac.x, pac.y = pac_x, pac_y
                        pac.alive = True
                        for g in ghosts:
                            gx, gy = get_random_position(grid, offset_x, offset_y)
                            g.x, g.y = gx, gy

        draw_grid(grid, screen, offset_x, offset_y, blink_timer)
        pac.draw(screen, offset_x, offset_y)
        for g in ghosts:
            g.draw(screen, offset_x, offset_y, power, blink_timer)

        score_text = big_font.render(f"SCORE: {score[0]:,}", True, YELLOW)
        screen.blit(score_text, (offset_x + 20, offset_y - 70))
        pac.draw_lives(screen, offset_x, offset_y, sw)

        if not any('0' in row or '2' in row for row in grid):
            win = big_font.render("VOCÊ VENCEU!", True, YELLOW)
            screen.blit(win, (sw//2 - win.get_width()//2, sh//2))
            pygame.display.flip()
            pygame.time.wait(2000)
            player_name = input_name(screen, score[0])
            if score[0] > highscore_score:
                save_highscore(score[0], player_name)
            running = False

        if pac.lives <= 0:
            go = big_font.render("GAME OVER – Pressione R", True, RED)
            screen.blit(go, (sw//2 - go.get_width()//2, sh//2))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()