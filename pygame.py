############ INSTALLATION
$pip install wheels pygame-ce
############ MAIN MODULES
- display
- time
- image
- mixer
- event
############ INITIAL SETUP
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("WINDOW TITLE")

display = pygame.Surface((640, 350)) # empty img-surface all black, render here and scale to screen

clock = pygame.time.Clock()

#pygame.transform.flip(img, True, False)

############ load resources

img = pygame.image.load('img path.png') # img.get_width()
img_optimal = pygame.image.load(path).convert()
img_optimal.set_colorkey((0, 0, 0)) # select image transparent color
img_optimal.set_alpha(100)

############ COLLISION
collision_rect = pygame.Rect(50, 50, 100, 100) # COLLISION
if rect2.colliderect(collision_rect):
    pygame.draw.rect(self.screen, (r, g, b), collision_rect)

if rect2.collidepoint((X, Y)):
############ MUSIC
sfx = pygame.mixer.Sound('sfx.wav') # .set_volume(0.6)
pygame.mixer.music.load('music.wav')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

########### GAME LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:      # QUIT
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN: # KEY DOWN
            if event.key == pygame.K_UP:
                pass
        elif event.type == pygame.KEYUP:   # KEY UP
            if event.key == pygame.K_UP:
                pass
        elif event.type == pygame.MOUSEBUTTONDOWN: #MOUSE BUTTON DOWN
            if event.button == 1:
                pass

    mouse_pos = pygame.mouse.get_pos()

    if collision_rect.colliderect(another_rect):
        pygame.draw.rect(screen, (R, G, B), area)

    display.blit(img, (X, Y), (CROP_X, CROP_Y, CROP_W, CROP_H) # FOR img from SPRITESHEET
    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    pygame.display.update()
    clock.tick(FPS)

    screen.fill((r, g, b)) # CLEAR the screen with single color

########### IMAGE LOADER
for img_name in os.listdir(ROOT_PATH + path):
    images.append(load_image(path + '/' + img_name))


############ executable

PyInstaller

py -m PyInstaller main.py --noconsole #copy imgs and sounds by hand
