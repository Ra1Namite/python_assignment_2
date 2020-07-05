class Mario:
    def __init__(self):
        self.game_stage = 1
        self.speed = 1
        self.life = 3
        self.size = 1
        self.mushroom_level = 0
        self.score = 0
    def info(self):
        print('\nGame_Info')
        print('stage:', self.game_stage)
        print('Number of lives:', self.life)
        print('Score:', self.score,'\n')
        
    def move_forward(self):
        print('moving forward')

    def move_backward(self):
        print('moving backward')
    
    def jump(self):
        print('jumping')

    def shoot(self):
        if self.mushroom_level > 1:
            print('shooting bullet')
        else:
            print("can't shoot")

    def eat_mushroom(self):
        print('eating mushroom')
        self.mushroom_level += 1
        self.score += 1000
        if self.mushroom_level == 1:
            self.size += 1
            self.speed += 0.5
        elif self.mushroom_level == 2:
            self.speed += 0.5

new_player = Mario()
new_player.info()
new_player.move_forward()
new_player.move_backward()
new_player.jump()
new_player.shoot()
new_player.eat_mushroom()
new_player.info()
new_player.eat_mushroom()
new_player.shoot()
new_player.info()



