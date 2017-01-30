import pygame

TileSize = 24
FPS = 120

# Resolution
WinX = 640
WinY = 480

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)

# Images
Tile = pygame.image.load('floor.png')
Humie = pygame.image.load('humie.png')

# Windows
FpsClock = pygame.time.Clock()
DISP = pygame.display.set_mode((WinX,WinY),0,32)

# Game constants
HumieX = 4; HumieY = 4
