import sys
import pygame
import random
import time
import ItemDragonBall
import ItemNangCap
import DauThan
import NutBam
import QuaiVat
import Dan
import PhiThuyen
import Diem

class BanPhiThuyen:
    def __init__(self):
        pygame.init()
        self.manhinh = pygame.display.set_mode((1000, 899))

        pygame.display.set_caption(r"Game Dragon Ball Super")

        pygame.mixer.music.load('D:\BanPhiThuyen\PicAndMusic\musicnen.mp3')
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.05)
        self.phithuyen = PhiThuyen.PhiThuyen(self)

        self.dan = pygame.sprite.Group()
        self.quaivat = pygame.sprite.Group()
        self.dauthan = pygame.sprite.Group()
        for i in range(self.phithuyen.sophithuyen):
            dauthan = DauThan.DauThan(self)
            dauthan.rect.x = i*dauthan.rect.width
            self.dauthan.add(dauthan)

        self.itemnangcap = pygame.sprite.Group()
        itemnangcap = ItemNangCap.ItemNangCap(self)
        self.itemnangcap.add(itemnangcap)

        self.itemdragonball = pygame.sprite.Group()
        itemdragonball = ItemDragonBall.ItemDragonBall(self)
        self.itemdragonball.add(itemdragonball)

        linkPlay = 'D:\BanPhiThuyen\PicAndMusic\PlayBut.png'
        linkQuit = 'D:\BanPhiThuyen\PicAndMusic\QuitBut.png'
        #linkSetting = 'D:\BanPhiThuyen\PicAndMusic\SettingBut.png'
        self.nutplay = NutBam.NutBam(self, linkPlay, 430, 200)
        self.nutquit = NutBam.NutBam(self, linkQuit, 430, 350)
        #self.nutsetting = NutBam.NutBam(self, linkSetting, 430, 500)

        self.dangchoi = False
        #self.dangsetting = False
        self.scores = 0
        self.speedqv = 3
        self.diem = Diem.Diem(self, f'Scores: {self.scores}')

    def capnhatscore(self):
        self.diem = Diem.Diem(self, f'Scores: {self.scores}'.format())

    def taoquaivat(self):
        if self.scores < 200:
            soda = 4
            self.speedqv = 3
        elif self.scores >= 200 and self.scores < 400:
            soda = 5
            self.speedqv = 4
        elif self.scores >= 400 and self.scores < 700:
            soda = 6
            self.speedqv = 5
        elif self.scores >= 700 and self.scores < 1000:
            soda = 10
            self.speedqv = 7
        elif self.scores >= 1000 and self.scores < 1500:
            soda = 15
            self.speedqv = 9
        elif self.scores >= 1500:
            soda = 20
            self.speedqv = 13
        for i in range(soda):
            quaivat = QuaiVat.QuaiVat(self)
            quaivat.rect.x = random.randint(0, 1000)
            quaivat.rect.y = 0
            self.quaivat.add(quaivat)

    def capnhatdauthan(self, sodau):
        for i in range(sodau):
            dauthan = DauThan.DauThan(self)
            dauthan.rect.x = i*dauthan.rect.width
            self.dauthan.add(dauthan)

    def capnhatitemnangcap(self):
        rd = random.randint(0, 20)
        if rd == 1:
            itemnangcap = ItemNangCap.ItemNangCap(self)
            itemnangcap.rect.x = random.randint(0, 1000)
            itemnangcap.rect.y = 0
            self.itemnangcap.add(itemnangcap)

    def capnhatitemdragonball(self):
        rd = random.randint(0, 20)
        if rd == 1:
            itemdragonball = ItemDragonBall.ItemDragonBall(self)
            itemdragonball.rect.x = random.randint(0, 1000)
            itemdragonball.rect.y = 0
            self.itemdragonball.add(itemdragonball)

    def main(self):
        while True:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.phithuyen.mousegoku(mouse_x, mouse_y)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.phithuyen.quaphai = True
                    if event.key == pygame.K_LEFT:
                        self.phithuyen.quatrai = True
                    if event.key == pygame.K_UP:
                        self.phithuyen.lentren = True
                    if event.key == pygame.K_DOWN:
                        self.phithuyen.xuongduoi = True
                    elif event.key == pygame.K_SPACE:
                        if self.dangchoi:
                            for i in range(self.phithuyen.sotiadan):
                                if i % 2 == 0:
                                    chanle = -1
                                else:
                                    chanle = 1
                                tmp = Dan.Dan(self)
                                if i < 3:
                                    tmp.rect.x += ((i+1)//2)*(tmp.rect.width)*(chanle)
                                else:
                                    tmp.rect.x += ((i + 1) // 2) * (tmp.rect.width) * (chanle) * 2
                                self.dan.add(tmp)
                                shootWeapon = pygame.mixer.Sound("D:\BanPhiThuyen\PicAndMusic\musiclaze.mp3")
                                shootWeapon.set_volume(0.03)
                                shootWeapon.play()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.phithuyen.quaphai = False
                    if event.key == pygame.K_LEFT:
                        self.phithuyen.quatrai = False
                    if event.key == pygame.K_UP:
                        self.phithuyen.lentren = False
                    if event.key == pygame.K_DOWN:
                        self.phithuyen.xuongduoi = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if self.nutplay.rect.collidepoint(pos) and not self.dangchoi:
                        self.dangchoi = True
                        self.phithuyen.sophithuyen = 3
                        self.scores = 0
                        self.capnhatscore()
                        pygame.mixer.music.load("D:\BanPhiThuyen\PicAndMusic\musicnen1.mp3")
                        pygame.mixer.music.play(loops=-1)
                        pygame.mixer.music.set_volume(0.1)
                    if self.nutquit.rect.collidepoint(pos) and not self.dangchoi:
                        sys.exit()
                    #if self.nutsetting.rect.collidepoint(pos) and not self.dangchoi:
                        #self.dangsetting = True
            #for quaivat in self.quaivat.sprites():
            #    if quaivat.rect.right >= self.manhinh.get_rect().right:
            #        quaivat.quatrai = True
            #        quaivat.quaphai = False
            #    if quaivat.rect.left <= 0:
            #        quaivat.quatrai = False
            #        quaivat.quaphai = True

            #Xử lý các item chạm vào vách màn hình
            for itemnangcap in self.itemnangcap.sprites():
                if itemnangcap.rect.right >= self.manhinh.get_rect().right:
                    itemnangcap.quatrai = True
                    itemnangcap.quaphai = False
                if itemnangcap.rect.left <= 0:
                    itemnangcap.quatrai = False
                    itemnangcap.quaphai = True
            for itemdragonball in self.itemdragonball.sprites():
                if itemdragonball.rect.right >= self.manhinh.get_rect().right:
                    itemdragonball.quatrai = True
                    itemdragonball.quaphai = False
                if itemdragonball.rect.left <= 0:
                    itemdragonball.quatrai = False
                    itemdragonball.quaphai = True

            #Cập nhật di chuyển của các đối tượng
            if self.dangchoi:
                self.phithuyen.capnhat()
                self.dan.update()
                # sodem = 0
                # if self.phithuyen.sotiadan == 5:
                #     for i in self.dan.sprites():
                #         sodem += 1
                #         if sodem > 5:
                #             sodem = 1
                #         if sodem % 4 == 0:
                #             i.rect.x += 2
                #         if sodem % 5 == 0:
                #             i.rect.x += -2
                self.quaivat.update(self.speedqv)
                self.itemnangcap.update()
                self.itemdragonball.update()

            #Xử lý va chạm
            # Va chạm đạn và đá
            vacham = pygame.sprite.groupcollide(self.dan, self.quaivat, False, False)
            if vacham:
                for quaivat in self.quaivat.sprites():
                    quaivat.soda = quaivat.soda - 1
                    print(f'Số đá: {quaivat.soda}')
                    if quaivat.soda < 1:
                        pygame.sprite.groupcollide(self.dan, self.quaivat, True, True)
                        self.capnhatitemnangcap()
                        self.capnhatitemdragonball()
                        for quaivat in vacham.values():
                            self.scores += 10 * len(quaivat)
                        self.capnhatscore()
                        shootBreak = pygame.mixer.Sound("D:\BanPhiThuyen\PicAndMusic\musitat.mp3")
                        shootBreak.set_volume(0.1)
                        shootBreak.play()
                        break
                    else:
                        pygame.sprite.groupcollide(self.dan, self.quaivat, True, False)
            # if pygame.sprite.groupcollide(self.dan, self.quaivat, True, True):
            #     self.capnhatitemnangcap()
            #     self.capnhatitemdragonball()
            #     self.scores += 10
            #     self.capnhatscore()
            #     shootBreak = pygame.mixer.Sound("D:\BanPhiThuyen\PicAndMusic\musitat.mp3")
            #     shootBreak.set_volume(0.1)
            #     shootBreak.play()
            #Va chạm phi thuyền và đá
            if pygame.sprite.spritecollideany(self.phithuyen, self.quaivat):
                self.quaivat.empty()
                self.dan.empty()
                self.taoquaivat()
                self.phithuyen.rect.midbottom = self.phithuyen.khung_man_hinh.midbottom
                self.phithuyen.sophithuyen -= 1
                if self.phithuyen.sotiadan > 1:
                    self.phithuyen.sotiadan -= 1
                self.dauthan.empty()
                self.capnhatdauthan(self.phithuyen.sophithuyen)
                shootLoser = pygame.mixer.Sound("D:\BanPhiThuyen\PicAndMusic\musicloser.mp3")
                shootLoser.set_volume(0.2)
                shootLoser.play()
                time.sleep(2)
            #Va chạm phi thuyền và item máu
            if pygame.sprite.spritecollideany(self.phithuyen, self.itemnangcap):
                self.phithuyen.sophithuyen += 1
                self.dauthan.empty()
                self.capnhatdauthan(self.phithuyen.sophithuyen)
                self.itemnangcap.empty()
            #Va chạm phi thuyền và item đạn
            if pygame.sprite.spritecollideany(self.phithuyen, self.itemdragonball):
                if self.phithuyen.sotiadan < 5:
                    self.phithuyen.sotiadan += 1
                self.itemdragonball.empty()

            #Hết mạng sẽ out game
            if self.phithuyen.sophithuyen == 0:
                self.dangchoi = False

            #Xóa đạn và quái vật nếu ra khỏi màn hình
            for dan in self.dan:
                if dan.rect.bottom <= 0:
                    self.dan.remove(dan)
            for quaivat in self.quaivat:
                if quaivat.rect.top >= 899:
                    self.quaivat.remove(quaivat)

            #Tạo thêm quái vật nếu không còn quái vật
            if not self.quaivat:
                #self.dan.empty()
                self.taoquaivat()

            if self.dangchoi:
                hinhnen = pygame.image.load('D:\BanPhiThuyen\PicAndMusic\galaxy.jpg')
            else:
                hinhnen = pygame.image.load('D:\BanPhiThuyen\PicAndMusic\galaxy1.jpg')

            self.manhinh.blit(hinhnen, (0, 0))

            #Vẽ các đối tượng lên màn hình
            if self.dangchoi:
                self.phithuyen.ve()
                for dan in self.dan.sprites():
                    dan.draw()
                self.quaivat.draw(self.manhinh)
                self.dauthan.draw(self.manhinh)
                self.itemnangcap.draw(self.manhinh)
                self.itemdragonball.draw(self.manhinh)
                self.diem.ve()
            if not self.dangchoi: #not self.dangsetting:
                self.nutplay.ve()
                self.nutquit.ve()
                #self.nutsetting.ve()

            pygame.display.flip()