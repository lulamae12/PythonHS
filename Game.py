from pygame import *
RED = (255, 0, 0)
display.init()
display.set_mode((600,600), 1, 8)
class Car(sprite.Sprite):
        def _init__(self, color, width, height):
                super().__init__()
                sprite.Sprite._init(self)
                self.image = pygame.Surface([width, height])
                self.image.fill(RED)
                self.image.set_colorkey(RED)
                draw.rect(self.image, color, [0, 0, width, height])
                self.rect = self.image.get_rect()
                all_sprites_list.draw(screen)
