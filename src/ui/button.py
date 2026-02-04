import pygame

class Button:
    def __init__(self, text, x, y, w, h, font):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.font = font

    def draw(self, surf):
        pygame.draw.rect(surf, (180,180,180), self.rect, border_radius=10)
        pygame.draw.rect(surf, (50,50,50), self.rect, 2, border_radius=10)
        txt = self.font.render(self.text, True, (0,0,0))
        surf.blit(txt, txt.get_rect(center=self.rect.center))

    def clicked(self, pos):
        return self.rect.collidepoint(pos)
