try:
    import pygame
    from pygame.locals import *
    import time
    import random
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    size=width,height=1000,800
    screen=pygame.display.set_mode((size))
    pygame.display.set_caption("SPACE FIGHTERS")
    icon=[pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/1.png"),(50,100)),270)]
    pygame.display.set_icon(icon[0])

    bgm=pygame.mixer.Sound("asset/background.mp3")
    bgm.play(-1)
    def msg(px,color,text,x,y):
        pygame.font.init()
        win=pygame.font.Font("asset/motter-tektura.ttf",px)
        font=win.render(text,1,color)
        screen.blit(font,(x,y))
    def username1():
        pygame.init()
        global player1
        p=[
            pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/1.png"),(300,350)),270),
            pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/2.png"),(300,350)),270),
            pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/3.png"),(300,350)),270)
            ]
        countp=0
        player=p[countp]
        p1=player.get_rect()
        p1.y=height/2-200
        p1.x=0
        gamebg=pygame.transform.scale(pygame.image.load("asset/bg/purple6.png"),(width,height))
        user=True
        player1=""
        win=pygame.font.Font("asset/motter-tektura.ttf",70)
        blink=0
        Next=win.render("NEXT",1,(0,0,0))
        NEXT=Next.get_rect()
        NEXT.x=width/2-NEXT.width/2
        NEXT.y=700
        ########
        sure=win.render("PLAYER 1 USERNAME",100,(255,255,255))
        surerect=sure.get_rect()
        surerect.x=width/2-surerect.width/2
        surerect.y=20    
        clock=pygame.time.Clock()
        while user:
            screen.blit(gamebg,(0,0))
            pygame.draw.rect(screen,(255,255,255),NEXT,0,20)
            p1.x+=4
            if p1.x>=width:
                p1.x=-270
            clock.tick(60)
            countp+=0.4
            if countp>=3:
                countp=0
            player=p[int(countp)]
            screen.blit(player,(p1.x,p1.y))
            blink+=1
            player1t=win.render(player1,1,((255,255,255)))
            player1r=player1t.get_rect()
            player1r.x=100
            player1r.y=600
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    user=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        if player1=="":
                            username1()
                            pygame.display.update()
                        else:
                            username2()
                    player1+=event.unicode.strip().upper()
            key=pygame.key.get_pressed()
            if len(player1)>=10:
                player1=player1[:-1]
                
            if key[pygame.K_BACKSPACE]:
                if len(player1)>0:
                    player1=player1[:-1]
            x,y=player1r.topright
            screen.blit(sure,(surerect.x,surerect.y))
            pygame.draw.rect(screen,(0,255,0),(player1r.x-20,player1r.y,player1r.x+700,player1r.height),0,50)
            if blink>=20:
                pygame.draw.rect(screen,((255,255,255)),(x,y+10,2,player1r.height-20))
            if blink==40:
                blink=0
            screen.blit(player1t,player1r)
            screen.blit(Next,NEXT)
            press=pygame.mouse.get_pressed()
            mou=pygame.mouse.get_pos()
            if press[0]:
                if NEXT.collidepoint(mou):
                    if player1=="":
                        username1()
                        pygame.display.update()
                    else:
                        username2()
            pygame.display.update()
        pygame.quit()
    def preload():
        pygame.init()
        gamebg=pygame.transform.scale(pygame.image.load("asset/bg/purple6.png"),(width,height))
        user=True
        init=""
        win=pygame.font.SysFont("arial",70,True)
        blink=0
        sure=win.render("WELCOME TO SPACE FIGHTERS",100,(255,255,255))
        surerect=sure.get_rect()
        surerect.x=width/2-surerect.width/2
        surerect.y=100

        win=pygame.font.SysFont("arial",30,True)
        load=0
        p=[
            pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/1.png"),(300,350)),270),
            pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/2.png"),(300,350)),270),
            pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/3.png"),(300,350)),270)
            ]
        countp=0
        player=p[countp]
        p1=player.get_rect()
        p1.y=height/2-200
        p1.x=width/2-p1.width/2
        clock=pygame.time.Clock()
        while user:
            load+=1
            if load >=0:
                init="loading. . .".title()
            if load>=50:
                init="initializing user interface. . .".title()
            if load>=100:
                init="initializing engine. . .".title()
            if load>=150:
                init="almost done. . .".title()
            if load>=200:
                username1()
            sure1=win.render(init,100,(255,255,255))
            sure1rect=sure1.get_rect()
            sure1rect.x=width/2-sure1rect.width/2
            sure1rect.y=600
            screen.blit(gamebg,(0,0))
            countp+=0.4
            if countp>=3:
                countp=0
            player=p[int(countp)]
            screen.blit(player,(p1.x,p1.y))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    user=False
            screen.blit(sure,(surerect.x,surerect.y))
            screen.blit(sure1,(sure1rect.x,sure1rect.y))
            msg(50,(255,255,255),"CREATED BY GODSPOWER",150,700)
            
            pygame.display.update()
        pygame.quit()
    def username2():
            pygame.init()
            global player2nd
            p=[
                pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/1.png"),(300,350)),90),
                pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/2.png"),(300,350)),90),
                pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/3.png"),(300,350)),90)
                ]
            countp=0
            player=p[countp]
            p1=player.get_rect()
            p1.y=height/2-200
            p1.x=width-270
            gamebg=pygame.transform.scale(pygame.image.load("asset/bg/purple6.png"),(width,height))
            user=True
            win=pygame.font.Font("asset/motter-tektura.ttf",70)
            player2nd=""
            sure1=win.render("PLAYER 2 USERNAME",100,(255,255,255))
            sure1rect=sure1.get_rect()
            sure1rect.x=width/2-sure1rect.width/2
            sure1rect.y=20
            Next=win.render("NEXT",1,(0,0,0))
            NEXT=Next.get_rect()
            NEXT.x=width/2-NEXT.width/2
            NEXT.y=700
            blink=0
            clock=pygame.time.Clock()
            while user:
                blink+=1
                screen.blit(gamebg,(0,0))
                player2t=win.render(player2nd,1,(255,255,255))
                player2r=player2t.get_rect()
                player2r.x=100
                player2r.y=600
                p1.x-=4
                if p1.x<=-270:
                    p1.x=width
                clock.tick(60)
                screen.blit(gamebg,(0,0))
                countp+=0.4
                if countp>=3:
                    countp=0
                player=p[int(countp)]
                screen.blit(player,(p1.x,p1.y))
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        user=False
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_SPACE:
                            if player2nd=="":
                                username2()
                                pygame.display.update()
                            else:
                                stage()
                        player2nd+=event.unicode.strip().upper()
                key=pygame.key.get_pressed()
                if key[pygame.K_BACKSPACE]:
                    player2nd=player2nd[:-1]
                if len(player2nd)>=10:
                    player2nd=player2nd[:-1]
                x,y=player2r.topright
                pygame.draw.rect(screen,(0,255,0),(player2r.x-20,player2r.y,player2r.x+700,player2r.height),0,50)
                if blink>=20:
                    pygame.draw.rect(screen,((255,255,255)),(x,y+10,2,player2r.height-20))
                if blink==40:
                    blink=0
                
                press=pygame.mouse.get_pressed()
                mou=pygame.mouse.get_pos()
                if press[0]:
                    if NEXT.collidepoint(mou):
                        if player2nd=="":
                            username2()
                        else:
                            stage()
                pygame.draw.rect(screen,(255,255,255),NEXT,0,20)
                screen.blit(Next,NEXT)
                screen.blit(player2t,player2r)
                screen.blit(sure1,sure1rect)
                pygame.display.update()
            pygame.quit()
    def stage():
        global text
        rounds=True
        gamebg=pygame.transform.scale(pygame.image.load("asset/bg/purple6.png"),(width,height))
        text=""
        win=pygame.font.Font("asset/motter-tektura.ttf",70)
        Next=win.render("NEXT",1,(0,0,0))
        NEXT=Next.get_rect()
        NEXT.x=width/2-NEXT.width/2
        NEXT.y=700
        blink=0
        
        while rounds:
            press=pygame.mouse.get_pressed()
            mou=pygame.mouse.get_pos()
            blink+=1
            screen.blit(gamebg,(0,0))
            pygame.draw.rect(screen,(255,255,255),NEXT,0,20)
            if text.isdigit():
                text=text
                
            else:
                text=text[:-1]
            rend=win.render(text,1,(255,255,255))
            rendr=rend.get_rect()
            rendr.x=width/2-rendr.width/2
            rendr.y=300
            msg(70,(255,255,255),"HOW MANY ROUNDS",140,50)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    rounds=False
                if event.type==pygame.KEYDOWN:
                    text+=event.unicode.strip().upper()
            
            key=pygame.key.get_pressed()
            if key[pygame.K_BACKSPACE]:
                text=text[:-1]
            if len(text)>2:
                text=text[:-1]
            pygame.draw.rect(screen,((0,255,0)),(width/2-rendr.x/2,rendr.y,rendr.x,rendr.height),0,30)
            x,y=rendr.topright
            if blink>=50:
                pygame.draw.rect(screen,((255,255,255)),(x,y,10,rendr.height))
            if blink>=100:
                blink=0
            if press[0]:
                if NEXT.collidepoint(mou):
                    if text=="":
                        stage()
                        pygame.display.update()
                    else:
                        menu()
                        total=int(text)
            screen.blit(rend,rendr)
            screen.blit(Next,NEXT)
            pygame.display.update()
    def gameover():
        pygame.init()
        pygame.font.init()
        gameover=True
        gamebg=pygame.transform.scale(pygame.image.load("asset/bg/purple6.png"),(width,height))
        r=[]
        g=[]
        b=[]
        rand=[]
        number=6
        for i in range(number):
            r.append(random.randint(0,255))
            g.append(random.randint(0,255))
            b.append(random.randint(0,255))
            rand.append(0)
        mesg=""
        ans=""
        while gameover:
            screen.blit(gamebg,(0,0))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameover=False
                    run=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_r:
                        main()
            ############# BUTTON #############
            win=pygame.font.Font("asset/motter-tektura.ttf",50)
            mou=pygame.mouse.get_pressed()
            moupos=pygame.mouse.get_pos()
            color=(255,255,255)
            color1=(255,255,255)
            player=pygame.font.SysFont("arial",60,True)
            
            for i in range(number):
                rand[i]+=1
                font=win.render("RESTART GAME",1,(r[3],g[3],b[3]))
                frect=font.get_rect()
                frect.x=width/2-frect.width/2
                frect.y=300
                if mou[0]:
                    if frect.collidepoint(event.pos):
                        main()
                
                if frect.collidepoint(moupos):
                    color=(0,0,0)
                    
                pygame.draw.rect(screen,color,frect,0,10)
                screen.blit(font,(frect.x,frect.y))
                
                font1=win.render("QUIT GAME",1,(r[2],g[2],b[2]))
                f1rect=font1.get_rect()
                f1rect.x=width/2-f1rect.width/2
                f1rect.y=550
                if mou[0]:
                    if f1rect.collidepoint(event.pos):
                        sure()
                if f1rect.collidepoint(moupos):
                    color1=(0,0,0)
                pygame.draw.rect(screen,color1,f1rect,0,10)
                screen.blit(font1,(f1rect.x,f1rect.y))

                
                if score1>=total:
                    ans=f"{player1} DEFEATED {player2nd}"
                    mesg=f"{player1} IS LEADING THE GAME"
                    
                if score2>=total:
                    ans=f"{player2nd} DEFEATED {player1}"
                    mesg=f"{player2nd} IS LEADING THE GAME"
                    
                font9=win.render(mesg,1,(r[5],g[5],b[5]))
                f9rect=font9.get_rect()
                f9rect.x=width/2-f9rect.width/2
                f9rect.y=650
                pygame.draw.rect(screen,color,f9rect,0,10)
                screen.blit(font9,(f9rect.x,f9rect.y))
                
                    
                font6=win.render("CHANGE USERS",1,(r[4],g[4],b[4]))
                f6rect=font6.get_rect()
                f6rect.x=width/2-f6rect.width/2
                f6rect.y=420
                c=(255,255,255)
                if mou[0]:
                    if f6rect.collidepoint(moupos):
                        username1()
                if f6rect.collidepoint(moupos):
                        c=(0,0,0)
                pygame.draw.rect(screen,c,f6rect,0,10)
                screen.blit(font6,(f6rect.x,f6rect.y))
                
                font2=player.render(ans,1,(r[0],g[0],b[0]))
                f2rect=font2.get_rect()
                f2rect.x=width/2-f2rect.width/2
                f2rect.y=150
                screen.blit(font2,(f2rect.x,f2rect.y))
                msg(100,(r[1],g[1],b[1]),"GAME OVER",width/2-300,10)
                
                if rand[i]>=10:
                    r[i]=random.randint(0,255)
                    g[i]=random.randint(0,255)
                    b[i]=random.randint(0,255)
                    rand[i]=0
                
             
            pygame.display.update()
        pygame.quit()
    def sure():
        pygame.init()
        pygame.font.init()
        sure=True
        imgs=pygame.transform.scale(pygame.image.load("asset/bg/purple6.png"),(width,height))
        while sure:
            screen.blit(imgs,(0,0))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sure=False
            win=pygame.font.Font('asset/motter-tektura.ttf',100)
            mouses=pygame.mouse.get_pressed()
            mousespos=pygame.mouse.get_pos()
            
            sure1=win.render("WANT TO QUIT",True,(255,255,255))
            sure1rect=sure1.get_rect()
            sure1rect.x=width/2-sure1rect.width/2
            sure1rect.y=150
            screen.blit(sure1,(sure1rect.x,sure1rect.y))
            
            sure=win.render("ARE YOU SURE YOU",True,(255,255,255))
            surerect=sure.get_rect()
            surerect.x=width/2-surerect.width/2
            surerect.y=20
            screen.blit(sure,(surerect.x,surerect.y))

            win1=pygame.font.Font('asset/motter-tektura.ttf',70)
            yes=win1.render("YES",True,(255,255,255))
            yesr=yes.get_rect()
            yesr.x=width/2-yesr.width-150
            yesr.y=400
            pygame.draw.rect(screen,(0,0,0),yesr,0,10)
            screen.blit(yes,yesr)
            if mouses[0]:
                if yesr.collidepoint(mousespos):
                    sure=False
                    pygame.quit()
            
            no=win1.render("NO",1,(255,255,255))
            nor=no.get_rect()
            nor.x=width/2+yesr.width
            nor.y=400
            pygame.draw.rect(screen,(0,0,0),nor,0,10)
            screen.blit(no,nor)
            if mouses[0]:
                if nor.collidepoint(mousespos):
                    sure=False
            pygame.display.update()

    def main():
        global total,score1,score2
        
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()
        bgm.stop()
        bg=[pygame.transform.scale(pygame.image.load("asset/bg/purple6.png"),(width,height+100))]
        bg2=[pygame.transform.scale(pygame.image.load("asset/bg/purple6.png"),(width,height+100))]

        p=[
            pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/1.png"),(150,200)),270),
            pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/2.png"),(150,200)),270),
            pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated/3.png"),(150,200)),270)
            ]
        pp=[
            pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated2/1.png"),(150,200)),90),
            pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated2/2.png"),(150,200)),90),
            pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/Animated2/3.png"),(150,200)),90)
            ]
        bw=100
        bh=100
        bomb=[pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_1.png"),(bw,bh)),
            pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_2.png"),(bw,bh)),
            pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_3.png"),(bw,bh)),
            pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_4.png"),(bw,bh)),
            pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_5.png"),(bw,bh)),
            pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_6.png"),(bw,bh)),
            pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_7.png"),(bw,bh)),
            pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_8.png"),(bw,bh)),
            pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_9.png"),(bw,bh)),
            pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_10.png"),(bw,bh)),
            ]
        bomw=200
        bomh=200
        bomcount=0
        bomb1=[pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_1.png"),(bomw,bomh)),
            pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_2.png"),(bomw,bomh)),
            pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_3.png"),(bomw,bomh)),
            pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_4.png"),(bomw,bomh)),
            pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_5.png"),(bomw,bomh)),
            pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_6.png"),(bomw,bomh)),
            pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_7.png"),(bomw,bomh)),
            pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_8.png"),(bomw,bomh)),
            pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_9.png"),(bomw,bomh)),
            pygame.transform.scale(pygame.image.load("asset/Explosion_1/Explosion_10.png"),(bomw,bomh)),
            ]

        bcount=0
        count=0
        wait=0
        pause=False
        fire=0
        
        pygame.mixer.music.load("asset/bgm.mp3")
        pygame.mixer.music.play(-1)

        shoot=pygame.mixer.Sound("asset/explosion.wav")
        gun=pygame.mixer.Sound("asset/shoot.wav")
        clock=pygame.time.Clock()
        play=0

        fps=60
        shot=0

        #fastness 
        vel=20
        bvel=30

        shake=20
        vibration=0
        vibrate=False

        health1=200
        health2=200
        
        life=25
        score1=0
        score2=0
        center=70
        total=int(text)
        end=False
        stop=0
        player=p[count]
        p1=player.get_rect()
        p1.y=height/2
        p1.x=0

        player2=pp[count]
        p2=player2.get_rect()
        
        p2.x=width-100
        p2.y=height/2+10

        bullet=False
        bimg=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/shot.png"),(20,20)),360)
        b=bimg.get_rect()
        b.x=0
        b.y=0

        bullet1=False
        bimg1=pygame.transform.rotate(pygame.transform.scale(pygame.image.load("asset/shot.png"),(20,20)),180)
        b1=bimg.get_rect()
        b1.x=0
        b1.y=0
        
        bgx=0
        bgy=0

        bg2x=width
        bg2y=0
        run=True
        startmenu=True
        color=(255,0,255)
      
        #######################################################################
        #########   GAME   LOOP  ##############################################
        while run:
            colorr=(255,255,255)
            colorr1=(255,255,255)
            time=clock.tick(fps)/1000
            background=bg[0]
            screen.blit(background,(bgx,bgy))
            bgx-=9
            if bgx <= -width:
                bgx=width
                
            background2=bg2[0]
            screen.blit(background2,(bg2x,bg2y))
            bg2x-=9
            if bg2x <= -width:
                bg2x=width
            msg(30,(255,255,255),f"{total} ROUNDS",width/2-5,60)
            win=pygame.font.Font("asset/motter-tektura.ttf",30)

            text1=win.render(player1,1,(255,255,255))
            text2=win.render(player2nd,1,(255,255,255))
            tr=text2.get_rect()

            screen.blit(text1,(220,15))
            screen.blit(text2,(width-200- 30-tr.width,15))
            
            mou=pygame.mouse.get_pressed()
            moupos=pygame.mouse.get_pos()
            font3=win.render("PAUSE",1,color)
            f3rect=font3.get_rect()
            f3rect.x=width/2-(f3rect.width+20)
            f3rect.y=60
            if mou[0]:
                if f3rect.collidepoint(moupos):
                    pauseme()
            if f3rect.collidepoint(moupos):
                colorr=(0,0,0)
            pygame.draw.rect(screen,colorr,f3rect,0,5)
            screen.blit(font3,(f3rect.x,f3rect.y))
            count+=0.4
            if count>=3:
                count=0
            player=p[int(count)]
            player2=pp[int(count)]
            
            if bullet==False:
                b.x=p1.x+center+35
                b.y=p1.y+center

            if bullet1==False:
                b1.x=p2.x+center
                b1.y=p2.y+center-10
            ################### FOR LOOP ###################
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pauseme()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        pygame.quit()
                    if event.key==pygame.K_p:
                        pauseme()
            key=pygame.key.get_pressed()
            #player1
            if key[pygame.K_LEFT]:
                p2.x-=vel
            if key[pygame.K_RIGHT]:
                p2.x+=vel
            if key[pygame.K_UP]:
                p2.y-=vel
            if key[pygame.K_DOWN]:
                p2.y+=vel
                
            #fire bullet
            if key[pygame.K_RCTRL]:
                bullet1=True
            if bullet1:
                b1.x-=bvel
            if b1.x<=p1.x:
                bullet1=False
                b1.x=p2.x+center
                b1.y=p2.y+center
                
           #player2
            if key[pygame.K_a]:
                p1.x-=vel
            if key[pygame.K_s]:
                p1.x+=vel
            if key[pygame.K_w]:
                p1.y-=vel
            if key[pygame.K_z]:
                p1.y+=vel
            
            #fire bullet
            if key[pygame.K_SPACE]:
                bullet=True        
                
            if bullet:
               b.x+=bvel
            if b.x>=p2.x+70:
                bullet=False
                b.x=p1.x+center+50
                b.y=p1.y+center
            #bullet and bullet collision
            if b.colliderect(b1):
                b.x=p1.x+center+50
                b.y=p1.y+center
                bom=bomb[4]
                screen.blit(bom,(b1.x,b1.y-50))
                
                b1.x=p2.x+center
                b1.y=p2.y+center
                bullet=False
                bullet1=False
                
            if b.colliderect(p2):
                vibrate=True
                shoot.play()
                bom=bomb[4]
                screen.blit(bom,(p2.x-10,p2.y+20))
                health2-=life
                b.x=p1.x+center+50
                b.y=p1.y+center
                bullet=False
            if vibrate:
                vibration+=1
                if vibration==5:
                    bgy-=shake
                    bg2y-=shake
                if vibration==10:
                    bgy+=shake
                    bg2y+=shake
                if vibration==15:
                    bgy-=shake
                    bg2y-=shake
                if vibration==20:
                    bgy+=shake
                    bg2y+=shake
                    vibration=0
                    vibrate=False
                
            if b1.colliderect(p1):
                shoot.play()
                vibrate=True
                bom=bomb[4]
                screen.blit(bom,(p1.x+center+35,p1.y+20))
                health1-=life
                b1.x=p2.x+center
                b1.y=p2.y+center
                bullet1=False
            if vibrate:
                vibration+=1
                if vibration==5:
                    bgy-=shake
                    bg2y-=shake
                if vibration==10:
                    bgy+=shake
                    bg2y+=shake
                if vibration==15:
                    bgy-=shake
                    bg2y-=shake
                if vibration==20:
                    bgy+=shake
                    bg2y+=shake
                    vibration=0
                    vibrate=False

            
            if p1.x >= width/2-150:
                p1.x=width/2-150
            if p1.x <=-50:
                p1.x=-50
            if p1.y >= height-70:
                p1.y=height-70
            if p1.y<= 20:
                p1.y=20

            if p2.x >= width-150:
                p2.x=width-150
            if p2.x <= width/2:
                p2.x=width/2
            if p2.y >= height-70:
                p2.y=height-70
            if p2.y <= 0:
                p2.y=0
            percent1=int(health1/200*100/1)
            percent2=int(health2/200*100/1)

            screen.blit(bimg1,(b1.x,b1.y))
            screen.blit(bimg,(b.x,b.y))
            screen.blit(player,(p1.x,p1.y))
            screen.blit(player2,(p2.x,p2.y))
            
            #1
            pygame.draw.rect(screen,(255,0,0),(10,15,200,30),0,20)
            pygame.draw.rect(screen,(0,255,0),(10,15,health1,30),0,20)
            
            
            #2
            pygame.draw.rect(screen,(255,0,0),(width-width/4.5,15,200,30),0,20)
            pygame.draw.rect(screen,(0,255,0),(width-width/4.5,15,health2,30),0,20)
            

            msg(25,(0,0,0),f"{percent1}%",230-230/2.2,15)
            msg(25,(0,0,0),f"{percent2}%",width-width/5,15)
           
            #life
            
            if health1 <= 0:
                score2+=1
                health1=200
                health2=200
                
            if score2>=total:
                wait+=1
                bomcount+=0.3
                if bomcount>=9:
                    bomcount=9
                boom=bomb1[int(bomcount)]
                screen.blit(boom,(p1.x,p1.y+center-90))
            if wait>=40:
                gameover()
                
            if health2 <= 0:
                score1+=1
                health1=200
                health2=200
                
            if score1>=total:
                bomcount+=0.3
                if bomcount>=9:
                    bomcount=9
                boom=bomb1[int(bomcount)]
                screen.blit(boom,(p2.x,p2.y+center-90))
                wait+=1
                        
            if wait>=40:
                gameover()
            if health2 <= 0 and health1 <= 0:
                score2=score2
                score1=score1
            
            msg(50,(255,255,255),f"{score1} : {score2}",width/2-50,10)     
            pygame.display.update()
        pygame.quit()
    ###########################################################
    ################ END OF LOOP ##############################
    def pauseme():
        pygame.init()
        pygame.font.init()
        pau=pygame.transform.scale(pygame.image.load("asset/bg/purple6.png"),(width,height))
        screen=pygame.display.set_mode((size))
        pause=True
        clock=pygame.time.Clock()
        while pause:
            pygame.mixer.music.pause()
            clock.tick(60)
            screen.blit(pau,(0,0))
            msg(100,(255,255,255),"GAME PAUSED",200,50)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pause=False
            win=pygame.font.Font("asset/motter-tektura.ttf",50)
            mou=pygame.mouse.get_pressed()
            moupos=pygame.mouse.get_pos()
            color=(255,255,0)
            
            font5=win.render("CONTINUE",1,color)
            f5rect=font5.get_rect()
            f5rect.x=width/2-f5rect.width/2
            f5rect.y=200
            c=(0,200,0)
            if mou[0]:
                if f5rect.collidepoint(moupos):
                    pause=False
                    pygame.mixer.music.unpause()
            if f5rect.collidepoint(moupos):
                    c=(0,0,0)
            pygame.draw.rect(screen,c,f5rect,0,10)
            screen.blit(font5,(f5rect.x,f5rect.y))

            font6=win.render("CHANGE USERS",1,color)
            f6rect=font6.get_rect()
            f6rect.x=width/2-f6rect.width/2
            f6rect.y=350
            c=(0,200,0)
            if mou[0]:
                if f6rect.collidepoint(moupos):
                    username1()
            if f6rect.collidepoint(moupos):
                    c=(0,0,0)
            pygame.draw.rect(screen,c,f6rect,0,10)
            screen.blit(font6,(f6rect.x,f6rect.y))

            font7=win.render("QUIT GAME",1,color)
            f7rect=font7.get_rect()
            f7rect.x=width/2-f7rect.width/2
            f7rect.y=500
            col=(0,200,0)
            if mou[0]:
                if f7rect.collidepoint(moupos):
                    sure()
            if f7rect.collidepoint(moupos):
                col=(0,0,0)
            pygame.draw.rect(screen,col,f7rect,0,10)
            screen.blit(font7,(f7rect.x,f7rect.y))
            pygame.display.update()
    def menu():
        pygame.init()
        pygame.font.init()
        menu=True
        if menu:
            count=0
            x=[]
            y=[]
            w=[]
            h=[]
            r=[]
            g=[]
            b=[]
            num=500
            for i in range(num):
                x.append(random.randint(0,width))
                y.append(random.randint(0,height))
                w.append(10)
                h.append(10)
                r.append(random.randint(0,255))
                g.append(random.randint(0,255))
                b.append(random.randint(0,255))
            count=0
            win=pygame.font.SysFont("arial",70,True)
            vs=win.render(f"{player1} VS {player2nd}",1,(0,255,0))
            VS=vs.get_rect()
            VS.x=width/2-VS.width/2
            VS.y=50
            while menu:
                screen.fill((0,0,0))
                count+=1
                key=pygame.key.get_pressed()
                for i in range(num):
                    x[i]+=1
                    if x[i]>=width:
                        x[i]=0
                    if count>=5:
                        x[i]=random.randint(0,width)
                        y[i]=random.randint(0,height)
                        r[i]=random.randint(0,255)
                        g[i]=random.randint(0,255)
                        b[i]=random.randint(0,255)
                        w[i]=50
                        h[i]=50
                        count=0
                    pygame.draw.rect(screen,(r[i],g[i],b[i]),(x[i],y[i],w[i],h[i]))
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        menu=False
                 
                moupos=pygame.mouse.get_pos()
                mou=pygame.mouse.get_pressed()
                color=(255,255,0)
                font5=win.render("START GAME",1,color)
                f5rect=font5.get_rect()
                f5rect.x=width/2-f5rect.width/2
                f5rect.y=height/2-100
                c=(0,200,0)
                if mou[0]:
                    if f5rect.collidepoint(moupos):
                        main()
                        pygame.display.update()
                if f5rect.collidepoint(moupos):
                        c=(0,0,0)
                pygame.draw.rect(screen,c,f5rect,0,10)
                screen.blit(font5,(f5rect.x,f5rect.y))
                
                font6=win.render("QUIT GAME",1,color)
                f6rect=font6.get_rect()
                f6rect.x=width/2-f6rect.width/2
                f6rect.y=height/2+100
                c=(0,200,0)
                if mou[0]:
                    if f6rect.collidepoint(moupos):
                        sure()
                        pygame.display.update()
                if f6rect.collidepoint(moupos):
                        c=(0,0,0)
                pygame.draw.rect(screen,c,f6rect,0,10)
                screen.blit(font6,(f6rect.x,f6rect.y))
                
                pygame.draw.rect(screen,(255,255,255),VS,0,20)
                screen.blit(vs,VS)
                pygame.display.update()
        pygame.quit()
    preload()
    pygame.display.update()
except:
    print("")
























