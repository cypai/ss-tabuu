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

def render_card(card, counter, font, bg):
    bg.fill((250, 250, 250))

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

    counter_text = font.render(str(counter), 1, (250, 10, 10))
    counter_pos = counter_text.get_rect()
    counter_pos.centerx = 16
    counter_pos.centery = 300 - 16
    bg.blit(counter_text, counter_pos)

def main():
    cards = get_words("words.txt")
    current_card = cards.pop(0)

    counter = 0

    pygame.init()
    screen = pygame.display.set_mode((200, 300))
    pygame.display.set_caption("Taboo")

    bg = pygame.Surface(screen.get_size())
    bg = bg.convert()

    font = pygame.font.Font(None, 36)
    render_card(current_card, counter, font, bg)

    screen.blit(bg, (0, 0))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == KEYDOWN and event.key == K_BACKSPACE:
                counter = 0
                render_card(current_card, counter, font, bg)
            elif event.type == KEYDOWN and event.key == K_RETURN:
                counter += 1
                if len(cards) > 0:
                    current_card = cards.pop(0)
                else:
                    current_card = ("Finished!", [])
                render_card(current_card, counter, font, bg)
        screen.blit(bg, (0, 0))
        pygame.display.flip()

if __name__ == '__main__':
    main()
