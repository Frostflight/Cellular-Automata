###------------------------------------------------------------------------
###Program: Game of Life Simulation
###------------------------------------------------------------------------

def main():
    #User Config
    scale = 8
    randomize = True

    #System Display Dimensions
    xDimDisplay = 1920
    yDimDisplay = 1080

    #Array Dimensions
    xDim = xDimDisplay//scale
    yDim = yDimDisplay//scale

    #Initialize boolean flags
    activeLayer = 0
    running = True
    pause = False
    draw = False
    grid = False
    erase = False
    line = False
    lineStart = False


    #Randomize strating array if flagged to do so
    if randomize:
        from random import randint
        array = [[[0 for x in range(xDim+2)] for y in range(yDim+2)] for copy in range(2)]

        #Values are randomized such that there is an empty buffer of 0s outside the visible range.
        for x in range(1,xDim+1):
            for y in range(1,yDim+1):
                array[0][y][x] = randint(0,1)
                
    #Otherwise, initialize empty array
    else:
        array = [[[0 for x in range(xDim+2)] for y in range(yDim+2)] for copy in range(2)]


    #Pygame startup
    import pygame
    pygame.init()
    screen = pygame.display.set_mode((xDimDisplay,yDimDisplay), pygame.FULLSCREEN)

    #Main Loop
    while running:
        if not pause:
            for x in range(1,(xDim+1)):
                for y in range(1,(yDim+1)):
                    near = (array[activeLayer][y+1][x+1]
                            + array[activeLayer][y+1][x]
                            + array[activeLayer][y+1][x-1]
                            + array[activeLayer][y][x+1]
                            + array[activeLayer][y][x-1]
                            + array[activeLayer][y-1][x+1]
                            + array[activeLayer][y-1][x]
                            + array[activeLayer][y-1][x-1])
                    if near == 3:
                        array[not activeLayer][y][x] = 1
                    elif near > 3 or near < 2:
                        array[not activeLayer][y][x] = 0
                    else:
                        array[not activeLayer][y][x] = array[activeLayer][y][x]
            for x in range(1,(xDim+1)):
                for y in range(1,(yDim+1)):
                    if array[activeLayer][y][x]:
                        pygame.draw.rect(screen,(255,255,255),pygame.Rect(x*scale-scale,y*scale-scale,scale,scale))
                    else:
                        pygame.draw.rect(screen,(0,0,0),pygame.Rect(x*scale-scale,y*scale-scale,scale,scale))
            
            activeLayer = not activeLayer

        if grid:
            for x in range(0,xDimDisplay//scale):
                pygame.draw.line(screen,(40,40,100),(x*scale,0),(x*scale,yDimDisplay))
            for y in range(0,yDimDisplay//scale):
                pygame.draw.line(screen,(40,40,100),(0,y*scale),(xDimDisplay,y*scale))

        if pause:
            pygame.draw.line(screen,(255,0,0),(0,0),(1919,0))
            pygame.draw.line(screen,(255,0,0),(1919,0),(1919,1079))
            pygame.draw.line(screen,(255,0,0),(1919,1079),(0,1079))
            pygame.draw.line(screen,(255,0,0),(0,1079),(0,0))

        if pause and draw:
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]

            boxX = mouseX - (mouseX%scale)
            boxY = mouseY - (mouseY%scale)
            
            pygame.draw.rect(screen,(150,255,150),pygame.Rect(boxX,boxY,scale,scale))

            array[activeLayer][boxY//scale+1][boxX//scale+1] = 1
            array[not activeLayer][boxY//scale+1][boxX//scale+1] = 1
            

        if pause and draw and erase:
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]

            boxX = mouseX - (mouseX%scale)
            boxY = mouseY - (mouseY%scale)
            
            pygame.draw.rect(screen,(100,0,0),pygame.Rect(boxX,boxY,scale,scale))

            array[activeLayer][boxY//scale+1][boxX//scale+1] = 0
            array[not activeLayer][boxY//scale+1][boxX//scale+1] = 0
        
        pygame.display.flip()    

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                
                if event.key == 114:
                    pause = not pause

                if event.key == 117:
                    grid = not grid

                if event.key == 308:
                    erase = True
                    
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()

                if event.key == 105:
                    array = [[[0 for x in range(xDim+2)] for y in range(yDim+2)] for copy in range(2)]

                if event.key == 111:
                    for x in range(1,xDim+1):
                        for y in range(1,yDim+1):
                            array[0][y][x] = randint(0,1)

            if event.type == pygame.KEYUP:
                if event.key == 308:
                    erase = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                draw = True

            if event.type == pygame.MOUSEBUTTONUP:
                draw = False

if __name__ == "__main__":
    main()
