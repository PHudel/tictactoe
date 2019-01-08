def DrawGrid(x1,x2,y1,y2):
    line (x1, y1, x1, y2)
    line(x2, y1, x2, y2)
    line(y1, x1, y2, x1)
    line(y1, x2, y2, x2)
    fill(255)
    rect(665,310,100,50)
    fill(0)
    text(trans[keyy],675,345)
    text(keyx,720,345)
    fill(0)
    textSize(20)
    for i in range(3):
        text(trans[i],30,100+ i*200)
        text (i,100+i*200,30)
    text('Selected Box:',655,300)

def Drawxo(x,y):
    global turn,board,count
    if board[x][y] == 0:
        if turn == True:
            image(opic,(x*200)+1,(y*200)+1)
            turn = False
            board[x][y] = 1
        else:
            image(xpic,(x*200)+1,(y*200)+1)
            turn = True
            board[x][y] = 2
        count += 1
        check()
            
def check():
    global winner,count
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != 0:
            winner = board[0][i]
        if board[i][0] == board[i][1] == board[i][2] != 0:
            winner = board[i][0]
    if board[0][0] == board[1][1] == board[2][2] != 0:
            winner = board[0][0]
    if board[2][0] == board[1][1] == board[0][2] != 0:
            winner = board[0][2]
    if count >8 and winner ==0:
        winner=3           
    
def winscreen(x):
    textSize(25)
    if x != 3:
        text(("Player %d Wins!")% x,625,100)
    else:
        text(("Tie game!"),625,100)    
    text("Press r to play again",600,150)
    if keyPressed and key == 'r':
        setup()


def drawletters(a):
    global takekey,keylist,keyx,keyy
    if a != ENTER:
        if takekey < 2:
            keylist.append(key)
            takekey += 1
        if takekey == 2:
            Drawxo(dict[keylist[1]],dict[keylist[0]])
            takekey = 0
            keylist = []
    else:
        Drawxo(keyx,keyy)

def drawlettersspecial(a):
    global keyx,keyy
    if a == 38 and keyy > 0:
        keyy -= 1
    elif a == 40 and keyy < 2:
        keyy += 1
    elif a == 37 and keyx > 0:
        keyx -= 1
    elif a == 39 and keyx < 2:
        keyx += 1

def mouseReleased():
    global dodraw,xloc,yloc
    if mouseX <= 600:
        xloc = mouseX
        yloc = mouseY
        dodraw=True

def keyReleased():
    global takekey,keylist,keyx,keyy
    gkeys,space = 'abc012', ENTER
    if key != CODED:
        if key in gkeys or key in space:
            drawletters(key)
    else:
        drawlettersspecial(keyCode)

def setup():
    global xpic,opic,winner,board,turn,count,board,takekey,keylist,keyx,keyy,trans,dict,dodraw,xloc,yloc
    size(880,600)
    background(255)
    xpic = loadImage('x.png')
    opic= loadImage('o.png')
    dict = {'a':0,'b':1,'c':2,'0':0,'1':1,'2':2}
    trans = {0:'A',1:'B',2:'C'}
    board = [[0,0,0],[0,0,0],[0,0,0]]
    keylist = []
    takekey = 0
    keyx, keyy = 1,1
    turn = True
    dodraw=False
    xloc,yloc=0,0
    winner,count = 0,0
                 
def draw():
    global dodraw,xloc,yloc
    if dodraw:
        Drawxo(xloc/200,yloc/200)
        dodraw=False
    DrawGrid(200, 400, 0, 600)
    if winner != 0:
        winscreen(winner)