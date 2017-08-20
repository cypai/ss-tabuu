#!/usr/bin/env python3

import pygame
from pygame.locals import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((200, 300))
    pygame.display.set_caption("Taboo")

    bg = pygame.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((250, 250, 250))

    font = pygame.font.Font(None, 36)
    text = font.render("Hi", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = bg.get_rect().centerx
    bg.blit(text, textpos)

    screen.blit(bg, (0, 0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(bg, (0, 0))
        pygame.display.flip()

if __name__ == '__main__':
    main()
