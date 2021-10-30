import pygame

class NutBam:
    def __init__(self, BanPhiThuyen, linkBut, posx, posy):
        #Lấy thông tin màn hình từ banphithuyen
        self.manhinh = BanPhiThuyen.manhinh
        self.khung_man_hinh = self.manhinh.get_rect()
        #Khởi tạo thuộc tính cho nút bấm
        self.chieurong = 230
        self.chieucao = 90
        self.image = pygame.image.load(linkBut)
        self.rect = self.image.get_rect()
        #Tạo nút bấm và đặt nó nằm ở vị trí chính giữa
        self.rect = pygame.Rect(posx, posy, self.chieurong, self.chieucao)
        #self.rect.center = self.khung_man_hinh.center

    def ve(self):
        self.manhinh.blit(self.image, self.rect)