import pygame

from pygame.sprite import Sprite

class ItemDragonBall(Sprite):
    def __init__(self, BanPhiThuyen):
        super().__init__()
        self.manhinh = BanPhiThuyen.manhinh
        self.khung_man_hinh = BanPhiThuyen.manhinh.get_rect()
        self.image = pygame.image.load('D:\BanPhiThuyen\PicAndMusic\itemdragonball.png')
        self.rect = self.image.get_rect()
        self.rect.midtop = self.khung_man_hinh.midtop

        self.quatrai = True
        self.quaphai = False

    def update(self):
        if self.quatrai:
            self.rect.x -= 2
            self.rect.y += 4
        if self.quaphai:
            self.rect.x += 2
            self.rect.y -= 4