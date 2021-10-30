import pygame

from pygame.sprite import Sprite

class QuaiVat(Sprite):
    def __init__(self, BanPhiThuyen):
        super().__init__()
        self.manhinh = BanPhiThuyen.manhinh
        self.khung_man_hinh = BanPhiThuyen.manhinh.get_rect()
        self.image = pygame.image.load('D:\BanPhiThuyen\PicAndMusic\da.png')
        self.rect = self.image.get_rect()
        self.rect.midtop = self.khung_man_hinh.midtop

        #self.quatrai = True
        #self.quaphai = False
        self.soda = 5

    def update(self, speed):
        self.rect.y += speed