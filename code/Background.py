from code.Const import ENTITY_MOVE, ENTITY_VISIBLE
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, aux_counter):

        print(aux_counter)

        if aux_counter >= 420:
            if aux_counter >= ENTITY_MOVE[self.name] + 360:
                self.rect.left = ENTITY_VISIBLE[self.name]
        elif aux_counter >= ENTITY_MOVE[self.name]:
            self.rect.left = 0

