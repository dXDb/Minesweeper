# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\user\Desktop\project\test\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
import random

# UI 정의 클래스
class Ui_MainWindow(QWidget):
    def __init__(self, xy, bomb):
        # 슈퍼클래스의 요소들을 가져옴
        super().__init__()

        self.xy = xy
        self.bomb = bomb
        self.board = list()
        self.board_hide = list()
        self.x = -1
        self.y = -1
        self.start = -1
    
    def setupUi(self, MainWindow):
        # 메인 윈도우 설정
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(30 * xy, 30 * xy)

        # central widget 부분 (상태바, 메뉴바 이런 것이 아닌 주요 기능을 하는 곳임)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #판 생성
        self.make_button()

        # centralwidget 부분에 객체들을 다 생성하고 centralwidget 생성
        MainWindow.setCentralWidget(self.centralwidget)

        # 우선은 안 쓰니 패스
        #self.menubar = QMenuBar(MainWindow)
        #self.menubar.setGeometry(QRect(0, 0, 800, 21))
        #self.menubar.setObjectName("menubar")

        #MainWindow.setMenuBar(self.menubar)
        #self.statusbar = QStatusBar(MainWindow)
        #self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # 슬라이스 처럼 해주는 듯
        _translate = QCoreApplication.translate
        
        # 윈도우 생성
        MainWindow.setWindowTitle(_translate("MainWindow", "지뢰찾기"))

        # 윈도우에 표시
        for y in range(xy):
            for x in range(xy):
                self.board[y][x].setText(_translate("MainWindow", ' '))
                self.board[y][x].clicked.connect(self.check)
                
    # 처음 판 생성
    def make_button(self):
        self.board = [[0 for j in range(self.xy)] for i in range(self.xy)]
        for y in range(xy):
            for x in range(xy):
                self.board[y][x] = QPushButton(self.centralwidget)
                self.board[y][x].setGeometry(QRect(0 + x * 30, 0 + y * 30, 30, 30))
                self.board[y][x].setObjectName("%d" %(x + y * xy))
                
    def check(self):
        now_y = int(self.sender().objectName()) // self.xy
        now_x = int(self.sender().objectName()) % self.xy
        
        # 처음 누르면 판 셋팅
        if self.start == -1:
            self.start = 0
            self.board_hide = [[0 for x in range(self.xy)] for y in range(self.xy)]
            for num in range(self.bomb):
                placex = random.randint(0, self.xy - 1)
                placey = random.randint(0, self.xy - 1)
                while self.board_hide[placey][placex] != 0 or (now_y == placey and now_x == placex):
                    placex = random.randint(0, self.xy - 1)
                    placey = random.randint(0, self.xy - 1)
                self.board_hide[placey][placex] = -1
            print(self.board_hide)
            self.mine_check(now_y, now_x)
            
        # 두번째 부터 체킹
        if self. start == 0:
            self.mine_check(now_y, now_x)

    # 지뢰 확인 함수
    def mine_check(self, nowy, nowx):
        if self.board_hide[nowy][nowx] == -1:
            print("실패")
            return
            
        if self.board_hide[nowy][nowx] == 0:
            cnt = 0
            if nowy - 1 > -1 and nowx - 1 > -1:
                if self.board_hide[nowy - 1][nowx - 1] == -1:
                    cnt += 1
            if nowy - 1 > -1:
                if self.board_hide[nowy - 1][nowx] == -1:
                    cnt += 1
            if nowy - 1 > -1 and nowx + 1 < xy:
                if self.board_hide[nowy - 1][nowx + 1] == -1:
                    cnt += 1
            if nowx - 1 > -1:
                if self.board_hide[nowy][nowx - 1] == -1:
                    cnt += 1
            if nowx + 1 < xy:
                if self.board_hide[nowy][nowx + 1] == -1:
                    cnt += 1
            if nowy + 1 < xy and nowx - 1 > -1:
                if self.board_hide[nowy + 1][nowx - 1] == -1:
                    cnt += 1
            if nowy + 1 < xy:
                if self.board_hide[nowy + 1][nowx] == -1:
                    cnt += 1
            if nowy + 1 < xy and nowx + 1 < xy:
                if self.board_hide[nowy + 1][nowx + 1] == -1:
                    cnt += 1

        self.board[nowy][nowx].setText('%d' %cnt)
        self.board[nowy][nowx].setEnabled(False)
        if cnt == 0:
            self.board[nowy][nowx].setText('  ')
            if nowy - 1 > -1 and nowx - 1 > -1 and self.board[nowy - 1][nowx - 1].text() == ' ':
                self.mine_check(nowy - 1, nowx - 1)
            if nowy - 1 > -1 and self.board[nowy - 1][nowx].text() == ' ':
                self.mine_check(nowy - 1, nowx)
            if nowy - 1 > -1 and nowx + 1 < xy and self.board[nowy - 1][nowx + 1].text() == ' ':
                self.mine_check(nowy - 1, nowx + 1)
            if nowx - 1 > -1 and self.board[nowy][nowx - 1].text() == ' ':
                self.mine_check(nowy, nowx - 1)
            if nowx + 1 < xy and self.board[nowy][nowx + 1].text() == ' ':
                self.mine_check(nowy, nowx + 1)
            if nowy + 1 < xy and nowx - 1 > -1 and self.board[nowy + 1][nowx - 1].text() == ' ':
                self.mine_check(nowy + 1, nowx - 1)
            if nowy + 1 < xy and self.board[nowy + 1][nowx].text() == ' ':
                self.mine_check(nowy + 1, nowx)
            if nowy + 1 < xy and nowx + 1 < xy and self.board[nowy + 1][nowx + 1].text() == ' ':
                self.mine_check(nowy + 1, nowx + 1)
                
        for i in range(xy):
            for j in range(xy):
                if self.board_hide[i][j] != -1:
                    if self.board[i][j].text() == ' ':
                        return
                    
        print('완료')
                    




# 메인 함수
print('칸수 N x N, 지뢰갯수 : ', end='')
xy, bomb = map(int, input().split())
while xy * xy < bomb:
    print("지뢰의 수가 칸의 수보다 많습니다. 다시 입력하세요.")
    xy, bomb = map(int, input().split())

if __name__ == "__main__":    
            
    import sys
    # 윈도우 작업
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow(xy, bomb)
    ui.setupUi(MainWindow)

    # 윈도우 보여주기
    MainWindow.show()

    # 윈도우 종료 버튼  안 할 시 오류
    sys.exit(app.exec_())

