#coding:utf-8
from lib import *
import jeu

txts=[pretexte("The Clash of Fighters 3",50,(250,100,50)),pretexte("Keys :",25,(0,0,0)),pretexte("move up",17,(0,0,0)),pretexte("move down",17,(0,0,0)),pretexte("move left",17,(0,0,0)),pretexte("move right",17,(0,0,0)),pretexte("att1",17,(0,0,0)),
      pretexte("att2",17,(0,0,0)),pretexte("att special",17,(0,0,0)),pretexte("defence",17,(0,0,0)),pretexte("Player 1 :",20,(255,255,255)),
      pretexte("key up",17,(0,0,0)),pretexte("key down",17,(0,0,0)),pretexte("key left",17,(0,0,0)),pretexte("key right",17,(0,0,0)),pretexte("suppr",17,(0,0,0)),pretexte("end",17,(0,0,0)),
      pretexte("page down",17,(0,0,0)),pretexte("page up",17,(0,0,0)),pretexte("Player 2 :",20,(255,255,255)),pretexte("e",17,(0,0,0)),
      pretexte("d",17,(0,0,0)),pretexte("s",17,(0,0,0)),pretexte("f",17,(0,0,0)),pretexte("x",17,(0,0,0)),pretexte("c",17,(0,0,0)),
      pretexte("v",17,(0,0,0)),pretexte("r",17,(0,0,0)),pretexte("Player 3 : ",20,(255,255,255)),pretexte("i",17,(0,0,0)),pretexte("k",17,(0,0,0)),pretexte("j",17,(0,0,0)),pretexte("l",17,(0,0,0)),
      pretexte("y",17,(0,0,0)),pretexte("u",17,(0,0,0)),pretexte("g",17,(0,0,0)),pretexte("h",17,(0,0,0)),pretexte("Player 4 :",20,(255,255,255)),
      pretexte("KP8",17,(0,0,0)),pretexte("KP2",17,(0,0,0)),pretexte("KP4",17,(0,0,0)),pretexte("KP6",17,(0,0,0)),pretexte("KP0",17,(0,0,0)),pretexte("KP .",17,(0,0,0)),pretexte("KP ENTER",17,(0,0,0)),pretexte("KP PLUS",17,(0,0,0)),
      pretexte("Play ! ",25,(0,0,0)),pretexte("humain",20,(0,0,0)),pretexte("bot",20,(0,0,0))]

print(len(txts))

clf=(64,121,204)
def aff_menu(p1,p2,p3,p4,fps):
    bts=[]
    for x in range(10): bts.append(None)
    fenetre.fill(clf)
    atexte(txts[0],250,50)
    
    atexte(txts[1],20,320)
    atexte(txts[2],25,350)
    atexte(txts[3],25,365)
    atexte(txts[4],25,380)
    atexte(txts[5],25,395)
    atexte(txts[6],25,410)
    atexte(txts[7],25,425)
    atexte(txts[8],25,440)
    atexte(txts[9],25,455)
    #player 1
    atexte(txts[10],150,150)
    bts[1]=button(150,230,100,100,(100,100,100),(0,0,0))
    if p1!=None:
        texte(persos[p1][0],150,180,20,(255,255,255))
        fenetre.blit(persos[p1][8],[rx(150),ry(230)])
    atexte(txts[11],150,350)
    atexte(txts[12],150,365)
    atexte(txts[13],150,380)
    atexte(txts[14],150,395)
    atexte(txts[15],150,410)
    atexte(txts[16],150,425)
    atexte(txts[17],150,440)
    atexte(txts[18],150,455)
    #player 2
    atexte(txts[19],300,150)
    bts[2]=button(300,230,100,100,(100,100,100),(0,0,0))
    if p2!=None:
        texte(persos[p2][0],300,180,20,(255,255,255))
        fenetre.blit(persos[p2][8],[rx(300),ry(230)])
    atexte(txts[20],300,350)
    atexte(txts[21],300,365)
    atexte(txts[22],300,380)
    atexte(txts[23],300,395)
    atexte(txts[24],300,410)
    atexte(txts[25],300,425)
    atexte(txts[26],300,440)
    atexte(txts[27],300,455)
    #player 3
    atexte(txts[28],450,150)
    bts[3]=button(450,230,100,100,(100,100,100),(0,0,0))
    if p3!=None:
        texte(persos[p3][0],450,180,20,(255,255,255))
        fenetre.blit(persos[p3][8],[rx(450),ry(230)])
    atexte(txts[29],450,350)
    atexte(txts[30],450,365)
    atexte(txts[31],450,380)
    atexte(txts[32],450,395)
    atexte(txts[33],450,410)
    atexte(txts[34],450,425)
    atexte(txts[35],450,440)
    atexte(txts[36],450,455)
    #player 4
    atexte(txts[37],600,150)
    bts[4]=button(600,230,100,100,(100,100,100),(0,0,0))
    if p4!=None:
        texte(persos[p4][0],600,180,20,(255,255,255))
        fenetre.blit(persos[p4][8],[rx(600),ry(230)])
    atexte(txts[38],600,350)
    atexte(txts[39],600,365)
    atexte(txts[40],600,380)
    atexte(txts[41],600,395)
    atexte(txts[42],600,410)
    atexte(txts[43],600,425)
    atexte(txts[44],600,440)
    atexte(txts[45],600,455)
    #
    bts[0]=button(350,650,200,100,(150,150,0),(0,0,0))
    atexte(txts[46],400,675)
    texte("fps : "+str(fps),5,5,15,(50,50,50))
    pygame.display.update()
    return bts

def main():
    p1=None
    p2=None
    p3=None
    p4=None
    p1keys=[K_UP,K_DOWN,K_LEFT,K_RIGHT,127,K_END,281,280]
    p2keys=[K_e,K_d,K_s,K_f,K_x,K_c,K_v,K_r]
    p3keys=[K_i,K_k,K_j,K_l,K_y,K_u,K_g,K_h]
    p4keys=[K_KP8,K_KP2,K_KP4,K_KP6,K_KP0,K_KP_PERIOD,K_KP_ENTER,K_KP_PLUS]
    p1tp=0
    p2tp=0
    p3tp=0
    p4tp=0
    fps=0
    encour=True
    while encour:
        t1=time.time()
        bts=aff_menu(p1,p2,p3,p4,fps)
        for event in pygame.event.get():
            if event.type==QUIT: encour=False
            elif event.type==KEYDOWN:
                if event.key==K_ESCAPE: encour=False
                print("event key ",event.key)
            elif event.type==MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                rpos=pygame.Rect(pos[0],pos[1],1,1)
                for b in bts:
                    if b != None and rpos.colliderect(b):
                        di=bts.index(b)
                        if di==1:
                            if p1==None: p1=0
                            elif p1<len(persos)-1: p1+=1
                            else: p1=None
                        elif di==2:
                            if p2==None: p2=0
                            elif p2<len(persos)-1: p2+=1
                            else: p2=None
                        elif di==3:
                            if p3==None: p3=0
                            elif p3<len(persos)-1: p3+=1
                            else: p3=None
                        elif di==4:
                            if p4==None: p4=0
                            elif p4<len(persos)-1: p4+=1
                            else: p4=None
                        elif di==0 and (p1!=None or p2!=None or p3!=None or p4!=None):
                            jeu.main(p1,p2,p3,p4,p1keys,p2keys,p3keys,p4keys,p1tp,p2tp,p3tp,p4tp)
        t2=time.time()
        tt=t2-t1
        fps=int(1.0/float(tt))

main()



