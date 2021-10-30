import pygame

class Diem:
    def __init__(self, BanPhiThuyen, nhan):
        #Lấy thông tin màn hình từ banphithuyen
        self.manhinh = BanPhiThuyen.manhinh
        self.khung_man_hinh = self.manhinh.get_rect()
        #Khởi tạo thuộc tính cho nút bấm
        self.chieurong = 250
        self.chieucao = 70
        self.mauchu = (249, 145, 51)
        #self.maunut = (102, 200, 232)
        self.fontchu = pygame.font.SysFont(None, 50)

        self.rect = pygame.Rect(0, 0, self.chieurong, self.chieucao)
        self.rect.topright = self.khung_man_hinh.topright

        self.chu = self.fontchu.render(nhan, True, self.mauchu,) #self.maunut)
        self.khung_chu = self.chu.get_rect()
        self.khung_chu.center = self.rect.center

    def ve(self):
        #self.manhinh.fill(self.maunut, self.rect)
        self.manhinh.blit(self.chu, self.khung_chu)