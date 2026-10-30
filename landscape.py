import pygame
import math




pygame.init()


WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)


screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


# ---------------------------
# Initialize global variables

circle_x = 300
circle_y = 300
cat_color = ("#424040")


cloud_x = 50
cloud_y = 50
x = 10

tri_x = 40 
tri_y = 40 
tri_z = 40 


# ---------------------------


running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)


    # GAME STATE UPDATES
    # All game math and comparisons happen here
    cloud_x += 5


    if cloud_x > WIDTH:
        cloud_x = -169

    x += 4
    y = ((x - WIDTH // 2) ** 2) / 300 + 100
    #     0   640   // 2 diff pos  smaller the# cruve lower 
    

    if x > WIDTH: 
        background_color = "#130426" 
        tree_color = "#033d0b"
        hill_color = "#06330c"
        treewood_color = "#292123"
        cat_color = "#2f332f"
        cloud_color = "#4a1d82"
        star_color = "#ffe600"
    else:    
        background_color = "#311270"
        tree_color = "#397a0d"
        hill_color = "#0c4a07"
        treewood_color = "#231709"
        cloud_color = "#A486F7"
        cat_color = "#424040"
        star_color = "#311270"

    

    tree1_point = [
    (180, 234),
    (146, 268),
    (208, 268)
    ]

    tree2_point = [
    (177, 265),
    (142, 302),
    (210, 299)
    ]

    tree3_point = [
    (179, 302),
    (144, 331),
    (217, 330)
    ]

    tree4_point = [
    (442, 221),
    (411, 255),
    (477, 257)
    ]

    tree5_point = [
    (441, 253),
    (401, 288),
    (472, 292)
    ]

    tree6_point = [
    (439, 290),
    (408, 317),
    (473, 319)
    ]

    

    treewood1_point = (167, 332, 20, 40)
    treewood2_point = (427, 320, 20, 40)

    catear1_point = [
    (circle_x -18, circle_y - 25),
    (circle_x -18, circle_y - 7),
    (circle_x -10, circle_y -18)
    ]
    
    catear2_point = [
    (circle_x +14, circle_y -26),
    (circle_x +8, circle_y -18),
    (circle_x +17, circle_y -8)
    ]

    # DRAWING

    screen.fill(background_color)  # always the first drawing command

    #stars 
    pygame.draw.circle(screen, star_color, (506, 51), 2)
    pygame.draw.circle(screen, star_color, (382, 33), 2)
    pygame.draw.circle(screen, star_color, (301, 121), 2)
    pygame.draw.circle(screen, star_color, (395, 141), 2)
    pygame.draw.circle(screen, star_color, (490, 154), 2)
    pygame.draw.circle(screen, star_color, (229, 162), 2)
    pygame.draw.circle(screen, star_color, (346, 243), 2)
    pygame.draw.circle(screen, star_color, (498, 230), 2)
    pygame.draw.circle(screen, star_color, (157, 194), 2)
    pygame.draw.circle(screen, star_color, (250, 158), 2)
    pygame.draw.circle(screen, star_color, (250, 158), 2)
    pygame.draw.circle(screen, star_color, (250, 158), 2)
    pygame.draw.circle(screen, star_color, (250, 158), 2)
    pygame.draw.circle(screen, star_color, (93, 83), 2)
    pygame.draw.circle(screen, star_color, (186, 30), 2)
    pygame.draw.circle(screen, star_color, (58, 143), 2)
    pygame.draw.circle(screen, star_color, (186, 30), 2)
    pygame.draw.circle(screen, star_color, (39, 38), 2)
    pygame.draw.circle(screen, star_color, (26, 214), 2)
    pygame.draw.circle(screen, star_color, (90, 262), 2)
    pygame.draw.circle(screen, star_color, (46, 318), 2)
    pygame.draw.circle(screen, star_color, (382, 286), 2)
    pygame.draw.circle(screen, star_color, (276, 230), 2)
    pygame.draw.circle(screen, star_color, (222, 291), 2)
    pygame.draw.circle(screen, star_color, (391, 215), 2)
    pygame.draw.circle(screen, star_color, (580, 132), 2)
    pygame.draw.circle(screen, star_color, (623, 240), 2)
    pygame.draw.circle(screen, star_color, (503, 334), 2)
    pygame.draw.circle(screen, star_color, (546, 273), 2)
    pygame.draw.circle(screen, star_color, (618, 359), 2)
    pygame.draw.circle(screen, star_color, (202, 87), 2)

   
    circle_color = ((200, 200, 200))
    pygame.draw.circle(screen, circle_color, (x,y), 40)

    # Hill
    hill_rect = (-50, HEIGHT -150, WIDTH + 100, HEIGHT)
    pygame.draw.ellipse(screen, hill_color, hill_rect)

    
    #tree
    pygame.draw.polygon(screen, tree_color, tree1_point)
    pygame.draw.polygon(screen, tree_color, tree2_point)
    pygame.draw.polygon(screen, tree_color, tree3_point)
    pygame.draw.polygon(screen, tree_color, tree4_point)
    pygame.draw.polygon(screen, tree_color, tree5_point)
    pygame.draw.polygon(screen, tree_color, tree6_point)
    pygame.draw.rect(screen, treewood_color, treewood1_point) 
    pygame.draw.rect(screen, treewood_color, treewood2_point) 

    #cat 
    cat_rect = (circle_x - 10, circle_y + 10, 60, 40)

    pygame.draw.ellipse(screen, cat_color, cat_rect)
    pygame.draw.circle(screen, cat_color, (circle_x, circle_y), 20)
    pygame.draw.polygon(screen, cat_color, catear1_point) 
    pygame.draw.polygon(screen, cat_color, catear2_point) 


    #clouds
    
    cloud_speed = x
    pygame.draw.circle(screen, cloud_color, (cloud_x + 74, cloud_y + 39), 40)
    pygame.draw.circle(screen, cloud_color, (cloud_x + 123, cloud_y + 66), 40)
    pygame.draw.circle(screen, cloud_color, (cloud_x + 56, cloud_y + 66), 40)
    pygame.draw.circle(screen, cloud_color, (cloud_x + 104, cloud_y + 82), 40)

    

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------




pygame.quit()
