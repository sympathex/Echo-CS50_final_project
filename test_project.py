import pygame
from project import get_correct_answer, shrink_time_limit, get_pressed_direction

def test_get_correct_answer():
    opposites = {"up": "down", "down": "up", "left": "right", "right": "left"}
    
    # Test when direction_color is yellow
    assert get_correct_answer("up", "yellow", opposites) == "up"
    assert get_correct_answer("down", "yellow", opposites) == "down"
    assert get_correct_answer("left", "yellow", opposites) == "left"
    assert get_correct_answer("right", "yellow", opposites) == "right"
    
    # Test when direction_color is not yellow
    assert get_correct_answer("up", "red", opposites) == "down"
    assert get_correct_answer("down", "blue", opposites) == "up"
    assert get_correct_answer("left", "green", opposites) == "right"
    assert get_correct_answer("right", "purple", opposites) == "left"
    
    
def test_shrink_time_limit():
    
    # Time limit decreases correctly
    assert shrink_time_limit(2000) == 1950
    assert shrink_time_limit(1500) == 1450
    assert shrink_time_limit(1100) == 1050
    
    # Time limit does not go below 1000
    assert shrink_time_limit(1000) == 1000
    assert shrink_time_limit(950) == 1000
    
def test_get_pressed_direction():
    mapping = {pygame.K_UP: "up", pygame.K_DOWN: "down", pygame.K_LEFT: "left", pygame.K_RIGHT: "right"}
    
    # Test each key
    assert get_pressed_direction(pygame.K_UP, mapping) == "up"
    assert get_pressed_direction(pygame.K_DOWN, mapping) == "down"
    assert get_pressed_direction(pygame.K_LEFT, mapping) == "left"
    assert get_pressed_direction(pygame.K_RIGHT, mapping) == "right"
    
    # Test unknown key
    assert get_pressed_direction(pygame.K_SPACE, mapping) is None