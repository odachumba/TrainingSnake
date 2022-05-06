
#defining our gameloop function
def gameloop():

    #setting background image
    bg = pygame.image.load('car game/bg.png')

    
    # setting our player
    maincar = pygame.image.load('car game\car.png')
    maincarX = 350
    maincarY = 495

    #other cars
    car1 = pygame.image.load('car game\car1.jpeg')
    car2 = pygame.image.load('car game\car2.png')
    car3 = pygame.image.load('car game\car3.png')

    
    


   
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
