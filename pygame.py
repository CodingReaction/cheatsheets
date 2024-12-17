############ INSTALLATION
$pip install wheels pygame-ce
############ MAIN MODULES
- display
- time
- image
- mixer
- event
- math #contains Vector2 & Vector3, vector.magnitude(), vector.normalize()
- draw #line, circle, rect
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
img_optimal = pygame.image.load(path).convert() ## .convert_alpha()
img_optimal.set_colorkey((0, 0, 0)) # select image transparent color
img_optimal.set_alpha(100)

############ COLLISION
pygame.FRect(pos, size) # rect with floats
surface.get_rect(center=(0, 0)) #origin, topleft, topright, left, midleft, right, center
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
    #other way to get input
    keys = pygame.key.get_pressed()

    mouse_pos = pygame.mouse.get_pos()

    if collision_rect.colliderect(another_rect):
        pygame.draw.rect(screen, (R, G, B), area)

    display.blit(img, (X, Y), (CROP_X, CROP_Y, CROP_W, CROP_H) # FOR img from SPRITESHEET
    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    dt = clock.tick(FPS) / 1000
    clock.get_fps()

    screen.fill((r, g, b)) # CLEAR the screen with single color
    pygame.display.update()

########### IMAGE LOADER
for img_name in os.listdir(ROOT_PATH + path):
    images.append(load_image(path + '/' + img_name))

########### TEXT
my_font = pygame.font.Font(None, size)
text_surface = font.render('text', True, 'red')
display_surface.blit(text_surface, (X, Y))

############ executable

PyInstaller

py -m PyInstaller main.py --noconsole #copy imgs and sounds by hand

############ SPRITE GROUP
group1 = pygame.sprite.Group()
group1.add(player)  # add sprite to group
group.draw(display_surface) -> draw all sprites on surface
group.update(args) -> call update with arg on every sprite

############ TIMER EVENTS
custom_event = pygame.event.custom_type()
pygame.time.set_timer(custom_event, DURATION_MS)
# in the event loop
if event.type == custom_event:
    #do something

current_time = pygame.time.get_ticks()
