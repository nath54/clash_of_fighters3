#coding:utf-8
from lib import * #on import toutes les données du programme lib.py

def main(p1,p2,p3,p4,p1keys,p2keys,p3keys,p4keys): #fonction main du programme jeu.py
    tm=75 #variable tm qui correspond au coté d'un case de la map
    tp=100 #variable tp qui correspond au à la taille des persos
    prs=[None,None,None,None] #liste prs qui contient les personnages des joueurs
    nbj=0  #variable nbj qui contient le nombre de joueurs
    if p1!=None: prs[0],nbj=Perso(p1,100,100,tp),nbj+1 #si p1 est différent de None , alors l'élément 0 de la liste prs vaut le personnage du player 1 et nbj est incrémenté de 1
    if p2!=None: prs[1],nbj=Perso(p2,100,100,tp),nbj+1 #si p2 est différent de None , alors l'élément 1 de la liste prs vaut le personnage du player 2 et nbj est incrémenté de 1
    if p3!=None: prs[2],nbj=Perso(p3,100,100,tp),nbj+1 #si p3 est différent de None , alors l'élément 2 de la liste prs vaut le personnage du player 3 et nbj est incrémenté de 1
    if p4!=None: prs[3],nbj=Perso(p4,100,100,tp),nbj+1 #si p4 est différent de None , alors l'élément 3 de la liste prs vaut le personnage du player 4 et nbj est incrémenté de 1
    fens=[] #liste fens qui contient toutes les fenetres
    if   nbj == 1 : fens = [ [0,0,tex,tey] ] #on crée les fenetres en fonction du nombre de joueurs
    elif nbj == 2 : fens = [ [0,0,tex,int(tey/2)] , [0,int(tey/2),tex,int(tey/2)] ] #on crée les fenetres en fonction du nombre de joueurs
    elif nbj == 3 : fens = [ [0,0,int(tex/2),int(tey/2)] , [int(tex/2),0,int(tex/2),int(tey/2)] , [0,int(tey/2),tex,int(tey/2)] ] #on crée les fenetres en fonction du nombre de joueurs
    elif nbj == 4 : fens = [ [0,0,int(tex/2),int(tey/2)] , [0,0,int(tex/2),int(tey/2)] , [0,0,int(tex/2),int(tey/2)] , [int(tex/2),int(tey/2),int(tex/2),int(tey/2)] ] #on crée les fenetres en fonction du nombre de joueurs
    imgmape=[] #liste imgmape qui va contenir toutes les images de la mape préparées
    for m in emaps: #boucle qui parcour toutes les valeurs de la liste emaps
        imgmape.append(pygame.transform.scale(pygame.image.load(dim+m[2]),[tm,tm])) #on ajoute a imgmape une image préparée
    mape=numpy.zeros([25,25],dtype=int) #matrice numpy mape qui est la map de la partie
    for x in range(mape.shape[0]): #boucle qui parcour tous les x de mape
        for y in range(mape.shape[1]): #boucle qui parcour tous les y de mape
            mape[x,y]=random.randint(0,len(emaps)-1) #on assigne a la mape une valeur aléatoire
    objsmap=[] #liste qui contient tous les objets qui seront sur la map (ex:un arbre)
    bonus=[] #liste bonus qui contient tous les bonus qui seront sur la map (ex:du bouclier)
    encoure=True #variable encoure qui est vraie tant que le jeu tourne
    while encoure: #tant que encoure est vrai
        #affichage
        a=0 #initialisation de la variable a
        if p1!=None and prs[0]!=None: #si p1 est différent de None
            fx,fy,ftx,fty=fens[a][0],fens[a][1],fens[a][2],fens[a][3] #variables fx,fy,ftx et fty qui correspondent à l'élément a de la liste fens
            affichage_jeu_fen(fenetre,0,0,tex,tey,mape,imgmape,objsmap,prs,prs[0],tm,bonus) #on affiche la fenetre du premier joueur
            a+=1 #on incrémente a de 1
        if p2!=None and prs[1]!=None: #si p2 est différent de None
            fx,fy,ftx,fty=fens[a][0],fens[a][1],fens[a][2],fens[a][3] #variables fx,fy,ftx et fty qui correspondent à l'élément a de la liste fens
            affichage_jeu_fen(fenetre,0,0,tex,tey,mape,imgmape,objsmap,prs,prs[1],tm,bonus) #on affiche la fenetre du second joueur
            a+=1 #on incrémente a de 1
        if p3!=None and prs[2]!=None: #si p3 est différent de None
            fx,fy,ftx,fty=fens[a][0],fens[a][1],fens[a][2],fens[a][3] #variables fx,fy,ftx et fty qui correspondent à l'élément a de la liste fens
            affichage_jeu_fen(fenetre,0,0,tex,tey,mape,imgmape,objsmap,prs,prs[2],tm,bonus) #on affiche la fenetre du troisieme joueur
            a+=1 #on incrémente a de 1
        if p4!=None and prs[3]!=None: #si p4 est différent de None
            fx,fy,ftx,fty=fens[a][0],fens[a][1],fens[a][2],fens[a][3] #variables fx,fy,ftx et fty qui correspondent à l'élément a de la liste fens
            affichage_jeu_fen(fenetre,0,0,tex,tey,mape,imgmape,objsmap,prs,prs[3],tm,bonus) #on affiche la fenetre du quatrieme joueur

        for event in pygame.event.get(): #boucle des evenements de pygame
            if event.type==QUIT: encoure=False #si il y a un événement QUITTER , encoure est faux
            elif event.type==KEYDOWN: #si il y a un événement KEYDOWN, alors:
                for k in p1keys: #boucle qui renvoie toutes les keys de p1keys dans k
                    if event.key==k: #si la touche appuyée est égale à k
                        di,pp=p1keys.index(k),0 #di est égal à l'index de l'élément k de la liste p1keys et pp est égal à 0
                        if di==0: prs[pp].bouger("Up",objsmap,prs) #si di est égal à 0 , alors le personnage va bouger vers le haut
                        elif di==1: prs[pp].bouger("Down",objsmap,prs) #si di est égal à 1 , alors le personnage va bouger vers le bas
                        elif di==2: prs[pp].bouger("Left",objsmap,prs) #si di est égal à 2 , alors le personnage va bouger vers la gauche
                        elif di==3: prs[pp].bouger("Right",objsmap,prs) #si di est égal à 3 , alors le personnage va bouger vers la droite
                        elif di==4: prs[pp].bouger("Att1",objsmap,prs) #si di est égal à 4 , alors le personnage va attaquer avec l'attaque 1
                        elif di==5: prs[pp].bouger("Att2",objsmap,prs) #si di est égal à 5 , alors le personnage va attaquer avec l'attaque 2
                        elif di==6: prs[pp].bouger("Att3",objsmap,prs) #si di est égal à 6 , alors le personnage va attaquer avec l'attaque 3
                        elif di==7: prs[pp].bouger("Defence",objsmap,prs) #si di est égal à 7 , alors le personnage va se défendre
                for k in p2keys: #boucle qui renvoie toutes les keys de p2keys dans k
                    if event.key==k: #si la touche appuyée est égale à k
                        di,pp=p2keys.index(k),1 #di est égal à l'index de l'élément k de la liste p2keys et pp est égal à 1
                        if di==0: prs[pp].bouger("Up",objsmap,prs) #si di est égal à 0 , alors le personnage va bouger vers le haut
                        elif di==1: prs[pp].bouger("Down",objsmap,prs) #si di est égal à 1 , alors le personnage va bouger vers le bas
                        elif di==2: prs[pp].bouger("Left",objsmap,prs) #si di est égal à 2 , alors le personnage va bouger vers la gauche
                        elif di==3: prs[pp].bouger("Right",objsmap,prs) #si di est égal à 3 , alors le personnage va bouger vers la droite
                        elif di==4: prs[pp].bouger("Att1",objsmap,prs) #si di est égal à 4 , alors le personnage va attaquer avec l'attaque 1
                        elif di==5: prs[pp].bouger("Att2",objsmap,prs) #si di est égal à 5 , alors le personnage va attaquer avec l'attaque 2
                        elif di==6: prs[pp].bouger("Att3",objsmap,prs) #si di est égal à 6 , alors le personnage va attaquer avec l'attaque 3
                        elif di==7: prs[pp].bouger("Defence",objsmap,prs) #si di est égal à 7 , alors le personnage va se défendre
                for k in p3keys: #boucle qui renvoie toutes les keys de p3keys dans k
                    if event.key==k: #si la touche appuyée est égale à k
                        di,pp=p3keys.index(k),2 #di est égal à l'index de l'élément k de la liste p3keys et pp est égal à 2
                        if di==0: prs[pp].bouger("Up",objsmap,prs) #si di est égal à 0 , alors le personnage va bouger vers le haut
                        elif di==1: prs[pp].bouger("Down",objsmap,prs) #si di est égal à 1 , alors le personnage va bouger vers le bas
                        elif di==2: prs[pp].bouger("Left",objsmap,prs) #si di est égal à 2 , alors le personnage va bouger vers la gauche
                        elif di==3: prs[pp].bouger("Right",objsmap,prs) #si di est égal à 3 , alors le personnage va bouger vers la droite
                        elif di==4: prs[pp].bouger("Att1",objsmap,prs) #si di est égal à 4 , alors le personnage va attaquer avec l'attaque 1
                        elif di==5: prs[pp].bouger("Att2",objsmap,prs) #si di est égal à 5 , alors le personnage va attaquer avec l'attaque 2
                        elif di==6: prs[pp].bouger("Att3",objsmap,prs) #si di est égal à 6 , alors le personnage va attaquer avec l'attaque 3
                        elif di==7: prs[pp].bouger("Defence",objsmap,prs) #si di est égal à 7 , alors le personnage va se défendre
                for k in p4keys: #boucle qui renvoie toutes les keys de p4keys dans k
                    if event.key==k: #si la touche appuyée est égale à k
                        di,pp=p4keys.index(k),3 #di est égal à l'index de l'élément k de la liste p4keys et pp est égal à 3
                        if di==0: prs[pp].bouger("Up",objsmap,prs) #si di est égal à 0 , alors le personnage va bouger vers le haut
                        elif di==1: prs[pp].bouger("Down",objsmap,prs) #si di est égal à 1 , alors le personnage va bouger vers le bas
                        elif di==2: prs[pp].bouger("Left",objsmap,prs) #si di est égal à 2 , alors le personnage va bouger vers la gauche
                        elif di==3: prs[pp].bouger("Right",objsmap,prs) #si di est égal à 3 , alors le personnage va bouger vers la droite
                        elif di==4: prs[pp].bouger("Att1",objsmap,prs) #si di est égal à 4 , alors le personnage va attaquer avec l'attaque 1
                        elif di==5: prs[pp].bouger("Att2",objsmap,prs) #si di est égal à 5 , alors le personnage va attaquer avec l'attaque 2
                        elif di==6: prs[pp].bouger("Att3",objsmap,prs) #si di est égal à 6 , alors le personnage va attaquer avec l'attaque 3
                        elif di==7: prs[pp].bouger("Defence",objsmap,prs) #si di est égal à 7 , alors le personnage va se défendre


