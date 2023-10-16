#imports
import pygame

import random

pygame.init()

screenSize = (800, 600)
screen = pygame.display.set_mode(screenSize)

pygame.display.set_caption("Title")

clock = pygame.time.Clock()

# colors
white = (255, 255, 255)
grey = (128, 128, 128)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
dankGreen = [0, 60, 0]
yellow = (255, 255, 0)
orange = (255, 128, 0)
lime = (128, 255, 0)

buttonPlayGreen = green
buttonGreenCredits = green
backButtonGreen = green
forwardButtonGreen = green
backButton2Green = green

ButtonAGreen = green
ButtonBGreen = green
ButtonCGreen = green
ButtonDGreen = green

page = 0
offset = 0
frame = 0
colorDarken = 0
yOffsetTitle = 0
yOffsetButtons = 0
titleYOffset = 200
yButtonsPlay = 400
yButtonsCredits = 475
topEndpoint = 225
bottomEndpoint = 375
yOffsetTextPlay = 491
yOffsetTextCredits = 416
rectangleThickness = 0
rectanglePos = 395
colorOffset = 0
questionYbox = 100
ySubbox1 = 400
ySubbox2 = 400
ySubbox3 = 500
ySubbox4 = 500
backButtonPressedCredits = False
mouseOnButton = False
gameButtonPressed = False
gameClosePressed = False
buttonPressed = False
creditsButtonPressed = False
backButtonPressed = False
backButton2Pressed = False
forwardButtonPressed = False
gameButtonPressed2 = False
gameButtonPressed3 = False
answerAButtonPressed = False
answerBButtonPressed = False
answerCButtonPressed = False
answerDButtonPressed = False
winner = False

answers = [
    "Paget’s Disease", "Polymyositis", "Stroke", "Type 2 Diabetes", "CAD"
]

symptoms = ["Bone", "Brain", "Skin", "Lungs", "Muscles", "Kidneys", "Heart"]
symptomsPosition = [(100, 300), (100, 100), (100, 400), (100, 200), (100, 400),
                    (600, 500), (600, 300)]
organsPosition = [(310,373), (375, 180), (304,322), (360, 300), (304, 322), (356, 387), (389,307)]
symptomsList = [["Bone", "Brain", "Skin"], ["Lungs", "Muscles"], ["Brain"],
                ["Kidneys", "Brain"], ["Lungs", "Brain", "Heart"]]

descriptionsFormatted = [
    ["The bone is too large, shape is abnormal", "", ""],
    ["Patient reports a tingling sensation across the body", "", ""],
    ["The skin feels warm over the affected area", "", ""]
], [
    ["Patient experiences trouble swallowing","", ""],
    ["Patient reports feeling weak and pain in", "the muscles", ""]
], [["Sudden weakness or numbness in the face", "trouble speaking, and problems with balance", "and coordination"]], [["Patient experiences frequent urination and ", "thirstiness throughout the day", ""],
    ["Patient experiences fatigue and numbness", "in their feet and hands", "" ]], [[
    "Patient experiences shortness of breath", "throughout the day", ""], 
    ["Patient experiences fatigue and", "light-headedness",""], 
    ["Patient has a constant tightening", "chest pain", ""
]]

descriptions = [
    ["The bone is too large, with the shape abnormal","Patient reports a tingling sensation across the body","The skin feels warm over the affected area"],
    [
        "Patient experiences trouble swallowing",
        "Patient reports feeling weak and pain in the muscles"
    ],
    [ 
        "Sudden weakness or numbness in the face, trouble speaking, and problems with balance and coordination"
    ],
    [
        "Patient experiences frequent urination and thirstiness throughout the day",
        "Patient experiences fatigue and numbness in their feet and hands"
    ],
    [
        "Patient experiences shortness of breath throughout the day",
        "Patient experiences fatigue and light-headedness",
        "Patient has a constant tightening chest pain"
    ]
]

#main fonts
font = pygame.font.Font('Eight-Bit Madness.ttf', 32)
font2 = pygame.font.Font('Eight-Bit Madness.ttf', 25)
fontTitle = pygame.font.Font('Eight-Bit Madness.ttf', 90)
font1 = pygame.font.Font('Eight-Bit Madness (copy).ttf', 50)
fontend = pygame.font.Font('Eight-Bit Madness (copy).ttf', 45)

#text blits
buttonCredits = font.render("Credits", 1, buttonPlayGreen)
buttonPlay = font.render("Play", 1, buttonGreenCredits)
title = fontTitle.render("MEDSCHOOL", 1, green)
question = font1.render("What is that disease?", 1, green)

#image blits
bodyDiagram = pygame.image.load("bodyDiagram.png")
#bodyDiagram = pygame.transform.scale(bodyDiagram, (225,297))
bodyDiagram = pygame.transform.scale(bodyDiagram, (300, 400))
armBoneRed = pygame.image.load("bodyDiagramOrgans/armbonered (1).png")
armBonePink = pygame.image.load("bodyDiagramOrgans/armbonepink (1).png")
armSkinPink = pygame.image.load("bodyDiagramOrgans/armskin (1).png")
armSkinRed = pygame.image.load("bodyDiagramOrgans/armskinred (1).png")
brainPink = pygame.image.load("bodyDiagramOrgans/brainpink (1).png")
brainRed = pygame.image.load("bodyDiagramOrgans/brainred (1).png")
kidneysPink = pygame.image.load("bodyDiagramOrgans/kidneyspink (1).png")
kidneysRed = pygame.image.load("bodyDiagramOrgans/kidneysred (1).png")
legsPink = pygame.image.load("bodyDiagramOrgans/legspink (1).png")
legsRed = pygame.image.load("bodyDiagramOrgans/legsred (1).png")
lungsPink = pygame.image.load("bodyDiagramOrgans/lungspink (1).png")
lungsRed = pygame.image.load("bodyDiagramOrgans/lungsred (1).png")
stomachPink = pygame.image.load("bodyDiagramOrgans/stomachpink (1).png")
stomachRed = pygame.image.load("bodyDiagramOrgans/stomachred (1).png")
heartPink = pygame.image.load("bodyDiagramOrgans/heartPink (1).png")
heartRed = pygame.image.load("bodyDiagramOrgans/heartRed (1).png")
                               
pinkOrgans = [armBonePink, brainPink, armSkinPink, lungsPink, armSkinPink, kidneysPink, heartPink]

redOrgans = [armBoneRed, brainRed, armSkinRed, lungsRed, armSkinRed, kidneysRed, heartRed] 



#answers
answerIndex = random.randint(0, 4)
correctAnswer = answers[answerIndex]
correctSymptoms = symptoms[answerIndex]

answerA = correctAnswer
answers.remove(answerA)

answerB = answers[random.randint(0, len(answers) - 1)]
answers.remove(answerB)

answerC = answers[random.randint(0, len(answers) - 1)]
answers.remove(answerC)

answerD = answers[random.randint(0, len(answers) - 1)]
answers.remove(answerD)

answersList = [answerA, answerB, answerC, answerD]
random.shuffle(answersList)

option1 = font.render(answersList[0], 1, buttonPlayGreen)
option2 = font.render(answersList[1], 1, buttonPlayGreen)
option3 = font.render(answersList[2], 1, buttonPlayGreen)
option4 = font.render(answersList[3], 1, buttonPlayGreen)

# print(len(symptomsList[answerIndex]))

#clickable boxes
class Boxes:
  #attributes
  boxesPos = [300, 100]
  green = (0, 255, 0)
  black = (0, 0, 0)
  isClicked = False
  bottomEndpointGame = 375
  topEndpointGame = 225
  rectangleThicknessGame = 0
  rectanglePosGame = 395
  symptom = "PLACEHOLDER"
  boxNumber = 0
  counter = 0
  symptomsOrgansMatch = 0
  
  #text blit

  #methods
  def draw(self):
    pygame.draw.rect(screen, self.green,
                     [self.boxesPos[0], self.boxesPos[1], 70, 70], 5)
    pygame.draw.rect(screen, self.black,
                     [self.boxesPos[0] + 5, self.boxesPos[1] + 5, 60, 60])
    pygame.draw.rect(screen, self.green,
                     [self.boxesPos[0] + 30, self.boxesPos[1] + 10, 10, 30])
    pygame.draw.rect(screen, self.green,
                     [self.boxesPos[0] + 30, self.boxesPos[1] + 45, 10, 10])
    pygame.draw.line(screen, self.green, [self.boxesPos[0] + 70, self.boxesPos[1] + 35], [organsPosition[self.symptomsOrgansMatch][0], organsPosition[self.symptomsOrgansMatch][1]], 5)
  def click(self):
    if self.bottomEndpointGame <= 555:
      pygame.draw.line(screen, green, (395, self.topEndpointGame),
                       (395, self.bottomEndpointGame), 5)
      self.bottomEndpointGame += 10
      self.topEndpointGame -= 10
    else:
      if self.rectangleThicknessGame != 600:
        self.rectangleThicknessGame += 20
        self.rectanglePosGame -= 10
        pygame.draw.rect(
            screen, black,
            [self.rectanglePosGame, 50, self.rectangleThicknessGame, 500])
        pygame.draw.rect(
            screen, green,
            [self.rectanglePosGame, 50, self.rectangleThicknessGame, 500], 5)
      pygame.draw.rect(
          screen, black,
          [self.rectanglePosGame, 50, self.rectangleThicknessGame, 500])
      pygame.draw.rect(
          screen, green,
          [self.rectanglePosGame, 50, self.rectangleThicknessGame, 500], 5)

    if self.rectangleThicknessGame >= 600:
      if self.boxNumber == 0:
        symptom = descriptionsFormatted[answerIndex][0][0:3][0:3]


      elif self.boxNumber == 1:
        symptom = descriptionsFormatted[answerIndex][1][0:3]


      elif self.boxNumber == 2:
        symptom = descriptionsFormatted[answerIndex][2][0:3]
        # print(symptom)


      text = font2.render(symptom[0], 1, green)
      screen.blit(text, (125, 100))
      #print(symptom[1])
      text1 = font2.render(symptom[1], 1, green)
      screen.blit(text1, (125, 150))
      #print(symptom[2])
      text2 = font2.render(symptom[2], 1, green)
      screen.blit(text2, (125, 200))
      
      #for i in range(len(symptom)):
      #[1,2,3]
      #[1]
      # print(symptom)
      #print(symptom)
      #text = font2.render(symptom[i], 1, green)

      #screen.blit(text, (100, 100))

if len(symptomsList[answerIndex]) >= 1:
  boxes = Boxes()
  boxes.boxesPos = symptomsPosition[answerIndex]
  boxes.symptomsOrgansMatch = symptoms.index(symptomsList[answerIndex][boxes.boxNumber])
  if len(symptomsList[answerIndex]) >= 2:
    boxes2 = Boxes()
    boxes2.boxNumber = 1
    boxes2.boxesPos = symptomsPosition[answerIndex]
    boxes2.symptomsOrgansMatch = symptoms.index(symptomsList[answerIndex][boxes2.boxNumber])
    if len(symptomsList[answerIndex]) == 3:
      boxes3 = Boxes()
      boxes3.boxNumber = 2
      boxes3.boxesPos = symptomsPosition[answerIndex]
      boxes3.symptomsOrgansMatch = symptoms.index(symptomsList[answerIndex][boxes3.boxNumber])

def titlePage():

  screen.fill(black)

  for x in range(0, screenSize[0], 50):
    for y in range(0, screenSize[1] * 4, 50):
      pygame.draw.rect(screen, dankGreen, (x, y - offset, 50, 50), 1)

  pygame.draw.rect(screen, buttonPlayGreen, (300, yButtonsPlay, 175, 50), 4)
  pygame.draw.rect(screen, buttonGreenCredits, (300, yButtonsCredits, 175, 50),
                   4)

  screen.blit(buttonCredits, (340, yOffsetTextPlay))
  screen.blit(buttonPlay, (358, yOffsetTextCredits))
  screen.blit(title, (190, titleYOffset))
  


def game():
  dankGreen = [0, 60, 0]
  screen.fill(black)
  for x in range(0, screenSize[0], 50):
    for y in range(0, screenSize[1] * 4, 50):
      pygame.draw.rect(screen, dankGreen, (x, y - offset, 50, 50), 1)
  pygame.draw.rect(screen, green, [213, 50, 350, 500], 4)
  pygame.draw.rect(screen, black, [217, 54, 340, 490])

  #backward button
  pygame.draw.rect(screen, backButtonGreen, [0, 0, 50, 50], 4)
  pygame.draw.polygon(screen, green, ((5, 25), (40, 5), (40, 45)))

  #forward button
  pygame.draw.rect(screen, forwardButtonGreen, [750, 550, 50, 50], 4)
  pygame.draw.polygon(screen, green, ((795, 575), (760, 595), (760, 555)))

  screen.blit(bodyDiagram, (240, 145))
  if len(symptomsList[answerIndex]) >= 1:
    boxes.draw()
    boxes.boxesPos = (100, 200)
    if len(symptomsList[answerIndex]) >= 2:
      boxes2.draw()
      boxes2.boxesPos = (100, 300)
      if len(symptomsList[answerIndex]) == 3:
        boxes3.draw()
        boxes3.boxesPos = (100, 500)


def trivia():
  screen.fill(black)

  for x in range(0, screenSize[0], 50):
    for y in range(0, screenSize[1] * 4, 50):
      pygame.draw.rect(screen, dankGreen, (x, y - offset, 50, 50), 1)

  pygame.draw.rect(screen, green, [125, 100, 550, 200], 4)

  #four boxes
  pygame.draw.rect(screen, ButtonAGreen, [125, 400, 250, 80], 4)
  pygame.draw.rect(screen, ButtonBGreen, [425, 400, 250, 80], 4)
  pygame.draw.rect(screen, ButtonCGreen, [125, 500, 250, 80], 4)
  pygame.draw.rect(screen, ButtonDGreen, [425, 500, 250, 80], 4)

  #backward button
  pygame.draw.rect(screen, backButton2Green, [0, 0, 50, 50], 4)
  pygame.draw.polygon(screen, green, ((5, 25), (40, 5), (40, 45)))

  #words
  screen.blit(question, [180, 190])
  screen.blit(option1, [150, 440])
  screen.blit(option2, [150, 540])
  screen.blit(option3, [450, 440])
  screen.blit(option4, [450, 540])


def victory():
  screen.fill(black)
  W = fontend.render("GG Doctor, I can't believe you got that!", 1, green)
  screen.blit(W, (50, 50))
  W1 = fontend.render("Now, go outside and get some air!", 1, green)
  screen.blit(W1, (100, 400))


loopExit = True
while loopExit:
  offset += 5
  if offset == 1000:
    offset = 0
  mousePosition = pygame.mouse.get_pos()
  hover = False
  hoverCredits = False
  hoverBack = False
  hover2Back = False
  hoverForward = False
  hoverLocationA = False
  hoverLocationB = False
  hoverLocationC = False
  hoverLocationD = False

  pygame.event.set_allowed(None)
  #for event detection
  # mousePosition = pygame.mouse.get_pos()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      loopExit = False

    if page == 0:

      if mousePosition[0] >= 300 and mousePosition[0] <= 475 and mousePosition[
          1] >= 400 and mousePosition[
              1] <= 450 and creditsButtonPressed == False:
        if event.type == pygame.MOUSEBUTTONDOWN:
          buttonPressed = True
        else:
          buttonPlayGreen = red
          hover = True
      elif hover == False:
        buttonPlayGreen = green
      if mousePosition[0] >= 300 and mousePosition[0] <= 475 and mousePosition[
          1] >= 475 and mousePosition[1] <= 525:
        if event.type == pygame.MOUSEBUTTONDOWN:
          creditsButtonPressed = True
        else:
          buttonGreenCredits = red
          hover = True
      elif hoverCredits == False:
        buttonGreenCredits = green

      if event.type == pygame.MOUSEBUTTONDOWN and creditsButtonPressed == True and mousePosition[
          0] >= rectanglePos and mousePosition[
              0] <= rectanglePos + rectangleThickness and mousePosition[
                  1] >= 50 and mousePosition[1] <= 500:
        backButtonPressedCredits = True

    if page == 1:
      if len(symptomsList[answerIndex]) >= 1:
        if event.type == pygame.MOUSEBUTTONDOWN and mousePosition[
            0] >= boxes.boxesPos[0] and mousePosition[0] <= boxes.boxesPos[
                0] + 70 and mousePosition[1] >= boxes.boxesPos[
                    1] and mousePosition[1] <= boxes.boxesPos[
                        1] + 70 and gameButtonPressed == False:
          # print(boxes.boxNumber)
          gameButtonPressed = True
      if len(symptomsList[answerIndex]) >= 2:
        if event.type == pygame.MOUSEBUTTONDOWN and mousePosition[
            0] >= boxes2.boxesPos[0] and mousePosition[0] <= boxes2.boxesPos[
                0] + 70 and mousePosition[1] >= boxes2.boxesPos[
                    1] and mousePosition[1] <= boxes2.boxesPos[
                        1] + 70 and gameButtonPressed2 == False:
          # print(boxes2.boxNumber)
          gameButtonPressed2 = True
      if len(symptomsList[answerIndex]) == 3:
        if event.type == pygame.MOUSEBUTTONDOWN and mousePosition[
            0] >= boxes3.boxesPos[0] and mousePosition[0] <= boxes3.boxesPos[
                0] + 70 and mousePosition[1] >= boxes3.boxesPos[
                    1] and mousePosition[1] <= boxes3.boxesPos[
                        1] + 70 and gameButtonPressed3 == False:
          # print(boxes3.boxNumber)
          gameButtonPressed3 = True

      if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        if gameButtonPressed:
          gameButtonPressed = False
        elif gameButtonPressed2:
          gameButtonPressed2 = False
        elif gameButtonPressed3:
          gameButtonPressed3 = False

#forward and backword buttons
      if mousePosition[0] <= 50 and mousePosition[0] >= 0 and mousePosition[
          1] <= 50 and mousePosition[1] >= 0:
        if event.type == pygame.MOUSEBUTTONDOWN:
          backButtonPressed = True
        else:
          backButtonGreen = red
          hoverBack = True
      elif hoverBack == False:
        backButtonGreen = green

      if mousePosition[0] <= 800 and mousePosition[0] >= 750 and mousePosition[
          1] <= 600 and mousePosition[1] >= 550:
        if event.type == pygame.MOUSEBUTTONDOWN:
          forwardButtonPressed = True
        else:
          forwardButtonGreen = red
          hover = True
      elif hoverForward == False:
        forwardButtonGreen = green

    

    if page == 3:
      #backbutton 2
      if mousePosition[0] <= 50 and mousePosition[0] >= 0 and mousePosition[1] <= 50 and mousePosition[1] >= 0:
        if event.type == pygame.MOUSEBUTTONDOWN:
          backButton2Pressed = True
        else:
          backButton2Green = red
          hover2Back = True
      elif hover2Back == False:
        BackButton2Green = green

      #answer buttons
      if mousePosition[0] <= 375 and mousePosition[0] >= 125 and mousePosition[
          1] <= 480 and mousePosition[1] >= 400:
        if event.type == pygame.MOUSEBUTTONDOWN:
          answerAButtonPressed = True
          if (answersList[0] == correctAnswer):
            winner = True
          elif (answersList[0] != correctAnswer):
            backButtonPressed = True
            page = 0
        else:
          ButtonAGreen = red
          hover = True
      elif hoverLocationA == False:
        ButtonAGreen = green

      if mousePosition[0] <= 675 and mousePosition[0] >= 425 and mousePosition[
          1] <= 480 and mousePosition[1] >= 400:
        if event.type == pygame.MOUSEBUTTONDOWN:
          answerBButtonPressed = True
          if (answersList[2] == correctAnswer):
            winner = True
          elif (answersList[2] != correctAnswer):
            backButtonPressed = True
            page = 0
        else:
          ButtonBGreen = red
          hover = True
      elif hoverLocationB == False:
        ButtonBGreen = green

      if mousePosition[0] <= 375 and mousePosition[0] >= 125 and mousePosition[
          1] <= 580 and mousePosition[1] >= 500:
        if event.type == pygame.MOUSEBUTTONDOWN:
          answerCButtonPressed = True
          if (answersList[1] == correctAnswer):
            winner = True
          elif (answersList[1] != correctAnswer):
            backButtonPressed = True
            page = 0
        else:
          ButtonCGreen = red
          hover = True
      elif hoverLocationC == False:
        ButtonCGreen = green

      if mousePosition[0] <= 675 and mousePosition[0] >= 425 and mousePosition[
          1] <= 580 and mousePosition[1] >= 500:
        if event.type == pygame.MOUSEBUTTONDOWN:
          answerDButtonPressed = True
          if (answersList[3] == correctAnswer):
            winner = True
          elif (answersList[3] != correctAnswer):
            backButtonPressed = True
            page = 0
        else:
          ButtonDGreen = red
          hover = True
      elif hoverLocationD == False:
        ButtonDGreen = green

      

  #print(hoverCredits)
  if buttonPressed == True:
    #animation for title --> game
    dankGreen = [0, 60 - colorDarken, 0]
    screen.blit(title, [190, titleYOffset])
    pygame.draw.rect(screen, green, [300, yButtonsPlay, 175, 50], 4)
    pygame.draw.rect(screen, green, [300, yButtonsCredits, 175, 50], 4)
    screen.blit(buttonCredits, [340, yOffsetTextPlay])
    screen.blit(buttonPlay, [358, yOffsetTextCredits])
    colorDarken += 3
    titleYOffset -= 10
    yButtonsPlay += 10
    yButtonsCredits += 10
    yOffsetTextPlay += 10
    yOffsetTextCredits += 10
    if colorDarken == 60:
      buttonPressed = False
      page = 1

  if backButtonPressed == True:
    dankGreen = [0, 60 + colorDarken, 0]
    screen.blit(title, [190, titleYOffset])
    pygame.draw.rect(screen, green, [300, yButtonsPlay, 175, 50], 4)
    pygame.draw.rect(screen, green, [300, yButtonsCredits, 175, 50], 4)
    screen.blit(buttonCredits, [340, yOffsetTextPlay])
    screen.blit(buttonPlay, [358, yOffsetTextCredits])
    colorDarken -= 3
    titleYOffset += 10
    yButtonsPlay -= 10
    yButtonsCredits -= 10
    yOffsetTextPlay -= 10
    yOffsetTextCredits -= 10
    if colorDarken == 0:
      backButtonPressed = False
      page = 0

  if forwardButtonPressed == True:
    # dankGreen = [0, 60 - colorDarken, 0]
    # colorDarken += 3
    # if colorDarken == 0:
    dankGreen = [0, 60, 0]
    forwardButtonPressed = False
    page = 3

  if backButton2Pressed == True:
    # dankGreen = [0, 60 - colorDarken, 0]
    # pygame.draw.rect(screen, green, [125, questionYbox, 550, 200], 4)
    # pygame.draw.rect(screen, ButtonAGreen, [125, ySubbox1, 250, 80], 4)
    # pygame.draw.rect(screen, ButtonBGreen, [425, ySubbox2, 250, 80], 4)
    # pygame.draw.rect(screen, ButtonCGreen, [125, ySubbox3, 250, 80], 4)
    # pygame.draw.rect(screen, ButtonDGreen, [425, ySubbox4, 250, 80], 4)

    # screen.blit(question, [180, 190])
    # screen.blit(option1, [150, 440])
    # screen.blit(option2, [150, 540])
    # screen.blit(option3, [450, 440])
    # screen.blit(option4, [450, 540])
    # colorDarken += 3
    # questionYbox -=10
    # ySubbox1 +=10
    # ySubbox2 +=10
    # ySubbox3 +=10
    # ySubbox4 +=10
    # if colorDarken == 60:
    # dankGreen = [0, 60, 0]
    backButton2Pressed = False
    backButton2Green = green
    page = 1

  mousePosition = pygame.mouse.get_pos()

  if page == 0:
    titlePage()
  if page == 1:
    game()
  if page == 3:
    trivia()
  if winner == True:
    victory()

  if creditsButtonPressed == True and backButtonPressedCredits == False:
    #animation for title --> credits
    if bottomEndpoint <= 555:
      pygame.draw.line(screen, green, (395, topEndpoint),
                       (395, bottomEndpoint), 5)
      bottomEndpoint += 10
      topEndpoint -= 10
    else:
      if rectangleThickness != 600:
        rectangleThickness += 20
        rectanglePos -= 10
      pygame.draw.rect(screen, black,
                       [rectanglePos, 50, rectangleThickness, 500])
      pygame.draw.rect(screen, green,
                       [rectanglePos, 50, rectangleThickness, 500], 5)
      if rectangleThickness == 600:
        cred_title = fontTitle.render("CREDITS", 1, green)
        screen.blit(cred_title, (150, 100))
        credit_1 = font2.render("Naayeli Prakash - User Interface Designer", 1, green)
        screen.blit(credit_1, (150, 200))
        credit_2 = font2.render("Terry Hao - Senior Developer", 1, green)
        screen.blit(credit_2, (150, 250))
        credit_3 = font2.render("Lang-Ji Li - Quality Assurance Engineer", 1, green)
        screen.blit(credit_3, (150, 300))
        credit_4 = font2.render("Jerry Huang - Lead Researcher", 1, green)
        screen.blit(credit_4, (150, 350))
        credit_5 = font2.render("Made by Pygame", 1, green)
        screen.blit(credit_5, (150, 400))
        credit_6 = font2.render("Thanks for HC Hackathon", 1, green)

  elif backButtonPressedCredits == True:
    #animation for credits --> title
    if rectangleThickness <= 600:
      rectangleThickness -= 20
      rectanglePos += 10
      pygame.draw.rect(screen, black,
                       [rectanglePos, 50, rectangleThickness, 500])
      pygame.draw.rect(screen, green,
                       [rectanglePos, 50, rectangleThickness, 500], 5)

    # elif rectangleThickness >= 600: 
    #   cred_title = fontTitle.render("CREDITS", 1, green)
    #   screen.blit(cred_title, (150, 100))
    #   credit_1 = font2.render("Naayeli Prakash - User Interface Designer/Artist", 1, green)
    #   screen.blit(credit_1, (150, 150))
    #   credit_2 = font2.render("Terry Hao - Senior Developer/Master Coder", 1, green)
    #   screen.blit(credit_2, (150, 200))
    #   credit_3 = font2.render("Lang-Ji Li - Quality Assurance Engineer/antiproblem", 1, green)
    #   screen.blit(credit_3, (150, 250))
    #   credit_4 = font2.render("Jerry Huang - Lead Researcher/investigator", 1, green)
    #   screen.blit(credit_4, (150, 350))
    #   credit_5 = font2.render("Made by Pygame", 1, green)
    #   screen.blit(credit_5, (150, 400))
    #   credit_6 = font2.render("Thanks for HC Hackathon", 1, green)

    else:
      if bottomEndpoint <= 555:
        pygame.draw.line(screen, green, (395, topEndpoint),
                         (395, bottomEndpoint), 5)
        bottomEndpoint -= 10
        topEndpoint += 10
    backButtonPressedCredits = False
    creditsButtonPressed = False

    rectangleThickness = 0
    rectanglePos = 395
    topEndpoint = 225
    bottomEndpoint = 375
    
    cred_title = fontTitle.render("CREDITS", 1, green)
    screen.blit(cred_title, (150, 100))
    credit_1 = font2.render("Naayeli Prakash - User Interface Designer", 1, green)
    screen.blit(credit_1, (150, 150))
    credit_2 = font2.render("Terry Hao - Senior Developer", 1, green)
    screen.blit(credit_2, (150, 200))
    credit_3 = font2.render("Lang-Ji Li - Quality Assurance Engineer", 1, green)
    screen.blit(credit_3, (150, 250))
    credit_4 = font2.render("Jerry Huang - Lead Researcher", 1, green)
    screen.blit(credit_4, (150, 350))
    credit_5 = font2.render("Made by Pygame", 1, green)
    screen.blit(credit_5, (150, 400))
    credit_6 = font2.render("Thanks for HC Hackathon", 1, green)


  if gameButtonPressed == True:
    boxes.click()
  if gameButtonPressed2 == True:
    boxes2.click()
  if gameButtonPressed3 == True:
    boxes3.click()
    
  #if text1complete = True:
  pygame.display.flip()
  clock.tick(60)
