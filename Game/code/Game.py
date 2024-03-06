#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH,WIN_HEIGHT))

    def run(self, ):
        pygame.mixer_music.load('.asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            menu = Menu(self.window)
            self.menu_text(50,"Mountain",(255,128,0),((WIN_WIDTH/2),70)
           menu.run()
    def menu_text(self,text_size: int, text: str, text_color: tuple, text_center_pos:tuple):
        text_font: Font = pygame.font.SysFont("LUcida Sans Tywriter" , size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf,dest=text_rect)

