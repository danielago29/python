import pygame
import random

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana del juego
window_width = 800
window_height = 600

# Colores
white = (255, 255, 255)
black = (0, 0, 0)
umbrella_image_good = pygame.image.load("umbrella.png")
granizo = pygame.image.load("granizo.png")

# Crear la ventana del juego
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Esquivar Obstáculos")

# Cargar el fondo
background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image, (window_width, window_height))

# Clase para el personaje controlado por el jugador
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(umbrella_image_good, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = window_width // 2
        self.rect.bottom = window_height - 20
        self.speed = 5

    def update(self):
        # Mover el personaje con las teclas de dirección
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < window_width:
            self.rect.x += self.speed

# Clase para los enemigos
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(granizo, (30, 30))        
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, window_width - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(1, 5)

    def update(self):
        # Mover los enemigos hacia abajo
        self.rect.y += self.speed
        if self.rect.y > window_height:
            self.rect.x = random.randint(0, window_width - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speed = random.randint(1, 5)

# Clase para las gemas
class Gem(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(umbrella_image_good, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, window_width - self.rect.width)
        self.rect.y = random.randint(-100, -40)
        self.speed = random.randint(1, 3)

    def update(self):
        # Mover las gemas hacia abajo
        self.rect.y += self.speed
        if self.rect.y > window_height:
            self.rect.x = random.randint(0, window_width - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speed = random.randint(1, 3)

# Clase para las gotas de lluvia
class Raindrop(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((2, 10))
        self.image.fill((150, 150, 255))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, window_width)
        self.rect.y = random.randint(-300, -10)
        self.speed = random.randint(5, 10)

    def update(self):
        # Mover las gotas de lluvia hacia abajo
        self.rect.y += self.speed
        if self.rect.y > window_height:
            self.rect.x = random.randint(0, window_width)
            self.rect.y = random.randint(-300, -10)
            self.speed = random.randint(5, 10)

# Grupos de sprites
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
gems = pygame.sprite.Group()
raindrops = pygame.sprite.Group()

# Crear el personaje
player = Player()
all_sprites.add(player)

# Generar enemigos iniciales
for _ in range(10):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Generar gemas iniciales
for _ in range(5):
    gem = Gem()
    all_sprites.add(gem)
    gems.add(gem)

# Reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()

# Puntuación
score = 0
font = pygame.font.Font(None, 36)

# Vidas
lives = 3

# Función para mostrar la puntuación en la pantalla
def show_score():
    text = font.render("Puntuación: " + str(score), True, white)
    window.blit(text, (10, 10))

# Función para mostrar las vidas en la pantalla
def show_lives():
    text = font.render("Vidas: " + str(lives), True, white)
    window.blit(text, (window_width - text.get_width() - 10, 10))

# Función para mostrar el mensaje de finalización del juego
def show_game_over():
    game_over_text = font.render("Game Over", True, black)
    score_text = font.render("Puntuación final: " + str(score), True, black)
    restart_text = font.render("Presiona R para reiniciar", True, black)
    restart_text2 = font.render("Presiona X para salir", True, black)
    window.blit(game_over_text, (window_width // 2 - game_over_text.get_width() // 2, window_height // 2 - 50))
    window.blit(score_text, (window_width // 2 - score_text.get_width() // 2, window_height // 2))
    window.blit(restart_text, (window_width // 2 - restart_text.get_width() // 2, window_height // 2 + 50))
    window.blit(restart_text2, (window_width // 2 - restart_text2.get_width() // 2, window_height // 2 + 100))

# Mostrar el menú de inicio
show_menu = True
while show_menu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                show_menu = False

    window.fill(white)
    title_font = pygame.font.Font(None, 48)
    story_font = pygame.font.Font(None, 24)
    title_text = title_font.render("Esquivar Obstáculos", True, black)
    story_text1 = story_font.render("¡Bienvenido al juego de Esquivar Obstáculos!", True, black)
    story_text2 = story_font.render("Te encuentras en un clima complicado con lluvia de granizo.", True, black)
    story_text3 = story_font.render("Tu objetivo es esquivar el granizo y recoger la mayor cantidad", True, black)
    story_text4 = story_font.render("de sombrillas para protegerte.", True, black)
    menu_text = font.render("Presiona ESPACIO para comenzar", True, (0, 0, 0))
    window.blit(title_text, (window_width // 2 - title_text.get_width() // 2, window_height // 2 - 100))
    window.blit(story_text1, (window_width // 2 - story_text1.get_width() // 2, window_height // 2 - 50))
    window.blit(story_text2, (window_width // 2 - story_text2.get_width() // 2, window_height // 2 - 10))
    window.blit(story_text3, (window_width // 2 - story_text3.get_width() // 2, window_height // 2 + 30))
    window.blit(story_text4, (window_width // 2 - story_text4.get_width() // 2, window_height // 2 + 70))
    window.blit(menu_text, (window_width // 2 - menu_text.get_width() // 2, window_height // 2 - menu_text.get_height() // 2 + 150))
    pygame.display.flip()

# Bucle principal del juego
running = True
game_over = False
while running:
    # Controlar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                # Reiniciar el juego
                all_sprites.empty()
                enemies.empty()
                gems.empty()
                raindrops.empty()
                player = Player()
                all_sprites.add(player)
                score = 0
                lives = 3
                game_over = False
            elif event.key == pygame.K_x:
                # Salir del juego
                running = False

    if not game_over:
        # Actualizar sprites
        all_sprites.update()

        # Comprobar colisiones entre el jugador y los enemigos
        if pygame.sprite.spritecollide(player, enemies, True):
            lives -= 1
            if lives <= 0:
                game_over = True  # Activar el estado de juego terminado

        # Comprobar colisiones entre el jugador y las gemas
        gems_collected = pygame.sprite.spritecollide(player, gems, True)
        for gem in gems_collected:
            score += 10

        # Añadir
        while len(enemies) < 10:
            enemy = Enemy()
            all_sprites.add(enemy)
            enemies.add(enemy)

        # Añadir nuevas gemas a medida que se recogen
        while len(gems) < 5:
            gem = Gem()
            all_sprites.add(gem)
            gems.add(gem)

        # Generar nuevas gotas de lluvia constantemente
        if len(raindrops) < 100:
            raindrop = Raindrop()
            all_sprites.add(raindrop)
            raindrops.add(raindrop)

        # Limpiar la pantalla
        window.blit(background_image, (0, 0))

        # Dibujar sprites en la pantalla
        all_sprites.draw(window)

        # Mostrar puntuación y vidas
        show_score()
        show_lives()

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la velocidad de actualización
        clock.tick(60)

    else:
        # Limpiar la pantalla
        window.blit(background_image, (0, 0))

        # Mostrar mensaje de finalización del juego
        show_game_over()

        # Actualizar la pantalla
        pygame.display.flip()

# Salir del juego
pygame.quit()
