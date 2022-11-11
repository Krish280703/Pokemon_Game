import pygame
import time
pygame.init()
pygame.mixer.init()

s = 'sound'

update = 0

size = 60

#Sets the window name to PokemonRoyal
pygame.display.set_caption('PokemonRoyal')

#Pokemon health
pikachu_health = 200
tortodile_health = 200

screen = pygame.display.set_mode((1280,719))
screen.fill((225,225,255))
pygame.display.flip()

red = (200, 0, 0 )
yellow = (255,255,0)
green = (0, 200, 0 )
blueish = (52, 229, 235)
gray = (171, 171, 166)
black = (0,0,0)
white = (255,255,255)
blue = (70,130,180)

#Background
background = pygame.image.load('Battle-Background-The-background-.png')
AshStartBackground = pygame.image.load('Ash.png')
GiovanniStartBackground = pygame.image.load('Giovanni.png')
StartScreeenBackground = pygame.image.load('StartScreen.jpg')

pygame.display.set_caption("Pokemon")
icon = pygame.image.load('pokeball.png')
pygame.display.set_icon(icon)

#Pokemon1
pikachuImg = pygame.image.load('pikachu new img.png')
pikachuX = 150
pikachuY = 350

def pikachu(x,y):
    screen.blit(pikachuImg, (x, y))

#Pokemon2
tortodileImg = pygame.image.load('tortodile.png')
tortodileX = 900
tortodileY = 140

def tortodile(x, y):
    screen.blit(tortodileImg, (x, y))


#Health Bars
def health_bars(pikachu_health, tortodile_health):
    if pikachu_health > 75:
        pikachu_health_color = green
    elif pikachu_health >50:
        pikachu_health_color = yellow
    else:
        pikachu_health_color = red

    if tortodile_health >75:
        tortodile_health_color = green
    elif tortodile_health >50:
        tortodile_health_color = yellow
    else:
        tortodile_health_color = red

    pygame.draw.rect(screen, pikachu_health_color, (220,380, pikachu_health,25))
    pygame.draw.rect(screen, tortodile_health_color, (900,100, tortodile_health,25))

#Button
class button():
    global size
    def __init__(self, color, x, y, width, height, text=''):

        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline=None):
            # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(screen, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', size)
            text = font.render(self.text, 1, (0, 0, 0))
            screen.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
            # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


def text_objects(text, font):
    textSureface = font.render(text, True, black)
    return textSureface, textSureface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = (350,100)
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    pygame.time.wait(2000)


def background_image():
    screen.blit(background, (0,0))

#All the Blits in one go its quit self explanatory
def updateScreen():
    if scene == 1:
        screen.blit(StartScreeenBackground, (0, 0))
        screen.blit(AshStartBackground, (-100,255))
        screen.blit(GiovanniStartBackground, (1000, 200))
        WelcomeButton.draw(screen, (0, 0, 0))
        StartButton.draw(screen, (0, 0, 0))
        EndButton.draw(screen, (0, 0, 0))
        pygame.display.update()
    if scene == 2:
        background_image()
        hydropumpButton.draw(screen, (0, 0, 0))
        tackleButton.draw(screen, (0, 0, 0))
        thunderboltButton.draw(screen, (0, 0, 0))
        thunderButton.draw(screen, (0, 0, 0))
        HydroPumpInfoButton.draw(screen, (0, 0, 0))
        BagButton.draw(screen, (0,0,0))
        health_bars(pikachu_health, tortodile_health)
        pikachu(pikachuX, pikachuY)
        tortodile(tortodileX, tortodileY)
        if tortodile_health <= 0:
            PlayAgainButton.draw(screen, (0, 0, 0))
        pygame.display.update()


def ClickButton(ButtonPressed, pos):
    global tortodile_health
    global scene
    global  running
    if StartButton.isOver(pos):
        scene = scene + 1
    if EndButton.isOver(pos):
        running = False
        pygame.quit()
        quit()

    if tortodile_health > 0:
        if hydropumpButton.isOver(pos):
            tortodile_health -= 40
            if tortodile_health < 0:
                tortodile_health = 0
            updateScreen()
            pygame.mixer.Sound.play(HydroPump)
            message_display("Pikachu used Hydropump and did 40 damage!")
        elif tackleButton.isOver(pos):
            tortodile_health -= 10
            if tortodile_health < 0:
                tortodile_health = 0
            updateScreen()
            pygame.mixer.Sound.play(Tackle)
            message_display("Pikachu used Tackle and did 10 damage!")
        elif thunderboltButton.isOver(pos):
            tortodile_health -= 20
            if tortodile_health < 0:
                tortodile_health = 0
            updateScreen()
            pygame.mixer.Sound.play(ThunderBolt)
            message_display("Pikachu used ThunderBolt and did 20 damage!")
        elif thunderButton.isOver(pos):
            tortodile_health -= 30
            if tortodile_health < 0:
                tortodile_health = 0
            updateScreen()
            pygame.mixer.Sound.play(Thunder)
            message_display("Pikachu used Thunder and did 30 damage!")
    elif PlayAgainButton.isOver(pos):
        tortodile_health = 200
        pikachu_health = 200
        updateScreen()
    else:
        tortodile_health = 0
        updateScreen()

hydropumpButton = button((blueish), 600, 500, 300, 100, 'Hydro Pump')
thunderboltButton = button((yellow), 600, 610, 300, 100, 'ThunderBolt')
tackleButton = button((gray), 920, 500, 300, 100, 'Tackle')
thunderButton = button((yellow), 920, 610, 300, 100, 'Thunder')
BagButton = button((green),600,435,140,60,'BAG')
HydroPumpInfoButton = button((red),880,500,20,20,'')
PlayAgainButton = button((red),920,435,300,60,'PLAY AGAIN')
#MainScreenButtons
WelcomeButton = button((blue),300,100,700,60,'Welcome to Pokemon Battle Royal')
StartButton = button((green),400,435,140,60,'Start')
EndButton = button((red),740,435,140,60,'Quit')

count = 1

scene = 1
updateScreen()
#Music and Sound Effects
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.load('opening.ogg')
pygame.mixer.music.play(-1)
WhosThatPokemon = pygame.mixer.Sound('WhosThatPokemon.ogg')
ItsPikachu = pygame.mixer.Sound('ItsPikachu.ogg')
Tackle = pygame.mixer.Sound('Tackle.ogg')
Thunder = pygame.mixer.Sound('ThunderShock.ogg')
ThunderBolt = pygame.mixer.Sound('Thunderbolt.ogg')
HydroPump = pygame.mixer.Sound('HydroPump.ogg')

running = True
while running:
    while scene == 1:     #StartScreen
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                ClickButton(StartButton, pygame.mouse.get_pos()) #Clicks Start Button
                updateScreen()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                ClickButton(EndButton, pygame.mouse.get_pos()) #closes screeen

    if scene != 1 or scene == 2:
        if count == 1:
            message_display("Please Wait 5 seconds...")
            pygame.mixer.Sound.play(WhosThatPokemon)
            pygame.time.wait(2000)       #stops the programme for 3 seconds any input will be invalid even closing
            pygame.mixer.Sound.stop(WhosThatPokemon)
            count = count + 1

        elif count == 2:
            pygame.mixer.Sound.play(ItsPikachu)
            pygame.time.wait(1000)
            pygame.mixer.Sound.stop(ItsPikachu)
            count = count + 1

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:

                running = False
                pygame.quit()
                quit()

            #HydroPumpPressed?
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ClickButton(hydropumpButton, pygame.mouse.get_pos())
            #TacklePressed?
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ClickButton(tackleButton, pygame.mouse.get_pos())
            #ThunderBoltPressed?
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ClickButton(thunderboltButton, pygame.mouse.get_pos())
            #ThunderPressed?
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ClickButton(thunderButton, pygame.mouse.get_pos())
            #PlayAgainPressed?
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ClickButton(PlayAgainButton, pygame.mouse.get_pos())

            #InfoButton1
            elif event.type == pygame.MOUSEMOTION:
                if HydroPumpInfoButton.isOver(pos):
                    size = 20
                    hydropumpButton = button((blueish), 600, 500, 300, 100, 'The strongest Water-type attack')
                    thunderboltButton = button((yellow), 600, 610, 300, 100, 'Electric-type move that never misses')
                    tackleButton = button((gray), 920, 500, 300, 100, 'Normal-type move that deals small  damage')
                    thunderButton = button((yellow), 920, 610, 300, 100, 'deals damage + 10% chance of paralyzing')
                    updateScreen()
                else:
                    size = 60
                    HydroPumpInfoButton.color = (red)
                    hydropumpButton = button((blueish), 600, 500, 300, 100, 'Hydro Pump')
                    thunderboltButton = button((yellow), 600, 610, 300, 100, 'ThunderBolt')
                    tackleButton = button((gray), 920, 500, 300, 100, 'Tackle')
                    thunderButton = button((yellow), 920, 610, 300, 100, 'Thunder')
                    updateScreen()
