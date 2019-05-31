#coding:utf-8
from lib import *

clf=(64,121,204)
def aff_menu(p1,p2,p3,p4,fps):
    bts=[]
    for x in range(10): bts.append(None)
    fenetre.fill(clf)
    texte("The Clash Of Fighters 3",250,50,50,(250,100,50))
    texte("KEYS : ",20,320,20,(0,0,0))
    texte("move up",25,350,15,(0,0,0))
    texte("move down",25,365,15,(0,0,0))
    texte("move left",25,380,15,(0,0,0))
    texte("move right",25,395,15,(0,0,0))
    texte("att 1",25,410,15,(0,0,0))
    texte("att 2",25,425,15,(0,0,0))
    texte("att special",25,440,15,(0,0,0))
    texte("defence",25,455,15,(0,0,0))
    #player 1
    texte("Player 1 : ",150,150,20,(255,255,255))
    bts[1]=button(150,230,100,100,(100,100,100),(0,0,0))
    if p1!=None:
        texte(persos[p1][0],150,180,20,(255,255,255))
        fenetre.blit(persos[p1][8],[rx(150),ry(230)])
    texte("key up",150,350,15,(0,0,0))
    texte("key down",150,365,15,(0,0,0))
    texte("key left",150,380,15,(0,0,0))
    texte("key right",150,395,15,(0,0,0))
    texte("suppr",150,410,15,(0,0,0))
    texte("end",150,425,15,(0,0,0))
    texte("page down",150,440,15,(0,0,0))
    texte("page left",150,455,15,(0,0,0))
    #player 2
    texte("Player 2 : ",300,150,20,(255,255,255))
    bts[2]=button(300,230,100,100,(100,100,100),(0,0,0))
    if p2!=None:
        texte(persos[p2][0],300,180,20,(255,255,255))
        fenetre.blit(persos[p2][8],[rx(300),ry(230)])
    texte("e",300,350,15,(0,0,0))
    texte("d",300,365,15,(0,0,0))
    texte("s",300,380,15,(0,0,0))
    texte("f",300,395,15,(0,0,0))
    texte("x",300,410,15,(0,0,0))
    texte("c",300,425,15,(0,0,0))
    texte("v",300,440,15,(0,0,0))
    texte("r",300,455,15,(0,0,0))
    #player 3
    texte("Player 3 : ",450,150,20,(255,255,255))
    bts[3]=button(450,230,100,100,(100,100,100),(0,0,0))
    if p3!=None:
        texte(persos[p3][0],450,180,20,(255,255,255))
        fenetre.blit(persos[p3][8],[rx(450),ry(230)])
    texte("i",450,350,15,(0,0,0))
    texte("k",450,365,15,(0,0,0))
    texte("j",450,380,15,(0,0,0))
    texte("l",450,395,15,(0,0,0))
    texte("y",450,410,15,(0,0,0))
    texte("u",450,425,15,(0,0,0))
    texte("g",450,440,15,(0,0,0))
    texte("h",450,455,15,(0,0,0))
    #player 4
    texte("Player 4 : ",600,150,20,(255,255,255))
    bts[4]=button(600,230,100,100,(100,100,100),(0,0,0))
    if p4!=None:
        texte(persos[p4][0],600,180,20,(255,255,255))
        fenetre.blit(persos[p4][8],[rx(600),ry(230)])
    texte("KP8",600,350,15,(0,0,0))
    texte("KP2",600,365,15,(0,0,0))
    texte("KP4",600,380,15,(0,0,0))
    texte("KP6",600,395,15,(0,0,0))
    texte("KP0",600,410,15,(0,0,0))
    texte("KP.",600,425,15,(0,0,0))
    texte("KP ENTER",600,440,15,(0,0,0))
    texte("KP+",600,455,15,(0,0,0))
    #
    bts[0]=button(350,500,200,100,(150,150,0),(0,0,0))
    texte("Play !",400,525,25,(0,0,0))
    texte("fps : "+str(fps),5,5,15,(50,50,50))
    pygame.display.update()
    return bts

def main():
    p1=None
    p2=None
    p3=None
    p4=None
    p1keys=[K_UP,K_DOWN,K_LEFT,K_RIGHT,K_CLEAR,K_END,K_PAGEDOWN,K_PAGEUP]
    p2keys=[K_e,K_d,K_s,K_f,K_x,K_c,K_v,K_r]
    p3keys=[K_i,K_k,K_j,K_l,K_y,K_u,K_g,K_h]
    p4keys=[K_KP8,K_KP2,K_KP4,K_KP6,K_KP0,K_KP_PERIOD,K_KP_ENTER,K_KP_PLUS]
    fps=0
    encour=True
    while encour:
        t1=time.time()
        bts=aff_menu(p1,p2,p3,p4,fps)
        for event in pygame.event.get():
            if event.type==QUIT: encour=False
            elif event.type==KEYDOWN:
                if event.key==K_ESCAPE: encour=False
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
                        elif di==0:
                            jeu.main(p1,p2,p3,p4,p1keys,p2keys,p3keys,p4keys)
        t2=time.time()
        tt=t2-t1
        fps=int(1.0/float(tt))

main()



