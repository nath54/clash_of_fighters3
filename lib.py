#coding:utf-8
#!/bin/python3
#lib.py
import random,pygame,time,numpy,math #on importe les librairies random , pygame , time , numpy et math
from pygame.locals import * #on importe tout dans la librairie pygame.locals

dim="images/" #variable dim qui contient le chemin du dossier contenant toutes les images du jeu

pygame.init() #on initialise pygame

btex,btey=1100,900 #variables btex et btey qui contiennent la taille originale de la fenetre de jeu
btx,bty=1280,1024 #variables btx et bty qui contiennent la taille originale de l'écran sur lequel a été programmé le jeu

io = pygame.display.Info() #on récurpère dans la variable io les infos sur l'affichage de l'utilisateur
mtex,mtey=io.current_w,io.current_h #on assigne à mtex et mtey la taille actuelle de l'ecran de l'ordinateur
tex,tey=int(btex/btx*mtex),int(btey/bty*mtey) #avec les données ci-dessus on calcule la taille de la fenetre du jeu pour qu'elle soit adaptée à l'écran de l'utilisateur

fenetre=pygame.display.set_mode([tex,tey]) #on crée la fenetre du jeu qu'on assigne à la variable fenetre
pygame.display.set_caption("Clash Of Fighters 3") #on nomme la fenetre du jeu "Clash Of Fighters 3"
pygame.key.set_repeat(40,30) #on autorise la répétition des touches du clavier

def rx(x): return int(x*btex/tex) #fonction rx qui retourne une adaptation de x en fonction de la taille de la fenetre du jeu de l'utilisateur
def ry(y): return int(y*btey/tey) #fonction ry qui retourne une adaptation de y en fonction de la taille de la fenetre du jeu de l'utilisateur
def button(x,y,tx,ty,cl,clb): #fonction bouton qui retourne un bouton
    b=pygame.draw.rect(fenetre,cl,(rx(x),ry(y),rx(tx),ry(ty)),0) #crée dans la variable b le fond du bouton
    pygame.draw.rect(fenetre,clb,(rx(x),ry(y),rx(tx),ry(ty)),1) #dessine le contour du bouton
    return b #retourne la variable b contenant le fond du bouton qui est cliquable
def pretexte(txt,t,cl): return pygame.font.SysFont("Serif",ry(t)).render(txt,t,cl) #fonction qui prépare le texte qui va être affiché
def atexte(pretxt,x,y): fenetre.blit( pretxt , [rx(x),ry(y)]) #fonction qui affiche le texte déjà préparé
def texte(txt,x,y,t,cl): fenetre.blit( pygame.font.SysFont("Serif",ry(t)).render(txt,t,cl) , [rx(x),ry(y)]) #fonction texte qui écrit un texte à l'ecran
def dist(x1,y1,x2,y2): return int(math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))) #fonction dist qui retourne la distance entre deoux points

#liste emaps qui contient toutes les données des éléments de la mape

emaps=[ ["herbe",True,"herbe.png"] , ["terre",True,"terre.png"] ]
#0=nom , 1=pmd

imgrandom=pygame.transform.scale(pygame.image.load("images/random.png"),[rx(100),ry(100)])

#liste persos qui contient toutes les données des personnages
persos=[  [ "jarry",1000,100,20,5,[35,350,1,[],15,"coup de pistolet",2],[20,70,0.7,[],5,"coup de poing",2],[250,250,50,[],50,"lasers dans le sol qui ressortent au niveau de l'ennemi",8],pygame.transform.scale(pygame.image.load(dim+"jarry_portrait.png"),[rx(100),ry(100)]),["sa portée augmente de 20","portée+",20,20]]
          ,["bismak",2000,200,10,3,[50,100,1.2,[],15,"coup d'épée",5],[50,100,1.2,[],15,"coup d'épée",5],[200,150,45,[],75,"super coup d'épée",5],pygame.transform.scale(pygame.image.load(dim+"bismak_portrait.png"),[rx(100),ry(100)]),["il inflige plus de degats","degats+",5,15]]
          ,["fantom",500,50,30,80,[2,70,0.2,[],10,"griffes",5],[25,60,2,[],20,"morsure",5],[60,500,30,[],50,"cri strident",5],pygame.transform.scale(pygame.image.load(dim+"fantom_portrait.png"),[rx(100),ry(100)]),["il devient plus rapide","vitesse+",1,15]]
          ,["savant_fou",850,300,18,8,[15,500,0.8,[],15,"pistolets",3],[25,500,5,["teletransportation"],18,"pistolets+teletransportation",5],[150,500,40,["teletransportation"],50,"super pistolets + teletransportation",3],pygame.transform.scale(pygame.image.load(dim+"savant_fou_portrait.png"),[rx(100),ry(100)]),["il se teletransporte","teletransportation+",1,7]]
          ,["guarde",100,1000,15,5,[35,80,1.5,[],10,"coup de lance",3],[50,60,3,["assomme"],15,"coup de bouclier",5],[30,300,2,[],5,"javelot",10],pygame.transform.scale(pygame.image.load(dim+"guarde_portrait.png"),[rx(100),ry(100)]),["regen bouclier","bouclier++",1,35]]
          #,["",0,0,0,0,[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],pygame.transform.scale(pygame.image.load(dim+".png"),[rx(100),ry(100)]),[]]
          #,["",0,0,0,0,[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],pygame.transform.scale(pygame.image.load(dim+".png"),[rx(100),ry(100)]),[]]
          #,["",0,0,0,0,[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],pygame.transform.scale(pygame.image.load(dim+".png"),[rx(100),ry(100)]),[]]
          #,["",0,0,0,0,[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],pygame.transform.scale(pygame.image.load(dim+".png"),[rx(100),ry(100)]),[]]
          #,["",0,0,0,0,[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],pygame.transform.scale(pygame.image.load(dim+".png"),[rx(100),ry(100)]),[]]
          #,["",0,0,0,0,[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],pygame.transform.scale(pygame.image.load(dim+".png"),[rx(100),ry(100)]),[]]
          #,["",0,0,0,0,[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],pygame.transform.scale(pygame.image.load(dim+".png"),[rx(100),ry(100)]),[]]
          #,["",0,0,0,0,[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],pygame.transform.scale(pygame.image.load(dim+".png"),[rx(100),ry(100)]),[]]
          #,["",0,0,0,0,[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],pygame.transform.scale(pygame.image.load(dim+".png"),[rx(100),ry(100)]),[]]
          #,["",0,0,0,0,[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],pygame.transform.scale(pygame.image.load(dim+".png"),[rx(100),ry(100)]),[]]
          #,["",0,0,0,0,[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],pygame.transform.scale(pygame.image.load(dim+".png"),[rx(100),ry(100)]),[]]
          #,["",0,0,0,0,[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],pygame.transform.scale(pygame.image.load(dim+".png"),[rx(100),ry(100)]),[]]
          #,["",0,0,0,0,[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],pygame.transform.scale(pygame.image.load(dim+".png"),[rx(100),ry(100)]),[]]
          #,["",0,0,0,0,[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],pygame.transform.scale(pygame.image.load(dim+".png"),[rx(100),ry(100)]),[]]
          #,["",0,0,0,0,[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],[0,0,0,[],0,"",None],pygame.transform.scale(pygame.image.load(dim+".png"),[rx(100),ry(100)]),[]]
          ]
#0=nom , 1=vie , 2=bouclier , 3=rapidité , 4=%esquive , 5=attaque 1 , 6=attaque 2 , 7=attaque 3(spécial) , 8=img portrait prechargé menu , 9=special
#attaque : 0=degats , 1=portee(pixels) , 2=temps (sec) , 3=effets , 4=%coup critique(x2 dégats) , 5=description , 6=image effet
#special : 0=description , 1=id , 2=effet , 3=temps

bonus=[ ["bouclier1","bouclier+",50,pygame.transform.scale(pygame.image.load("images/bouclier1.png")                    ,[rx(50),ry(50)]),10]
       ,["bouclier1","bouclier+",100,pygame.transform.scale(pygame.image.load("images/bouclier2.png")                   ,[rx(50),ry(50)]),5]
       ,["bouclier1","bouclier++",1,pygame.transform.scale(pygame.image.load("images/bouclier3.png")                    ,[rx(50),ry(50)]),1]
       ,["vie1","vie+",50,pygame.transform.scale(pygame.image.load("images/vie1.png")                                   ,[rx(50),ry(50)]),3]
       ,["vie2","vie+",100,pygame.transform.scale(pygame.image.load("images/vie2.png")                                  ,[rx(50),ry(50)]),2]
       ,["vie3","vie++",1,pygame.transform.scale(pygame.image.load("images/vie3.png")                                   ,[rx(50),ry(50)]),1]
       ,["+att dégats1","att_degats+",3,pygame.transform.scale(pygame.image.load("images/att_degats1.png")              ,[rx(50),ry(50)]),6]
       ,["+att dégats2","att_degats+",10,pygame.transform.scale(pygame.image.load("images/att_degats2.png")             ,[rx(50),ry(50)]),2]
       ,["+vitesse1","vitesse+",1,pygame.transform.scale(pygame.image.load("images/vitesse1.png")                       ,[rx(50),ry(50)]),4]
       ,["+vitesse2","vitesse+",3,pygame.transform.scale(pygame.image.load("images/vitesse2.png")                       ,[rx(50),ry(50)]),2]
       ,["portail magique","teletransportation",1,pygame.transform.scale(pygame.image.load("images/portail.png")        ,[rx(50),ry(50)]),10]
       ,["cape invisibilite","invisibilite",15,pygame.transform.scale(pygame.image.load("images/cape.png")              ,[rx(50),ry(50)]),3]
       ,["potion invincibilite","invincibilite",10,pygame.transform.scale(pygame.image.load("images/pot_invinc.png")    ,[rx(50),ry(50)]),5]
       ,["potion affaiblissement","affaiblissement",10,pygame.transform.scale(pygame.image.load("images/pot_aff.png")   ,[rx(50),ry(50)]),10]
       ,["grappin","teletransportation_to_ennemi",1,pygame.transform.scale(pygame.image.load("images/grappin.png")      ,[rx(50),ry(50)]),10]
       ,["brouillard de guerre","brouillard",7.5,pygame.transform.scale(pygame.image.load("images/brouillard.png")      ,[rx(50),ry(50)]),10]
       ,["potion de degats","-degats",25,pygame.transform.scale(pygame.image.load("images/pot_degats.png")              ,[rx(50),ry(50)]),10]
       ,["potion d'agilité","esquive+",2,pygame.transform.scale(pygame.image.load("images/pot_agil.png")                ,[rx(50),ry(50)]),6]
      ]

bns=[]
for b in bonus:
    for x in range(b[4]): bns.append(b)

#0=nom , 1=effet , 2=valeur effet , 3=image , 4=probabilite

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
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_special1.png"),[t,t])) #on ajoute l'image nom+"_special1.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_special2.png"),[t,t])) #on ajoute l'image nom+"_special2.png" à la liste
    lst.append(pygame.transform.scale(pygame.image.load(dim+nom+"_special3.png"),[t,t])) #on ajoute l'image nom+"_special3.png" à la liste
    return lst #on retourne la liste

def isobstacle(x1,y1,x2,y2,lo): #fonction isobstacle qui retourne si il y a un obstacle entre deux points
    d=pygame.draw.line(fenetre,(0,0,0),(x1,y1),(x2,y2),1) #on récupère dans la variable d le rect de la ligne qui part de (x1,y1) et qui va a (x2,y2)
    c=False #on inititalise la variable c
    for o in lo: #on parcoure tous les obstacles
        if d.colliderect(o.rect): c=True #si le rect d rentre en collision avec un obstacle, la variable c est vraie
    return c #on retourne la variable c qui contient si il y a un obstacle ou pas

def peutbouger(perso,objsmap,mape,t):
    r=pygame.Rect(perso.posX,perso.posY,perso.tx,perso.ty)
    c=True
    for o in objsmap:
        if r.colliderect(o.rect): c=False
    if perso.posX <= 0: c=False
    if perso.posX >= mape.shape[0]*t-2*t: c=False
    if perso.posY <= 0: c=False
    if perso.posY >= mape.shape[1]*t-2*t: c=False
    return c

class Perso(): #classe personnage
    def update_cam(self):
        self.cam=[-self.posX+self.ftx/2,-self.posY+self.fty/2] #liste cam qui contient les coordonnées de la caméra du personnage
    def __init__(self,p,x,y,t,fx,fy,ftx,fty): #fonction initialisation du personnage
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
        self.special=persos[p][9]
        self.dspec=time.time()
        self.posX=x #variable posX qui contient la position x du personnage
        self.posY=y #variable posY qui contient la position y du personnage
        self.tx=t #variable tx qui contient la taille x du personnage
        self.ty=t #variable ty qui contient la taille y du personnage
        self.fx=fx #variable fx qui contient la position x de la fenetre du personnage
        self.fy=fy #variable fy qui contient la position y de la fenetre du personnage
        self.ftx=ftx #variable ftx qui contient la taille x de la fenetre du personnage
        self.fty=fty #variable fty qui contient la taille y de la fenetre du personnage
        self.update_cam()
        self.imgs=loadimgprs(self.nom,t) #liste imgs qui contient toutes les images du personnage
        #0=normal , 1=haut(1) , 2=haut(2) , 3=haut(3) , 4=bas(1) , 5=bas(2) , 6=bas(3) , 7=gauche(1) , 8=gauche(2) , 9=gauche(3)
        #10=droite(1) , 11=droite(2) , 12=droite(3) , 13=defence(1) , 14=defence(2) , 15=defence(3)  , 16=att1(1) , 17=att1(2) , 18=att1(3)
        #19=effets att1 , 20=att2(1) , 21=att2(2) , 22=att2(3) , 23=effets att2 , 24=att3(1) , 25=att3(2) , 26=att3(3) , 27=effets att3
        #28=mort , 29=icon , 30=portrait
        self.image=self.imgs[0] #variable image qui contient l'image qui va etre affichée
        self.image_effet=None #variable image_effet qui contient les effets subis par le personnage
        self.animactu=None #liste animactu qui contient l'animation du personnage en cour
        self.tpsbouger=0.01 #variable tpsbouger qui contient le temps que le personnage va mettre entre chaque mouvement
        self.dbouger=time.time() #variable dbouger qui contient le temps où le personnage a bougé pour la derniere fois
        self.bloquerattaque=False #variable bloquerattaque qui dit si le personnage est en train de bloquer les attaques ou pas
        self.tpef=time.time() #variable tpef qui indique le temps où le personnage a subit pour la derniere fois un effet(attaques)
        self.hist_degats_texte=[] #liste hist_degats_texte qui contient tous les textes qui sont affichés en haut à droite du personnage (ex : -50dg , esquive , bloqué)
        self.hist_bonus_texte=[] #liste hist_bonus_texte qui contient tous les textes qui sont affichés en haut à gauche du personnage ( ex : +50 pv , +50bc )
        self.drdgts=time.time() #variable drdgts qui contient le temps où le personnage a encaissé des dégats pour la dernière fois
        self.cible=None #variable cible contennant la cible du perso (NE SERT QUE POUR LES BOTS)
        self.etat=[]
        self.tpsrestant_etat=[]
        self.dtpsetat=time.time()
        self.dernier_attaque=[]
    def bouger(self,aa,objsmap,prs,mape,t): #fonction bouger du personnage qui permet au personnage de bouger, d'attaquer et de parer les coups de l'adversaire
        if aa=="Up": #bouger vers le haut
            if time.time()-self.dbouger >= self.tpsbouger and self.vie>0 : #on vérifie que le temps qu'il y a entre la derniere fois que le personnage a bougé et maintenant est supérieur ou égal au temps minimum
                self.bloquerattaque=False #le personnage ne bloque plus les attaques
                self.dbouger=time.time() #mise à jour de la variable (derniere fois bouger)
                vit=self.vitesse
                if "ralentit" in self.etat: vit=int(vit/2)
                if "rapide" in self.etat: vit*=2
                self.posY-=vit #on bouge le personnage
                self.cam[1]+=vit #on bouge la camera
                if not peutbouger(self,objsmap,mape,t): #on vérifie si le perso peut bouger (collisions avec les objets de la map)
                    self.posY+=vit+1 #si le perso rentre en collision avec un autre objet de la map, il rebondit
                    self.cam[1]-=vit+1 #on bouge la camera
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
            if time.time()-self.dbouger >= self.tpsbouger and self.vie>0 : #on vérifie que le temps qu'il y a entre la derniere fois que le personnage a bougé et maintenant est supérieur ou égal au temps minimum
                self.bloquerattaque=False #le personnage ne bloque plus les attaques
                self.dbouger=time.time() #mise à jour de la variable (derniere fois bouger)
                vit=self.vitesse
                if "ralentit" in self.etat: vit=int(vit/2)
                if "rapide" in self.etat: vit*=2
                self.posY+=vit #on bouge le personnage
                self.cam[1]-=vit #on bouge la camera
                if not peutbouger(self,objsmap,mape,t): #on vérifie si le perso peut bouger (collisions avec les objets de la map)
                    self.posY-=vit+1 #si le perso rentre en collision avec un autre objet de la map, il rebondit
                    self.cam[1]+=vit+1 #on bouge la camera
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
            if time.time()-self.dbouger >= self.tpsbouger and self.vie>0 : #on vérifie que le temps qu'il y a entre la derniere fois que le personnage a bougé et maintenant est supérieur ou égal au temps minimum
                self.bloquerattaque=False #le personnage ne bloque plus les attaques
                self.dbouger=time.time() #mise à jour de la variable (derniere fois bouger)
                vit=self.vitesse
                if "ralentit" in self.etat: vit=int(vit/2)
                if "rapide" in self.etat: vit*=2
                self.posX-=vit #on bouge le personnage
                self.cam[0]+=vit #on bouge la camera
                if not peutbouger(self,objsmap,mape,t): #on vérifie si le perso peut bouger (collisions avec les objets de la map)
                    self.posX+=vit+1 #si le perso rentre en collision avec un autre objet de la map, il rebondit
                    self.cam[0]-=vit+1 #on bouge la camera
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
            if time.time()-self.dbouger >= self.tpsbouger and self.vie>0 : #on vérifie que le temps qu'il y a entre la derniere fois que le personnage a bougé et maintenant est supérieur ou égal au temps minimum
                self.bloquerattaque=False #le personnage ne bloque plus les attaques
                self.dbouger=time.time() #mise à jour de la variable (derniere fois bouger)
                vit=self.vitesse
                if "ralentit" in self.etat: vit=int(vit/2)
                if "rapide" in self.etat: vit*=2
                self.posX+=vit #on bouge le personnage
                self.cam[0]-=vit #on bouge la camera
                if not peutbouger(self,objsmap,mape,t): #on vérifie si le perso peut bouger (collisions avec les objets de la map)
                    self.posX-=vit+1 #si le perso rentre en collision avec un autre objet de la map, il rebondit
                    self.cam[0]+=vit+1 #on bouge la camera
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
        elif aa=="Att1": #Attaque 1
            attres=False
            if time.time()-self.datt1 >= self.attaque1[2] and self.vie>0: #on vérifie que le temps qu'il y a entre la derniere fois que le personnage a attaqué avec l'attaque 1 et maintenant est supérieur ou égal au temps minimum
                self.bloquerattaque=False #le personnage ne bloque plus les attaques
                self.datt1=time.time() #mise à jour de la variable (derniere fois attaque 1)
                for p in prs: #boucle qui retourne tous les personages
                    if  p!=None and p!=self and p.vie>0  and dist(p.posX,p.posY,self.posX,self.posY) <= self.attaque1[1]: #on vérifie que le personnage n'est pas celui qui attaque et que la distance entre les deux persos est inférieure à la portée de l'attaque
                        a=random.randint(0,100) #on prend un chiffre aléatoire entre 0 et 100
                        if a<=p.esquive or ( p.bloquerattaque and p.bouclier > 0 ) or isobstacle(p.posX,p.posY,self.posX,self.posY,objsmap) and not "invincible" in p.etat: #on vérifie si le le personnage attaqué a esquivé ou n'est pas en train de bloquer l'attaque ou qu'il n'y ait pas d'obstacle entre les personnages
                            if p.bloquerattaque:
                                p.hist_degats_texte.append( ["bloqué",0] )
                                p.bouclier-=1
                                p.drgts=time.time()
                                p.bloquerattaque=False
                                p.image=p.imgs[0]
                            elif a<=p.esquive: p.hist_degats_texte.append( ["esquivé",0])
                            elif "invincible" in p.etat: p.hist_degats_texte.append( ["invincible",0])
                        else: #si le personnage attaqué n'a pas esquivé
                            dgts=self.attaque1[0] #on assigne à la valeur dgts les dégats de l'attaque 1
                            if "affaibli" in p.etat: dgts*=1.5
                            p.hist_degats_texte.append( ["-"+str(dgts)+"dg",0] )
                            if p.bouclier > 0: #on vérifie si le bouclier du personnage attaqué est supérieur à zéro
                                if p.bouclier >= dgts: #on vérifie si le bouclier du personnage attaqué est supérieur ou égal au dégats de l'attaque
                                    p.bouclier-=dgts #on enlève au bouclier les dégats de l'attaque
                                    dgts=0 #les dégats de l'attaque on étés absorbés par le bouclier du personnage attqué
                                else: #si le bouclier du personnage
                                    dgts-=p.bouclier #une partie des dégats de l'attaque on étés absorbés par le bouclier du personnage attaqué
                                    p.bouclier=0 #le bouclier ne peux plus absorber de dégats
                            for e in self.attaque1[3]: #on applique les effets de l'attaque
                                if e=="teletransportation":
                                    p.posX,p.posY=random.randint(100,(mape.shape[0]*t)-200),random.randint(100,(mape.shape[1]*t)-200)
                                    p.update_cam()
                                    p.hist_degats_texte.append( ["teletransporté",0] )
                                if e=="drain":
                                    self.vie+=dgts
                                    self.hist_bonus_texte.append( ["+"+str(dgts)+" pv",0] )
                                    if self.vie>self.vie_totale: self.vie=self.vie_totale
                                    p.hist_degats_texte.append( ["drainé",0] )
                            p.vie-=dgts #on enlève à la vie du personnage attaqué les dégats restants
                            if p.vie<=0: p.image=p.imgs[28]
                            if self.attaque1[6]!=None: p.image_effet,p.tpef=[self.imgs[19],self.attaque1[6]],time.time()
                            p.drdgts=time.time()
                            attres=True
            if self.animactu==None or self.animactu[0]!="att1": #si il n'y a pas d'animation ou une différente de l'animation (attaque 1)
                self.animactu=["att1",0] #on update l'animation en cour
                self.image=self.imgs[16] #on update l'image
            elif self.animactu[0]=="att1" and self.animactu[1]==0: #on vérifie l'état de l'animation
                self.animactu=["att1",1] #on update l'animation en cour
                self.image=self.imgs[17] #on update l'image
            elif self.animactu[0]=="att1" and self.animactu[1]==1: #on vérifie l'état de l'animation
                self.animactu=["att1",2] #on update l'animation en cour
                self.image=self.imgs[18] #on update l'image
            elif self.animactu[0]=="att1" and self.animactu[1]==2 and attres: #on vérifie l'état de l'animation
                self.animactu=["att1",0] #on update l'animation en cour
                self.image=self.imgs[16] #on update l'image
        elif aa=="Att2": #Attaque 2
            attres=False
            if time.time()-self.datt2 >= self.attaque2[2] and self.vie>0: #on vérifie que le temps qu'il y a entre la derniere fois que le personnage a attaqué avec l'attaque 2 et maintenant est supérieur ou égal au temps minimum
                self.bloquerattaque=False #le personnage ne bloque plus les attaques
                self.datt2=time.time() #mise à jour de la variable (derniere fois attaque 2)
                for p in prs: #boucle qui retourne tous les personages
                    if p!=None and  p!=self and p.vie>0  and dist(p.posX,p.posY,self.posX,self.posY) <= self.attaque2[1]: #on vérifie que le personnage n'est pas celui qui attaque et que la distance entre les deux persos est inférieure à la portée de l'attaque
                        a=random.randint(0,100) #on prend un chiffre aléatoire entre 0 et 100
                        if a<=p.esquive or ( p.bloquerattaque and p.bouclier > 0) or isobstacle(p.posX,p.posY,self.posX,self.posY,objsmap) and not "invincible" in p.etat: #on vérifie si le le personnage attaqué a esquivé ou n'est pas en train de bloquer l'attaque ou qu'il n'y ait pas d'obstacle entre les personnages
                            if p.bloquerattaque:
                                p.hist_degats_texte.append( ["bloqué",0] )
                                p.bouclier-=1
                                p.drgts=time.time()
                                p.bloquerattaque=False
                                p.image=p.imgs[0]
                            elif a<=p.esquive: p.hist_degats_texte.append( ["esquivé",0])
                            elif "invincible" in p.etat: p.hist_degats_texte.append( ["invincible",0])
                        else: #si le personnage attaqué n'a pas esquivé
                            dgts=self.attaque2[0] #on assigne à la valeur dgts les dégats de l'attaque 2
                            if "affaibli" in p.etat: dgts*=1.5
                            p.hist_degats_texte.append( ["-"+str(dgts)+"dg",0] )
                            if p.bouclier > 0: #on vérifie si le bouclier du personnage attaqué est supérieur à zéro
                                if p.bouclier >= dgts: #on vérifie si le bouclier du personnage attaqué est supérieur ou égal au dégats de l'attaque
                                    p.bouclier-=dgts #on enlève au bouclier les dégats de l'attaque
                                    dgts=0 #les dégats de l'attaque on étés absorbés par le bouclier du personnage attqué
                                else: #si le bouclier du personnage
                                    dgts-=p.bouclier #une partie des dégats de l'attaque on étés absorbés par le bouclier du personnage attaqué
                                    p.bouclier=0 #le bouclier ne peux plus absorber de dégats
                            for e in self.attaque2[3]: #on applique les effets de l'attaque
                                if e=="teletransportation":
                                    p.posX,p.posY=random.randint(100,(mape.shape[0]*t)-200),random.randint(100,(mape.shape[1]*t)-200)
                                    p.update_cam()
                                    p.hist_degats_texte.append( ["teletransporté",0] )
                                if e=="drain":
                                    self.vie+=dgts
                                    self.hist_bonus_texte.append( ["+"+str(dgts)+" pv",0] )
                                    if self.vie>self.vie_totale: self.vie=self.vie_totale
                                    p.hist_degats_texte.append( ["drainé",0] )
                            p.vie-=dgts #on enlève à la vie du personnage attaqué les dégats restants
                            if p.vie<=0: p.image=p.imgs[28]
                            if self.attaque2[6]!=None: p.image_effet,p.tpef=[self.imgs[23],self.attaque2[6]],time.time()
                            p.drdgts=time.time()
                            attres=True
            if self.animactu==None or self.animactu[0]!="att2": #si il n'y a pas d'animation ou une différente de l'animation (attaque 2)
                self.animactu=["att2",0] #on update l'animation en cour
                self.image=self.imgs[20] #on update l'image
            elif self.animactu[0]=="att2" and self.animactu[1]==0: #on vérifie l'état de l'animation
                self.animactu=["att2",1] #on update l'animation en cour
                self.image=self.imgs[21] #on update l'image
            elif self.animactu[0]=="att2" and self.animactu[1]==1: #on vérifie l'état de l'animation
                self.animactu=["att2",2] #on update l'animation en cour
                self.image=self.imgs[22] #on update l'image
            elif self.animactu[0]=="att2" and self.animactu[1]==2 and attres: #on vérifie l'état de l'animation
                self.animactu=["att2",0] #on update l'animation en cour
                self.image=self.imgs[20] #on update l'image
        elif aa=="Att3": #Attaque 3
            attres=False
            if time.time()-self.datt3 >= self.attaque3[2] and self.vie>0: #on vérifie que le temps qu'il y a entre la derniere fois que le personnage a attaqué avec l'attaque 3 et maintenant est supérieur ou égal au temps minimum
                self.bloquerattaque=False #le personnage ne bloque plus les attaques
                self.datt3=time.time() #mise à jour de la variable (derniere fois attaque 3)
                for p in prs: #boucle qui retourne tous les personages
                    if p!=None and p!=self and p.vie>0 and dist(p.posX,p.posY,self.posX,self.posY) <= self.attaque3[1]: #on vérifie que le personnage n'est pas celui qui attaque et que la distance entre les deux persos est inférieure à la portée de l'attaque
                        a=random.randint(0,100) #on prend un chiffre aléatoire entre 0 et 100
                        if a<=p.esquive or ( p.bloquerattaque and p.bouclier > 0 ) or isobstacle(p.posX,p.posY,self.posX,self.posY,objsmap) and not "invincible" in p.etat: #on vérifie si le le personnage attaqué a esquivé ou n'est pas en train de bloquer l'attaque ou qu'il n'y ait pas d'obstacle entre les personnages
                            if p.bloquerattaque:
                                p.hist_degats_texte.append( ["bloqué",0] )
                                p.bouclier-=1
                                p.drgts=time.time()
                                p.bloquerattaque=False
                                p.image=p.imgs[0]
                            elif a<=p.esquive: p.hist_degats_texte.append( ["esquivé",0])
                            elif "invincible" in p.etat: p.hist_degats_texte.append( ["invincible",0])
                        else: #si le personnage attaqué n'a pas esquivé
                            dgts=self.attaque3[0] #on assigne à la valeur dgts les dégats de l'attaque 1
                            if "affaibli" in p.etat: dgts*=1.5
                            p.hist_degats_texte.append( ["-"+str(dgts)+"dg",0] )
                            if p.bouclier > 0: #on vérifie si le bouclier du personnage attaqué est supérieur à zéro
                                if p.bouclier >= dgts: #on vérifie si le bouclier du personnage attaqué est supérieur ou égal au dégats de l'attaque
                                    p.bouclier-=dgts #on enlève au bouclier les dégats de l'attaque
                                    dgts=0 #les dégats de l'attaque on étés absorbés par le bouclier du personnage attqué
                                else: #si le bouclier du personnage
                                    dgts-=p.bouclier #une partie des dégats de l'attaque on étés absorbés par le bouclier du personnage attaqué
                                    p.bouclier=0 #le bouclier ne peux plus absorber de dégats
                            for e in self.attaque3[3]: #on applique les effets de l'attaque
                                if e=="teletransportation":
                                    p.posX,p.posY=random.randint(100,(mape.shape[0]*t)-200),random.randint(100,(mape.shape[1]*t)-200)
                                    p.update_cam()
                                    p.hist_degats_texte.append( ["teletransporté",0] )
                                if e=="drain":
                                    self.vie+=dgts
                                    self.hist_bonus_texte.append( ["+"+str(dgts)+" pv",0] )
                                    if self.vie>self.vie_totale: self.vie=self.vie_totale
                                    p.hist_degats_texte.append( ["drainé",0] )
                            p.vie-=dgts #on enlève à la vie du personnage attaqué les dégats restants
                            if p.vie<=0: p.image=p.imgs[28]
                            if self.attaque3[6]!=None: p.image_effet,p.tpef=[self.imgs[27],self.attaque3[6]],time.time()
                            p.drdgts=time.time()
                            attres=True
            if self.animactu==None or self.animactu[0]!="att3": #si il n'y a pas d'animation ou une différente de l'animation (attaque 3)
                self.animactu=["att3",0] #on update l'animation en cour
                self.image=self.imgs[24] #on update l'image
            elif self.animactu[0]=="att3" and self.animactu[1]==0: #on vérifie l'état de l'animation
                self.animactu=["att3",1] #on update l'animation en cour
                self.image=self.imgs[25] #on update l'image
            elif self.animactu[0]=="att3" and self.animactu[1]==1: #on vérifie l'état de l'animation
                self.animactu=["att3",2] #on update l'animation en cour
                self.image=self.imgs[26] #on update l'image
            elif self.animactu[0]=="att3" and self.animactu[1]==2 and attres: #on vérifie l'état de l'animation
                self.animactu=["att3",0] #on update l'animation en cour
                self.image=self.imgs[24] #on update l'image
        elif aa=="Defence": #Défence
            if self.vie>0:
                self.bloquerattaque=True # le personnage bloque les attaques
                if self.animactu==None or (not self.animactu[0]=="def" and self.animactu[1]==2):
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
        elif aa=="Special":
            if time.time()-self.dspec >= self.special[3]:
                self.dspec=time.time()
                if self.special[1]=="degats+":
                    self.attaque1[0]+=self.special[2]
                    self.attaque2[0]+=self.special[2]
                    self.attaque3[0]+=self.special[2]
                    self.hist_bonus_texte.append( ["+"+str(self.special[2])+"dg",0] )
                elif self.special[1]=="portée+":
                    self.attaque1[1]+=self.special[2]
                    self.attaque2[1]+=self.special[2]
                    self.attaque3[1]+=self.special[2]
                    self.hist_bonus_texte.append( ["+"+str(self.special[2])+"portée",0] )
                elif self.special[1]=="temps-":
                    self.attaque1[2]-=self.special[2]
                    self.attaque2[2]-=self.special[2]
                    self.attaque3[2]-=self.special[2]
                    self.hist_bonus_texte.append( ["-"+str(self.special[2])+"temps d'attaque",0] )
                elif self.special[1]=="critique+":
                    self.attaque1[4]-=self.special[4]
                    self.attaque2[4]-=self.special[4]
                    self.attaque3[4]-=self.special[4]
                    self.hist_bonus_texte.append( ["+"+str(self.special[2])+"% critique",0] )
                elif self.special[1]=="rapidite+":
                    self.vitesse+=self.special[2]
                    self.hist_bonus_texte.append( ["+"+str(self.special[2])+" vitesse",0] )
                elif self.special[1]=="esquive+":
                    self.vitesse+=self.special[2]
                    self.hist_bonus_texte.append( ["+"+str(self.special[2])+"dg",0] )
                elif self.special[1]=="bouclier++":
                    self.hist_bonus_texte.append( ["+"+str(self.bouclier_total-self.bouclier)+"bouclier",0] )
                    self.bouclier=self.bouclier_total
                elif self.special[1]=="vie++":
                    self.hist_bonus_texte.append( ["+"+str(self.vie_totale-self.vie)+"dg",0] )
                    self.vie=self.vie_total
                elif self.special[1]=="reset temps attspecial":
                    self.datt3=0
                    self.hist_bonus_texte.append( ["att special",0] )
                elif self.special[1]=="teletransportation+":
                    self.posX,self.posY=random.randint(100,(mape.shape[0]*t)-200),random.randint(100,(mape.shape[1]*t)-200)
                    self.update_cam()
                    self.hist_bonus_texte.append( ["teletransporté",0] )
                elif self.special[1]=="-teletransportation":
                    for p in prs:
                        if p != None:
                            p.posX,p.posY=random.randint(100,(mape.shape[0]*t)-200),random.randint(100,(mape.shape[1]*t)-200)
                            p.update_cam()
                            p.hist_degats_texte.append( ["teletransporté",0] )
                elif self.special[1]=="ralentissement":
                    for p in prs:
                        if p!=None:
                            if p.vitesse>=self.special[2] : p.vitesse-=self.special[2]
                            p.hist_degats_texte.append( ["-"+str(self.special[2])+" vitesse",0] )
                elif self.special[1]=="-degats":
                    for p in prs:
                        if p != None:
                            if p.attaque1[0]>=self.special[2]: p.attaque1[0]-=self.special[2]
                            if p.attaque2[0]>=self.special[2]: p.attaque2[0]-=self.special[2]
                            if p.attaque3[0]>=self.special[2]: p.attaque3[0]-=self.special[2]
                            p.hist_degats_texte.append( ["-"+str(self.special[2])+" dg",0] )
                elif self.special[1]=="-portée":
                    for p in prs:
                        if p!=None:
                            if p.attaque1[1]>=self.special[2]: p.attaque1[1]-=self.special[2]
                            if p.attaque2[1]>=self.special[2]: p.attaque2[1]-=self.special[2]
                            if p.attaque3[1]>=self.special[2]: p.attaque3[1]-=self.special[2]
                            p.hist_degats_texte.append( ["-"+str(self.special[2])+" portée",0] )
                elif self.special[1]=="+temps":
                    for p in prs:
                        if p!=None:
                            if p.attaque1[2]>=self.special[2]: p.attaque1[2]-=self.special[2]
                            if p.attaque2[2]>=self.special[2]: p.attaque2[2]-=self.special[2]
                            if p.attaque3[2]>=self.special[2]: p.attaque3[2]-=self.special[2]
                            p.hist_degats_texte.append( ["+"+str(self.special[2])+" temps att",0] )
                elif self.special[1]=="-critique":
                    for p in prs:
                        if p!=None:
                            if p.attaque1[4]>=self.special[2]: p.attaque1[0]-=self.special[2]
                            if p.attaque2[4]>=self.special[2]: p.attaque2[0]-=self.special[2]
                            if p.attaque3[4]>=self.special[2]: p.attaque3[0]-=self.special[2]
                            p.hist_degats_texte.append( ["-"+str(self.special[2])+" % critique",0] )
            if self.animactu==None or self.animactu[0]!="special": #si il n'y a pas d'animation ou une différente de l'animation (defence)
                self.animactu=["special",0] #on update l'animation en cour
                self.image=self.imgs[3] #on update l'image
            elif self.animactu[0]=="special" and self.animactu[1]==0: #on vérifie l'état de l'animation
                self.animactu=["special",1] #on update l'animation en cour
                self.image=self.imgs[32] #on update l'image
            elif self.animactu[0]=="special" and self.animactu[1]==1: #on vérifie l'état de l'animation
                self.animactu=["special",2] #on update l'animation en cour
                self.image=self.imgs[33] #on update l'image
            elif self.animactu[0]=="special" and self.animactu[1]==2: #on vérifie l'état de l'animation
                self.animactu=["special",0] #on update l'animation en cour
                self.image=self.imgs[31] #on update l'image

class Objet:
    def __init__(self,tp,x,y):
        self.nom=tp[0]
        self.tp_effet=tp[1]
        self.effet=tp[2]
        self.image=tp[3]
        self.delete=False
        self.rect=pygame.Rect(x,y,rx(50),ry(50))
        self.posX=x
        self.posY=y
    def util(self,perso,prs,mape,t):
        if self.tp_effet=="bouclier+":
            perso.bouclier+=self.effet
            if perso.bouclier>perso.bouclier_total: perso.bouclier=perso.bouclier_total
            perso.hist_bonus_texte.append( ["bouclier +"+str(self.effet),0] )
        elif self.tp_effet=="bouclier++":
            perso.bouclier=perso.bouclier_total
            perso.hist_bonus_texte.append( ["bouclier rempli",0] )
        elif self.tp_effet=="vie+":
            perso.vie+=self.effet
            if perso.vie>perso.vie_totale: perso.vie=perso.vie_totale
            perso.hist_bonus_texte.append( ["vie +"+str(self.effet)+"pv",0] )
        elif self.tp_effet=="vie++":
            perso.vie=perso.vie_totale
            perso.hist_bonus_texte.append( ["guéri",0] )
        elif self.tp_effet=="att_degats+":
            perso.attaque1[0]+=self.effet
            perso.attaque2[0]+=self.effet
            perso.attaque3[0]+=self.effet
            perso.hist_bonus_texte.append( ["att +"+str(self.effet)+" dgts",0] )
        elif self.tp_effet=="vitesse+":
            perso.vitesse+=self.effet
            perso.hist_bonus_texte.append( ["vitesse +"+str(self.effet),0] )
        elif self.tp_effet=="teletransportation":
            xx=random.randint(100,mape.shape[0]*t-200)
            yy=random.randint(100,mape.shape[1]*t-200)
            perso.posX,perso.posY=xx,yy
            perso.update_cam()
            perso.hist_bonus_texte.append( ["télétransporté",0] )
        elif self.tp_effet=="teletransportation_to_ennemi":
            en=random.choice(prs)
            nb=0
            while en==None or en==perso:
                en=random.choice(prs)
                nb+=1
                if nb==100: break
            xx=en.posX+random.randint(-50,50)
            yy=en.posY+random.randint(-50,50)
            perso.posX,perso.posY=xx,yy
            perso.update_cam()
            perso.hist_bonus_texte.append( ["télétransporté",0] )
        elif self.tp_effet=="-degats":
            for p in prs:
                if p!=None and p!=perso:
                    p.vie-=self.effet
                    p.hist_degats_texte.append( ["-"+str(self.effet)+"pv",0] )
        elif self.tp_effet=="brouillard":
            for p in prs:
                if p!=None and p!=perso:
                    p.etat.append("brouillard")
                    p.tpsrestant_etat.append(self.effet)
                    p.hist_degats_texte.append(["brouillard ("+str(self.effet)+"sec)",0])
        elif self.tp_effet=="invisibilite":
            perso.etat.append("invisible")
            perso.tpsrestant_etat.append(self.effet)
            perso.hist_bonus_texte.append( ["invisible ("+str(self.effet)+"sec)",0])
        elif self.tp_effet=="invincibilite":
            perso.etat.append("invincible")
            perso.tpsrestant_etat.append(self.effet)
            perso.hist_bonus_texte.append( ["invincible ("+str(self.effet)+"sec)",0])
        elif self.tp_effet=="affaiblissement":
            for p in prs:
                if p!=None and p!=perso:
                    p.etat.append("affaibli")
                    p.tpsrestant_etat.append(self.effet)
                    p.hist_degats_texte.append( ["affaibli ("+str(self.effet)+"sec)",0] )
        elif self.tp_effet=="esquive+":
            perso.esquive+=self.effet
            if perso.esquive > 95: perso.esquive=95
            perso.hist_bonus_texte.append( ["esquive +"+str(self.effet)+"%",0] )
            

txtvem=pretexte("Vous etes mort !",35,(100,100,00))
def affichage_jeu_fen(fenetre,mape,imgmape,objsmap,prs,perso,t,bons,imgbrouillard): #fonction afficheg_jeu_fen qui va afficher les parties de l'ecran des joueurs
    fenx,feny,fentx,fenty=perso.fx,perso.fy,perso.ftx,perso.fty
    pygame.draw.rect(fenetre,(0,0,0),(fenx,feny,fentx,fenty),0) #on nettoie l'ecran en noir
    pygame.draw.rect(fenetre,(250,250,250),(fenx,feny,fentx,fenty),3) #on affiche les contours de l'ecran
    for o in objsmap: #on parcoure tous les objets qu'il y a sur la map et on les affiche
        if o.image != None and o.posX >= perso.cam[0] and o.posX <= perso.cam[0]+fentx and o.posY >= perso.cam[1] and o.posY <= perso.cam[1]+fenty: #si l'image de cette objet n'est pas nulle et si l'objet est dans l'ecran, on ne va pas afficher l'objet alors qu'on ne le voit pas ! #OPTIMISATION!
            fenetre.blit(o.image,[fenx+o.posX+perso.cam[0],feny+o.posY+perso.cam[1]]) #on affiche alors l'objet
    for x in range( int(-perso.cam[0]/t) , int((-perso.cam[0]+fentx)/t) ): #on parcour la map afin de l'afficher
        for y in range( int(-perso.cam[1]/t) , int((-perso.cam[1]+fenty)/t) ):  #on parcour la map afin de l'afficher
            if x >= 0 and x < mape.shape[0]-1 and y >= 0 and y < mape.shape[1]-1: #si les coordonnées xx,yy sont dans la map  alors,
                xx=perso.cam[0]+x*t
                yy=perso.cam[1]+y*t
                if xx >= 0 and xx+t <= fentx and yy >= 0 and yy+t <= fenty: #si elle est completement dans l'écran
                    fenetre.blit(imgmape[mape[x,y]],[fenx+xx,feny+yy]) #on affiche la case xx,yy de la map
                """
                elif ( xx+t>0 or xx<fentx ) or ( yy+t>0 or yy<fenty ):
                    if xx+t>0: xxx,ax,txx=0,-xx,t-1
                    elif xx<tex: xxx,ax,txx=xx,0,tex-xx
                    else: xxx,ax,txx=xx,0,t-1
                    if yy+t>0: yyy,ay,tyy=0,-yy,t-1
                    elif yy<tey: yyy,ay,tyy=yy,0,tey-yy
                    else: yyy,ay,tyy=yy,0,t-1
                    img=imgmape[mape[x,y]].subsurface(pygame.Rect(ax,ay,txx,tyy))
                    fenetre.blit(img,[xxx,yyy])
                    """
    for p in prs: #on parcour tous les personnages
        if p!=None :
            if (p.posX+perso.cam[0]>=0 and p.posX+perso.cam[0]<=fentx and p.posY+perso.cam[1]>=0 and p.posY+perso.cam[1]<=fenty) and not "invisible" in p.etat: #si le personnage existe et qu'il est différent du personnage de la fenetre
                fenetre.blit(p.image,[fenx+perso.cam[0]+p.posX,feny+perso.cam[1]+p.posY])
                if p.image_effet!=None:
                    fenetre.blit(p.image_effet[0],[fenx+perso.cam[0]+p.posX,feny+perso.cam[1]+p.posY])
                    if time.time()-p.tpef>=p.image_effet[1]: p.image_effet=None
                for ht in p.hist_degats_texte:
                    texte(ht[0],fenx+perso.cam[0]+p.posX+p.tx,feny+perso.cam[1]+p.posY-ht[1],25,(255,0,0))
                for ht in p.hist_bonus_texte:
                    texte(ht[0],fenx+perso.cam[0]+p.posX-p.tx/2,feny+perso.cam[1]+p.posY-ht[1],25,(0,0,255))
            if p.nom=="jarry":
                if p.animactu in [["att1",2],["att2",2]]:
                    for pp in p.dernier_attaque:
                        pygame.draw.line(fenetre,(0,0,0),(fenx+p.posX+p.tx/2,feny+p.posY+p.ty/2),(fenx+pp.posX+pp.tx/2,feny+pp.posY+pp.ty/2),1)
    for b in bons:
        if b.posX+perso.cam[0] >= 0 and b.posX+perso.cam[0] <= fentx and b.posY+perso.cam[1] >= 0 and b.posY+perso.cam[1] <= fenty:
            fenetre.blit(b.image,[fenx+perso.cam[0]+b.posX,feny+perso.cam[1]+b.posY])
    if "brouillard" in perso.etat:
        fenetre.blit(imgbrouillard,[fenx,feny])
    clvie=[int(perso.vie/perso.vie_totale*255.0),0,0]
    if clvie[0]<0 or clvie[0]> 255: clvie[0]=0
    clvie=tuple(clvie)
    pygame.draw.rect(fenetre,clvie,(fenx+50,feny+15,int(perso.vie/perso.vie_totale*float(fentx-100.0)),35),0)
    pygame.draw.rect(fenetre,(0,0,0),(fenx+50,feny+15,int(fentx-100),35),2)
    texte(str(perso.vie)+"/"+str(perso.vie_totale),fenx+60,feny+27,15,(255-clvie[0],0,0))
    clbouclier=[0,0,int(perso.bouclier/perso.bouclier_total*255.0)]
    if clbouclier[2] < 0 or clbouclier[2] > 255: clbouclier[2]=0
    clbouclier=tuple(clbouclier)
    pygame.draw.rect(fenetre,clbouclier,(fenx+50,feny+60,int(perso.bouclier/perso.bouclier_total*float(fentx-100.0)),15),0)
    pygame.draw.rect(fenetre,(0,0,0),(fenx+50,feny+60,int(fentx-100),15),1)
    texte(str(perso.bouclier)+"/"+str(perso.bouclier_total),fenx+60,feny+59,15,(0,0,255-clbouclier[2]))
    clatt1=(25,25,25)
    if time.time()-perso.datt1 >= perso.attaque1[2]: clatt1=(250,150,0)
    clatt2=(25,25,25)
    if time.time()-perso.datt2 >= perso.attaque2[2]: clatt2=(250,150,0)
    clatt3=(25,25,25)
    if time.time()-perso.datt3 >= perso.attaque3[2]: clatt3=(250,150,0)
    clspec=(0,25,50)
    if time.time()-perso.dspec >= perso.special[3]: clspec=(0,150,250)
    pygame.draw.circle(fenetre,clatt1,(fenx+50,feny+100),rx(5),0)
    pygame.draw.circle(fenetre,(0,0,0),(fenx+50,feny+100),rx(5),1)
    pygame.draw.circle(fenetre,clatt2,(fenx+70,feny+100),rx(5),0)
    pygame.draw.circle(fenetre,(0,0,0),(fenx+70,feny+100),rx(5),1)
    pygame.draw.circle(fenetre,clatt3,(fenx+90,feny+100),rx(5),0)
    pygame.draw.circle(fenetre,(0,0,0),(fenx+90,feny+100),rx(5),1)
    pygame.draw.circle(fenetre,clspec,(fenx+110,feny+100),rx(5),0)
    pygame.draw.circle(fenetre,(0,0,0),(fenx+110,feny+100),rx(5),1)
    if perso.vie<=0:
        atexte(txtvem,fenx+fentx/2,feny+fenty/2)
    pygame.display.update()


def aff_mini_mape(prs,mape,tm):
    pf=[tex/2-rx(50),tey/2-ry(50),rx(100),ry(100)]
    pygame.draw.rect(fenetre,(255,255,255),pf,0)
    if prs[0] != None: pygame.draw.rect(fenetre,(0,0,150),(  pf[0]+(prs[0].posX/(mape.shape[0]*tm)*pf[2]) , pf[1]+(prs[0].posY/(mape.shape[1]*tm)*pf[3]) , rx(3) , ry(3) ),0)
    if prs[1] != None: pygame.draw.rect(fenetre,(150,0,0),(  pf[0]+(prs[1].posX/(mape.shape[0]*tm)*pf[2]) , pf[1]+(prs[1].posY/(mape.shape[1]*tm)*pf[3]) , rx(3) , ry(3) ),0)
    if prs[2] != None: pygame.draw.rect(fenetre,(0,150,0),(  pf[0]+(prs[2].posX/(mape.shape[0]*tm)*pf[2]) , pf[1]+(prs[2].posY/(mape.shape[1]*tm)*pf[3]) , rx(3) , ry(3) ),0)
    if prs[3] != None: pygame.draw.rect(fenetre,(150,150,0),(  pf[0]+(prs[3].posX/(mape.shape[0]*tm)*pf[2]) , pf[1]+(prs[3].posY/(mape.shape[1]*tm)*pf[3]) , rx(3) , ry(3) ),0)

def bot(perso,prs,objsmap,mape,t):
    if perso.cible==None or perso.cible.vie==0:
        aa=random.choice(prs)
        nbr=0
        while aa==None or aa==perso:
            aa=random.choice(prs)
            nbr+=1
            if nbr>=100: break
        perso.cible=aa
    if perso.cible!=None and not "invisible" in perso.cible.etat:
        rb=2
        fb=20
        if "brouillard" in perso.etat:
            rb*=2
            fb*=2
        if random.randint(1,rb)==1:
            if perso.cible.posX < perso.posX and abs(perso.posX-perso.cible.posX) > perso.vitesse : perso.bouger("Left",objsmap,prs,mape,t)
        if random.randint(1,rb)==1:
            if perso.cible.posX > perso.posX and abs(perso.posX-perso.cible.posX) > perso.vitesse: perso.bouger("Right",objsmap,prs,mape,t)
        if random.randint(1,rb)==1:
            if perso.cible.posY < perso.posY and abs(perso.posY-perso.cible.posY) > perso.vitesse: perso.bouger("Up",objsmap,prs,mape,t)
        if random.randint(1,rb)==1:
            if perso.cible.posY > perso.posY and abs(perso.posY-perso.cible.posY) > perso.vitesse: perso.bouger("Down",objsmap,prs,mape,t)
        dd=dist(perso.cible.posX,perso.cible.posY,perso.posX,perso.posY)
        if random.randint(1,fb)==1:
            if dd < perso.attaque1[1]: perso.bouger("Att1",objsmap,prs,mape,t)
        if random.randint(1,fb)==1:
            if dd < perso.attaque2[1]: perso.bouger("Att2",objsmap,prs,mape,t)
        if random.randint(1,fb)==1:
            if dd < perso.attaque3[1]: perso.bouger("Att3",objsmap,prs,mape,t)
        if random.randint(1,fb)==1:
            if dd < perso.cible.attaque1[1]: perso.bouger("Defence",objsmap,prs,mape,t)
        if random.randint(1,fb)==1:
            if dd < perso.cible.attaque2[1]: perso.bouger("Defence",objsmap,prs,mape,t)
        if random.randint(1,fb)==1:
            if dd < perso.cible.attaque3[1]: perso.bouger("Defence",objsmap,prs,mape,t)
        if random.randint(1,fb):
            if time.time()-perso.dspec>=perso.special[3]: perso.bouger("Special",objsmap,prs,mape,t)
    else:
        lst=["Left","Right","Up","Down","Att1","Att2","Att3","Defence"]
        perso.bouger(random.choice(lst),objsmap,prs,mape,t)
    








