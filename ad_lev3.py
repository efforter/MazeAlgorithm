from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from queue import Queue,PriorityQueue
import sys,random
import numpy as np
import time

WIDTH, HEIGHT=799,799
COL_LEN, ROW_LEN = 0,0
COL_NUM, ROW_NUM = 0,0
maz = np.ones((ROW_NUM,COL_NUM))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1090, 860)
        MainWindow.center()
        font = QtGui.QFont()
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.label0 = QtWidgets.QLabel(self.centralwidget)
        self.label0.setGeometry(QtCore.QRect(800, 40, 301, 151))
        font.setPointSize(40)
        self.label0.setFont(font)

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(900, 210, 151, 50))
        font.setPointSize(20)
        self.label1.setFont(font)

        self.pushButton1_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1_1.setGeometry(QtCore.QRect(810, 270, 80, 80))
        font.setPointSize(13)
        self.pushButton1_1.setFont(font)
        
        self.pushButton1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1_2.setGeometry(QtCore.QRect(905, 270, 80, 80))
        font.setPointSize(13)
        self.pushButton1_2.setFont(font)
        
        self.pushButton1_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1_3.setGeometry(QtCore.QRect(1000, 270, 80, 80))
        font.setPointSize(13)
        self.pushButton1_3.setFont(font)
        
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(890, 410, 151, 50))
        font.setPointSize(20)
        self.label2.setFont(font)

        self.pushButton2_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2_1.setGeometry(QtCore.QRect(830, 470, 100, 80))
        font.setPointSize(13)
        self.pushButton2_1.setFont(font)

        self.pushButton2_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2_2.setGeometry(QtCore.QRect(970, 470, 100, 80))
        font.setPointSize(13)
        self.pushButton2_2.setFont(font)

        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(830, 610, 250, 50))
        font.setPointSize(20)
        self.label3.setFont(font)

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 805, 805))
        self.graphicsView.setStyleSheet("")
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.graphicsView.setBackgroundBrush(brush)

        MainWindow.setCentralWidget(self.centralwidget)
        self.rename(MainWindow)
        
    def rename(self, MainWindow):
        tran = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(tran("MainWindow", "My Maze"))
        self.label0.setText(tran("MainWindow", " 미로만들기"))
        self.label1.setText(tran("MainWindow", "난이도"))
        self.pushButton1_1.setText(tran("MainWindow", "초급"))
        self.pushButton1_2.setText(tran("MainWindow", "중급"))
        self.pushButton1_3.setText(tran("MainWindow", "고급"))
        self.label2.setText(tran("MainWindow", "정답 찾기"))
        self.pushButton2_1.setText(tran("MainWindow", "BFS"))
        self.pushButton2_2.setText(tran("MainWindow", "A*"))

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class Board(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Board, self).__init__()
        self.setupUi(self)
        self.graphicsView.scene=QtWidgets.QGraphicsScene(0,0,WIDTH,HEIGHT)
        maze=Maze()
        self.graphicsView.scene.addItem(maze)
        self.graphicsView.setScene(self.graphicsView.scene)
        self.connection()
        self.show()

    def connection(self):
        self.pushButton1_1.clicked.connect(self.beginner)
        self.pushButton1_2.clicked.connect(self.middle)
        self.pushButton1_3.clicked.connect(self.advanced)
        self.pushButton2_1.clicked.connect(self.start_bfs)
        self.pushButton2_2.clicked.connect(self.start_astar)

    def beginner(self):
        global COL_NUM,ROW_NUM,COL_LEN,ROW_LEN,maz,a
        a=[]
        record=[]
        COL_NUM = 10
        ROW_NUM = 10
        number = 1
        self.Parameter(number)
        maze = Maze()
        maze.setPos(0, 0)
        self.update(maze)

    def middle(self):
        global COL_NUM,ROW_NUM,COL_LEN,ROW_LEN,maz,a
        a=[]
        record=[]
        COL_NUM = 30
        ROW_NUM = 30
        number = 2
        self.Parameter(number)
        maze = Maze()
        maze.setPos(0, 0)
        self.update(maze)

    def advanced(self):
        global COL_NUM,ROW_NUM,COL_LEN,ROW_LEN,maz,a
        a=[]
        record=[]
        COL_NUM = 70
        ROW_NUM = 70
        number = 3
        self.Parameter(number)
        maze = Maze()
        maze.setPos(0, 0)
        self.update(maze)

    def start_bfs(self):
        global a, record
        a=[]
        record=[]
        start = time.time()
        bfs((1,0))
        maze = Maze()
        maze.setPos(0, 0)
        self.update(maze)
        end = time.time()
        count = end - start
        QMessageBox.information(self, "bfs 시간", f"{end - start:.5f} sec")

    def start_astar(self):
        global a, record
        a=[]
        record=[]
        start = time.time()
        Astar()
        maze = Maze()
        maze.setPos(0, 0)
        self.update(maze)
        end = time.time()
        count = end - start
        QMessageBox.information(self, "astar 시간", f"{end - start:.5f} sec")

    def generate(self):
        global maz
        maz = np.ones((ROW_NUM+2,COL_NUM+2))
        make = MAKE()
        make.dfs()

    def Parameter(self,number):
        global COL_GAP, ROW_GAP, WIDTH, COL_NUM, ROW_NUM, COL_LEN, ROW_LEN, end_x, end_y
        self.generate()
        ROW_NUM,COL_NUM = maz.shape
        COL_GAP = int(0.1 * WIDTH / (COL_NUM-1))
        ROW_GAP = int(0.1 * HEIGHT / (ROW_NUM-1))
        if (number==1):
            COL_LEN = int(0.92 * WIDTH / COL_NUM)
            ROW_LEN = int(0.92 * HEIGHT / ROW_NUM)
        else:
            COL_LEN = int(0.94 * WIDTH / COL_NUM)
            ROW_LEN = int(0.94 * HEIGHT / ROW_NUM)
        end_x,end_y = ROW_NUM - 2, COL_NUM - 1

    def update(self,maze):
        self.graphicsView.scene.addItem(maze)
        self.graphicsView.setScene(self.graphicsView.scene)
        self.show()

class DFS(object):
    def __init__(self, width, height):
        self.width = (width // 2) * 2 + 1
        self.height = (height // 2) * 2 + 1
        self.start = [1, 0]
        self.end = [self.height - 2, self.width - 1]
        self.matrix = None

    def generate_dfs(self):
        self.matrix = -np.ones((self.height, self.width))
        self.matrix[self.start[0], self.start[1]] = 0
        self.matrix[self.end[0], self.end[1]] = 0
        visit = [[0 for i in range(self.width)] for j in range(self.height)]

        def dfs(row, col):
            visit[row][col] = 1
            self.matrix[row][col] = 0
            directions = [[0, 2], [0, -2], [2, 0], [-2, 0]]
            random.shuffle(directions)
            for d in directions:
                row_next, col_next = row + d[0], col + d[1]
                if row_next > 0 and row_next < self.height - 1 and col_next > 0 and col_next < self.width - 1 and visit[row_next][col_next] == 0:
                    if row == row_next:
                        visit[row][min(col, col_next) + 1] = 1
                        self.matrix[row][min(col, col_next) + 1] = 0
                    else:
                        visit[min(row, row_next) + 1][col] = 1
                        self.matrix[min(row, row_next) + 1][col] = 0
                    dfs(row_next, col_next)

        dfs(self.end[0], self.end[1] - 1)

class MAKE():
    def dfs(self):
        global maz
        k = DFS(ROW_NUM,COL_NUM)
        k.generate_dfs()
        maz = k.matrix

def Keep(temp):
    global a, record
    a = tuple(temp)
    
def bfs(i):
    global q,end_x,end_y,record
    store={}
    visited=[(1,0)]
    q = Queue()
    q.put(i)
    while q:
        temp = q.get()
        if temp[0]==end_x and temp[1] == end_y:
            break
        for (bfs_x, bfs_y) in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            x = bfs_x + temp[0]
            y = bfs_y + temp[1]
            if (x > 0 and y > 0 and x < ROW_NUM and y < COL_NUM and maz[x][y] == 0 and (x,y) not in visited):
                q.put((x, y))
                visited.append((x, y))
                store[(x,y)] = (temp[0],temp[1])
                if (x==end_x and y==end_y):
                    break
    record.append((end_x,end_y))
    (x,y)=store[(end_x,end_y)]
    record.append((x, y))
    while (x,y)!=(1,0):
        (x,y)=store[x,y]
        record.append((x, y))
    Keep(record)

def Astar():
    start = (1, 0)
    final = (ROW_NUM - 2, COL_NUM - 1)
    front = PriorityQueue()
    front.put(start)
    cur = {}
    cur[start] = None
    sum_cost = {}
    sum_cost[start] = 0
    j=0
    while front:
        current = front.get()
        if current == final:
            break
        for (end_x, end_y) in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            x = current[0] + end_x
            y = current[1] + end_y
            if isOK((x, y)):
                cost = sum_cost[current] + calcuCost(current, (x, y))
                if (x, y) not in sum_cost or cost < sum_cost[(x, y)]:
                    sum_cost[(x, y)] = cost
                    priority = cost + heuristic(start, (x, y))
                    front.put((x, y), priority)
                    cur[(x, y)] = current
                    if (x, y) == final:
                        break
    temp = final
    while temp:
        record.append(temp)
        temp = cur[temp]
    Keep(record)

def isOK(a):
    return (a[0]>0 and a[1]>0 and a[0]<ROW_NUM and a[1]<COL_NUM and maz[a[0]][a[1]]==0)

def calcuCost(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def heuristic(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

class Maze(QGraphicsItem):
    def __init__(self):
        super(Maze, self).__init__()
    def boundingRect(self):
        return QRectF(0, 0, WIDTH, HEIGHT)
    def paint(self, painter, option, widget):
        global COL_GAP, ROW_GAP, WIDTH, COL_NUM, ROW_NUM, COL_LEN, ROW_LEN, maz, ROUTE
        for i in range(COL_NUM):
            for j in range(ROW_NUM):
                if(maz[i][j]!=0):
                   painter.setPen(Qt.white)
                   painter.setBrush(Qt.white)
                   painter.drawRect(i*(COL_LEN+COL_GAP), j*(ROW_LEN+ROW_GAP), COL_LEN, ROW_LEN)
                if((i,j) in a):
                   painter.setPen(Qt.black)
                   painter.setBrush(Qt.red)
                   painter.drawRect(i*(COL_LEN+COL_GAP), j*(ROW_LEN+ROW_GAP), COL_LEN, ROW_LEN)

def main():
    global board
    app = QApplication(sys.argv)
    board = Board()
    board.show()
    sys.exit(app.exec_())

main()