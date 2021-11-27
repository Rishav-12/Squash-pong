import pygame

pygame.init()

win = pygame.display.set_mode((750,500))

pygame.display.set_caption("Let's Play Pong!")
clock = pygame.time.Clock()

white_color = (255,255,255)
black_color = (0,0,0)
red_color = (255,0,0)
green_color = (0,255,0)

paddle_width = 75
paddle_inc_width = 10

class Paddle(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([10,paddle_width])
		self.image.fill(white_color)
		self.rect = self.image.get_rect()
		self.points = 0
		self.streak = 0

class Wall(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([20,500])
		self.image.fill(white_color)
		self.rect = self.image.get_rect()

class Ball(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([10,10])
		self.image.fill(white_color)
		self.rect = self.image.get_rect()
		self.speed = 8
		self.dirnx = 1
		self.dirny = 1

paddle = Paddle()
paddle.rect.x = 715
paddle.rect.y = 225

wall = Wall()
wall.rect.x = 0
wall.rect.y = 0

pong = Ball()
pong.rect.x = 375
pong.rect.y = 250

all_sprites = pygame.sprite.Group()
all_sprites.add(wall, paddle, pong)

def redrawWindow():
	win.fill(black_color)
	font = pygame.font.SysFont("comicsans", 30)
	text = font.render("SQUASH PONG", False, green_color)
	textRect = text.get_rect()
	textRect.center = (750 // 2, 25)
	win.blit(text, textRect)

	score = font.render(f"Score: {paddle.points}", False, red_color)
	rect = score.get_rect()
	rect.center = (660, 50)
	win.blit(score, rect)

	streak = font.render(f"Streak: {paddle.streak}", False, red_color)
	rect = streak.get_rect()
	rect.center = (660, 80)
	win.blit(streak, rect)

	all_sprites.draw(win)
	pygame.display.update()

run = True
while run:
	#pygame.time.delay(100)
	clock.tick(30)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	key = pygame.key.get_pressed()
	if key[pygame.K_UP]:
		paddle.rect.y += -10

	if key[pygame.K_DOWN]:
		paddle.rect.y += 10

	pong.rect.x += pong.speed*pong.dirnx
	pong.rect.y += pong.speed*pong.dirny

	if pong.rect.y > 490:
		pong.dirny = -1

	if pong.rect.x > 740:
		pong.rect.x, pong.rect.y = 375, 225
		#pong.dirnx = -1
		paddle.points -= 1
		paddle.streak = 0

	if pong.rect.y < 0:
		pong.dirny = 1

	if paddle.rect.y > 425:
		paddle.rect.y = 425

	if paddle.rect.y < 0:
		paddle.rect.y = 0

	if wall.rect.colliderect(pong.rect):
		pong.dirnx = 1

	if paddle.rect.colliderect(pong.rect):
		pong.dirnx = -1
		paddle.streak += 1
		if paddle.streak % 5 == 0:
			paddle.points += 1

	redrawWindow()

pygame.quit()
