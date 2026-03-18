import math

#Definindo a resolução a taxa de quadro
Resolucao = WIDTH, HEIGH = 1600, 900
#Metade do valor da resolução
HALF_WIDTH = WIDTH // 2
HALF_HEIGH = HEIGH // 2
FPS = 0

#configurações iniciais
PLAYER_POS = 1.5, 5 #mini_map posição do jogador no mapa
PLAYER_ANGLE = 0 #angulo
PLAYER_SPEED = 0.004 #Velocidade do movimento
PLAYER_ROT_SPEED = 0.002 #velocidade de rotação

#definimos o campo de visão
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

#Distância para a localização da tela
SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

#Tamanho das texturas
TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2