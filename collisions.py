import pygame
from pygame import mixer


pygame.mixer.init()
hurdle_sound=mixer.Sound('Music/explosion.mp3')
booster_sound=mixer.Sound('Music/booster.mp3')

class Collision:
    
    @staticmethod
    def spacecraft_black_hole(game):

        hurdle_sound.play()
        game.spacecraft.reduce_health(4)


    @staticmethod
    def spacecraft_large_asteroid(game):

        hurdle_sound.play()
        game.spacecraft.reduce_health(3)


    @staticmethod
    def spacecraft_small_asteroid(game):

        hurdle_sound.play()
        game.spacecraft.reduce_health(1)


    @staticmethod
    def spacecraft_comet1(game):

        hurdle_sound.play()
        game.spacecraft.reduce_health(1)
        
        
    @staticmethod
    def spacecraft_comet2(game):

        hurdle_sound.play()
        game.spacecraft.reduce_health(1)

        
    @staticmethod
    def spacecraft_frost_ball(game):

        booster_sound.play()
        game.fl_objs.frost_ball = True
        game.frost_ball_timer = pygame.time.get_ticks()
         
    
    @staticmethod
    def spacecraft_health_booster(game):

        booster_sound.play()
        game.spacecraft.increase_health()
        
            
    # for collison of flying obj with weapon
    @staticmethod
    def bullet_large_asteroid(game):

        hurdle_sound.play()
        game.score += 5
        

    @staticmethod
    def bullet_comet1(game):

        hurdle_sound.play()
        game.score += 3
        

    @staticmethod
    def bullet_comet2(game):

        hurdle_sound.play()
        game.score += 3
        
    
    @staticmethod
    def bullet_small_asteroid(game):

        hurdle_sound.play()
        game.score += 1
        
    
    @staticmethod
    def bullet_black_hole(game):

        #hurdle_sound.play()
        pass

    
    @staticmethod
    def bullet_frost_ball(game):

        booster_sound.play()
        game.fl_objs.frost_ball = True
        game.frost_ball_timer = pygame.time.get_ticks()


    @staticmethod
    def bullet_health_booster(game):

        booster_sound.play()
        game.spacecraft.increase_health()
        

