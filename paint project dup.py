import pygame   #imports pygame
pygame.init()   #initialises it


fps = 60  #frame rate
timer = pygame.time.Clock()   #clock speed
WIDTH, HEIGHT = 800, 600  #app res
active_size = 0
active_colour = "white"
screen = pygame.display.set_mode([WIDTH, HEIGHT])   #sets screen size
pygame.display.set_caption("Paint!")    #app name
painting = []




def draw_menu(size, colour):
    pygame.draw.rect(screen, "gray", [0, 0, WIDTH, 70])   #changes colour of interface area
    pygame.draw.line(screen, "black", (0,70), (WIDTH, 70), 3)   #outlines interface
    xl_brush = pygame.draw.rect(screen, "black", [10, 10, 50 , 50 ])   #makes brush size buttons
    pygame.draw.circle(screen, "white", (35, 35), 20)
    l_brush = pygame.draw.rect(screen, "black", [70, 10, 50 , 50 ])
    pygame.draw.circle(screen, "white", (95, 35), 15)
    m_brush = pygame.draw.rect(screen, "black", [130, 10, 50 , 50 ])
    pygame.draw.circle(screen, "white", (155, 35), 10)
    s_brush = pygame.draw.rect(screen, "black", [190, 10, 50 , 50 ])
    pygame.draw.circle(screen, "white", (215, 35), 5)
    brush_list = [xl_brush, l_brush, m_brush, s_brush]   #list of brushes

    if size == 20:
        pygame.draw.rect(screen, "green", [10, 10, 50, 50], 3)  #creates a border around paint brush sizes when selected
    elif size == 15:
        pygame.draw.rect(screen, "green", [70, 10, 50, 50], 3)
    elif size == 10:
        pygame.draw.rect(screen, "green", [130, 10, 50, 50], 3)
    elif size == 5:
        pygame.draw.rect(screen, "green", [190, 10, 50, 50], 3)

    pygame.draw.circle(screen, colour, (400, 35), 30)   #makes circle to show what your selected coulour is
    pygame.draw.circle(screen, "dark gray", (400, 35), 30, 3)  

    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25])   #colour boxes in top right
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 35, 35, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25])
    teal = pygame.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 10, 25, 25])
    purple = pygame.draw.rect(screen, (255, 0, 255), [WIDTH - 85, 35, 25, 25])
    white = pygame.draw.rect(screen, (255, 255, 255), [WIDTH - 110, 10, 25, 25])
    black = pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 35, 25, 25])
    colour_rect = [blue, green, red, yellow, teal, purple, white, black]
    rgb_list = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255), (255, 255, 255), (0, 0, 0)]

    return brush_list, colour_rect, rgb_list

def draw_painting(paints):
    for i in range(len(paints)):
        pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])   #draws circle

run = True
while run:
    timer.tick(fps)   #sets refresh rate
    screen.fill("white")   #bg colour
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    
    if left_click and mouse[1] > 70:   #if aint on interface you can see it
        painting.append((active_colour, mouse, active_size))
    draw_painting(painting)

    if mouse[1] > 70:   #hides drawing on interface
        pygame.draw.circle(screen, active_colour, mouse, active_size)

    brushes, colours, rgbs = draw_menu(active_size, active_colour)   #calls brush size and colour into main program

    for event in pygame.event.get():   #gets input
        if event.type == pygame.QUIT:   #checks for when user presses quit
            run = False   #stops app

        if event.type == pygame.MOUSEBUTTONDOWN:    #if mouse button 1 is pressed:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):   #checks if mouse is on brush button
                    active_size = 20 - (i * 5)    #sets brush size
    
            for i in range(len(colours)):
                if colours[i].collidepoint(event.pos):   #checks if mouse is on brush button
                    active_colour = rgbs[i]    #sets active colour

    pygame.display.flip()    #allows you to input stuff onto screen

pygame.quit()
