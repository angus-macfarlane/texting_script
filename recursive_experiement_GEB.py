#Recursive Word Generator

import random
random.seed(3)

def ornate_noun():
	articles = ["a", "an", "the"]
	adjectives = ["adorable", "adventurous", "aggressive", "agreeable", "alert"]
	nouns = ["ambulance", "animal", "hair", "helicopter", "bear", "genie", "tortoise"]
	print(random.choice(articles), random.choice(adjectives), random.choice(nouns))


def fancy_noun():
	def track_0():
		print("track 0")
		
	
	def track_1():
		ornate_noun()
		

	def track_2():
		preposition = ["against", "along", "before", "past", "on", "throughout", "since"]
		print("TRACK 2", random.choice(preposition), fancy_noun()) #it's recursing out here. Why??
		quit()

	def track_3():
		return "track 3"
		# relative_pronoun = ["who", "whoever", "whom", "when", "where", "whose"]
		# def track_3_1():
		# 	verb = ["be", "taste", "run", "walk", "fly", "skate", "cook"]
		# 	fancy_noun()
		# 	print(random.choice(verb), fancy_noun())
		# def track_3_2():
		# 	fancy_noun()
		# 	verb = ["tangle", "paint", "craft", "sculpt", "research"]
		# 	print(fancy_noun(), random.choice(verb))
	functions = [track_0, track_1, track_2]
	functions[random.randrange(0, 3)]()
	



def main():
	print("Ornate Noun")
	ornate_noun()
	print("*******************")
	print("Fancy Noun")
	fancy_noun()



if __name__ == '__main__':
	main()



