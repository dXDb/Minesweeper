# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\user\Desktop\project\test\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *

import sys
import random



# 설정 UI 클래스
class Ui_SubWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("SubWindow")
        MainWindow.setFixedSize(170, 126)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("sub_centralwidget")

        self.Label1        = QLabel(self.centralwidget)
        self.Label2        = QLabel(self.centralwidget)
        self.Label3        = QLabel(self.centralwidget)
        self.Label1.setGeometry(QRect(10, 10, 75, 25))
        self.Label2.setGeometry(QRect(10, 37, 75, 25))
        self.Label3.setGeometry(QRect(10, 64, 75, 25))
        self.Label1.setObjectName("1")
        self.Label2.setObjectName("2")
        self.Label3.setObjectName("3")
        self.Label1.setText('가로 5~40')
        self.Label2.setText('세로 5~20')
        self.Label3.setText('지뢰갯수 20~')

        self.textEdit1     = QLineEdit(self.centralwidget)
        self.textEdit2     = QLineEdit(self.centralwidget)
        self.textEdit3     = QLineEdit(self.centralwidget)
        self.textEdit1.setGeometry(QRect(85, 10, 75, 25))
        self.textEdit2.setGeometry(QRect(85, 37, 75, 25))
        self.textEdit3.setGeometry(QRect(85, 64, 75, 25))
        self.textEdit1.setObjectName("textx")
        self.textEdit2.setObjectName("texty")
        self.textEdit3.setObjectName("bomb_cnt")

        self.pushbutton    = QPushButton(self.centralwidget)
        self.pushbutton.setGeometry(QRect(10, 91, 150, 25))
        self.pushbutton.setObjectName("setting")
        self.pushbutton.setText("확인")
        self.pushbutton.clicked.connect(self.go_Main)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        
        
    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("SubWindow", "설정"))
        
        
    def go_Main(self):
        global gx
        global gy
        global gbomb
        if int(self.textEdit1.text()) >= 5 and int(self.textEdit1.text()) <= 40 and int(self.textEdit2.text()) >= 5 and int(self.textEdit2.text()) <= 20 and int(self.textEdit3.text()) >= 20 and int(self.textEdit3.text()) < int(self.textEdit1.text()) * int(self.textEdit2.text()):
            gx      = int(self.textEdit1.text())
            gy      = int(self.textEdit2.text())
            gbomb   = int(self.textEdit3.text())
            start_main()
        else:
            message = QMessageBox.about(self, "오류", "범위를 다시 지정해주세요.")



# 지뢰찾기 UI 정의 클래스
class Ui_MainWindow(QWidget):
    def __init__(self, x, y, bomb):
        # 슈퍼클래스의 요소들을 가져옴
        super().__init__()

        self.xx         = x
        self.yy         = y
        self.bomb       = bomb
        self.board      = list()
        self.board_hide = list()
        self.x          = -1
        self.y          = -1
        self.start      = -1
        self.fail_value = False
        self.icon_board = list()


    def setupUi(self, MainWindow):
        # 메인 윈도우 설정
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(30 * self.xx, 30 * self.yy + 21 + 50)

        # central widget 부분 (상태바, 메뉴바 이런 것이 아닌 주요 기능을 하는 곳임)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background:black")
        
        #판 생성
        self.reset_board = QPushButton(self.centralwidget)
        self.reset_board.setGeometry(QRect((30 * self.xx) / 2 - 20, 5, 40, 40))
        self.reset_board.setObjectName("replace")
        self.reset_board.setIcon(QIcon("reset.png"))
        self.reset_board.setStyleSheet("background:black")
        self.Label4      = QLabel(self.centralwidget)
        self.Label4.setGeometry(QRect(0, 49, 30 * self.xx, 2))
        self.Label4.setStyleSheet("background:white")
        self.make_button()

        # win or lose 이미지
        self.winB   = QLabel(self.centralwidget)
        self.winB.setGeometry(QRect(0, 0, 0, 0))
        self.winB.setStyleSheet("background:black")
        self.winL   = QLabel(self.centralwidget)
        self.winL.setGeometry(QRect(0, 0, 0, 0))
        self.win    = QPushButton(self.centralwidget)
        self.win.setStyleSheet("background:black")
        self.win.setGeometry(QRect(0, 0, 0, 0))
        
        self.loseB  = QLabel(self.centralwidget)
        self.loseB.setGeometry(QRect(0, 0, 0, 0))
        self.loseB.setStyleSheet("background:black")
        self.loseL  = QLabel(self.centralwidget)
        self.loseL.setGeometry(QRect(0, 0, 0, 0))
        self.lose   = QPushButton(self.centralwidget)
        self.lose.setStyleSheet("background:black")
        self.lose.setGeometry(QRect(0, 0, 0, 0))

        # centralwidget 부분에 객체들을 다 생성하고 centralwidget 생성
        MainWindow.setCentralWidget(self.centralwidget)
        
        # 메뉴 생성
        self.menubar = QMenuBar(MainWindow)
        self.menu    = QMenu(MainWindow)
        self.reset   = QAction(MainWindow)
        self.reset.setObjectName("setting")
        self.reset.triggered.connect(reset_board)
        self.menu.setObjectName("menu")
        self.menu.addAction(self.reset)
        self.menubar.setGeometry(QRect(0, 0, 30 * self.xx, 21))
        self.menubar.setObjectName("menubar")
        self.menubar.addAction(self.menu.menuAction())
        MainWindow.setMenuBar(self.menubar)
        
        # 우선은 안 쓰니 패스
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
        self.menu.setTitle(_translate("MainWindow", "설정"))
        self.reset.setText(_translate("MainWindow", "Setting"))

        # 윈도우에 표시
        self.Label4.setText(_translate("MainWindow", ''))
        self.reset_board.setText(_translate("MainWindow", ''))
        self.reset_board.clicked.connect(lambda : setting_board(self.xx, self.yy, self.bomb))
        for y in range(self.yy):
            for x in range(self.xx):
                self.board[y][x].setText(_translate("MainWindow", ' '))
                self.board[y][x].clicked.connect(self.check)
                self.board[y][x].setContextMenuPolicy(Qt.CustomContextMenu)
                self.board[y][x].customContextMenuRequested.connect(self.mine_expect)
        
        # 버튼 동작
        self.win.clicked.connect(reset_board)
        self.lose.clicked.connect(reset_board)
                       
    # 처음 판 생성
    def make_button(self):
        self.board = [[0 for j in range(self.xx)] for i in range(self.yy)]
        self.icon_board = [[0 for j in range(self.xx)] for i in range(self.yy)]
        for y in range(self.yy):
            for x in range(self.xx):
                self.board[y][x] = QPushButton(self.centralwidget)
                self.board[y][x].setGeometry(QRect(0 + x * 30, 50 + y * 30, 30, 30))
                self.board[y][x].setObjectName("%d" %(x + (y * self.xx)))
                self.board[y][x].setStyleSheet("background:white")
                
        
    # 오른쪽 클릭        
    def mine_expect(self):
        if self.sender().text() == ' ' and self.icon_board[int(self.sender().objectName()) // self.xx][int(self.sender().objectName()) % self.xx] == 0:
            self.sender().setIcon(QIcon('reset.png'))
            self.icon_board[int(self.sender().objectName()) // self.xx][int(self.sender().objectName()) % self.xx] = 1            
            return

        if self.sender().text() == ' ' and self.icon_board[int(self.sender().objectName()) // self.xx][int(self.sender().objectName()) % self.xx] == 1:
            self.sender().setIcon(QIcon(''))
            self.icon_board[int(self.sender().objectName()) // self.xx][int(self.sender().objectName()) % self.xx] = 0            

            
    def check(self):
        now_y = int(self.sender().objectName()) // self.xx
        now_x = int(self.sender().objectName()) % self.xx
        
        # 처음 누르면 판 셋팅
        if self.start == -1:
            self.start      = 0
            self.board_hide = [[0 for x in range(self.xx)] for y in range(self.yy)]
            for num in range(self.bomb):
                placex = random.randint(0, self.xx - 1)
                placey = random.randint(0, self.yy - 1)
                while self.board_hide[placey][placex] != 0 or (now_y == placey and now_x == placex):
                    placex = random.randint(0, self.xx - 1)
                    placey = random.randint(0, self.yy - 1)
                self.board_hide[placey][placex] = -1
            print(self.board_hide)
            self.mine_check(now_y, now_x)
            
        # 두번째 부터 체킹
        if self. start == 0:
            self.mine_check(now_y, now_x)


    # 지뢰 확인 함수
    def mine_check(self, nowy, nowx):
        # 지뢰찾기 틀림
        if self.board_hide[nowy][nowx] == -1:
            self.board[nowy][nowx].setText('')
            self.board[nowy][nowx].setIcon(QIcon('-1.png'))
            self.mine_fail()
            return
            
        # 지뢰찾기
        if self.board_hide[nowy][nowx] == 0:
            cnt = 0
            if nowy - 1 > -1      and nowx - 1 > -1:
                if self.board_hide[nowy - 1][nowx - 1] == -1:
                    cnt += 1
            if nowy - 1 > -1:
                if self.board_hide[nowy - 1][nowx]     == -1:
                    cnt += 1
            if nowy - 1 > -1      and nowx + 1 < self.xx:
                if self.board_hide[nowy - 1][nowx + 1] == -1:
                    cnt += 1
            if nowx - 1 > -1:
                if self.board_hide[nowy][nowx - 1]     == -1:
                    cnt += 1
            if nowx + 1 < self.xx:
                if self.board_hide[nowy][nowx + 1]     == -1:
                    cnt += 1
            if nowy + 1 < self.yy and nowx - 1 > -1:
                if self.board_hide[nowy + 1][nowx - 1] == -1:
                    cnt += 1
            if nowy + 1 < self.yy:
                if self.board_hide[nowy + 1][nowx]     == -1:
                    cnt += 1
            if nowy + 1 < self.yy and nowx + 1 < self.xx:
                if self.board_hide[nowy + 1][nowx + 1] == -1:
                    cnt += 1

        # 숫자 설정
        self.board[nowy][nowx].setText('')
        self.board[nowy][nowx].setIcon(QIcon('%d.png' %cnt))
        self.board[nowy][nowx].setStyleSheet("background:black")
        
        # 주변에 지뢰가 없을 때
        if cnt == 0:
            self.board[nowy][nowx].setText('')
            self.board[nowy][nowx].setStyleSheet("background:black")
            if nowy - 1 > -1      and nowx - 1 > -1      and self.board[nowy - 1][nowx - 1].text() == ' ':
                self.mine_check(nowy - 1, nowx - 1)
            if nowy - 1 > -1      and                        self.board[nowy - 1][nowx].text()     == ' ':
                self.mine_check(nowy - 1, nowx)
            if nowy - 1 > -1      and nowx + 1 < self.xx and self.board[nowy - 1][nowx + 1].text() == ' ':
                self.mine_check(nowy - 1, nowx + 1)
            if nowx - 1 > -1      and                        self.board[nowy][nowx - 1].text()     == ' ':
                self.mine_check(nowy, nowx - 1)
            if nowx + 1 < self.xx and                        self.board[nowy][nowx + 1].text()     == ' ':
                self.mine_check(nowy, nowx + 1)
            if nowy + 1 < self.yy and nowx - 1 > -1      and self.board[nowy + 1][nowx - 1].text() == ' ':
                self.mine_check(nowy + 1, nowx - 1)
            if nowy + 1 < self.yy and                        self.board[nowy + 1][nowx].text()     == ' ':
                self.mine_check(nowy + 1, nowx)
            if nowy + 1 < self.yy and nowx + 1 < self.xx and self.board[nowy + 1][nowx + 1].text() == ' ':
                self.mine_check(nowy + 1, nowx + 1)

        #끝났는지 확인해주기        
        for i in range(self.yy):
            for j in range(self.xx):
                if self.board_hide[i][j] != -1:
                    if self.board[i][j].text() == ' ':
                        return
                    
        if not self.fail_value:
            self.mine_clear()
        
        
    def mine_clear(self):
        for i in range(self.yy):
            for j in range(self.xx):
                if self.board[i][j].text() == ' ':
                    self.board[i][j].setStyleSheet("background:black")
                    self.board[i][j].setText('')
                    self.board[i][j].setIcon(QIcon('-1.png'))
        self.winL.setPixmap(QPixmap('win.png'))
        self.winL.resize(30 * self.xx, 30 * self.yy + 21 + 50)
        self.winL.move((30 * self.xx)/2 - 75, 0)
        self.winB.resize(30 * self.xx, 30 * self.yy + 21 + 50)
        self.win.resize(30 * self.xx, 30 * self.yy + 21 + 50)
        opacity_effect = QGraphicsOpacityEffect(self.win)
        opacity_effect.setOpacity(0)
        self.win.setGraphicsEffect(opacity_effect)
        
        
    def mine_fail(self):
        self.fail_value = True
        for i in range(self.yy):
            for j in range(self.xx):
                if self.board[i][j].text() == ' ':
                    self.mine_check(i, j)
        self.loseL.setPixmap(QPixmap('lose.png'))
        self.loseL.resize(30 * self.xx, 30 * self.yy + 21 + 50)
        self.loseL.move((30 * self.xx)/2 - 75, 0)
        self.loseB.resize(30 * self.xx, 30 * self.yy + 21 + 50)
        self.lose.resize(30 * self.xx, 30 * self.yy + 21 + 50)
        opacity_effect = QGraphicsOpacityEffect(self.lose)
        opacity_effect.setOpacity(0)
        self.lose.setGraphicsEffect(opacity_effect)
        


def reset_board():
    goMainWindow.close()
    SubWindow.show()



def setting_board(x, y, bomb):
    goMainWindow.close()
    ui = Ui_MainWindow(x, y, bomb)
    ui.setupUi(goMainWindow)
    goMainWindow.show()    



def start_main():
    global gx
    global gy
    global gbomb
    global SubWindow
    global goMainWindow
    global ui
    print(gx, gy, gbomb)
    
    ui = Ui_MainWindow(gx, gy, gbomb)
    ui.setupUi(goMainWindow)
    SubWindow.close()
    goMainWindow.show()    



# 메인 함수
if __name__  == "__main__":    
            
    # 윈도우 작업
    app          = QApplication(sys.argv)
    SubWindow    = QMainWindow()
    sub_ui       = Ui_SubWindow()
    sub_ui.setupUi(SubWindow)

    goMainWindow = QMainWindow()
    ui           = 0

    # 윈도우 보여주기
    SubWindow.show()

    # 윈도우 종료 버튼  안 할 시 오류
    sys.exit(app.exec_())

