import pygame

class PhiThuyen:
    def __init__(self, BanPhiThuyen):
        self.manhinh = BanPhiThuyen.manhinh
        self.khung_man_hinh = BanPhiThuyen.manhinh.get_rect()
        self.anh_phi_thuyen = pygame.image.load('D:\BanPhiThuyen\PicAndMusic\goku.png')
        self.rect = self.anh_phi_thuyen.get_rect()
        self.rect.midbottom = self.khung_man_hinh.midbottom
        self.sophithuyen = 3
        self.sotiadan = 1

        self.quaphai = False
        self.quatrai = False
        self.lentren = False
        self.xuongduoi = False

    def ve(self):
        self.manhinh.blit(self.anh_phi_thuyen, self.rect)

    def capnhat(self):
        if self.quaphai == True and self.rect.right < self.khung_man_hinh.right:
            self.rect.x += 5

        if self.quatrai == True and self.rect.left > 0:
            self.rect.x -= 5

        if self.lentren == True and self.rect.top > 0:
            self.rect.y -= 5

        if self.xuongduoi == True and self.rect.bottom < self.khung_man_hinh.bottom:
            self.rect.y += 5

    def mousegoku(self, posx, posy):
        self.rect.x = posx
        self.rect.y = posy