import pygame
from datetime import datetime


pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


curr_time = datetime.now()
curr_sec = curr_time.second
curr_min = curr_time.minute


clock_image = pygame.transform.scale(pygame.image.load('images/mickeyclock.jpeg'), (800, 600))
minute = pygame.image.load('images/11hand.png')
minute = pygame.transform.scale(minute, (200, 50))
minhand_rect = minute.get_rect()
minhand_rect.center = (400, 300)
second = pygame.image.load('images/2hand2.png')
second = pygame.transform.scale(second, (250, 75))
sechand_rect = second.get_rect()
sechand_rect.center = (400, 300)


running = True
while running:

    screen.blit(clock_image, (0, 0))

    rot_minhand = pygame.transform.rotate(minute, -1 * (6 * curr_min) - 95)
    rot_minhand_rect = rot_minhand.get_rect()
    rot_minhand_rect.center = minhand_rect.center
    screen.blit(rot_minhand, rot_minhand_rect)

    rot_sechand = pygame.transform.rotate(second, -1 * (6 * curr_sec) + 90)
    rot_sechand_rect = rot_sechand.get_rect()
    rot_sechand_rect.center = sechand_rect.center
    screen.blit(rot_sechand, rot_sechand_rect)

    curr_time = datetime.now()
    curr_sec = curr_time.second
    curr_min = curr_time.minute

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    clock.tick(60)
