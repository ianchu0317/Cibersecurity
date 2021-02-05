#!/usr/bin/env python3 

from random import choice		#Import the choice function from the random module
from string import digits, punctuation 		 #Import these function to use when invalidate the input
from os import system, listdir		#Import this module to clear the output
from platform import system as sys	#Import this module to detect the system 
from time import sleep			#Import this module to have a clean and organizated game

try:
	from colorama import Fore, Back, Style			#Coloring is fun
except ModuleNotFoundError:
	system("python3 -m pip install colorama")


logo = '''
 ▄▄▄·  ▐ ▄  ▄▄▄·  ▄▄ • ▄▄▄   ▄▄▄· • ▌ ▄ ·.      ▄▄ •  ▄▄▄· • ▌ ▄ ·. ▄▄▄ .
▐█ ▀█ •█▌▐█▐█ ▀█ ▐█ ▀ ▪▀▄ █·▐█ ▀█ ·██ ▐███▪    ▐█ ▀ ▪▐█ ▀█ ·██ ▐███▪▀▄.▀·
▄█▀▀█ ▐█▐▐▌▄█▀▀█ ▄█ ▀█▄▐▀▀▄ ▄█▀▀█ ▐█ ▌▐▌▐█·    ▄█ ▀█▄▄█▀▀█ ▐█ ▌▐▌▐█·▐▀▀▪▄
▐█ ▪▐▌██▐█▌▐█ ▪▐▌▐█▄▪▐█▐█•█▌▐█ ▪▐▌██ ██▌▐█▌    ▐█▄▪▐█▐█ ▪▐▌██ ██▌▐█▌▐█▄▄▌
 ▀  ▀ ▀▀ █▪ ▀  ▀ ·▀▀▀▀ .▀  ▀ ▀  ▀ ▀▀  █▪▀▀▀    ·▀▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀ 
'''
logo1 = '''
   __                                    ()  ,               
  /  )                                   /`-'|               
 /--/ ____  __.  _,  __  __.  ______    /   / __.  ______  _ 
/  (_/ / <_(_/|_(_)_/ (_(_/|_/ / / <_  /__-<_(_/|_/ / / <_</_
                 /|                                          
                |/                                           
'''
logo2= '''
  /\                                   /~~\                
 /__\ |/~\ /~~|/~~||/~\/~~||/~\ /~\   |  __/~~||/~\ /~\ /~/
/    \|   |\__|\__||   \__||   |   |   \__/\__||   |   |\/_
               \__|                                        
'''
logo3= '''

 ___   ____  ___   ____  ____  ___   ____    ____  ___   ____  ____ 
|_  \ |__  ||_  \ | _  ||_   ||_  \ |_   |  | _  ||_  \ |_   ||    |
 _|> | _/ /  _|> || \|_| / | | _|> | _< <   | \|_| _|> | _< < ||_| |
|___/ |____||___/ \__|  |/\__/|___/ |____|  \__|  |___/ |____||_||_|

'''
logo4 = '''

  AAA                                                           GGGG                             
 AAAAA  nn nnn    aa aa  gggggg rr rr    aa aa mm mm mmmm      GG  GG   aa aa mm mm mmmm    eee  
AA   AA nnn  nn  aa aaa gg   gg rrr  r  aa aaa mmm  mm  mm    GG       aa aaa mmm  mm  mm ee   e 
AAAAAAA nn   nn aa  aaa ggggggg rr     aa  aaa mmm  mm  mm    GG   GG aa  aaa mmm  mm  mm eeeee  
AA   AA nn   nn  aaa aa      gg rr      aaa aa mmm  mm  mm     GGGGGG  aaa aa mmm  mm  mm  eeeee 
                         ggggg                                                                   
'''
logo5 = '''
                                                           
,---.                                  ,---.               
|---|,---.,---.,---.,---.,---.,-.-.    |  _.,---.,-.-.,---.
|   ||   |,---||   ||    ,---|| | |    |   |,---|| | ||---'
`   '`   '`---^`---|`    `---^` ' '    `---'`---^` ' '`---'
               `---'                                       
'''
class Game: 
	def __init__(self):
		self.words = ["AREEGO", "SAFWAAN", "LOGIC"]
		self.punctuation = punctuation
		self.digits = digits
		self.platform = sys()
		self.score = 0		#Initial score
		self.min_score = 0	#Min score
		self.max_score = 0	#Max score
		self.score_menu = f'''
		"__Score Menu__"
		- Actual score = {self.score}
		- Min score = {self.min_score}
		- Max score = {self.max_score}
'''
		self.user_word = " "		
		self.filename = " "


	#Ask the user if he/she want to save the score into a .txt file		
	def ask_save(self):
		want_to_save = input("[+] Do you want to save your score ? (y/n): ").upper().strip().replace(" ", "")
		if want_to_save == "Y":
			return True
		elif want_to_save == "N": 
			return False
		else:
			print("[-] The entered answer is invalid :(")
			sleep(1)
			self.clear()
			self.ask_save()
		
	#write the score into a file
	def write_score(self):
		if f"{self.filename}.txt" in listdir():
			print("[+] File with that name already exist")
		with open(f"{self.filename}.txt", "a") as file:
			file.write(f"{self.score_menu}")
			
				
	#Keep the track of the scoring system
	def score_calculator(self):		
		if self.score >= self.max_score:
			self.max_score = self.score
		elif self.score <= self.min_score:
			self.min_score = self.score

		else: 
			pass
			
		self.score_menu = f'''
		"__Score Menu__"
		- Actual score = {self.score}
		- Min score = {self.min_score}
		- Max score = {self.max_score}
'''
	
	#Clear the player screen
	def clear(self):
		if self.platform == "Linux" or self.platform == "Darwin":
			system("clear")
		else:
			system("cls")


	#Say goodbye to the user/player
	def goodbye(self):
		self.clear()
		want_to_save = self.ask_save()
		if want_to_save:
			self.filename = input("[+] Enter the filename for the score file: ").strip().replace(" ", "")
			self.write_score()
		else:
			pass
			
		self.score_calculator()
		print(f"{self.score_menu}\n\n")
		print("See you next time :) ")
		exit()

	#Check if the user want to continue playing this game
	def continue_playing(self):
		self.clear()
		continue_ = input("[+] Do you want to continue playing ? [y/n]: ").lower()
		if continue_ == "y": 
			self.main()
		elif continue_ == "n": 
			self.goodbye()
		else: 
			print("[*] Invalid option... :(")
			sleep(3)
			self.continue_playing()


	#Check the user input word with the lenght of every word in the dictionary(list)
	def check_lenght(self):
		counter = 0
		for word in self.words:
			if len(word) != len(self.user_word):
				pass
			else: 
				counter +=1
		if counter > 0:
			print()
			return True
		else:
			return False
		
		
	#Check if the word is anagram in the known words
	def check_anagram(self):
		for word in self.words:
			if sorted(word) == sorted(self.user_word):
				print(sorted(word))
				print(sorted(self.user_word))
				return True
				break
			else:
				pass
		return False
		
	
	#Compare the random chosen word with the user input word
	def compare_word(self):
		lenght = self.check_lenght()
		if lenght==False:		#The intered word dont match with the guessing word (we check the lenght of the input with the lenght of the guessing word)
				print("The entered word lenght don't match\n\n")
				self.score -= 1
				self.score_calculator()
				self.main()
		else: 				
			is_anagram = self.check_anagram()			#If the entered word has the same lenght, we will continue to check if has the same letters
			if is_anagram:						#If the entered word has the same letters, he has won, else, he lose 
				print("You won :)")
				self.score += 1
				print(self.score)
				self.score_calculator()
				print("Please wait 3 second")
				sleep(3)
				self.continue_playing()
			else:
				print("Wrong answer :(\n\n")
				self.score -= 1
				self.score_calculator()
				self.main()


	#Check the word letter by letter
	def check_spelling(self):
		for letter in self.user_word: 
			if letter in self.punctuation: 
				print("The entered word has punctuation :(\n\n")
				self.score -= 1
				self.score_calculator()
				self.main()
			elif letter in self.digits: 
				print("The entered word has digits :(\n\n")
				self.score -= 1
				self.score_calculator()
				self.main()
			else: 
				pass


	#A function to ask the user input
	def input_word(self):
		self.user_word = str(input("[+] Enter a word to play or 'q' to quit: ")).upper().strip()
		if self.user_word == "Q":
			self.goodbye()
		else:
			pass


	#Main function to run all the script
	def main(self):
		print(f"The list of known words is {self.words} (Just printing for testing)")
		self.input_word()
		self.check_spelling()
		self.compare_word()



#Ask the user if he/she want to play the game
def want_to_play():
	try:
		print(Fore.YELLOW)
		question = input("[?] Do you want to play this game ? [y/n]: ").strip(" ").lower()
		if question == "y":
			return True
		elif question == "n":
			return False
		else:
			print("[-] Invalid answer :/")
			want_to_play()
	except KeyboardInterrupt:
		quit()



#Check if the self.user_word is running in the main script 
if __name__ == "__main__":
	print(Fore.RED,logo)
	sleep(1.5)
	print(Fore.GREEN, logo1)
	sleep(1.5)
	print(Fore.BLUE, logo2)
	sleep(1.5)
	print(Fore.CYAN, logo3)
	sleep(1.5)
	print(Fore.YELLOW, logo4)
	sleep(1.5)
	print(Fore.WHITE, logo5)
	
	_want_to_play = want_to_play()
	game = Game()	#Create game object
	if _want_to_play:
		try:	
			game.clear()	#Clear the console
			game.main()	#Run the main script
		except KeyboardInterrupt:
			quit()
	else:
		try:
			game.goodbye()
		except KeyboardInterrupt:
			quit()
