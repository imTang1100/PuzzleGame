'''
    cs5001
    Yifan Tang
    Final Project
    Class file
'''

from pathlib import Path
import turtle
import time
import random
import math

scc = turtle.Screen()
bg = 'Resources/background2.gif'
scc.bgpic(bg)
sc = turtle.Screen()
ttt = turtle.Turtle()
tttt = turtle.Turtle()
tttt.hideturtle()

class start_game: # use this class to store some datas temporily
    lo_name = None
    player = None
    goal = None
    def __init__(self):
        self.x = 'meow' # default puzzle
        self.y = 'Mr.unknown'
        self.z = 200
          
    def get_ins():
        if start_game.lo_name == None:
            start_game.lo_name = start_game()  
        return start_game.lo_name

    def get_p():
        if start_game.player == None:
            start_game.player = start_game()
        return start_game.player

    def get_z():
        if start_game.goal == None:
            start_game.goal = start_game()
        return start_game.goal 

def save_name(x = 'meow'): # when there is no valid puz typed
    ins = start_game.get_ins()
    ins.x = x
  
def get_name():
    ins = start_game.get_ins()
    return ins.x

def save_player(y = 'Mr.unknown'): # when there is no valid name typed
    pl = start_game.get_p()
    pl.y = y 

def get_player():
    pl = start_game.get_p()
    return pl.y

def save_goal(z = 200): 
    go = start_game.get_z()
    go.z = z

def get_goal():
    go = start_game.get_z()
    return go.z
    
def run_game():
    puz = get_name()
    x = game_time(puz)
    y = x.play_mode()
    z = x.get_list_seq()
    tt = x.tthum
    
    x.set_thumb(tt, sc, x)
    x.game_random(ttt, sc, z)
    set_leader()
    return x
 
def draw_board():
    scc.setup(800, 800)
    tttt.hideturtle()
    show_splash() 
    show_input(scc)
    draw_game_board(tttt)
    set_buttons(scc) 

def set_leader():
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.setpos(170, -200) 
    a = []
    with open ('player.txt', 'r') as file:
        for lines in file:
            a.append(lines)

    for i in range(len(a)):
        a[i] = a[i][:-1]
        a[i] = a[i].split(', ')
        a[i] = [int(a[i][0]), a[i][1]]

    a.sort()
    a = a[:10]
    b = str('Leader: \n \n')
    for i in a:
        i[0] = str(i[0])
        ' '.join(i)
        b = b + i[0] + ': ' + i[1] + '\n'
    
    t.color('white')
    t.write(f'{b}', font=('roboto', 24, 'normal'))
    
def set_main():
    aaa = run_game() 
    def start_click(x, y):
        inty = False
        try:
            cc = aaa.click_xy(x, y)
            result = aaa.dicide_win()    
            decide_recursive(cc)
        
        except SystemExit:
            g_f = get_goal()
            if int(g_f) > aaa.step: # if win
                good = 'Resources/winner.gif'
                turtle_present_gif(good, 2)
                s_n = aaa.step
                nn = get_player()
                with open ('player.txt','a') as file:
                    file.write(f'{s_n}, {nn}\n') 
            sc.bye()
        except ValueError:   
            aaa.reset()
            aaa.step = 0 
            aaa.step_write()
            sc.onclick(start_click)
    
        except RuntimeError: 
            g_n = aaa.loadgame 
            save_name(g_n)
            ttt.clear()   
            aaa.tstep.clear()
            aaa.tthum.hideturtle()
            # aaa.set_thumb(tt, sc, x, 0) # clear the old thumb
            for i in aaa.dic:
                aaa.dic[i][4].hideturtle()
            set_main()
      
    def decide_recursive(x):
        if x is False:
            sc.onclick(start_click)
         
    sc.onclick(start_click)

def turtle_present_gif(x, y): # x is relative address, y is presening time
    t_l = turtle.Turtle()
    sc.addshape(x)
    t_l.shape(x)
    time.sleep(y)
    t_l.hideturtle()
    
def show_splash(): # the beginning of the game
    '''
        Function: show_splash_input_name,
        takes one parameter, the instance of turtle.Screen
        load a gif pic for 3 seconds then clear it
        pop up a window for user to input name
    '''
    zz = 'Resources/splash_screen.gif'
    tot = turtle.Turtle()
    scc.addshape(zz)    
    tot.shape(zz)
    time.sleep(3)
    tot.hideturtle()

def show_input(scc):
    time.sleep(3.1) 
    def input_name():
        b = scc.textinput("CS5001 Puzzle Slide", "Your Name")
        if len(b.strip()) == 0:
            print('Try a true name')
            save_player()
        else:
            save_player(b)
        set_leader()

    def input_moves():
        t1 = '5001 Puzzle Slide - Moves'
        s1 = 'Enter the number of moves (chances) you want (5-200)'
        a = scc.numinput(t1, s1, default=None, minval=5, maxval=200)
        #a = scc.textinput(t1, s1)
        save_goal(a)

    def run_input():
        a = [input_name(), input_moves()]
        i = 0 
        for i in range(2):
            a[i]  
            i += 1
    
    run_input()

def draw_game_board(t): # set the whole game board
    '''
        Function: draw_game_board,
        takes one parameter, the instance of turtle.Turtle
        draw the game board (play area, status area and leader board)
    '''
    x, y, z, c = [-350, 320], [485, 520], 10, "white" 
    draw_square(t, x, y, z, c) # play area
    x, y, z, c = [150, 320], [200, 520], 5, "white"
    draw_square(t, x, y, z, c) # leader board
    x, y, z, c = [-350, -215], [700, 100], 3, "white"
    draw_square(t, x, y, z, c) # status area

def draw_square(t, x, y, z, c):
    '''
        Nested function: draw_square,
        takes four parameter, t is the instance,
        x is the sequence of setposition: [a, b],
        y is the list of he square's size: [c, d] = c * d,
        z is the line's width, c is the pen color
    '''
    t.speed(200)
    t.penup()
    t.setpos(x[0], x[1])
    t.down()
    t.pensize(z)
    t.pencolor(c)
    # set the start position, color and width of the pen
    
    t.forward(y[0])
    t.right(90)
    t.forward(y[1])
    t.right(90)
    t.forward(y[0])
    t.right(90)
    t.forward(y[1])
    t.right(90)

def new_turtle_shape(t, sc, x, y, z, p=1):
    '''
        Function: new_turtle_shape
        takes four parameters, sc is the instance of turtle.Screen
        x, y is the coordinates
        z is relative pos of gif
    '''
    if p == 1:
        t.hideturtle()
        t.penup()
        t.setpos(x, y)
        t.pendown()
        sc.addshape(z)
        t.shape(z) 
        t.showturtle()
    else:
        t.clear()

def set_buttons(sc):
    ''' 
        Function: set_buttons
        takes one parameters, sc is the instance of turtle.Screen
    '''
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t3 = turtle.Turtle()
    quit_b = 'Resources/quit.gif'
    load_b = 'Resources/loadbutton.gif'
    reset_b = 'Resources/resetbutton.gif'
    new_turtle_shape(t1, sc, 100, -265, reset_b)
    new_turtle_shape(t2, sc, 200, -265, load_b)
    new_turtle_shape(t3, sc, 300, -265, quit_b)
     
class game_time:
    def __init__(self, game_name):
        self.name = str(game_name) + '.puz'
        self.oriname = game_name
        self.tthum = turtle.Turtle() # turtle to set thumb
        self.tstep = turtle.Turtle() # turtle to record steps
        self.step = 0
        self.step_write() 
        script_loc = Path(__file__).absolute().parent # generate the relative path 
        file_loc = script_loc / self.name
             
        with open(file_loc, 'r') as puz:
            li = []  
            for lines in puz:
                lines = lines.replace('\n', '')
                li.append(lines)     
        self.li = li
        self.loc = script_loc
        self.step = 0 # record the steps
        self.puzname = game_name  
          
    def get_name(self):
        return self.name

    def get_number(self):
        a = self.li[1]
        a = a.replace('number: ', '')
        self.number = a
        return int(self.number)
   
    def get_size(self):
        b = self.li[2]
        b = b.replace('size: ', '')
        self.size = b
        return self.size
 
    def get_thu(self):
        c = self.li[3]
        c = c.replace('thumbnail: ','')
        self.thu = str(self.loc / c)
        d = self.thu.index('assets-2022/Images') + 12 # find the relative pos
        relative_loc = self.thu[d:] 
        return relative_loc

    def get_gif(self):
        gif = {}
        m = self.li[:]
        ii = 1
        for i in range(len(m) - 1, 3, -1):
            ind = m[i].index(':') + 2
            gif[ii] = m[i][ind:]
            ii += 1
        self.gif_li = gif
        return gif # return dic linking index and gif's address
    
    def play_mode(self):
        s_ori = self.get_gif() # copy of the puzzle dic in right sequence
        g_n = str(self.oriname)
        s_ori[0] = 'Images/' + g_n + '/blank.gif' # ensure the first one is always blank
        in_seq = int(self.get_number())
        i = 1
        li_seq = []
        while i <= in_seq:
            li_seq.append(i)
            i += 1
        li_or = li_seq[:]
        random.shuffle(li_seq)
        self.li_or = li_or
        self.li_seq = li_seq # the list in random order

    def get_list_seq(self):
        return self.li_seq

    def get_list_or(self):
        return self.li_or

    def set_thumb(self, t, sc, a, p = 1):
        '''
            Function: set_thumb
            takes two parameters, sc is the instance of turtle.Screen
            x is name of the puzzle  
        '''
        a_thu = self.get_thu() 
        if p == 1:
            new_turtle_shape(t, sc, 285, 235, a_thu)
        else:
            new_turtle_shape(t, sc, 285, 235, a_thu, 0)
        
    def game_random(self, ttt, sc, alist):
        s_li = alist
        a_siz = int(self.get_size())
        a_num = int(self.get_number())
        a_num_root = math.sqrt(a_num)
        a_gif = self.get_gif()
        puz = []
        s_xy = {} # this dic saves the coordination of each tile
        
        if a_siz > 80:
            gap = a_siz + 5 # gap is constant
        else:
            gap = 2.2 * a_siz
        x_start = (485 - (gap * a_num_root)) / 2 - 350
        x, y, z, c = [-310, 280], [a_siz + 2, a_siz + 2], 1, "black"

        i = 0 
        j = 0
        ii = 0 # iterate s_li by ii
        while i <= (a_num_root - 1):
            puz.append([])
            while j <= (a_num_root - 1):
                puz[i].append(j)
                
                xx, yy = int(x[0] + a_siz / 2), int(x[1] - a_siz / 2)
                # center of the tile
                
                # draw_square(t, x, y, z, c)
                tt = turtle.Turtle()
                gif_temp = a_gif[s_li[ii]]  
                tt.hideturtle()
                tt.penup()
                tt.setpos(xx, yy)
                tt.pendown()
                sc.addshape(gif_temp)
                tt.shape(gif_temp)
                tt.showturtle()
                # create new turtle as 'tile'
      
                p = a_siz / 2
                s_xy[ii] = [xx - p, xx + p, yy - p, yy + p, tt, s_li[ii]]
                # each tile's click zone, turtle object, and original gif
                
                x[0] += gap
                j += 1
                ii += 1 
            j = 0
            i += 1
            x[0] = -310
            x[1] -= gap
        self.dic = s_xy

    def get_dic(self):
        return self.dic

    def get_aroundxy(self, x):
        d = self.get_dic()
        num = self.get_number()
        if 0 <= x < num:
            x1, x2 = d[x][0], d[x][1]
            y1, y2 = d[x][2], d[x][3]
        else:
            x1, x2, y1, y2 = 1, 0, 1, 0
        return [x1, x2, y1, y2]

    def get_left(self, blank):
        x = blank
        d = self.get_dic()
        num = self.get_number()
        p = math.sqrt(num)
        if x % p == 0:
            x1, x2, y1, y2 = 1, 0, 1, 0
        else:
            x1, x2 = d[x-1][0], d[x-1][1]
            y1, y2 = d[x-1][2], d[x-1][3]
        return [x1, x2, y1, y2]

    def get_right(self, blank):
        x = blank
        d = self.get_dic()
        num = self.get_number()
        p = math.sqrt(num)
        if x % p == (p - 1):
            x1, x2, y1, y2 = 1, 0, 1, 0
        else:
            x1, x2 = d[x+1][0], d[x+1][1]
            y1, y2 = d[x+1][2], d[x+1][3]
        return [x1, x2, y1, y2]
    
    def load_button(self):
        inf = "Load Puzzle"
        prompt = 'Enter the name of the puzzle you wish to load. Choices are:\
                \nmeow \nfifteen \nluigi \nmario \nsmiley \nyoshi'
        a = scc.textinput(inf, prompt)
        if a != None:
            save_name(a)
        a_nn = get_name()
        g_n = a_nn.lower()    
        plist = ['fifteen', 'luigi', 'mario', 'smiley', 'yoshi', 'meow']
        if g_n not in plist:
            ero = 'Resources/file_error.gif'
            turtle_present_gif(ero, 2)
            return False
        elif g_n in plist:
            self.loadgame = g_n
            return True
    
    def click_xy(self, x, y):
        if (60 <= x <= 140) and (-305 <= y <= -225) is True: 
            raise ValueError
        if (160 <= x <= 240) and (-305 <= y <= -225) is True:
            m = self.load_button()
            if m is True: 
                raise RuntimeError
        if (260 <= x <= 340) and (-305 <= y <= -225) is True:
            seu = 'Resources/quitmsg.gif'
            turtle_present_gif(seu, 2)
            sc.bye()
        # avoid click reset calling the rest steps  
        
        dic = self.dic
        a_list = self.li_seq

        a = a_list.index(1) # blank tile's position
        b = math.sqrt(len(a_list))
           
        a_up, a_down = a - b, a + b
        a_left, a_right = a - 1, a + 1
    
        u1, u2 = self.get_aroundxy(a_up)[0], self.get_aroundxy(a_up)[1]
        u3, u4 = self.get_aroundxy(a_up)[2], self.get_aroundxy(a_up)[3]
        
        d1, d2 = self.get_aroundxy(a_down)[0], self.get_aroundxy(a_down)[1]
        d3, d4 = self.get_aroundxy(a_down)[2], self.get_aroundxy(a_down)[3]

        l1, l2 = self.get_left(a)[0], self.get_left(a)[1]
        l3, l4 = self.get_left(a)[2], self.get_left(a)[3]

        r1, r2 = self.get_right(a)[0], self.get_right(a)[1]
        r3, r4 = self.get_right(a)[2], self.get_right(a)[3]
        re = bool
          
        if (u1 <= x <= u2) and (u3 <= y <= u4) is True:
            self.swap_tile(a, a_up)
            self.step = self.step  + 1
            re = True
        elif (d1 <= x <= d2) and (d3 <= y <= d4) is True:
            self.swap_tile(a, a_down)
            self.step = self.step  + 1
            re = True
        elif (l1 <= x <= l2) and (l3 <= y <= l4) is True:
            self.swap_tile(a, a_left)
            self.step = self.step  + 1
            re = True
        elif (r1 <= x <= r2) and (r3 <= y <= r4) is True:
            self.swap_tile(a, a_right) 
            self.step = self.step  + 1
            re = True
        else:
            re = False

        self.step_write()
         
    def step_write(self):
        step = self.tstep
        step.color('white')
        step.hideturtle()
        step.clear()
        step.penup()
        step.speed(0)
        step.setpos(-310, -280) 
        step.write(f'Player Moves: {self.step}', font=('roboto', 30, 'normal'))
        
    def reset(self):
        a_num = int(self.get_number())
        for i in range(a_num):
            self.dic[i][4].clear()
            self.dic[i][4].shape(self.gif_li[a_num - i])
            self.dic[i][5] = a_num - i
        self.step = 0
        ns = self.li_or[:]
        self.li_seq = ns[:]
        self.li_seq = self.li_seq[::-1]
        
    def swap_tile(self, blank, another):
        dic = self.dic
        x, y = int(blank), int(another)
        i_a = self.li_seq.index(dic[y][5]) # index of 'another' in random list
        z = int(dic[y][5]) 
        a = dic[x][:]
        dic[x][5] = dic[y][5]
        dic[x][4].shape(self.gif_li[dic[y][5]])
        
        dic[y][5] = a[5]
        dic[y][4].shape(self.gif_li[a[5]])
        
        aa = self.li_seq.index(1)
        self.li_seq[aa] = z
        self.li_seq[i_a] = 1

    def dicide_win(self):
        if self.li_seq[::-1] == self.li_or:
            raise SystemExit
        
        s_final = get_goal()
        if self.step == int(s_final):
            t_f = turtle.Turtle()
            p1, p2 = 'Resources/Lose.gif', 'Resources/credits.gif'
            turtle_present_gif(p1, 1)
            turtle_present_gif(p2, 2)
            scc.bye()
