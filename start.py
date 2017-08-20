#!/usr/bin/env python3

from random import shuffle
import pygame
from pygame.locals import *

def parse_card(line):
    words = line.split(',')
    return (words[0], words[1:])

def get_words(filename):
    with open(filename, 'r') as f:
        content = f.readlines()
    cards = [parse_card(line.strip()) for line in content]
    shuffle(cards)
    return cards

def render_card(card, font, bg):
    centerx = bg.get_rect().centerx
    word = font.render(card[0], 1, (10, 10, 10))
    wordpos = word.get_rect()
    wordpos.centerx = centerx
    wordpos.centery = 24
    bg.blit(word, wordpos)

    pygame.draw.line(bg, (10, 10, 10), (0, 64), (300, 64))

    centery = 92
    for taboo_word in card[1]:
        taboo_text = font.render(taboo_word, 1, (10, 10, 10))
        taboo_pos = taboo_text.get_rect()
        taboo_pos.centerx = centerx
        taboo_pos.centery = centery
        bg.blit(taboo_text, taboo_pos)
        centery += 40

def main():
    cards = get_words("words.txt")
    current_card = cards.pop(0)

    pygame.init()
    screen = pygame.display.set_mode((200, 300))
    pygame.display.set_caption("Taboo")

    bg = pygame.Surface(screen.get_size())
    bg = bg.convert()
    bg.fill((250, 250, 250))

    font = pygame.font.Font(None, 36)
    render_card(current_card, font, bg)

    screen.blit(bg, (0, 0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                return
        screen.blit(bg, (0, 0))
        pygame.display.flip()

if __name__ == '__main__':
    main()
