import pygame
import pyperclip
import json
import win32clipboard
import ast

# Initialize pygame
pygame.init()

# CONSTANTS
GRID_SIZE = [8, 32]
FONT = pygame.font.SysFont("calibri, arial", 20)
STR_FONT = pygame.font.SysFont("calibri, arial", 10)

MAX_STORAGE = 20000000
START_WARNING = 80
START_ERROR = 100

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)

tools = [WHITE, GREEN, RED, BLUE, YELLOW, PURPLE]

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
MARGIN = 1

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(GRID_SIZE[0]):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(GRID_SIZE[1]):
        grid[row].append(0)  # Append a cell

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[1][5] = 1

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [672, 350]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption(f"yay v1.2")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Variables
selection = 1
show_string = False
storage_used = 0
final_str = []
animation_fps = 60
change_fps = False
page = 1
show_clipboard_paste = False
show_text_clipboard_paste_error = False


# Funcitons


def display_image(image):
    for i in range(256):
        y = i // 8
        x = i % 8

        if str(x) + " " + str(y) in list(image.keys()):
            if image[str(x) + " " + str(y)] == 1:
                color = (0, 255, 0)
            elif image[str(x) + " " + str(y)] == 2:
                color = (255, 0, 0)
            elif image[str(x) + " " + str(y)] == 3:
                color = (0, 0, 255)
            elif image[str(x) + " " + str(y)] == 4:
                color = (255, 255, 0)
            elif image[str(x) + " " + str(y)] == 5:
                color = (255, 0, 255)
            else:
                color = (255, 255, 255)

            if y % 2 == 0:
                pygame.draw.rect(screen, color, [(y * 21), (x * 21), 20, 20])
            else:
                pygame.draw.rect(screen, color, [(y * 21), 147 - (x * 21), 20, 20])


# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            try:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row = pos[1] // (HEIGHT + MARGIN)
                # Set that location to one
                grid[row][column] = selection
                print("Click ", pos, "Grid coordinates: ", row, column)

                # Update string
                new_list = {}

                for count, i in enumerate(grid):
                    for second_count, j in enumerate(i):
                        if j != 0:
                            if second_count % 2 == 0:
                                new_list[f'{count} {second_count}'] = j
                            else:
                                new_list[f'{7 - count} {second_count}'] = j

                pygame.display.set_mode((672, 450))
                show_string = True
                print(new_list)

                storage_used = len(str(final_str))

            except:
                pos = pygame.mouse.get_pos()

                if 200 < pos[1] < 230:
                    if 10 < pos[0] < 40:
                        selection = 0
                    elif 41 < pos[0] < 71:
                        selection = 1
                    elif 72 < pos[0] < 102:
                        selection = 2
                    elif 103 < pos[0] < 133:
                        selection = 3
                    elif 134 < pos[0] < 164:
                        selection = 4
                    elif 165 < pos[0] < 195:
                        selection = 5

                if page == 1:
                    pos = pygame.mouse.get_pos()

                    if 440 < pos[0] < 540 and 300 < pos[1] < 330:
                        # Clear Frame

                        grid = []
                        for row in range(GRID_SIZE[0]):
                            # Add an empty array that will hold each cell
                            # in this row
                            grid.append([])
                            for column in range(GRID_SIZE[1]):
                                grid[row].append(0)  # Append a cell

                    elif 550 < pos[0] < 650 and 300 < pos[1] < 330:
                        # Add frame

                        if storage_used < MAX_STORAGE:
                            try:
                                final_str.append(new_list)
                                storage_used = len(str(final_str))
                            except:
                                pass

                    elif 550 < pos[0] < 650 and 400 < pos[1] < 430:
                        # Copy load string
                        pyperclip.copy(str(final_str))

                    elif 330 < pos[0] < 430 and 300 < pos[1] < 330:
                        # Clear all
                        final_str = []

                    elif 220 < pos[0] < 320 and 300 < pos[1] < 330:
                        # Preview
                        for count, i in enumerate(final_str):
                            pygame.event.pump()
                            screen.fill(BLACK)
                            display_image(i)
                            clock.tick(animation_fps)

                            pygame.draw.rect(screen, WHITE, [10, 180, 652, 15])
                            try:
                                pygame.draw.rect(screen, GREEN, [10, 180, round((count / len(final_str)) * 652), 15])
                            except ZeroDivisionError:
                                pass

                            text = FONT.render(f"{round(len(final_str) / animation_fps)}s", True, WHITE)
                            screen.blit(text, (632, 200))

                            text = FONT.render(f"{round(count / animation_fps, 1)}s", True, WHITE)
                            screen.blit(text, (10, 200))

                            pygame.display.update()

                    elif 150 < pos[0] < 210 and 300 < pos[1] < 330:
                        change_fps = True

                    elif 60 < pos[0] < 90 and 300 < pos[1] < 330:
                        page = 2

                    else:
                        change_fps = False

                else:
                    pos = pygame.mouse.get_pos()

                    if 550 < pos[0] < 650 and 300 < pos[1] < 330:
                        # Delete frame

                        if len(final_str) != 0 and len(final_str) != 1:
                            grid = []
                            last_frame = final_str[len(final_str) - 2]

                            for row in range(GRID_SIZE[0]):
                                # Add an empty array that will hold each cell
                                # in this row
                                grid.append([])
                                for column in range(GRID_SIZE[1]):
                                    if column % 2 == 1:
                                        if f"{7 - row} {column}" in list(last_frame.keys()):
                                            grid[row].append(last_frame[f"{7 - row} {column}"])  # Append a cell
                                        else:
                                            grid[row].append(0)
                                    else:
                                        if f"{row} {column}" in list(last_frame.keys()):
                                            grid[row].append(last_frame[f"{row} {column}"])  # Append a cell
                                        else:
                                            grid[row].append(0)

                            del final_str[-1]
                            storage_used = len(str(final_str))

                    elif 440 < pos[0] < 540 and 300 < pos[1] < 330:
                        pygame.display.set_mode((672, 550))
                        show_clipboard_paste = True

                    elif 440 < pos[0] < 540 and 510 < pos[1] < 540:
                        show_text_clipboard_paste_error = False
                        show_clipboard_paste = False
                        pygame.display.set_mode((672, 350))

                    elif 550 < pos[0] < 650 and 510 < pos[1] < 540:
                        try:
                            show_text_clipboard_paste_error = False

                            win32clipboard.OpenClipboard()
                            animation_string = win32clipboard.GetClipboardData()
                            win32clipboard.CloseClipboard()

                            final_list = []

                            animation_string = animation_string.replace("'", "\"")
                            json_decode = ast.literal_eval(animation_string)

                            final_str = json_decode

                            grid = []
                            last_frame = final_str[-1]

                            for row in range(GRID_SIZE[0]):
                                # Add an empty array that will hold each cell
                                # in this row
                                grid.append([])
                                for column in range(GRID_SIZE[1]):
                                    if column % 2 == 1:
                                        if f"{7 - row} {column}" in list(last_frame.keys()):
                                            grid[row].append(last_frame[f"{7 - row} {column}"])  # Append a cell
                                        else:
                                            grid[row].append(0)
                                    else:
                                        if f"{row} {column}" in list(last_frame.keys()):
                                            grid[row].append(last_frame[f"{row} {column}"])  # Append a cell
                                        else:
                                            grid[row].append(0)

                            show_clipboard_paste = False
                            pygame.display.set_mode((672, 350))
                        except:
                            show_text_clipboard_paste_error = True

                    elif 20 < pos[0] < 50 and 300 < pos[1] < 330:
                        page = 1



        elif event.type == pygame.KEYDOWN:
            if change_fps:
                try:
                    if event.key == pygame.K_1:
                        animation_fps = str(animation_fps)
                        animation_fps += "1"
                        animation_fps = int(animation_fps)
                    if event.key == pygame.K_2:
                        animation_fps = str(animation_fps)
                        animation_fps += "2"
                        animation_fps = int(animation_fps)
                    if event.key == pygame.K_3:
                        animation_fps = str(animation_fps)
                        animation_fps += "3"
                        animation_fps = int(animation_fps)
                    if event.key == pygame.K_4:
                        animation_fps = str(animation_fps)
                        animation_fps += "4"
                        animation_fps = int(animation_fps)
                    if event.key == pygame.K_5:
                        animation_fps = str(animation_fps)
                        animation_fps += "5"
                        animation_fps = int(animation_fps)
                    if event.key == pygame.K_6:
                        animation_fps = str(animation_fps)
                        animation_fps += "6"
                        animation_fps = int(animation_fps)
                    if event.key == pygame.K_7:
                        animation_fps = str(animation_fps)
                        animation_fps += "7"
                        animation_fps = int(animation_fps)
                    if event.key == pygame.K_8:
                        animation_fps = str(animation_fps)
                        animation_fps += "8"
                        animation_fps = int(animation_fps)
                    if event.key == pygame.K_9:
                        animation_fps = str(animation_fps)
                        animation_fps += "9"
                        animation_fps = int(animation_fps)
                    if event.key == pygame.K_0:
                        animation_fps = str(animation_fps)
                        animation_fps += "0"
                        animation_fps = int(animation_fps)

                    if event.key == pygame.K_BACKSPACE:
                        animation_fps = str(animation_fps)
                        animation_fps = animation_fps[0: len(animation_fps) - 1]
                        animation_fps = int(animation_fps)

                except ValueError:
                    animation_fps = 0

    # Set the screen background
    screen.fill(BLACK)

    # Create tools
    for i, tool in enumerate(tools):
        pygame.draw.rect(screen, tool, [10 + (i * 31), 200, 30, 30])

    try:
        pygame.draw.rect(screen, WHITE, [10, 260, 652, 10])

        if int((storage_used / MAX_STORAGE) * 100) > START_ERROR:
            pygame.draw.rect(screen, RED, [10, 260, int((storage_used / MAX_STORAGE) * 652), 10])
        elif int((storage_used / MAX_STORAGE) * 100) > START_WARNING:
            pygame.draw.rect(screen, YELLOW, [10, 260, int((storage_used / MAX_STORAGE) * 652), 10])
        else:
            pygame.draw.rect(screen, GREEN, [10, 260, int((storage_used / MAX_STORAGE) * 652), 10])

        text = FONT.render(f"Memory used: {len(str(final_str))} / {MAX_STORAGE} "
                           f"({int((storage_used / MAX_STORAGE) * 100)}% Used)", True, WHITE)
        screen.blit(text, (10, 235))

        text = FONT.render(f"Frames: {len(final_str)} Length: {round(len(final_str) / animation_fps, 2)}s Estimated "
                           f"frames left: "
                           f"{int((MAX_STORAGE - len(str(final_str))) / (len(str(final_str)) / len(final_str)))}",
                           True, WHITE)
        screen.blit(text, (10, 277))

    except:
        pass

    pos = pygame.mouse.get_pos()

    if page == 1:
        if 550 < pos[0] < 650 and 300 < pos[1] < 330:
            output_button = pygame.draw.rect(screen, (200, 200, 200), [550, 300, 100, 30])
        else:
            output_button = pygame.draw.rect(screen, WHITE, [550, 300, 100, 30])

        text = FONT.render("Next Frame", True, BLACK)
        screen.blit(text, (560, 305))

        clear = pygame.draw.rect(screen, (200, 200, 200) if 440 < pos[0] < 540 and 300 < pos[1] < 330 else WHITE,
                                 [440, 300, 100, 30])
        text = FONT.render("Clear Frame", True, BLACK)
        screen.blit(text, (450, 305))

        clear_all = pygame.draw.rect(screen, (200, 200, 200) if 330 < pos[0] < 430 and 300 < pos[1] < 330 else WHITE,
                                     [330, 300, 100, 30])
        text = FONT.render("Clear All", True, BLACK)
        screen.blit(text, (340, 305))

        preview = pygame.draw.rect(screen, (200, 200, 200) if 220 < pos[0] < 320 and 300 < pos[1] < 330 else WHITE,
                                   [220, 300, 100, 30])
        text = FONT.render("Preview", True, BLACK)
        screen.blit(text, (230, 305))

        fps_button = pygame.draw.rect(screen, (200, 200, 200) if 130 < pos[0] < 210 and 300 < pos[1] < 330 else WHITE,
                                      [130, 300, 80, 30])
        text = FONT.render(f"FPS: {animation_fps}", True, BLACK)
        screen.blit(text, (140, 305))

    else:

        delete_frame = pygame.draw.rect(screen, (200, 200, 200) if 550 < pos[0] < 650 and 300 < pos[1] < 330 else WHITE,
                                        [550, 300, 100, 30])
        text = FONT.render("Delete frame", True, BLACK)
        screen.blit(text, (560, 305))

        load_button = pygame.draw.rect(screen, (200, 200, 200) if 440 < pos[0] < 540 and 300 < pos[1] < 330 else WHITE,
                                       [440, 300, 100, 30])
        text = FONT.render("Load", True, BLACK)
        screen.blit(text, (450, 305))

    # Page turn buttons

    page_1 = pygame.draw.rect(screen, (200, 200, 200) if page == 1 else WHITE,
                              [20, 300, 30, 30])
    text = FONT.render("1", True, BLACK)
    screen.blit(text, (30, 305))

    page_2 = pygame.draw.rect(screen, (200, 200, 200) if page == 2 else WHITE,
                              [60, 300, 30, 30])
    text = FONT.render("2", True, BLACK)
    screen.blit(text, (70, 305))

    if show_clipboard_paste:
        text = FONT.render("Clipboard load:", True, WHITE)
        screen.blit(text, (10, 460))

        text = FONT.render("Please copy the string you want to load, thn press OK", True, WHITE)
        screen.blit(text, (10, 490))

        ok_load_button = pygame.draw.rect(screen,
                                          (200, 200, 200) if 550 < pos[0] < 650 and 510 < pos[1] < 540 else WHITE,
                                          [550, 510, 100, 30])
        text = FONT.render("OK", True, BLACK)
        screen.blit(text, (560, 515))

        cancel_load_button = pygame.draw.rect(screen,
                                              (200, 200, 200) if 440 < pos[0] < 540 and 510 < pos[1] < 540 else WHITE,
                                              [440, 510, 100, 30])
        text = FONT.render("Cancel", True, BLACK)
        screen.blit(text, (450, 515))

    if show_text_clipboard_paste_error:
        text = FONT.render("Error: Invalid Save String", True, RED)
        screen.blit(text, (10, 515))

    if show_string:
        text = FONT.render("Save Strings:", True, WHITE)
        screen.blit(text, (10, 355))

        if len(str(final_str)) >= 200:
            text = STR_FONT.render(str(final_str)[0: 200] + "...", True, WHITE)
        else:
            text = STR_FONT.render(str(final_str)[0: -1], True, WHITE)
        screen.blit(text, (10, 380))

        if 550 < pos[0] < 650 and 400 < pos[1] < 430:
            copy_button = pygame.draw.rect(screen, (200, 200, 200), [550, 400, 100, 30])
        else:
            copy_button = pygame.draw.rect(screen, WHITE, [550, 400, 100, 30])
        text = FONT.render("Copy", True, BLACK)
        screen.blit(text, (560, 405))

    # Draw the grid
    for row in range(GRID_SIZE[0]):
        for column in range(GRID_SIZE[1]):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            elif grid[row][column] == 2:
                color = RED
            elif grid[row][column] == 3:
                color = BLUE
            elif grid[row][column] == 4:
                color = YELLOW
            elif grid[row][column] == 5:
                color = PURPLE

            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
