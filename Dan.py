import pygame

from pygame.sprite import Sprite

class Dan(Sprite):
    def __init__(self, BanPhiThuyen):
        super().__init__()
        self.manhinh = BanPhiThuyen.manhinh
        self.anhdan = pygame.image.load('D:\BanPhiThuyen\PicAndMusic\genki2.png')
        self.rect = self.anhdan.get_rect()
        self.rect.midtop = BanPhiThuyen.phithuyen.rect.midtop

    def draw(self):
        self.manhinh.blit(self.anhdan, self.rect)

    def update(self):
        self.rect.y -= 5