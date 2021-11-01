import pygame,pygame.image, pygame.display, pygame.event,pygame.mouse, pygame.sprite
pygame.init()
windowName = pygame.image.load('lugi.png')
bigButton = pygame.image.load('board.png')
screen = pygame.display.set_mode((400,400))
buttonCords = []
buttons = []
for col in range(0,400, 100):

    for row in range(0, 400, 100):
        
        buttons += [screen.blit(bigButton, (row, col))]
        buttonCords += [[row,col]]
#background.set_colorkey((0,0,0))
pygame.display.set_icon(windowName)
pygame.display.set_caption("minimal program")

print(buttonCords)

# create a surface on screen that has the size of 240 x 180


from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
class X(pygame.sprite.Sprite):
    def __init__(self):
        super(X, self).__init__()
        self.image = pygame.image.load('redDot.png').convert_alpha()
        
        self.rect = self.image.get_rect()
all_sprites_list  = pygame.sprite.Group()
le = X()
all_sprites_list.add(le)
def main():
    
    # lode window information
   
    
    
    # define a variable to control the main loop
    running = True

    # how many pixels we move our smiley each frame
    xpos = 50
    ypos = 50
    # how many pixels we move our smiley each frame
    step_x = 1
    step_y = 1
    while running:
        # event handling, gets all event from the event queue
        # check if the smiley is still on screen, if not change direction
           
        pygame.display.flip()  
        clickLoc = pygame.mouse.get_pos() 
        for event in pygame.event.get():
            # click light goes on
            #screen.blit(background, (0,0))
            if pygame.mouse.get_pressed()[0]:#get_focused()
                # test1 controlls the first col positions
                test1 = 100

                for buttonLoc in buttonCords:
                   # i have 2 lists with intergers i should add them and see what numbers i get between them
                    if (clickLoc[0] <= test1 and clickLoc[1] >= test1) :
                        # add if stament for clicklock[1] for button row in col 0,
                        # if y <= 100: ect. 0 t0 400
                    
                        le.rect.x , le.rect.y = buttonLoc
                        all_sprites_list.draw(screen)
                        
                        print(buttonLoc, clickLoc)
                        break
                    elif (clickLoc[0] >= test1) and clickLoc[1] <= test1:
                        le.rect.x , le.rect.y = buttonLoc
                        all_sprites_list.draw(screen)
                    
                        print(buttonLoc, clickLoc)
                        break
                    else:
                        test1 += 100
                        pass
                        
                    
                # first erase the screen 
                
                
                pygame.display.flip()
                # and update the screen               
                
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
