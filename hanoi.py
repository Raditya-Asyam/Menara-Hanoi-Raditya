import pygame
import time

# Inisialisasi Pygame
pygame.init()

# Dimensi layar
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Visualisasi Menara Hanoi")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Posisi tiang
PEGS = [(200, 300), (400, 300), (600, 300)]
DISK_HEIGHT = 20
disk_colors = [(255, 100 + i * 30, 100) for i in range(10)]  # Gradasi warna untuk cakram
font = pygame.font.Font(None, 36)

# Data menara
num_disks = 3
towers = {'A': list(range(num_disks, 0, -1)), 'B': [], 'C': []}
peg_map = {'A': 0, 'B': 1, 'C': 2}
moves = []

# Algoritma Menara Hanoi dengan pencatatan langkah
def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        moves.append((source, destination))
        return
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    moves.append((source, destination))
    tower_of_hanoi(n - 1, auxiliary, source, destination)

# Menyelesaikan dan mendapatkan langkah-langkah
tower_of_hanoi(num_disks, 'A', 'B', 'C')

# Fungsi untuk menggambar tiang dan cakram
def draw_towers(move_text=""):
    screen.fill(WHITE)

    # Menggambar tiang
    for x, y in PEGS:
        pygame.draw.rect(screen, BLACK, (x - 5, y - 150, 10, 150))

    # Menggambar cakram
    for peg, stack in towers.items():
        peg_x = PEGS[peg_map[peg]][0]
        for i, disk in enumerate(stack):
            width = 30 + disk * 20
            disk_rect = pygame.Rect(peg_x - width // 2, 300 - (i + 1) * DISK_HEIGHT, width, DISK_HEIGHT)
            pygame.draw.rect(screen, disk_colors[disk - 1], disk_rect)
    
    # Menampilkan teks pergerakan cakram
    text_surface = font.render(move_text, True, BLACK)
    screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, 20))

    pygame.display.flip()

# Animasi pergerakan cakram
def move_disk(source, destination):
    disk = towers[source].pop()
    towers[destination].append(disk)
    move_text = f"Pindahkan cakram {disk} dari {source} ke {destination}"
    print(move_text)  # Cetak teks pergerakan ke terminal
    draw_towers(move_text)
    time.sleep(0.5)

# Menjalankan visualisasi
running = True
draw_towers("Memulai Menara Hanoi")
time.sleep(1)  # Jeda sebelum memulai

for move in moves:
    if not running:
        break
    move_disk(move[0], move[1])

# Keluar dari Pygame setelah selesai
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()