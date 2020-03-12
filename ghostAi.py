from random import randint


def ghost_intersection_behavior(ghost, pacman, intersection):
    # special code for intersection 24
    if ghost.DEAD and intersection.number == 24:
        ghost.moving_left = False
        ghost.moving_right = False
        ghost.moving_up = False
        ghost.moving_down = True
    elif not ghost.DEAD and intersection.number == 24 and not ghost.last_intersection == intersection.number:
        ghost.moving_left = False
        ghost.moving_right = False
        ghost.moving_up = False
        ghost.moving_down = False
        if (pacman.rect.x <= ghost.rect.x and abs(pacman.rect.x - ghost.rect.x) > 3) and intersection.left:
            ghost.moving_left = True
        elif (pacman.rect.x >= ghost.rect.x and abs(pacman.rect.x - ghost.rect.x) > 3) and intersection.right:
            ghost.moving_right = True
        else:  # failsafe because ghosts keep getting stuck in the shield
            ghost.moving_left = True
        ghost.last_intersection = intersection.number

    # intersection 30 is the one in the box
    elif intersection.number == 30:
        ghost.moving_left = False
        ghost.moving_right = False
        ghost.moving_up = True
        ghost.moving_down = False

        ghost.DEAD = False
        ghost.afraid = False

    # x,y = 351, 234 is the location of intersection number 24, the entrance of the box
    elif ghost.DEAD:
        if ((abs(351 - ghost.rect.x) <= abs(234 - ghost.rect.y))
                and not ghost.last_intersection == intersection.number):
            ghost.moving_left = False
            ghost.moving_right = False
            ghost.moving_up = False
            ghost.moving_down = False
            if intersection.up or intersection.down:
                if (234 <= ghost.rect.y and abs(234 - ghost.rect.y) > 3) and intersection.up:
                    ghost.moving_up = True
                elif (234 >= ghost.rect.y and abs(234 - ghost.rect.y) > 3) and intersection.down:
                    ghost.moving_down = True
                elif intersection.left or intersection.right:
                    if intersection.left:
                        ghost.moving_left = True
                    elif intersection.right:
                        ghost.moving_right = True
            elif intersection.left or intersection.right:
                if (351 <= ghost.rect.x and abs(351 - ghost.rect.x) > 3) and intersection.left:
                    ghost.moving_left = True
                elif (351 >= ghost.rect.x and abs(351 - ghost.rect.x) > 3) and intersection.right:
                    ghost.moving_right = True
                elif intersection.up or intersection.down:
                    if intersection.up:
                        ghost.moving_up = True
                    elif intersection.down:
                        ghost.moving_down = True
            ghost.last_intersection = intersection.number

        elif ((abs(351 - ghost.rect.x) >= abs(234 - ghost.rect.y))
              and not ghost.last_intersection == intersection.number):
            ghost.moving_left = False
            ghost.moving_right = False
            ghost.moving_up = False
            ghost.moving_down = False
            if (intersection.left or intersection.right):
                if ((351 <= ghost.rect.x and abs(351 - ghost.rect.x) > 3) and intersection.left):
                    ghost.moving_left = True
                elif ((351 >= ghost.rect.x and abs(351 - ghost.rect.x) > 3) and intersection.right):
                    ghost.moving_right = True
                elif (intersection.up or intersection.down):
                    if (intersection.up):
                        ghost.moving_up = True
                    elif (intersection.down):
                        ghost.moving_down = True
            elif (intersection.up or intersection.down):
                if ((234 <= ghost.rect.y and abs(234 - ghost.rect.y) > 3) and intersection.up):
                    ghost.moving_up = True
                elif ((234 >= ghost.rect.y and abs(234 - ghost.rect.y) > 3) and intersection.down):
                    ghost.moving_down = True
                elif (intersection.left or intersection.right):
                    if (intersection.left):
                        ghost.moving_left = True
                    elif (intersection.right):
                        ghost.moving_right = True
            ghost.last_intersection = intersection.number

    elif (ghost.afraid):  # if afraid, run from pacman
        ghost.moving_left = False
        ghost.moving_right = False
        ghost.moving_up = False
        ghost.moving_down = False
        if (pacman.rect.x <= ghost.rect.x and abs(pacman.rect.x - ghost.rect.x) > 3):
            ghost.moving_right = True
        elif (pacman.rect.x >= ghost.rect.x and abs(pacman.rect.x - ghost.rect.x) > 3):
            ghost.moving_left = True
        if (pacman.rect.y <= ghost.rect.y and abs(pacman.rect.y - ghost.rect.y) > 3):
            ghost.moving_down = True
        elif (pacman.rect.y >= ghost.rect.y and abs(pacman.rect.y - ghost.rect.y) > 3):
            ghost.moving_up = True

    elif (randint(1,
                  100) <= 25 and not ghost.last_intersection == intersection.number):  # go in a random direction every once in a while
        ghost.moving_left = False
        ghost.moving_right = False
        ghost.moving_up = False
        ghost.moving_down = False
        while (True):
            if (randint(0, 1) == 0 and intersection.left):
                ghost.moving_left = True
                break
            elif (randint(0, 1) == 0 and intersection.right):
                ghost.moving_right = True
                break
            elif (randint(0, 1) == 0 and intersection.up):
                ghost.moving_up = True
                break
            elif (randint(0, 1) == 0 and intersection.down):
                ghost.moving_down = True
                break
        ghost.last_intersection = intersection.number

    elif ((abs(pacman.rect.x - ghost.rect.x) <= abs(pacman.rect.y - ghost.rect.y))
          and not ghost.last_intersection == intersection.number):
        ghost.moving_left = False
        ghost.moving_right = False
        ghost.moving_up = False
        ghost.moving_down = False
        if (intersection.up or intersection.down):
            if ((pacman.rect.y <= ghost.rect.y and abs(pacman.rect.y - ghost.rect.y) > 3) and intersection.up):
                ghost.moving_up = True
            elif ((pacman.rect.y >= ghost.rect.y and abs(pacman.rect.y - ghost.rect.y) > 3) and intersection.down):
                ghost.moving_down = True
            elif (intersection.left or intersection.right):
                if (intersection.left):
                    ghost.moving_left = True
                elif (intersection.right):
                    ghost.moving_right = True
        elif (intersection.left or intersection.right):
            if ((pacman.rect.x <= ghost.rect.x and abs(pacman.rect.x - ghost.rect.x) > 3) and intersection.left):
                ghost.moving_left = True
            elif ((pacman.rect.x >= ghost.rect.x and abs(pacman.rect.x - ghost.rect.x) > 3) and intersection.right):
                ghost.moving_right = True
            elif (intersection.up or intersection.down):
                if (intersection.up):
                    ghost.moving_up = True
                elif (intersection.down):
                    ghost.moving_down = True
        ghost.last_intersection = intersection.number

    elif ((abs(pacman.rect.x - ghost.rect.x) >= abs(pacman.rect.y - ghost.rect.y))
          and not ghost.last_intersection == intersection.number):
        ghost.moving_left = False
        ghost.moving_right = False
        ghost.moving_up = False
        ghost.moving_down = False
        if (intersection.left or intersection.right):
            if ((pacman.rect.x <= ghost.rect.x and abs(pacman.rect.x - ghost.rect.x) > 3) and intersection.left):
                ghost.moving_left = True
            elif ((pacman.rect.x >= ghost.rect.x and abs(pacman.rect.x - ghost.rect.x) > 3) and intersection.right):
                ghost.moving_right = True
            elif (intersection.up or intersection.down):
                if (intersection.up):
                    ghost.moving_up = True
                elif (intersection.down):
                    ghost.moving_down = True
        elif (intersection.up or intersection.down):
            if ((pacman.rect.y <= ghost.rect.y and abs(pacman.rect.y - ghost.rect.y) > 3) and intersection.up):
                ghost.moving_up = True
            elif ((pacman.rect.y >= ghost.rect.y and abs(pacman.rect.y - ghost.rect.y) > 3) and intersection.down):
                ghost.moving_down = True
            elif (intersection.left or intersection.right):
                if (intersection.left):
                    ghost.moving_left = True
                elif (intersection.right):
                    ghost.moving_right = True
        ghost.last_intersection = intersection.number