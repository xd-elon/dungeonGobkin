import pygame

class player: 
  def __init__(self, name, level, hp, mp, atk, df):
    #status
    self.name = name
    self.level = level
    self.hp = hp
    self.mp = mp
    self.atk = atk
    self.df = df


    self.vel_x = 0
    self.vel_y = 0

  def move(self, keys): 
    self.vel_x, self.vel_y = 0, 0

    if keys[pygame.K_LEFT]:
      self.vel_x = -5
    if keys[pygame.K_RIGHT]:
      self.vel_x =  5
    if keys[pygame.K_UP]:
      self.vel_y = -5
    if keys[pygame.K_DOWN]:
      self.vel_y =  5

    self.rect.x += self.vel_x
    self.rect.y += self.vel_y

  def take_damage(self, targe): 
    self.hp -targe

  def draw(): 
    # draw
    print("drwa")

  def update(): 
    # update
    print("update")