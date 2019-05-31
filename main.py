#coding:utf-8
from lib import *

clf=(64,121,204)
def aff_menu(p1,p2,p3,p4,fps):
    bts=[]
    for x in range(10): bts.append(None)
    fenetre.fill(clf)
    texte("The Clash Of Fighters 3",250,50,50,(250,100,50))
    #player 1
    texte("Player 1 : ",150,150,20,(255,255,255))
    bts[1]=button(150,230,100,100,(100,100,100),(0,0,0))
    if p1!=None:
        texte(persos[p1][0],150,180,20,(255,255,255))
        fenetre.blit(persos[p1][8],[rx(150),ry(230)])
    #player 2
    texte("Player 2 : ",300,150,20,(255,255,255))
    bts[2]=button(300,230,100,100,(100,100,100),(0,0,0))
    if p2!=None:
        texte(persos[p2][0],300,180,20,(255,255,255))
        fenetre.blit(persos[p2][8],[rx(300),ry(230)])
    #player 3
    texte("Player 3 : ",450,150,20,(255,255,255))
    bts[3]=button(450,230,100,100,(100,100,100),(0,0,0))
    if p3!=None:
        texte(persos[p3][0],450,180,20,(255,255,255))
        fenetre.blit(persos[p3][8],[rx(450),ry(230)])
    #player 4
    texte("Player 4 : ",600,150,20,(255,255,255))
    bts[4]=button(600,230,100,100,(100,100,100),(0,0,0))
    if p4!=None:
        texte(persos[p4][0],600,180,20,(255,255,255))
        fenetre.blit(persos[p4][8],[rx(600),ry(230)])
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
                            jeu.main(p1,p2,p3,p4)
        t2=time.time()
        tt=t2-t1
        fps=int(1.0/float(tt))

main()



