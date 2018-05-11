class Game:
    
    def __init__(self):
        #speed must be < player size
        self.player1 = 1
        self.player2 = -1
        self.width = 240
        self.high = 160
        #bullets = matrix, each list contains: x,y,directions
        self.player1_bullets = []
        self.player2_bullets = []
        self.player1_position = [20,20]
        self.player2_position = [220,20]
        #resize number = 1 or = 2
        self.player1_resize = 1
        self.player2_resize = 1
        self.player1_lifepoints = 5
        self.player2_lifepoints = 5
        #player_size is half player size
        self.players_size = 5
        #bullets_size is half bullets size
        self.bullets_size = 2
        self.max_bullets = 7
        self.life_position = [120,80]
        self.life_size = 1
        self.speed = 2
        
    #directions:
    #1 = up
    #2 = down
    #3 = left
    #4 = right
    
    def move_player(self, player, directions):
        
        if(player > 0):
            if(directions == 1):
                
                if(self.player1_position[1] - self.players_size*player1_resize >= self.speed and not (self.player2_position[1] - self.players_size*player2_resize <= self.player1[1] - self.players_size*player1_resize - self.speed and self.player1[1] - self.players_size*player1_resize - self.speed <= self.player2_position[1] + self.players_size*player2_resize)):
                    self.player1_position[1] -= self.speed
            
            elif (directions == 2):
                if(self.player1_position[1] + self.players_size*player1_resize <= self.high - self.speed and not (self.player2_position[1] - self.players_size*player2_resize <= self.player1[1] + self.players_size*player1_resize + self.speed and self.player1[1] - self.players_size*player1_resize + self.speed <= self.player2_position[1] + self.players_size*player2_resize)):
                    self.player1_position[1] += self.speed
                    
            elif (directions == 3):
                if(self.player1_position[0] - self.players_size*player1_resize >= self.speed - self.speed and not (self.player2_position[0] - self.players_size*player2_resize <= self.player1[0] + self.players_size*player1_resize + self.speed and self.player1[0] - self.players_size*player1_resize + self.speed <= self.player2_position[0] + self.players_size*player2_resize)):
                    self.player1_position[0] -= self.speed
                    
            else:
                if(self.player1_position[0] + self.players_size*player1_resize <= self.width - self.speed and not (self.player2_position[0] - self.players_size*player2_resize <= self.player1[0] + self.players_size*player1_resize + self.speed and self.player1[0] - self.players_size*player1_resize + self.speed <= self.player2_position[0] + self.players_size*player2_resize)):
                    self.player1_position[0] += self.speed
            
            return self.player1_position
                    
        else:
            if(directions == 1):
                
                if(self.player2_position[1] - self.players_size*player2_resize >= self.speed and not (self.player1_position[1] - self.players_size*player1_resize <= self.player2[1] - self.players_size*player2_resize - self.speed and self.player2[1] - self.players_size*player2_resize - self.speed <= self.player1_position[1] + self.players_size*player1_resize)):
                    self.player2_position[1] -= self.speed
            
            elif (directions == 2):
                if(self.player2_position[1] + self.players_size*player2_resize <= self.high - self.speed and not (self.player1_position[1] - self.players_size*player1_resize <= self.player2[1] + self.players_size*player2_resize + self.speed and self.player2[1] - self.players_size*player2_resize + self.speed <= self.player1_position[1] + self.players_size*player1_resize)):
                    self.player2_position[1] += self.speed
                    
            elif (directions == 3):
                if(self.player2_position[0] - self.players_size*player2_resize >= self.speed - self.speed and not (self.player1_position[0] - self.players_size*player1_resize <= self.player2[0] + self.players_size*player2_resize + self.speed and self.player2[0] - self.players_size*player2_resize + self.speed <= self.player1_position[0] + self.players_size*player1_resize)):
                    self.player2_position[0] -= self.speed
                    
            else:
                if(self.player2_position[0] + self.players_size*player2_resize <= self.width - self.speed and not (self.player1_position[0] - self.players_size*player1_resize <= self.player2[0] + self.players_size*player2_resize + self.speed and self.player2[0] - self.players_size*player2_resize + self.speed <= self.player1_position[0] + self.players_size*player1_resize)):
                    self.player2_position[0] += self.speed
            
            return self.player2_position
            
        
    def move_bullets(self):
    
        len1 = len(self.player1_bullets)
        len2 = len(self.player2_bullets)
        
        remove_bullets = []
        for i in range(0,len1):
            if(self.player1_bullets[i][-1] == 1):
                if(self.player1_bullets[i][1] - self.bullet_size >= self.speed):
                    if (self.player2_position[1] - self.players_size*player2_resize <= self.player1_bullets[i][1] - self.bullet_size - self.speed and self.player1_bullets[i][1] - self.speed - self.bullet_size <= self.player2_position[1] + self.players_size*player2_resize)):
                        remove_bullets.append(self.player1_bullets[i])
                        self.player2_lifepoints -= 1
                    
                    else:
                        self.player1_bullets[i][1] -= self.speed
                else:
                    remove_bullets.append(self.player1_bullets[i])
                    
            elif(self.player1_bullets[i][-1] == 2):
                if(self.player1_bullets[i][1] + self.bullet_size <= self.high - self.speed):
                    if (self.player2_position[1] - self.players_size*player2_resize <= self.player1_bullets[i][1] + self.bullet_size + self.speed and self.player1_bullets[i][1] + self.speed + self.bullet_size <= self.player2_position[1] + self.players_size*player2_resize)):
                        remove_bullets.append(self.player1_bullets[i])
                        self.player2_lifepoints -= 1
                    
                    else:
                        self.player1_bullets[i][1] += self.speed
                else:
                    remove_bullets.append(self.player1_bullets[i])
                    
            elif(self.player1_bullets[i][-1] == 3):
                if(self.player1_bullets[i][0] - self.bullet_size >= self.speed):
                    if (self.player2_position[0] - self.players_size*player2_resize <= self.player1_bullets[i][0] - self.bullet_size - self.speed and self.player1_bullets[i][0] - self.speed - self.bullet_size <= self.player2_position[0] + self.players_size*player2_resize)):
                        remove_bullets.append(self.player1_bullets[i])
                        self.player2_lifepoints -= 1
                    
                    else:
                        self.player1_bullets[i][0] -= self.speed
                else:
                    remove_bullets.append(self.player1_bullets[i])
                    
            elif(self.player1_bullets[i][-1] == 2):
                if(self.player1_bullets[i][0] + self.bullet_size <= self.width - self.speed):
                    if (self.player2_position[0] - self.players_size*player2_resize <= self.player1_bullets[i][0] + self.bullet_size + self.speed and self.player1_bullets[i][0] + self.speed + self.bullet_size <= self.player2_position[0] + self.players_size*player2_resize)):
                        remove_bullets.append(self.player1_bullets[i])
                        self.player2_lifepoints -= 1
                    
                    else:
                        self.player1_bullets[i][0] += self.speed
                else:
                    remove_bullets.append(self.player1_bullets[i])
                    
        for i in range(0,len(remove_bullets):
            if(remove_bullets[i] in self.player1_bullets):
                self.player1_bullets.remove(remove_bullets[i])
                
                
        remove_bullets = []
        for i in range(0,len2):
            if(self.player2_bullets[i][-1] == 1):
                if(self.player2_bullets[i][1] - self.bullet_size >= self.speed):
                    if (self.player1_position[1] - self.players_size*player1_resize <= self.player2_bullets[i][1] - self.bullet_size - self.speed and self.player2_bullets[i][1] - self.speed - self.bullet_size <= self.player1_position[1] + self.players_size*player1_resize)):
                        remove_bullets.append(self.player2_bullets[i])
                        self.player1_lifepoints -= 1
                    
                    else:
                        self.player2_bullets[i][1] -= self.speed
                else:
                    remove_bullets.append(self.player2_bullets[i])
                    
            elif(self.player2_bullets[i][-1] == 2):
                if(self.player2_bullets[i][1] + self.bullet_size <= self.high - self.speed):
                    if (self.player1_position[1] - self.players_size*player1_resize <= self.player2_bullets[i][1] + self.bullet_size + self.speed and self.player2_bullets[i][1] + self.speed + self.bullet_size <= self.player1_position[1] + self.players_size*player1_resize)):
                        remove_bullets.append(self.player2_bullets[i])
                        self.player1_lifepoints -= 1
                    
                    else:
                        self.player2_bullets[i][1] += self.speed
                else:
                    remove_bullets.append(self.player2_bullets[i])
                    
            elif(self.player2_bullets[i][-1] == 3):
                if(self.player2_bullets[i][0] - self.bullet_size >= self.speed):
                    if (self.player1_position[0] - self.players_size*player1_resize <= self.player2_bullets[i][0] - self.bullet_size - self.speed and self.player2_bullets[i][0] - self.speed - self.bullet_size <= self.player1_position[0] + self.players_size*player1_resize)):
                        remove_bullets.append(self.player2_bullets[i])
                        self.player1_lifepoints -= 1
                    
                    else:
                        self.player2_bullets[i][0] -= self.speed
                else:
                    remove_bullets.append(self.player2_bullets[i])
                    
            elif(self.player2_bullets[i][-1] == 2):
                if(self.player2_bullets[i][0] + self.bullet_size <= self.width - self.speed):
                    if (self.player1_position[0] - self.players_size*player1_resize <= self.player2_bullets[i][0] + self.bullet_size + self.speed and self.player2_bullets[i][0] + self.speed + self.bullet_size <= self.player1_position[0] + self.players_size*player1_resize)):
                        remove_bullets.append(self.player2_bullets[i])
                        self.player1_lifepoints -= 1
                    
                    else:
                        self.player2_bullets[i][0] += self.speed
                else:
                    remove_bullets.append(self.player2_bullets[i])
                    
            for i in range(0,len(remove_bullets):
                if(remove_bullets[i] in self.player2_bullets):
                    self.player2_bullets.remove(remove_bullets[i])
                    
    def shooting(self, player, directions):
    
        if(player > 0):
            if(len(self.player1_bullets) < self.max_bullets):
                if(directions == 1):
                    if(self.player1_position[1] - self.player1_resize*self.player_size - 2*self.bullet_size -1 > 0):
                        self.player1_bullets.append([self.player1_position[0]][self.player1_position[1] - self.player1_resize*self.player_size - self.bullet_size - 1][1])
                        self.bullet_hits_player(player,self.player1_bullets[-1])
                elif(directions == 2):
                    if(self.player1_position[1] + self.player1_resize*self.player_size + 2*self.bullet_size + 1 < self.high):
                        self.player1_bullets.append([self.player1_position[0]][self.player1_position[1] + self.player1_resize*self.player_size + self.bullet_size + 1][2])
                        self.bullet_hits_player(player,self.player1_bullets[-1])
                
                elif (directions == 3):
                    if(self.player1_position[0] - self.player1_resize*self.player_size - 2*self.bullet_size -1 > 0):
                        self.player1_bullets.append([self.player1_position[0] - self.player1_resize*self.player_size - self.bullet_size - 1][self.player_position[1]][3])
                        self.bullet_hits_player(player,self.player1_bullets[-1])
                
                else:
                    if(self.player1_position[0] + self.player1_resize*self.player_size + 2*self.bullet_size + 1 > self.width):
                        self.player1_bullets.append([self.player1_position[0] + self.player1_resize*self.player_size + self.bullet_size + 1][self.player_position[1]][4])
                        self.bullet_hits_player(player,self.player1_bullets[-1])
                        
        else:
            if(len(self.player2_bullets) < self.max_bullets):
                if(directions == 1):
                    if(self.player2_position[1] - self.player2_resize*self.player_size - 2*self.bullet_size -1 > 0):
                        self.player2_bullets.append([self.player2_position[0]][self.player2_position[1] - self.player2_resize*self.player_size - self.bullet_size - 1][1])
                        self.bullet_hits_player(player,self.player2_bullets[-1])
                elif(directions == 2):
                    if(self.player2_position[1] + self.player2_resize*self.player_size + 2*self.bullet_size + 1 < self.high):
                        self.player2_bullets.append([self.player2_position[0]][self.player2_position[1] + self.player2_resize*self.player_size + self.bullet_size + 1][2])
                        self.bullet_hits_player(player,self.player2_bullets[-1])
                
                elif (directions == 3):
                    if(self.player2_position[0] - self.player2_resize*self.player_size - 2*self.bullet_size -1 > 0):
                        self.player2_bullets.append([self.player2_position[0] - self.player2_resize*self.player_size - self.bullet_size - 1][self.player2_position[1]][3])
                        self.bullet_hits_player(player,self.player2_bullets[-1])
                
                else:
                    if(self.player2_position[0] + self.player2_resize*self.player_size + 2*self.bullet_size + 1 > self.width):
                        self.player2_bullets.append([self.player2_position[0] + self.player2_resize*self.player_size + self.bullet_size + 1][self.player2_position[1]][4])
                        self.bullet_hits_player(player,self.player2_bullets[-1])
                        
       
	def bullet_hits_player(self,player,bullet):
            
        enemy = -player
        if(enemy > 0):
         
            for i in range(0,self.bullet_size + 1):
                if(bullet[0] + i >= self.player1_position[0] - self.player1_resize*self.player_size and bullet[0] + i <= self.player1_position[0] + self.player1_resize*self.player_size):
                    if (bullet[1] + i >= self.player1_position[1] - self.player1_resize*self.player_size and bullet[1] + i <= self.player1_position[1] + self.player1_resize*self.player_size):
                        self.player1_lifepoints -= 1
                        self.player1_bullets.remove(bullet)
                        break
                    
                if (bullet[0] - i >= self.player1_position[0] - self.player1_resize*self.player_size and bullet[0] - i <= self.player1_position[0] + self.player1_resize*self.player_size):
                    if (bullet[1] - i >= self.player1_position[1] - self.player1_resize*self.player_size and bullet[1] - i <= self.player1_position[1] + self.player1_resize*self.player_size):
                        self.player1_lifepoints -= 1
                        self.player1_bullets.remove(bullet)
                        break
                        
                    
                        
                    
        else:
            for i in range(0,self.bullet_size + 1):
                if(bullet[0] + i >= self.player2_position[0] - self.player2_resize*self.player_size and bullet[0] + i <= self.player2_position[0] + self.player2_resize*self.player_size):
                    if (bullet[1] + i >= self.player2_position[1] - self.player2_resize*self.player_size and bullet[1] + i <= self.player2_position[1] + self.player2_resize*self.player_size):
                        self.player2_lifepoints -= 1
                        self.player2_bullets.remove(bullet)
                        break
                    
                if (bullet[0] - i >= self.player2_position[0] - self.player2_resize*self.player_size and bullet[0] - i <= self.player2_position[0] + self.player2_resize*self.player_size):
                    if (bullet[1] - i >= self.player2_position[1] - self.player2_resize*self.player_size and bullet[1] - i <= self.player2_position[1] + self.player2_resize*self.player_size):
                        self.player2_lifepoints -= 1
                        self.player2_bullets.remove(bullet)
                        break
                        
                    
                        
                    
                        
        
	def player_takes_life(self,player):
	
		if(player > 0):
			for i in range(0,self.life_size + 1):
				if(self.life_position[0] + i >= self.player1_position[0] - self.player1_resize*self.player_size and self.life_position[0] + i <= self.player1_position[0] + self.player1_resize*self.player_size):
					if (self.life_position[1] + i >= self.player1_position[1] - self.player1_resize*self.player_size and self.life_position[1] + i <= self.player1_position[1] + self.player1_resize*self.player_size):
						self.player1_lifepoints += 1
						return True
				
				if (self.life_position[0] - i >= self.player1_position[0] - self.player1_resize*self.player_size and self.life_position[0] - i <= self.player1_position[0] + self.player1_resize*self.player_size):
					if (self.life_position[1] - i >= self.player1_position[1] - self.player1_resize*self.player_size and self.life_position[1] - i <= self.player1_position[1] + self.player1_resize*self.player_size):
						self.player1_lifepoints += 1
						return True
		else:
			for i in range(0,self.life_size + 1):
				if(self.life_position[0] + i >= self.player2_position[0] - self.player2_resize*self.player_size and self.life_position[0] + i <= self.player2_position[0] + self.player2_resize*self.player_size):
					if (self.life_position[1] + i >= self.player2_position[1] - self.player2_resize*self.player_size and self.life_position[1] + i <= self.player2_position[1] + self.player2_resize*self.player_size):
						self.player2_lifepoints += 1
						return True
				
				if (self.life_position[0] - i >= self.player2_position[0] - self.player2_resize*self.player_size and self.life_position[0] - i <= self.player2_position[0] + self.player2_resize*self.player_size):
					if (self.life_position[1] - i >= self.player2_position[1] - self.player2_resize*self.player_size and self.life_position[1] - i <= self.player2_position[1] + self.player2_resize*self.player_size):
						self.player2_lifepoints += 1
						return True
   
		return False    
			
	def player_resize(self,player):
		if(player > 0):
			if (self.player1_resize == 1):
				self.player1_resize = 2
			else:
				self.player1_resize = 1
		else:
			if (self.player2_resize == 1):
				self.player2_resize = 2
			else:
				self.player2_resize = 1
                
                
        
