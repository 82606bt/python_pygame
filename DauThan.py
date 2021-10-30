import pygame

from pygame.sprite import Sprite

class DauThan(Sprite):
    def __init__(self, BanPhiThuyen):
        super().__init__()
        self.manhinh = BanPhiThuyen.manhinh
        self.khung_man_hinh = BanPhiThuyen.manhinh.get_rect()
        self.image = pygame.image.load('D:\BanPhiThuyen\PicAndMusic\dauthan.png')
        self.rect = self.image.get_rect()
        self.rect.bottomright = self.khung_man_hinh.bottomright