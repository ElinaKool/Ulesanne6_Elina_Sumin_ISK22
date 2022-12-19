import pygame, random # pygame moodulite importimine

pygame.init() # PyGame-i käivitamine

# taustavärv
lBlue = [153, 204, 255] #taustavärv

# ekraaniseaded pikkuse ja laiuse määramine
screenX = 640
screenY = 480

screen = pygame.display.set_mode([screenX, screenY]) #ekraani suuruse loomine programmi poolt, etteantud suurustega
pygame.display.set_caption("Ülesanne6 - PingPong") #Ekraani nime kuvamine

screen.fill(lBlue) #Ekraani täitmine sinise värviga, mille muutujad sai programmi päises ära määratud.
fps = pygame.time.Clock()

#Heli
pygame.mixer.music.load("backgroundSound.mp3.mp3") #helifaili lisamine projektile
pygame.mixer.music.play(-1) #hääle kordamine lõpmatult
pygame.mixer.music.set_volume(0.2) #Helitugevus reguleerimine antud väärtusega

#Pall(ball)
ballX = random.randint(50, 600) #palli kordinaatide määrimine randomina. Vahemikus 50-600, X-teljel
ballY = random.randint(50, 600) #palli kordinaatide määramine randomiga. Vahemikus 50-600, Y-teljel

ball = pygame.Rect(ballX, ballY, 20, 20) #Palli suuruse muutujate määramine

ballPic = pygame.image.load("ball.png") #Palli pildi lisamine ekraanile
ballPic = pygame.transform.scale(ballPic, [ball.width, ball.height]) # Palli pildi suuruse määramine loodavas mängus.

ballSpeedX = 3  #Palli kiiruse määramine x-teljel
ballSpeedY = 4  #Palli kiiruse määramine Y-teljel

#Alus(Pad)
padX = 260  #Aluse kordinaatide määramine X teljel
padY = screenY/1.5 #Aluse kordinaatide määramine Y-teljel

pad = pygame.Rect(padY, padY, 120, 20) # Aluse suuruse määramine: 20 pikslit kõrge ja 120 pikslit lai

padPic = pygame.image.load("pad.png") #Aluse pildi lisamine ekraanile
padPic = pygame.transform.scale(padPic, [pad.width, pad.height]) #aluse suuruse määramine

padMovingDirection = 0 #Aluse suuna muutuja määramine
padSpeed = 6 #Aluse liikumiskiiruse määramine

font = pygame.font.Font(pygame.font.match_font("Fantasy"), 28) #Määratakse "Fantasy" font ja selle suurus on 28
score = 0 #Punktiarvestuse muutuja, algväärtus 0, kuna mängu alustades on mängijal 0 punkti.

Gameover=False #Mängu alustades ei ole mäng läbi

while not Gameover: #Seni kuni mäng ei ole läbi
    fps.tick(60) #toimub ekraani kaadri värskendamine

    ball = pygame.Rect(ballX, ballY, 20, 20) #Palli suuruse määramine 20x20 pikslit
    ballX -= ballSpeedX
    ballY -= ballSpeedY

    pad = pygame.Rect(padX, padY, 120, 20)

    text = font.render("Skoor on: " + str(score), True, [255, 255, 255])

    for gameSession in pygame.event.get():
            #Mängu sulgemine ristist
        if gameSession.type == pygame.QUIT:
            Gameover = True
            exit()
            #Juhtimine klaviatuuri abil
        if gameSession.type == pygame.KEYDOWN:
            if gameSession.key == pygame.K_RIGHT: #kui paremat nuppu vajutatakse alla, siis alus liigub paremale
                padMovingDirection = "Parem"
            elif gameSession.key == pygame.K_LEFT: #kui vasakut nuppu hoitakse all, siis alus liibug vasakule
                padMovingDirection = "Vasak"

        if gameSession.type == pygame.KEYUP:
            if gameSession.key == pygame.K_RIGHT: #kui paremat nuppu lastakse lahti, siis alus lõpetab liikumise paremale
                padMovingDirection = 0
            elif gameSession.key == pygame.K_LEFT: #kui vasakut noole klahvi lastakse ülesse, siis alus lõpetab liikumise vasakule
                padMovingDirection = 0
    #mängu piirjoonte tuvastamine
    if padMovingDirection == "Parem":  #kui alus puutub kokku parema seinaga, siis alus enam paremale ei liigu (nähtava ekraanist välja)
        if padX + padPic.get_rect().width < screenX:
            padX += padSpeed
    elif padMovingDirection == "Vasak": #kui alus puutub kokku vasaku seinaga, siis alus enam vasakule ei liigu(nähtava ekraani alast)
        if padX > 0:
            padX -= padSpeed

    #Kokkupärke tuvastamine - kui pall puudutab alust, lisatakse skoorile/tulemusele 1 punkt juurde
    if ball.colliderect(pad) and ballSpeedY < 0:
        score += 1
        ballSpeedY = -ballSpeedY
    #kui pall puudutab ääri (X või Y äärt), siis pall muudab suunda
    if ballX > screenX -ballPic.get_rect().width or ballX < 0:
        ballSpeedX = -ballSpeedX
    if ballY > screenY -ballPic.get_rect().width or ballY < 0:
        ballSpeedY = -ballSpeedY


    screen.fill(lBlue)  #ekraanile määratakse sinine taust
    screen.blit(ballPic, ball)
    screen.blit(padPic, pad)
    screen.blit(text, [500,25])
    pygame.display.flip()

    #Kui pall puudutab alumst äärt, siis mäng sulgub
    if ballY > screenY-ballPic.get_rect().height:
        pygame.quit()
        exit()
