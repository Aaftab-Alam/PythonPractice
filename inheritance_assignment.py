class Player:
	def getdata(self):
		self.name=input("Enter your name: ")
		self.no_of_matches=int(input("Enter number of matches: "))
		
		
	def display(self):
		print("Name of Player:",self.name)
		print("Number of Matches Played:",self.no_of_matches)
		
		
class Bowler(Player):
	def getdata(self):
		super().getdata()
		self.no_of_wickets=int(input("Number of Wickets: "))
		self.no_of_overs=int(input("Number of overs: "))
		self.runs_conceded=int(input("Number of runs conceded: "))
		
	def display(self):
		super().display()
		print("Number of Wickets:",self.no_of_wickets)
		print("Number of Overs:",self.no_of_overs)
		print("Number of Runs Conceded:",self.runs_conceded)
		
		

class Batsman(Player):
	def getdata(self):
		super().getdata()
		self.runs=int(input("Runs: "))
		self.balls_faced=int(input("Balls Faced: "))
		
	def display(self):
		super().display()
		print("Runs:",self.runs)
		print("Balls faced:",self.balls_faced)
		
class Allrounder(Bowler,Batsman):
		def getdata(self):
			#Bowler.getdata(self)
			#Batsman.getdata(self)
			super().getdata()
			
		def display(self):
			Bowler.display(self)
			Batsman.display(self)
		
#player=Bowler()
#player.getdata()
#player.display()

player2=Allrounder()
player2.getdata()
player2.display()