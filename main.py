#Vamo usar a biblioteca pygame
import pygame as pg
#modulo de sistema
import sys
#Arquivos de configuração
from settings import *
#importando o mapa
from map import *
#importando o arquivo do jogador
from player import *
#importar o raycasting
from raycasting import *
#Acesso as texturas
from object_render import *
#Arquivo sprite
from sprite_object import *
from object_handler import *

class Game:
    def __init__(self):
        pg.init()
        #Desabilitar o cursor
        pg.mouse.set_visible(False)
        #Criando um tela
        self.screen = pg.display.set_mode(Resolucao)
        self.clock = pg.time.Clock()
        #Velocidade do personagem independente da taxa de quadro
        self.delta_time = 1
        self.new_game()

    #Modulo game vazio
    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_render = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        #self.static_sprite = SpriteObject(self)
        #self.animated_sprite = AnimatedSprite(self)
        self.object_handler = ObjectHandler(self)

    #Atualização de tela
    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.upadate()
        #self.static_sprite.update()
        #self.animated_sprite.update()
        pg.display.flip()
        #Exibir info do FPS
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    #A cada interação pintaremos nossa tela de preto
    def draw(self):
        #Preencher a tela com preto
        #self.screen.fill('black') 
        self.object_render.draw() #3D
        #self.map.draw() #2D
        #self.player.draw() #2D

    #Verificamos os eventos de fechamento
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    #looping principal do jogo, onde o jogo e executado
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

#instância para chamr o método run
if __name__ == '__main__':
    game = Game()
    game.run()