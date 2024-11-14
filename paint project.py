import pygame  # imports pygame 
import os
pygame.init()  # initializes it

fps = 360 # frame rate
timer = pygame.time.Clock()  # clock speed
WIDTH, HEIGHT = 800, 600  # app resolution
active_size = 0
active_colour = "white"
screen = pygame.display.set_mode([WIDTH, HEIGHT])  # sets screen size
pygame.display.set_caption("Paint.")  # app name
in_settings = False
painting = []
painting_surface = pygame.Surface((WIDTH, HEIGHT))
painting_surface.fill("white")

# Set up font 
font = pygame.font.SysFont("Comic Sans MS", 20)  # use Comic Sans with font size 20
settings_font = pygame.font.SysFont("Times New Roman", 30)
title_font = pygame.font.SysFont("Times New Roman", 60)

def draw_menu(size, colour):
    pygame.draw.rect(screen, "gray", [0, 0, WIDTH, 70])  # interface area color
    pygame.draw.line(screen, "black", (0, 70), (WIDTH, 70), 3)  # interface outline

    # Brush size buttons
    xl_brush = pygame.draw.rect(screen, "black", [70, 10, 50, 50])
    pygame.draw.circle(screen, "white", (95, 35), 15)
    l_brush = pygame.draw.rect(screen, "black", [130, 10, 50, 50])
    pygame.draw.circle(screen, "white", (155, 35), 12)
    m_brush = pygame.draw.rect(screen, "black", [190, 10, 50, 50])
    pygame.draw.circle(screen, "white", (215, 35), 9)
    s_brush = pygame.draw.rect(screen, "black", [250, 10, 50, 50])
    pygame.draw.circle(screen, "white", (275, 35), 6)
    brush_list = [xl_brush, l_brush, m_brush, s_brush]  # list of brushes

    # Highlight selected brush size
    if size == 15:
        pygame.draw.rect(screen, "green", [70, 10, 50, 50], 3)
    elif size == 12:
        pygame.draw.rect(screen, "green", [130, 10, 50, 50], 3)
    elif size == 9:
        pygame.draw.rect(screen, "green", [190, 10, 50, 50], 3)
    elif size == 6:
        pygame.draw.rect(screen, "green", [250, 10, 50, 50], 3)


    # Display selected color circle
    pygame.draw.circle(screen, colour, (400, 35), 30)
    pygame.draw.circle(screen, "black", (400, 35), 30, 3)

    # Color selection boxes
    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 35, 35, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25])
    teal = pygame.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 10, 25, 25])
    purple = pygame.draw.rect(screen, (255, 0, 255), [WIDTH - 85, 35, 25, 25])
    grey = pygame.draw.rect(screen, (128, 128, 128), [WIDTH - 110, 10, 25, 25])
    black = pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 35, 25, 25])

    #erase box
    erase = pygame.draw.rect(screen, (255, 255, 255), [WIDTH - 250, 10, 50, 50])
    if active_colour == (255, 255, 255):  # Highlight with green if erase is selected
        pygame.draw.rect(screen, "green", [WIDTH - 250, 10, 50, 50], 3)
    else:
        pygame.draw.rect(screen, "black", [WIDTH - 250, 10, 50, 50], 3)

    erase_img = pygame.image.load("erase.png")
    erase_img = pygame.transform.scale(erase_img, (40, 40))
    screen.blit(erase_img, (WIDTH - 246, 15))

    colour_rect = [blue, green, red, yellow, teal, purple, grey, black, erase]
    rgb_list = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 0), (0, 255, 255), (255, 0, 255), (128, 128, 128), (0, 0, 0), (255, 255, 255)]

    # settings box
    settings_box = pygame.draw.rect(screen, "white", [10, 10, 50, 50])
    settings_img = pygame.image.load("settings.png")
    settings_img = pygame.transform.scale(settings_img, (40, 40))
    screen.blit(settings_img, (14, 15))
    pygame.draw.rect(screen, "black", [10, 10, 50, 50], 3)

    # Clear box
    clear_box = pygame.draw.rect(screen, "white", [WIDTH - 180, 10, 50, 50])
    pygame.draw.rect(screen, "black", [WIDTH - 180, 10, 50, 50], 3)  # border for Clear box

    # clear image
    clear_img = pygame.image.load("clear.png")
    clear_img = pygame.transform.scale(clear_img, (40, 40))
    screen.blit(clear_img, (WIDTH - 176, 15))


    return brush_list, colour_rect, rgb_list, clear_box, settings_box

def draw_painting(paints):
    for i in range(len(paints)):
        pygame.draw.circle(painting_surface, paints[i][0], paints[i][1], paints[i][2])  # draws circle

def draw_settings():
    screen.fill("lightgray")

    save_button = pygame.draw.rect(screen, "black", [285, 225, 225, 50])    # YOU HAVE NOT CODED THE FUNCTION YET
    load_button = pygame.draw.rect(screen, "black", [285, 325, 225, 50])     # YOU HAVE NOT CODED THE FUNCTION YET
    close_button = pygame.draw.rect(screen, "black", [285, 425, 225, 50])
    

    # render text for boxes and put it on screen
    settings_title = title_font.render("Settings:", True, "black")
    save_text = settings_font.render("Save", True, "white")
    load_text = settings_font.render("Load", True, "white")
    close_text = settings_font.render("Close settings", True, "white")

    screen.blit(settings_title, (292, 95))
    screen.blit(save_text, (368, 235))
    screen.blit(load_text, (367, 335))
    screen.blit(close_text, (314, 435))
    return close_button, save_button, load_button

def save_painting():
    global in_settings
    input_active = True
    user_text = ''
    while input_active:
        screen.fill("grey")
        prompt_text = settings_font.render("Enter file name: ", True, "black")
        user_input = settings_font.render(user_text, True, "black")
        screen.blit(prompt_text, (305, HEIGHT // 2 - 50))
        screen.blit(user_input, (50, HEIGHT // 2))

        # Draw the Back button
        back_button = pygame.draw.rect(screen, "black", [10, 10, 100, 40])  # Back button position
        back_text = font.render("Back", True, "white")
        screen.blit(back_text, (38, 15))

        save_title = title_font.render("Save Image", True, "black")
        screen.blit(save_title, (258, 95))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                input_active = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):  # Check if "Back" button is clicked
                    input_active = False
                    in_settings = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Save on 'Enter' key
                    file_path = os.path.expanduser(f"~/Downloads/{user_text}")
                    pygame.image.save(painting_surface, file_path)
                    print("Painting saved to", file_path)
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]  # Handle backspace
                else:
                    user_text += event.unicode  # Append new character

        pygame.display.flip()

def load_painting():
    global in_settings
    global painting
    input_active = True
    user_text = ''
    while input_active:
        screen.fill("grey")
        prompt_text = settings_font.render("Enter file name to load: ", True, "black")
        user_input = settings_font.render(user_text, True, "black")
        screen.blit(prompt_text, (255, HEIGHT // 2 - 50))
        screen.blit(user_input, (50, HEIGHT // 2))

        # Draw the Back button
        back_button = pygame.draw.rect(screen, "black", [10, 10, 100, 40])  # Back button position
        back_text = font.render("Back", True, "white")
        screen.blit(back_text, (38, 15))

        load_title = title_font.render("Load Image", True, "black")
        screen.blit(load_title, (255, 95))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                input_active = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):  # Check if "Back" button is clicked
                    input_active = False
                    in_settings = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Load on 'Enter' key
                    file_path = os.path.expanduser(f"~/Downloads/{user_text}")
                    try:
                        loaded_image = pygame.image.load(file_path)
                        loaded_image = pygame.transform.scale(loaded_image, (WIDTH, HEIGHT))  # Scale to fit canvas
                        painting = []  # clear painting
                        painting_surface.fill("white")
                        painting_surface.blit(loaded_image, (0, 0))  # Display on the painting surface
                        print(f"Loaded painting from {file_path}")
                    except FileNotFoundError:
                        print(f"File {file_path} not found. Please ensure the file exists in Downloads.")
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]  # Handle backspace
                else:
                    user_text += event.unicode  # Append new character

        pygame.display.flip()

run = True
prev_mouse_pos = None

while run:
    timer.tick(fps)  # sets refresh rate
    screen.fill("white")  # background color
    screen.blit(painting_surface, (0, 0))
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]

    if not in_settings:

        if left_click and mouse[1] > 70:  # if not on interface area
            painting.append((active_colour, mouse, active_size))
            if prev_mouse_pos:
                pygame.draw.line(painting_surface, active_colour, prev_mouse_pos, mouse, active_size * 2)
            prev_mouse_pos = mouse
        else:
            prev_mouse_pos = None

        if left_click and mouse[1] > 70:  # Prevent drawing on interface area
            pygame.draw.circle(painting_surface, active_colour, mouse, active_size)
            painting.append((active_colour, mouse, active_size))

        brushes, colours, rgbs, clear_box, settings_box = draw_menu(active_size, active_colour)  # call menu elements
    
    else:
        close_button, save_button, load_button = draw_settings()

    for event in pygame.event.get():  # get input
        if event.type == pygame.QUIT:  # check for quit event
            run = False  # stop app

        if left_click:
            if not in_settings:
                if clear_box.collidepoint(event.pos):  # if "clear" box clicked
                    painting = []  # clear painting
                    painting_surface.fill("white")
            
                if settings_box.collidepoint(event.pos):  # if "settings" box clicked
                    in_settings = True

                for i in range(len(brushes)):
                    if brushes[i].collidepoint(event.pos):  # check if brush selected
                        active_size = 15 - (i * 3)  # set brush size

                for i in range(len(colours)):
                    if colours[i].collidepoint(event.pos):  # check if color selected
                        active_colour = rgbs[i]  # set active color
            else:
                if close_button.collidepoint(event.pos):
                    in_settings = False
                
                elif save_button.collidepoint(event.pos):
                    save_painting()

                elif load_button.collidepoint(event.pos):
                    load_painting()

    pygame.display.flip()  # update display

pygame.quit()
