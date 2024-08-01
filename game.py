import pygame
import random
import transitionCalc as TC

# pygame setup
pygame.init()
# Get the current display resolution
display_info = pygame.display.Info()
screen_width = display_info.current_w
screen_height = display_info.current_h

# Print screen resolution - useful for debugging
print(f'Screen resolution: {screen_width}x{screen_height}')

# Set the display mode to fill the screen but not full screen and include a window frame
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

clock = pygame.time.Clock()
running = True
dt = 0
# window title
pygame.display.set_caption('Threat: Risk Edition')
title_font = pygame.font.Font(None, 48)  # Larger font for the title

probabilities = {
    "3V2 Attack Win": 0.3717,  # 37.17%
    "3V2 Defense Win": 0.2926,  # 29.26%
    "3V2 Tie": 0.3358,  # 33.58%
    "3V1 Attack Win": 0.6597,  # 65.97%
    "3V1 Defense Win": 0.3403,  # 34.03%
    "2V2 Attack Win": 0.2276,  # 22.76%
    "2V2 Defense Win": 0.4483,  # 44.83%
    "2V2 Tie": 0.3241,  # 32.41%
    "2V1 Attack Win": 0.5787,  # 57.87%
    "2V1 Defense Win": 0.4213,  # 42.13%
    "1V2 Attack Win": 0.2546,  # 25.46%
    "1V2 Defense Win": 0.7454,  # 74.54%
    "1V1 Attack Win": 0.4167,  # 41.67%
    "1V1 Defense Win": 0.5833,  # 58.33%
}
scenarios = {
    "3V2": ["3V2 Attack Win", "3V2 Defense Win", "3V2 Tie"],
    "3V1": ["3V1 Attack Win", "3V1 Defense Win"],
    "2V2": ["2V2 Attack Win", "2V2 Defense Win", "2V2 Tie"],
    "2V1": ["2V1 Attack Win", "2V1 Defense Win"],
    "1V2": ["1V2 Attack Win", "1V2 Defense Win"],
    "1V1": ["1V1 Attack Win", "1V1 Defense Win"],
}


def prob_check(attack_num, defend_num):
    scenario_key = f"{attack_num}V{defend_num}"
    # Check if the scenario exists in the dictionary.
    if scenario_key in scenarios:
        # Get the list of probability events for the given scenario.
        keys = scenarios[scenario_key]

        # Create a dictionary of the probabilities for the given scenario.
        result = {key: probabilities[key] for key in keys}

        return result

    # If the scenario does not exist, return an appropriate message.
    return "Invalid scenario"


# Function to convert probabilities to percentages
def convert_to_percentages(prob_dict):
    if isinstance(prob_dict, dict):
        return {k: f"{v * 100:.2f}%" for k, v in prob_dict.items()}
    return prob_dict


# Setting up font and size
font_size = 40
font = pygame.font.Font(None, font_size)  # None uses the default font

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (100, 100, 100)
LIGHT_GREY = (200, 200, 200)
RED = (255, 0, 0)
# ball position
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
newAttacking = 0
newDefending = 0


def roll_dice(num_dice):
    die = [1, 2, 3, 4, 5, 6]
    rolls = [random.choice(die) for _ in range(num_dice)]
    return rolls


# input box class
class OptionBox():

    def __init__(self, x, y, w, h, color, highlight_color, font, option_list, selected=0):
        self.color = color
        self.highlight_color = highlight_color
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.option_list = option_list
        self.selected = selected
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1

    def draw(self, surf):
        pygame.draw.rect(surf, self.highlight_color if self.menu_active else self.color, self.rect)
        pygame.draw.rect(surf, (0, 0, 0), self.rect, 2)
        msg = self.font.render(self.option_list[self.selected], 1, (0, 0, 0))
        surf.blit(msg, msg.get_rect(center=self.rect.center))

        if self.draw_menu:
            for i, text in enumerate(self.option_list):
                rect = self.rect.copy()
                rect.y += (i + 1) * self.rect.height
                pygame.draw.rect(surf, self.highlight_color if i == self.active_option else self.color, rect)
                msg = self.font.render(text, 1, (0, 0, 0))
                surf.blit(msg, msg.get_rect(center=rect.center))
            outer_rect = (
                self.rect.x, self.rect.y + self.rect.height, self.rect.width, self.rect.height * len(self.option_list))
            pygame.draw.rect(surf, (0, 0, 0), outer_rect, 2)

    def update(self, event_list):
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)

        self.active_option = -1
        for i in range(len(self.option_list)):
            rect = self.rect.copy()
            rect.y += (i + 1) * self.rect.height
            if rect.collidepoint(mpos):
                self.active_option = i
                break

        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_active:
                    self.draw_menu = not self.draw_menu
                elif self.draw_menu and self.active_option >= 0:
                    self.selected = self.active_option
                    self.draw_menu = False
                    return self.active_option
        return -1


# Button class
class Button:
    def __init__(self, x, y, width, height, text, font, text_color, button_color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = font
        self.text_color = text_color
        self.button_color = button_color
        self.hover_color = hover_color
        self.clicked = False

    def draw(self, screen):
        # Change color on hover
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.button_color

        if self.rect.collidepoint(mouse_pos) and mouse_pressed[0]:
            self.clicked = True
        else:
            self.clicked = False

        # Draw button
        pygame.draw.rect(screen, color, self.rect)

        # Render text on button
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self):
        return self.clicked


# Function to display a pop-up
popup_visible = False


# Function to display a pop-up
def display_popup():
    popup_width = 600
    popup_height = 200
    popup_x = (screen.get_width() // 2) - (popup_width // 2)
    popup_y = (screen.get_height() // 2) - (popup_height // 2)

    # Draw the pop-up window
    pygame.draw.rect(screen, GREY, (popup_x, popup_y, popup_width, popup_height))

    # Render the pop-up text
    popup_text = "The Battle Results Are:"
    popup_text_surface = font.render(popup_text, True, BLACK)
    popup_text_rect = popup_text_surface.get_rect(center=((screen.get_width() // 2), popup_y + 50))
    screen.blit(popup_text_surface, popup_text_rect)

    # Render the result number
    result_number = "Attackers #: " + str(newAttacking) + " and Defenders #: " + str(newDefending)
    result_number_surface = font.render(result_number, True, BLACK)
    result_number_rect = result_number_surface.get_rect(center=((screen.get_width() // 2), popup_y + 100))
    screen.blit(result_number_surface, result_number_rect)

    # Create a close button for the pops-up
    close_button = Button(popup_x + (popup_width // 2) - 50, popup_y + popup_height - 50, 100, 30, "Close", font,
                          BLACK, RED, LIGHT_GREY)
    close_button.draw(screen)

    return close_button


attackingList = OptionBox(
    40, 40, 200, 40, (150, 150, 150), (100, 200, 255), pygame.font.SysFont(None, 30),
    ["Attacking Army #", "1", "2", "3"])
defendingList = OptionBox(
    screen.get_width() - 250, 40, 200, 40, (150, 150, 150), (100, 200, 255), pygame.font.SysFont(None, 30),
    ["Defending Army #", "1", "2"])

click_flag = False
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("aquamarine")
    country_one = pygame.image.load('Assets/ColombiaImage.png')
    screen.blit(country_one, (0, 100))
    country_two = pygame.image.load('Assets/GhanaImage.png')
    screen.blit(country_two, (550, 100))

    # option box draw
    attack_selected_option = attackingList.update(event_list)
    attackingList.draw(screen)

    defend_selected_option = defendingList.update(event_list)
    defendingList.draw(screen)

    # Render the number onto a new Surface
    attackText = font.render(attackingList.option_list[attackingList.selected], True, (255, 255, 255))  # White text
    defendText = font.render(defendingList.option_list[defendingList.selected], True, (255, 255, 255))  # White text
    if attackingList.option_list[attackingList.selected] != "Attacking Army #":
        screen.blit(attackText, (350, 500))
    if defendingList.option_list[defendingList.selected] != "Defending Army #":
        screen.blit(defendText, (900, 500))

    # Create button instance
    button_width = 200
    button_height = 50
    button_x = (screen.get_width() // 2) - (button_width // 2)
    button_y = screen.get_height() - button_height - 40
    button = Button(button_x, button_y, button_width, button_height, "BATTLE", font, BLACK, GREY, LIGHT_GREY)

    if ((attackingList.option_list[attackingList.selected] != "Attacking Army #") and (
            defendingList.option_list[defendingList.selected] != "Defending Army #")):
        probabilities_display = convert_to_percentages(
            prob_check(int(attackingList.option_list[attackingList.selected]),
                       int(defendingList.option_list[
                               defendingList.selected])))
        button.draw(screen)
        # Display the title
        title_surface = title_font.render("Probabilities:", True, (0, 0, 0))
        title_rect = title_surface.get_rect(center=(screen.get_width() // 2, 30))
        screen.blit(title_surface, title_rect)

        # Display the probabilities
        y_offset = 80  # Adjust this to position text below the title
        if isinstance(probabilities_display, dict):
            for key, percentage in probabilities_display.items():
                text_surface = font.render(f"{key}: {percentage}", True, (0, 0, 0))
                text_rect = text_surface.get_rect(center=(screen.get_width() // 2, y_offset))
                screen.blit(text_surface, text_rect)
                y_offset += 40
        else:
            text_surface = font.render(probabilities_display, True, (255, 0, 0))
            text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            screen.blit(text_surface, text_rect)
        if button.is_clicked() and not click_flag:
            click_flag = True
            popup_visible = True
            attackOption = attackingList.option_list[attackingList.selected]
            defenseOption = defendingList.option_list[defendingList.selected]
            battleOutcome = TC.determine_outcomes(int(attackOption), int(defenseOption))
            print(battleOutcome)
            if battleOutcome[0] != 0:
                attackOption = int(attackOption) - battleOutcome[0]
                newAttacking = attackOption
                newDefending = defenseOption
            elif battleOutcome[1] != 0:
                defenseOption = int(defenseOption) - battleOutcome[1]
                newAttacking = attackOption
                newDefending = defenseOption
            elif battleOutcome[2] != 0:
                attackOption = int(attackOption) - battleOutcome[2]
                defenseOption = int(defenseOption) - battleOutcome[2]
                newAttacking = attackOption
                newDefending = defenseOption

    if not pygame.mouse.get_pressed()[0]:
        click_flag = False

    close_button = None
    if popup_visible:
        close_button = display_popup()
        if close_button.is_clicked():
            popup_visible = False

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()
