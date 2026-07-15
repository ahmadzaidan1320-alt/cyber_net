import pygame
import math
import os

# Konfigurasi
WIDTH, HEIGHT = 640, 480
FPS = 30
DURATION = 5  # detik
TOTAL_FRAMES = FPS * DURATION

# Inisialisasi
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Warna
BLACK = (15, 17, 23)
CYAN = (21, 82, 203)
MAGENTA = (203, 21, 194)
GOLD = (240, 192, 64)
WHITE = (232, 234, 240)

def draw_neon_pulse(frame):
    screen.fill(BLACK)
    center = (WIDTH // 2, HEIGHT // 2)
    
    # Animated circles
    for i in range(15):
        t = (frame * 0.1 + i * 0.4) % 6
        radius = int(40 + t * 40)
        
        # Color interpolation
        r = int(CYAN[0] + (MAGENTA[0] - CYAN[0]) * (math.sin(frame * 0.05 + i) + 1) / 2)
        g = int(CYAN[1] + (MAGENTA[1] - CYAN[1]) * (math.sin(frame * 0.05 + i) + 1) / 2)
        b = int(CYAN[2] + (MAGENTA[2] - CYAN[2]) * (math.sin(frame * 0.05 + i) + 1) / 2)
        
        # Glow effect
        for j in range(4):
            alpha = max(0, 180 - j * 45)
            pygame.draw.circle(screen, (r, g, b), center, radius + j * 8, 3 - j)
    
    # Center logo
    font = pygame.font.SysFont("Consolas", 32, bold=True)
    text = font.render("CYBER_NET", True, GOLD)
    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - 16))
    
    # Particle sparkles
    import random
    for _ in range(20):
        x = center[0] + random.randint(-150, 150)
        y = center[1] + random.randint(-100, 100)
        size = random.randint(1, 3)
        color = random.choice([CYAN, GOLD, WHITE])
        pygame.draw.circle(screen, color, (x, y), size)

# Buat folder output
os.makedirs("frames", exist_ok=True)

print("🎬 Generating animation frames...")

for f in range(TOTAL_FRAMES):
    draw_neon_pulse(f)
    pygame.image.save(screen, f"frames/frame_{f:04d}.png")
    if f % 30 == 0:
        print(f"  ✓ Frame {f}/{TOTAL_FRAMES}")

pygame.quit()
print("\n📦 Converting to GIF...")

# Convert ke GIF
from PIL import Image

frames = []
for f in range(TOTAL_FRAMES):
    img = Image.open(f"frames/frame_{f:04d}.png")
    frames.append(img.convert('RGB'))

frames[0].save(
    'cyber_net_animation.gif',
    save_all=True,
    append_images=frames[1:],
    duration=33,
    loop=0
)

print("✅ Selesai! File: cyber_net_animation.gif")