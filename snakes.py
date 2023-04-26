print("enter o  to play clasic interpratation of snake")
print("enter n to play new interpratation of snake")

gv = input('enter a alpabet = ')
if gv =='o':
    import pygame
    import sys
    import random


    class Snake():
        def __init__(self):
            self.length = 1
            self.positions = [((screen_width / 2), (screen_height / 2))]
            self.direction = random.choice([up, down, left, right])
            self.color = (0, 255, 0)
            self.score = 0

        def get_head_position(self):
            return self.positions[0]

        def turn(self, point):
            if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
                return
            else:
                self.direction = point

        def move(self):
            cur = self.get_head_position()
            x, y = self.direction
            new = (((cur[0] + (x * gridsize)) % screen_width), (cur[1] + (y * gridsize)) % screen_height)
            if len(self.positions) > 2 and new in self.positions[2:]:
                self.reset()
            else:
                self.positions.insert(0, new)
                if len(self.positions) > self.length:
                    self.positions.pop()

        def reset(self):
            self.length = 1
            self.positions = [((screen_width / 2), (screen_height / 2))]
            self.direction = random.choice([up, down, left, right])
            self.score = 0

        def draw(self, surface):
            for p in self.positions:
                r = pygame.Rect((p[0], p[1]), (gridsize, gridsize))
                pygame.draw.rect(surface, self.color, r)
                pygame.draw.rect(surface, (0, 255, 0), r, 1)

        def handle_keys(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.turn(up)
                    elif event.key == pygame.K_DOWN:
                        self.turn(down)
                    elif event.key == pygame.K_LEFT:
                        self.turn(left)
                    elif event.key == pygame.K_RIGHT:
                        self.turn(right)


    class Food():
        def __init__(self):
            self.position = (0, 0)
            self.color = (204, 0, 204)
            self.randomize_position()

        def randomize_position(self):
            self.position = (
            random.randint(0, grid_width - 1) * gridsize, random.randint(0, grid_height - 1) * gridsize)

        def draw(self, surface):
            r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (0, 255, 0), r, 1)


    def drawGrid(surface):
        for y in range(0, int(grid_height)):
            for x in range(0, int(grid_width)):
                if (x + y) % 2 == 0:
                    r = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))
                    pygame.draw.rect(surface, (0, 153, 153), r)
                else:
                    rr = pygame.Rect((x * gridsize, y * gridsize), (gridsize, gridsize))
                    pygame.draw.rect(surface, (0, 204, 204), rr)


    screen_width = 480
    screen_height = 480

    gridsize = 20
    grid_width = screen_width / gridsize
    grid_height = screen_height / gridsize

    up = (0, -1)
    down = (0, 1)
    left = (-1, 0)
    right = (1, 0)


    def main():
        pygame.init()

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

        surface = pygame.Surface(screen.get_size())
        surface = surface.convert()
        drawGrid(surface)

        snake = Snake()
        food = Food()

        myfont = pygame.font.SysFont("freesansbold.tff", 36)

        while (True):
            clock.tick(10)
            snake.handle_keys()
            drawGrid(surface)
            snake.move()
            if snake.get_head_position() == food.position:
                snake.length += 1
                snake.score += 1
                food.randomize_position()
            snake.draw(surface)
            food.draw(surface)
            screen.blit(surface, (0, 0))
            text = myfont.render("Score {0}".format(snake.score), 1, (0, 0, 0))
            screen.blit(text, (5, 10))
            pygame.display.update()



    main()






if gv =='n':
    import pygame
    import sys
    from pygame.math import Vector2
    import random



    class SNAKE():
        def __init__(self):
            self.body = [Vector2(11, 10), Vector2(12, 10), Vector2(13, 10)]
            self.direction = Vector2(0, 0)
            self.new_block = False

            self.head_up = pygame.image.load("graphics/head_up.png")
            self.head_down = pygame.image.load("graphics/head_down.png")
            self.head_left = pygame.image.load("graphics/head_left.png")
            self.head_right = pygame.image.load("graphics/head_right.png")

            self.tail_up = pygame.image.load("graphics/tail_up.png")
            self.tail_down = pygame.image.load("graphics/tail_down.png")
            self.tail_left = pygame.image.load("graphics/tail_left.png")
            self.tail_right = pygame.image.load("graphics/tail_right.png")

            self.body_horizontal = pygame.image.load("graphics/body_horizontal.png")
            self.body_vertical = pygame.image.load("graphics/body_vertical.png")

            self.body_topleft = pygame.image.load("graphics/body_topleft.png")
            self.body_topright = pygame.image.load("graphics/body_topright.png")
            self.body_bottomleft = pygame.image.load("graphics/body_bottomleft.png")
            self.body_bottomright = pygame.image.load("graphics/body_bottomright.png")
            self.crunch_sound = pygame.mixer.Sound("sound/crunch.wav")

        def draw_snake(self):
            self.update_head_graphics()
            self.update_tail_graphics()

            for index, block in enumerate(self.body):
                x_position = (block.x * cell_size)
                y_position = (block.y * cell_size)
                block_rect = pygame.Rect(x_position, y_position, cell_size, cell_size)

                if index == 0:
                    screen.blit(self.head, block_rect)
                elif index == len(self.body) - 1:
                    screen.blit(self.tail, block_rect)

                else:
                    previous_block = self.body[index + 1] - block
                    next_block = self.body[index - 1] - block
                    if previous_block.y == next_block.y:
                        screen.blit(self.body_horizontal, block_rect)
                    elif previous_block.x == next_block.x:
                        screen.blit(self.body_vertical, block_rect)
                    else:
                        if previous_block.y == -1 and next_block.x == -1 or previous_block.x == -1 and next_block.y == -1:
                            screen.blit(self.body_topleft, block_rect)
                        elif previous_block.y == -1 and next_block.x == 1 or previous_block.x == 1 and next_block.y == -1:
                            screen.blit(self.body_topright, block_rect)
                        elif previous_block.y == 1 and next_block.x == 1 or previous_block.x == 1 and next_block.y == 1:
                            screen.blit(self.body_bottomright, block_rect)
                        else:
                            screen.blit(self.body_bottomleft, block_rect)

        def update_head_graphics(self):
            head_relation = self.body[1] - self.body[0]

            if head_relation == Vector2(1, 0):
                self.head = self.head_left
            elif head_relation == Vector2(-1, 0):
                self.head = self.head_right
            elif head_relation == Vector2(0, 1):
                self.head = self.head_up
            elif head_relation == Vector2(0, -1):
                self.head = self.head_down

        def update_tail_graphics(self):
            tail_relation = self.body[- 2] - self.body[- 1]

            if tail_relation == Vector2(1, 0):
                self.tail = self.tail_left
            elif tail_relation == Vector2(-1, 0):
                self.tail = self.tail_right
            elif tail_relation == Vector2(0, 1):
                self.tail = self.tail_up
            elif tail_relation == Vector2(0, -1):
                self.tail = self.tail_down

        def move_snake(self):
            if self.new_block == True:
                body_copy = self.body[:]
                body_copy.insert(0, body_copy[0] + self.direction)
                self.body = body_copy[:]
                self.new_block = False
            else:
                body_copy = self.body[:-1]
                body_copy.insert(0, body_copy[0] + self.direction)
                self.body = body_copy[:]

        def add_block(self):
            self.new_block = True

        def sound(self):
            self.crunch_sound.play()

        def reset_game(self):
            self.body = [Vector2(11, 10), Vector2(12, 10), Vector2(13, 10)]
            self.direction = Vector2(0, 0)


    class FRUIT:
        def __init__(self):
            self.randomize()

        def draw_fruit(self):
            fruit_rect = pygame.Rect(int(self.position.x * cell_size), int(self.position.y * cell_size), cell_size,
                                     cell_size)
            screen.blit(apple, fruit_rect)
            # pygame.draw.ellipse(screen, "red", fruit_rect)

        def randomize(self):
            self.x = random.randint(0, cell_number - 1)
            self.y = random.randint(0, cell_number - 1)
            self.position = Vector2(self.x, self.y)


    class MAIN:
        def __init__(self):
            self.snake = SNAKE()
            self.fruit = FRUIT()

        def update(self):
            self.snake.move_snake()
            self.check_collision()
            self.check_fail()

        def draw_elements(self):
            self.draw_grass()
            self.fruit.draw_fruit()
            self.snake.draw_snake()
            self.draw_score()

        def check_collision(self):
            if self.fruit.position == self.snake.body[0]:
                self.fruit.randomize()
                self.snake.add_block()
                self.snake.sound()

            for block in self.snake.body[1:]:
                if block == self.fruit.position:
                    self.fruit.randomize()

        def check_fail(self):
            if not 0 <= self.snake.body[0].x < cell_number:
                self.game_over()

            if not 0 <= self.snake.body[0].y < cell_number:
                self.game_over()

            for block in self.snake.body[1:]:
                if block == self.snake.body[0]:
                    self.game_over()

        def game_over(self):
            self.snake.reset_game()

        def draw_grass(self):
            grass_color = (180, 240, 90)

            for rows in range(cell_number):
                if rows % 2 == 0:
                    for columns in range(cell_number):
                        if columns % 2 == 0:
                            grass_rectangle = pygame.Rect(columns * cell_size, rows * cell_size, cell_size, cell_size)
                            pygame.draw.rect(screen, grass_color, grass_rectangle)
                else:
                    for columns in range(cell_number):
                        if columns % 2 == 1:
                            grass_rectangle = pygame.Rect(columns * cell_size, rows * cell_size, cell_size, cell_size)
                            pygame.draw.rect(screen, grass_color, grass_rectangle)

        def draw_score(self):
            score_text = str((len(self.snake.body) - 3) * 10)
            score_surface = game_font.render(score_text, True, (50, 80, 20))
            score_x = int((cell_size * cell_number) - 60)
            score_y = int((cell_size * cell_number) - 60)
            score_rect = score_surface.get_rect(center=(score_x, score_y))
            apple_rect = apple.get_rect(center=(score_x - 25, score_y))
            bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 5,
                                  apple_rect.height)

            pygame.draw.rect(screen, (160, 200, 60), bg_rect)
            screen.blit(score_surface, score_rect)
            screen.blit(apple, apple_rect)
            pygame.draw.rect(screen, (50, 80, 60), bg_rect, 2)


    pygame.init()
    cell_size = 30
    cell_number = 20
    framerate = 60
    screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
    clock = pygame.time.Clock()
    apple = pygame.image.load("graphics/apple.png").convert_alpha()
    game_font = pygame.font.Font(None, 25)

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 200)

    main_game = MAIN()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == SCREEN_UPDATE:
                main_game.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_RIGHT:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_LEFT:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1, 0)

        screen.fill((175, 225, 100))
        main_game.draw_elements()
        pygame.display.update()
        clock.tick(framerate)



