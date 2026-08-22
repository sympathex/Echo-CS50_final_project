import pygame
import random
import asyncio

async def main():
    while True:
        screen = setup()
        await loop(screen)

def setup():
    # basic game setup, runs once
    pygame.init()
    screen = pygame.display.set_mode((640, 740))
    return screen

async def loop(screen):
    clock = pygame.time.Clock()
    fontT = pygame.font.SysFont("consolas", 35)
    font = pygame.font.SysFont("consolas", 20)
    running = True
    while running:
        
        #   Buttons:
        play_button = pygame.Rect(260, 375, 120, 50)
        quit_button = pygame.Rect(260, 440, 120, 50)
        
        #   Events:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if play_button.collidepoint(event.pos):
                    print("Left mouse button clicked on Play Button.")
                    result = await game(screen)
                    while result == "replay":
                        result = await game(screen)
                    if result == "quit":
                        running = False
                    if result == "menu":
                        ...
                    
                        
                if quit_button.collidepoint(event.pos):
                    print("Left mouse button clicked on Quit button.")
                    return pygame.quit()
                
                
        screen.fill("black")    
                
        # -----Main Menu-------------------------------------------------------------------------------------

        #   Instructions:
        instructions = fontT.render("Instructions:", antialias=True, color="white")
        instructions_text_line1 = font.render("Use WASD or Arrow keys to move",antialias=True, color="white")
        instructions_text_line2_part1 = font.render("If you see a",antialias=True, color="white")
        instructions_text_line2_part2 = font.render("yellow",antialias=True, color="yellow")
        instructions_text_line2_part3 = font.render("arrow, do as it says",antialias=True, color="white")
        instructions_text_line3_part1 = font.render("If you see a",antialias=True, color="white")
        instructions_text_line3_part2 = font.render("red",antialias=True, color="red")
        instructions_text_line3_part3 = font.render("arrow, do the opposite",antialias=True, color="white")

        screen.blit(instructions, (190, 55))
        screen.blit(instructions_text_line1, (140, 100))
        screen.blit(instructions_text_line2_part1, (85, 117))
        screen.blit(instructions_text_line2_part2, (227, 117))
        screen.blit(instructions_text_line2_part3, (305, 117))
        screen.blit(instructions_text_line3_part1, (90, 134))
        screen.blit(instructions_text_line3_part2, (230, 134))
        screen.blit(instructions_text_line3_part3, (270, 134))


        #    Buttons:
        
        play_button = pygame.draw.rect(screen, (128, 128, 128), play_button, border_radius=8)
        play_text = font.render("Play",antialias=True, color="black")
        screen.blit(play_text, (300, 390))
        
        quit_button = pygame.draw.rect(screen, (128, 128, 128), quit_button, border_radius=8)
        quit_text = font.render("Quit",antialias=True, color="black")
        screen.blit(quit_text, (300, 455))
        
        
        # Hover animation:
        #                 Play button:
        if play_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (211, 211, 211), play_button)
        else:
            pygame.draw.rect(screen, (128, 128, 128), play_button)
        screen.blit(play_text, (300, 390))
        #                 Quit Button:
        if quit_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (211, 211, 211), quit_button)
        else:
            pygame.draw.rect(screen, (128, 128, 128), quit_button)
        screen.blit(quit_text, (300, 455))
        
        pygame.display.update()
            
            

        clock.tick(60)
        await asyncio.sleep(0)

    # ---Quit-----------------------------------------------------------------------------------------------
    pygame.quit()



# ~~~Starting Game~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
async def game(screen):
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 40)
    
    directions = ["up", "down", "left", "right"]
    current_direction = random.choice(directions)
    direction_color = random.choice(["yellow", "red"])
    shown_at = pygame.time.get_ticks()
    score = 0
    game_over = False
    
    key_to_direction = {
        pygame.K_UP: "up", pygame.K_w: "up",
        pygame.K_DOWN: "down", pygame.K_s: "down",
        pygame.K_LEFT: "left", pygame.K_a: "left",
        pygame.K_RIGHT: "right", pygame.K_d: "right",
    }
    
    opposites = {"up": "down", "down": "up", "left": "right", "right": "left"}
    
    time_limit = 5000
    
    character = pygame.Rect(290, 535, 50, 50)
    character_color = (255, 255, 255)
    moving = False
    move_start = 0
    move_duration = 150
    center_x, center_y = 290, 535
        
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                
                pressed_direction = get_pressed_direction(event.key, key_to_direction)
                
                correct_answer = get_correct_answer(current_direction, direction_color, opposites)
                    
                if pressed_direction == correct_answer:
                    score += 1
                    current_direction = random.choice(directions)
                    direction_color = random.choice(["yellow", "red"])
                    shown_at = pygame.time.get_ticks()
                    time_limit = shrink_time_limit(time_limit)
                    
                    if correct_answer == "up":
                        character = pygame.Rect(290, 470, 50, 50)
                    elif correct_answer == "down":
                        character = pygame.Rect(290, 600, 50, 50)
                    elif correct_answer == "right":
                        character = pygame.Rect(355, 535, 50, 50)
                    elif correct_answer == "left":
                        character = pygame.Rect(225, 535, 50, 50)
                        
                    character_color = (144, 238, 144)
                    moving = True
                    move_start = pygame.time.get_ticks()
                    
                else:
                    game_over = True
                pass
        
            
        elapsed = pygame.time.get_ticks() - shown_at
        
        if elapsed > time_limit:
            game_over = True
        
        if game_over:
            running = False
            continue
        
        
        if moving and move_duration <= pygame.time.get_ticks() - move_start:
            character = pygame.Rect(center_x, center_y, 50, 50)
            character_color = (255, 255, 255)
            moving = False
        
        screen.fill("black")
        
        
        direction_text = font.render(current_direction, antialias=True, color=direction_color)
        direction_rect = direction_text.get_rect(center=(320, 300))
        screen.blit(direction_text, direction_rect)
        
        score_text = font.render(f"Score: {score}", antialias=True, color="white")
        score_rect = score_text.get_rect(topleft=(20, 20))
        screen.blit(score_text, score_rect)
        
        time_left = (time_limit - elapsed) / 1000
        time_left_text = font.render(f"{time_left:.3f}", antialias=True, color="white")
        screen.blit(time_left_text, (400, 20))
        
        #    Blocks on the ground:
        block_size = 60
        gap = 5
        grid_start_x = 220
        grid_start_y = 465
        
        for row in range(3):
            for col in range(3):
                block_x = grid_start_x + col * (block_size + gap)
                block_y = grid_start_y + row * (block_size + gap)
                block = pygame.Rect(block_x, block_y, block_size, block_size)
                pygame.draw.rect(screen, (100, 100, 100), block)

        pygame.draw.rect(screen, character_color, character)
        
        pygame.display.update()    
        clock.tick(60)
        await asyncio.sleep(0)
        
            
    result = await game_over_screen(screen, score)
    return result
        
async def game_over_screen(screen, score):
    
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("consolas", 20)
        
    replay_button = pygame.Rect(260, 375, 120, 50)
    menu_button = pygame.Rect(250, 440, 140, 50)
    quit_button = pygame.Rect(260, 505, 120, 50)
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if replay_button.collidepoint(event.pos):
                    return "replay"
                if menu_button.collidepoint(event.pos):
                    return "menu"
                if quit_button.collidepoint(event.pos):
                    return "quit"
        
        screen.fill("black")
        
        score_text = font.render(f"Score: {score}", antialias=True, color="white")
        score_rect = score_text.get_rect(center=(320, 260))
        screen.blit(score_text, score_rect)
        
        replay_button = pygame.draw.rect(screen, (128, 128, 128), replay_button, border_radius=8)
        replay_text = font.render("Replay",antialias=True, color="black")
        screen.blit(replay_text, (288, 390))
        
        menu_button = pygame.draw.rect(screen, (128, 128, 128), menu_button, border_radius=8)
        menu_text = font.render("Main Menu",antialias=True, color="black")
        screen.blit(menu_text, (271, 457))
        
        quit_button = pygame.draw.rect(screen, (128, 128, 128), quit_button, border_radius=8)
        quit_text = font.render("Quit",antialias=True, color="black")
        screen.blit(quit_text, (297, 520))
        

        if replay_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (211, 211, 211), replay_button)
        else:
            pygame.draw.rect(screen, (128, 128, 128), replay_button)
        screen.blit(replay_text, (287, 390))
        
        if menu_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (211, 211, 211), menu_button)
        else:
            pygame.draw.rect(screen, (128, 128, 128), menu_button)
        screen.blit(menu_text, (272, 455))
        
        if quit_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (211, 211, 211), quit_button)
        else:
            pygame.draw.rect(screen, (128, 128, 128), quit_button)
        screen.blit(quit_text, (300, 520))
        
        
        pygame.display.update()
        clock.tick(60)
        await asyncio.sleep(0)
        
def get_correct_answer(current_direction, direction_color, opposites):
    if direction_color == "yellow":
        return current_direction
    else:
        return opposites[current_direction]
    

def shrink_time_limit(time_limit):
    return max(1000, time_limit - 50)


def get_pressed_direction(key, key_to_direction):
    return key_to_direction.get(key)

if __name__ == "__main__":
    asyncio.run(main())
