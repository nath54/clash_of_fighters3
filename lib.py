#coding:utf-8
#lib.py
import random,pygame,time,numpy,math #on importe les librairies random , pygame , time , numpy et math
from pygame.locals import * #on importe tout dans la librairie pygame.locals

dim="images/" #variable dim qui contient le chemin du dossier contenant toutes les images du jeu

pygame.init() #on initialise pygame

btex,btey=1000,800 #variables btex et btey qui contiennent la taille originale de la fenetre de jeu
btx,bty=1280,1024 #variables btx et bty qui contiennent la taille originale de l'écran sur lequel a été programmé le jeu

io = pygame.display.Info() #on récurpère dans la variable io les infos sur l'affichage de l'utilisateur
mtex,mtey=io.current_w,io.current_h #on assigne à mtex et mtey la taille actuelle de l'ecran de l'ordinateur
tex,tey=int(btex/btx*mtex),int(btey/bty*mtey) #avec les données ci-dessus on calcule la taille de la fenetre du jeu pour qu'elle soit adaptée à l'écran de l'utilisateur

fenetre=pygame.display.set_mode([tex,tey]) #on crée la fenetre du jeu qu'on assigne à la variable fenetre
pygame.display.set_caption("Clash Of Fighters 3") #on nomme la fenetre du jeu "Clash Of Fighters 3"

def rx(x): return int(x*btex/tex) #fonction rx qui retourne une adaptation de x en fonction de la taille de la fenetre du jeu de l'utilisateur
def ry(y): return int(y*btey/tey) #fonction ry qui retourne une adaptation de y en fonction de la taille de la fenetre du jeu de l'utilisateur
def button(x,y,tx,ty,cl,clb): #fonction bouton qui retourne un bouton
    b=pygame.draw.rect(fenetre,cl,(rx(x),ry(y),rx(tx),ry(ty)),0) #crée dans la variable b le fond du bouton
    pygame.draw.rect(fenetre,clb,(rx(x),ry(y),rx(tx),ry(ty)),1) #dessine le contour du bouton
    return b #retourne la variable b contenant le fond du bouton qui est cliquable
def pretexte(txt,t,cl): return pygame.font.SysFont("Serif",ry(t)).render(txt,t,cl) #fonction qui prépare le texte qui va être affiché
def atexte(pretxt,x,y): fenetre.blit( pretxt , [rx(x),ry(y)]) #fonction qui affiche le texte déjà préparé
def texte(txt,x,y,t,cl): fenetre.blit( pygame.font.SysFont("Serif",ry(t)).render(txt,t,cl) , [rx(x),ry(y)]) #fonction texte qui écrit un texte à l'ecran
def dist(x1,y1,x2,y2): return int(math.square(math.pow(x1-x2,2)+math.pow(y1-y2,2))) #fonction dist qui retourne la distance entre deoux points

#liste emaps qui contient toutes les données des éléments de la mape

emaps=[ ["herbe",True,"herbe.png"] , ["terre",True,"terre.png"] ]
#0=nom , 1=pmd

#liste persos qui contient toutes les données des personnages
persos=[  [ "jarry",1000,100,20,5,[35,350,1,[],15,"coup de pistolet"],[20,70,0.7,[],5,"coup de poing"],[250,250,50,[],50,"lasers dans le sol qui ressortent au niveau de l'ennemi"],pygame.transform.scale(pygame.image.load(dim+"jarry.png"),[rx(100),ry(100)]) ]
          ,["bismak",2000,200,10,3,[50,100,1.2,[],15,"coup d'épée"],[50,100,1.2,[],15,"coup d'épée"],[200,150,45,[],75,"super coup d'épée"],pygame.transform.scale(pygame.image.load(dim+"bismak.png"),[rx(100),ry(100)])]
          #,["",0,0,0,0,[0,0,0,[],0,""],[0,0,0,[],0,""],[0,0,0,[],0,""]]
          #,["",0,0,0,0,[0,0,0,[],0,""],[0,0,0,[],0,""],[0,0,0,[],0,""]]
          #,["",0,0,0,0,[0,0,0,[],0,""],[0,0,0,[],0,""],[0,0,0,[],0,""]]
          #,["",0,0,0,0,[0,0,0,[],0,""],[0,0,0,[],0,""],[0,0,0,[],0,""]]
          #,["",0,0,0,0,[0,0,0,[],0,""],[0,0,0,[],0,""],[0,0,0,[],0,""]]
          #,["",0,0,0,0,[0,0,0,[],0,""],[0,0,0,[],0,""],[0,0,0,[],0,""]]
          #["",0,0,0,0,[0,0,0,[],0,""],[0,0,0,[],0,""],[0,0,0,[],0,""]]
          #,["",0,0,0,0,[0,0,0,[],0,""],[0,0,0,[],0,""],[0,0,0,[],0,""]]
          #,["",0,0,0,0,[0,0,0,[],0,""],[0,0,0,[],0,""],[0,0,0,[],0,""]]
          #,["",0,0,0,0,[0,0,0,[],0,""],[0,0,0,[],0,""],[0,0,0,[],0,""]]
          ]

#0=nom , 1=vie , 2=bouclier , 3=rapidité , 4=%esquive , 5=attaque 1 , 6=attaque 2 , 7=attaque 3(spécial) , 8=img portrait prechargé menu
#attaque : 0=degats , 1=portee(pixels) , 2=temps (sec) , 3=effets , 4=%coup critique(x2 dégats) , 5=description

def loadimgprs(nom,t): #fonction loadimgprs qui va retourner une liste avec toutes les images du personnage avec son nom et la taille des images
    lst=[] #initialisation de la liste lst
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+".png"),[t,t])) #on ajoute l'image nom+".png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_haut1.png"),[t,t])) #on ajoute l'image nom+"_haut1.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_haut2.png"),[t,t])) #on ajoute l'image nom+"_haut2.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_haut3.png"),[t,t])) #on ajoute l'image nom+"_haut3.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_bas1.png"),[t,t])) #on ajoute l'image nom+"_bas1.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_bas2.png"),[t,t])) #on ajoute l'image nom+"_bas2.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_bas3.png"),[t,t])) #on ajoute l'image nom+"_bas3.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_gauche1.png"),[t,t])) #on ajoute l'image nom+"_gauche1.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_gauche2.png"),[t,t])) #on ajoute l'image nom+"_gauche2.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_gauche3.png"),[t,t])) #on ajoute l'image nom+"_gauche3.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_droite1.png"),[t,t])) #on ajoute l'image nom+"_droite1.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_droite2.png"),[t,t])) #on ajoute l'image nom+"_droite2.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_droite3.png"),[t,t])) #on ajoute l'image nom+"_droite3.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_defence1.png"),[t,t])) #on ajoute l'image nom+"_defence1.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_defence2.png"),[t,t])) #on ajoute l'image nom+"_defence2.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_defence3.png"),[t,t])) #on ajoute l'image nom+"_defence3.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_att11.png"),[t,t])) #on ajoute l'image nom+"_att11.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_att12.png"),[t,t])) #on ajoute l'image nom+"_att12.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_att13.png"),[t,t])) #on ajoute l'image nom+"_att13.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_effet_att1.png"),[t,t])) #on ajoute l'image nom+"_effets_att1.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_att21.png"),[t,t])) #on ajoute l'image nom+"_att21.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_att22.png"),[t,t])) #on ajoute l'image nom+"_att22.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_att23.png"),[t,t])) #on ajoute l'image nom+"_att23.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_effet_att2.png"),[t,t])) #on ajoute l'image nom+"_effets_att2.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_att31.png"),[t,t])) #on ajoute l'image nom+"_att31.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_att32.png"),[t,t])) #on ajoute l'image nom+"_att32.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_att33.png"),[t,t])) #on ajoute l'image nom+"_att33.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_effet_att3.png"),[t,t])) #on ajoute l'image nom+"_effets_att3.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_mort.png"),[t,t])) #on ajoute l'image nom+"_mort.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_icon.png"),[t,t])) #on ajoute l'image nom+"_icon.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_portrait.png"),[t,t])) #on ajoute l'image nom+"_portrait.png" à la liste
    return lst #on retourne la liste

def isobstacle(x1,y1,x2,y2,lo): #fonction isobstacle qui retourne si il y a un obstacle entre deux points
    d=pygame.draw.line(fenetre,(0,0,0),(x1,y1),(x2,y2),1) #on récupère dans la variable d le rect de la ligne qui part de (x1,y1) et qui va a (x2,y2)
    c=False #on inititalise la variable c
    for o in lo: #on parcoure tous les obstacles
        if d.colliderect(o.rect): c=True #si le rect d rentre en collision avec un obstacle, la variable c est vraie
    return c #on retourne la variable c qui contient si il y a un obstacle ou pas

def peutbouger(perso,objsmap):
    r=pygame.Rect(perso.posX,perso.posY,perso.tx,perso.ty)
    c=True
    for o in objsmap:
        if r.colliderect(o.rect): c=False
    return c

class Perso(): #classe personnage
    def __init__(self,p,x,y,t): #fonction initialisation du personnage
        self.nom=persos[p][0] #variable nom qui contient le nom du personnage
        self.vie_totale=persos[p][1] #variable vie_totale qui contient la vie totale du personnage
        self.vie=self.vie_totale #variable vie qui contient la vie du personnage
        self.bouclier_total=persos[p][2] #variable bouclier_total qui contient le bouclier total du personnage
        self.bouclier=self.bouclier_total #variable bouclier qui contient le bouclier du personnage
        self.vitesse=persos[p][3] #variable vitesse qui contient la vitesse du personnage
        self.esquive=persos[p][4] #variable esquive qui contient la probabilité (en %) que le personnage esquive une attaque
        self.attaque1=persos[p][5] #liste attque1 qui contient les infos de l'attaque 1 du personnage
        self.attaque2=persos[p][6] #liste attque2 qui contient les infos de l'attaque 2 du personnage
        self.attaque3=persos[p][7] #liste attque3 qui contient les infos de l'attaque 3 du personnage
        self.datt1=time.time() #variable datt1 qui contient le temps où le personnage a utilisé l'attaque 1 pour la derniere fois
        self.datt2=time.time() #variable datt2 qui contient le temps où le personnage a utilisé l'attaque 2 pour la derniere fois
        self.datt3=time.time() #variable datt3 qui contient le temps où le personnage a utilisé l'attaque 3 pour la derniere fois
        self.posX=x #variable posX qui contient la position x du personnage
        self.posY=y #variable posY qui contient la position y du personnage
        self.tx=t #variable tx qui contient la taille x du personnage
        self.ty=t #variable ty qui contient la taille y du personnage
        self.cam=[self.posX-int(tex/2),self.posY-int(tey/2)] #liste cam qui contient les coordonnées de la caméra du personnage
        self.imgs=loadimgprs(self.nom,t) #liste imgs qui contient toutes les images du personnage
        #0=normal , 1=haut(1) , 2=haut(2) , 3=haut(3) , 4=bas(1) , 5=bas(2) , 6=bas(3) , 7=gauche(1) , 8=gauche(2) , 9=gauche(3)
        #10=droite(1) , 11=droite(2) , 12=droite(3) , 13=defence(1) , 14=defence(2) , 15=defence(3)  , 16=att1(1) , 17=att1(2) , 18=att1(3)
        #19=effets att1 , 20=att2(1) , 21=att2(2) , 22=att2(3) , 23=effets att2 , 24=att3(1) , 25=att3(2) , 26=att3(3) , 27=effets att3
        #28=mort , 29=icon , 30=portrait
        self.image=self.imgs[0] #variable image qui contient l'image qui va etre affichée
        self.images_effet=None #variable image_effet qui contient les effets subis par le personnage
        self.animactu=None #liste animactu qui contient l'animation du personnage en cour
        self.tpsbouger=0.1 #variable tpsbouger qui contient le temps que le personnage va mettre entre chaque mouvement
        self.dbouger=time.time() #variable dbouger qui contient le temps où le personnage a bougé pour la derniere fois
        self.bloquerattaque=False #variable bloquerattaque qui dit si le personnage est en train de bloquer les attaques ou pas
    def bouger(self,aa,objsmap,prs): #fonction bouger du personnage qui permet au personnage de bouger, d'attaquer et de parer les coups de l'adversaire
        if aa=="Up": #bouger vers le haut
            if time.time()-self.dbouger >= self.tpsbouger: #on vérifie que le temps qu'il y a entre la derniere fois que le personnage a bougé et maintenant est supérieur ou égal au temps minimum
                self.bloquerattaque=False #le personnage ne bloque plus les attaques
                self.dbouger=time.time() #mise à jour de la variable (derniere fois bouger)
                self.posY-=self.vitesse #on bouge le personnage
                if not peutbouger(self,objsmap): #on vérifie si le perso peut bouger (collisions avec les objets de la map)
                    self.posY+=self.vitesse+1 #si le perso rentre en collision avec un autre objet de la map, il rebondit
                if self.animactu==None or self.animactu[0]!="haut": #si il n'y a pas d'animation ou une différente de l'animation (bouger vers le haut)
                    self.animactu=["haut",0] #on update l'animation en cour
                    self.image=self.imgs[1] #on update l'image
                elif self.animactu[0]=="haut" and self.animactu[1]==0: #on vérifie l'état de l'animation
                    self.animactu=["haut",1] #on update l'animation en cour
                    self.image=self.imgs[2] #on update l'image
                elif self.animactu[0]=="haut" and self.animactu[1]==1: #on vérifie l'état de l'animation
                    self.animactu=["haut",2] #on update l'animation en cour
                    self.image=self.imgs[3] #on update l'image
                elif self.animactu[0]=="haut" and self.animactu[1]==2: #on vérifie l'état de l'animation
                    self.animactu=["haut",0] #on update l'animation en cour
                    self.image=self.imgs[1] #on update l'image
        elif aa=="Down": #bouger vers le bas
            if time.time()-self.dbouger >= self.tpsbouger: #on vérifie que le temps qu'il y a entre la derniere fois que le personnage a bougé et maintenant est supérieur ou égal au temps minimum
                self.bloquerattaque=False #le personnage ne bloque plus les attaques
                self.dbouger=time.time() #mise à jour de la variable (derniere fois bouger)
                self.posY+=self.vitesse #on bouge le personnage
                if not peutbouger(self,objsmap): #on vérifie si le perso peut bouger (collisions avec les objets de la map)
                    self.posY-=self.vitesse+1 #si le perso rentre en collision avec un autre objet de la map, il rebondit
                if self.animactu==None or self.animactu[0]!="bas": #si il n'y a pas d'animation ou une différente de l'animation (bouger vers le bas)
                    self.animactu=["bas",0] #on update l'animation en cour
                    self.image=self.imgs[4] #on update l'image
                elif self.animactu[0]=="bas" and self.animactu[1]==0: #on vérifie l'état de l'animation
                    self.animactu=["bas",1] #on update l'animation en cour
                    self.image=self.imgs[5] #on update l'image
                elif self.animactu[0]=="bas" and self.animactu[1]==1: #on vérifie l'état de l'animation
                    self.animactu=["bas",2] #on update l'image
                    self.image=self.imgs[6] #on update l'animation en cour
                elif self.animactu[0]=="bas" and self.animactu[1]==2: #on vérifie l'état de l'animation
                    self.animactu=["bas",0] #on update l'animation en cour
                    self.image=self.imgs[4] #on update l'image
        elif aa=="Left": #bouger vers la gauche
            if time.time()-self.dbouger >= self.tpsbouger: #on vérifie que le temps qu'il y a entre la derniere fois que le personnage a bougé et maintenant est supérieur ou égal au temps minimum
                self.bloquerattaque=False #le personnage ne bloque plus les attaques
                self.dbouger=time.time() #mise à jour de la variable (derniere fois bouger)
                self.posX-=self.vitesse #on bouge le personnage
                if not peutbouger(self,objsmap): #on vérifie si le perso peut bouger (collisions avec les objets de la map)
                    self.posX+=self.vitesse+1 #si le perso rentre en collision avec un autre objet de la map, il rebondit
                if self.animactu==None or self.animactu[0]!="gauche": #si il n'y a pas d'animation ou une différente de l'animation (bouger vers la gauche)
                    self.animactu=["gauche",0] #on update l'animation en cour
                    self.image=self.imgs[7] #on update l'image
                elif self.animactu[0]=="gauche" and self.animactu[1]==0: #on vérifie l'état de l'animation
                    self.animactu=["gauche",1] #on update l'animation en cour
                    self.image=self.imgs[8] #on update l'image
                elif self.animactu[0]=="gauche" and self.animactu[1]==1: #on vérifie l'état de l'animation
                    self.animactu=["gauche",2] #on update l'animation en cour
                    self.image=self.imgs[9] #on update l'image
                elif self.animactu[0]=="gauche" and self.animactu[1]==2: #on vérifie l'état de l'animation
                    self.animactu=["gauche",0] #on update l'animation en cour
                    self.image=self.imgs[7] #on update l'image
        elif aa=="Right": #bouger vers la droite
            if time.time()-self.dbouger >= self.tpsbouger: #on vérifie que le temps qu'il y a entre la derniere fois que le personnage a bougé et maintenant est supérieur ou égal au temps minimum
                self.bloquerattaque=False #le personnage ne bloque plus les attaques
                self.dbouger=time.time() #mise à jour de la variable (derniere fois bouger)
                self.posX+=self.vitesse #on bouge le personnage
                if not peutbouger(self,objsmap): #on vérifie si le perso peut bouger (collisions avec les objets de la map)
                    self.posX-=self.vitesse+1 #si le perso rentre en collision avec un autre objet de la map, il rebondit
                if self.animactu==None or self.animactu[0]!="droite": #si il n'y a pas d'animation ou une différente de l'animation (bouger vers la droite)
                    self.animactu=["droite",0] #on update l'animation en cour
                    self.image=self.imgs[10] #on update l'image
                elif self.animactu[0]=="droite" and self.animactu[1]==0: #on vérifie l'état de l'animation
                    self.animactu=["droite",1] #on update l'animation en cour
                    self.image=self.imgs[11] #on update l'image
                elif self.animactu[0]=="droite" and self.animactu[1]==1: #on vérifie l'état de l'animation
                    self.animactu=["droite",2] #on update l'animation en cour
                    self.image=self.imgs[12] #on update l'image
                elif self.animactu[0]=="droite" and self.animactu[1]==2: #on vérifie l'état de l'animation
                    self.animactu=["droite",0] #on update l'animation en cour
                    self.image=self.imgs[10] #on update l'image
        elif aa=="Attaque1": #Attaque 1
            if time.time()-self.datt1 >= self.attaque1[2]: #on vérifie que le temps qu'il y a entre la derniere fois que le personnage a attaqué avec l'attaque 1 et maintenant est supérieur ou égal au temps minimum
                self.bloquerattaque=False #le personnage ne bloque plus les attaques
                self.datt1=time.time() #mise à jour de la variable (derniere fois attaque 1)
                for p in prs: #boucle qui retourne tous les personages
                    if p!=self and dsit(p.posX,p.posY,self.posX,self.posY) <= self.attaque1[1]: #on vérifie que le personnage n'est pas celui qui attaque et que la distance entre les deux persos est inférieure à la portée de l'attaque
                        a=random.randint(0,100) #on prend un chiffre aléatoire entre 0 et 100
                        if a<=p.esquives or p.bloquerattaque or isobstacle(p.posX,p.posY,self.posX,self.posY,objsmap): #on vérifie si le le personnage attaqué a esquivé ou n'est pas en train de bloquer l'attaque ou qu'il n'y ait pas d'obstacle entre les personnages
                            print("l'attaque est évitée") #on affiche "l'attaque est évitée" si le personnage attaqué à esquivé
                        else: #si le personnage attaqué n'a pas esquivé
                            dgts=self.attaque1[1] #on assigne à la valeur dgts les dégats de l'attaque 1
                            if p.bouclier > 0: #on vérifie si le bouclier du personnage attaqué est supérieur à zéro
                                if p.bouclier >= dgts: #on vérifie si le bouclier du personnage attaqué est supérieur ou égal au dégats de l'attaque
                                    p.bouclier-=dgts #on enlève au bouclier les dégats de l'attaque
                                    dgts=0 #les dégats de l'attaque on étés absorbés par le bouclier du personnage attqué
                                else: #si le bouclier du personnage
                                    dgts-=p.bouclier #une partie des dégats de l'attaque on étés absorbés par le bouclier du personnage attaqué
                                    p.bouclier=0 #le bouclier ne peux plus absorber de dégats
                            p.vie-=dgts #on enlève à la vie du personnage attaqué les dégats restants
                if self.animactu==None or self.animactu[0]!="att1": #si il n'y a pas d'animation ou une différente de l'animation (attaque 1)
                    self.animactu=["att1",0] #on update l'animation en cour
                    self.image=self.imgs[16] #on update l'image
                elif self.animactu[0]=="att1" and self.animactu[1]==0: #on vérifie l'état de l'animation
                    self.animactu=["att1",1] #on update l'animation en cour
                    self.image=self.imgs[17] #on update l'image
                elif self.animactu[0]=="att1" and self.animactu[1]==1: #on vérifie l'état de l'animation
                    self.animactu=["att1",2] #on update l'animation en cour
                    self.image=self.imgs[18] #on update l'image
                elif self.animactu[0]=="att1" and self.animactu[1]==2: #on vérifie l'état de l'animation
                    self.animactu=["att1",0] #on update l'animation en cour
                    self.image=self.imgs[16] #on update l'image
        elif aa=="Attaque2": #Attaque 2
            if time.time()-self.datt2 >= self.attaque2[2]: #on vérifie que le temps qu'il y a entre la derniere fois que le personnage a attaqué avec l'attaque 2 et maintenant est supérieur ou égal au temps minimum
                self.bloquerattaque=False #le personnage ne bloque plus les attaques
                self.datt2=time.time() #mise à jour de la variable (derniere fois attaque 2)
                for p in prs: #boucle qui retourne tous les personages
                    if p!=self and dsit(p.posX,p.posY,self.posX,self.posY) <= self.attaque2[1]: #on vérifie que le personnage n'est pas celui qui attaque et que la distance entre les deux persos est inférieure à la portée de l'attaque
                        a=random.randint(0,100) #on prend un chiffre aléatoire entre 0 et 100
                        if a<=p.esquives or p.bloquerattaque or isobstacle(p.posX,p.posY,self.posX,self.posY,objsmap): #on vérifie si le le personnage attaqué a esquivé ou n'est pas en train de bloquer l'attaque ou qu'il n'y ait pas d'obstacle entre les personnages
                            print("l'attaque est évitée") #on affiche "l'attaque est évitée" si le personnage attaqué à esquivé
                        else: #si le personnage attaqué n'a pas esquivé
                            dgts=self.attaque2[1] #on assigne à la valeur dgts les dégats de l'attaque 2
                            if p.bouclier > 0: #on vérifie si le bouclier du personnage attaqué est supérieur à zéro
                                if p.bouclier >= dgts: #on vérifie si le bouclier du personnage attaqué est supérieur ou égal au dégats de l'attaque
                                    p.bouclier-=dgts #on enlève au bouclier les dégats de l'attaque
                                    dgts=0 #les dégats de l'attaque on étés absorbés par le bouclier du personnage attqué
                                else: #si le bouclier du personnage
                                    dgts-=p.bouclier #une partie des dégats de l'attaque on étés absorbés par le bouclier du personnage attaqué
                                    p.bouclier=0 #le bouclier ne peux plus absorber de dégats
                            p.vie-=dgts #on enlève à la vie du personnage attaqué les dégats restants
                if self.animactu==None or self.animactu[0]!="att2": #si il n'y a pas d'animation ou une différente de l'animation (attaque 2)
                    self.animactu=["att2",0] #on update l'animation en cour
                    self.image=self.imgs[20] #on update l'image
                elif self.animactu[0]=="att2" and self.animactu[1]==0: #on vérifie l'état de l'animation
                    self.animactu=["att2",1] #on update l'animation en cour
                    self.image=self.imgs[21] #on update l'image
                elif self.animactu[0]=="att2" and self.animactu[1]==1: #on vérifie l'état de l'animation
                    self.animactu=["att2",2] #on update l'animation en cour
                    self.image=self.imgs[22] #on update l'image
                elif self.animactu[0]=="att2" and self.animactu[1]==2: #on vérifie l'état de l'animation
                    self.animactu=["att2",0] #on update l'animation en cour
                    self.image=self.imgs[20] #on update l'image
        elif aa=="Attaque3": #Attaque 3
            if time.time()-self.datt3 >= self.attaque3[2]: #on vérifie que le temps qu'il y a entre la derniere fois que le personnage a attaqué avec l'attaque 3 et maintenant est supérieur ou égal au temps minimum
                self.bloquerattaque=False #le personnage ne bloque plus les attaques
                self.datt1=time.time() #mise à jour de la variable (derniere fois attaque 3)
                for p in prs: #boucle qui retourne tous les personages
                    if p!=self and dsit(p.posX,p.posY,self.posX,self.posY) <= self.attaque3[1]: #on vérifie que le personnage n'est pas celui qui attaque et que la distance entre les deux persos est inférieure à la portée de l'attaque
                        a=random.randint(0,100) #on prend un chiffre aléatoire entre 0 et 100
                        if a<=p.esquives or p.bloquerattaque or isobstacle(p.posX,p.posY,self.posX,self.posY,objsmap): #on vérifie si le le personnage attaqué a esquivé ou n'est pas en train de bloquer l'attaque ou qu'il n'y ait pas d'obstacle entre les personnages
                            print("l'attaque est évitée") #on affiche "l'attaque est évitée" si le personnage attaqué à esquivé
                        else: #si le personnage attaqué n'a pas esquivé
                            dgts=self.attaque3[1] #on assigne à la valeur dgts les dégats de l'attaque 1
                            if p.bouclier > 0: #on vérifie si le bouclier du personnage attaqué est supérieur à zéro
                                if p.bouclier >= dgts: #on vérifie si le bouclier du personnage attaqué est supérieur ou égal au dégats de l'attaque
                                    p.bouclier-=dgts #on enlève au bouclier les dégats de l'attaque
                                    dgts=0 #les dégats de l'attaque on étés absorbés par le bouclier du personnage attqué
                                else: #si le bouclier du personnage
                                    dgts-=p.bouclier #une partie des dégats de l'attaque on étés absorbés par le bouclier du personnage attaqué
                                    p.bouclier=0 #le bouclier ne peux plus absorber de dégats
                            p.vie-=dgts #on enlève à la vie du personnage attaqué les dégats restants
                if self.animactu==None or self.animactu[0]!="att3": #si il n'y a pas d'animation ou une différente de l'animation (attaque 3)
                    self.animactu=["att3",0] #on update l'animation en cour
                    self.image=self.imgs[24] #on update l'image
                elif self.animactu[0]=="att3" and self.animactu[1]==0: #on vérifie l'état de l'animation
                    self.animactu=["att3",1] #on update l'animation en cour
                    self.image=self.imgs[25] #on update l'image
                elif self.animactu[0]=="att3" and self.animactu[1]==1: #on vérifie l'état de l'animation
                    self.animactu=["att3",2] #on update l'animation en cour
                    self.image=self.imgs[26] #on update l'image
                elif self.animactu[0]=="att3" and self.animactu[1]==2: #on vérifie l'état de l'animation
                    self.animactu=["att3",0] #on update l'animation en cour
                    self.image=self.imgs[24] #on update l'image
        elif aa=="Defence": #Défence
            self.bloquerattaque=True # le personnage bloque les attaques
            if self.animactu==None or self.animactu[0]!="def": #si il n'y a pas d'animation ou une différente de l'animation (defence)
                self.animactu=["def",0] #on update l'animation en cour
                self.image=self.imgs[13] #on update l'image
            elif self.animactu[0]=="def" and self.animactu[1]==0: #on vérifie l'état de l'animation
                self.animactu=["def",1] #on update l'animation en cour
                self.image=self.imgs[14] #on update l'image
            elif self.animactu[0]=="def" and self.animactu[1]==1: #on vérifie l'état de l'animation
                self.animactu=["def",2] #on update l'animation en cour
                self.image=self.imgs[15] #on update l'image
            elif self.animactu[0]=="def" and self.animactu[1]==2: #on vérifie l'état de l'animation
                self.animactu=["def",0] #on update l'animation en cour
                self.image=self.imgs[13] #on update l'image
    
def affichage_jeu_fen(fenetre,fenx,feny,fentx,fenty,mape,imgmape,objsmap,prs,perso,t,bonus):
    pygame.draw.rect(fenetre,(0,0,0),(fenx,feny,fentx,fenty),0)
    for o in objsmap:
        if o.image != None and o.posX >= perso.cam[0] and o.posX <= perso.cam[0]+fentx and o.posY >= perso.cam[1] and o.posY <= perso.cam[1]+fenty:
            fenetre.blit(o.image,[o.posX+perso.cam[0],o.posY+perso.cam[1]])
    for x in range( int(perso.cam[0]/t) , int((perso.cam[0]+fentx)/t) ):
        for y in range( int(perso.cam[1]/t) , int((perso.cam[1]+fenty)/t) ):
            if x >= 0 and x < mape.shape[0]-1 and y >= 0 and y < mape.shape[1]-1:
                fenetre.blit(imgmape[mape[x,y]],[x*t+perso.cam[0],y*t+perso.cam[1]])
    for p in prs:
        if p!=None:
            if p.posX+p.tx >= perso.cam[0] and p.posX-p.tx <= perso.cam[0]+fentx and p.posY+p.ty >= perso.cam[1] and p.posY-p.ty <= perso.cam[1]+fenty:
                fenetre.blit(p.image,[perso.cam[0]+p.posX,perso.cam[1]+p.posY])
    for b in bonus:
        if b.posX >= perso.cam[0] and b.posX <= perso.cam[0]+fentx and b.posY >= perso.cam[1] and b.posY <= perso.cam[1]+fenty:
            fenetre.blit(b.image,[perso.cam[0]+b.posX,perso.cam[1]+b.posY])
    pygame.draw.rect(fenetre,(int(perso.vie/perso.vie_totale*255.0),0,0),(fenx+50,feny+15,int(perso.vie/perso.vie_totale*float(fentx-100.0)),35),0)
    pygame.draw.rect(fenetre,(0,0,0),(fenx+50,feny+15,int(fentx-100),35),2)
    pygame.draw.rect(fenetre,(0,0,int(perso.bouclier/perso.bouclier_total*255.0)),(fenx+50,feny+60,int(perso.vie/perso.vie_totale*float(fentx-100.0)),5),0)
    pygame.draw.rect(fenetre,(0,0,0),(fenx+50,feny+60,int(fentx-100),5),1)
    pygame.display.update()














