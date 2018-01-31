import random

def ask_user():
	user_input = input("What is your question?")

<<<<<<< HEAD
	if user_input[-1] != "?":
		print("I'm sorry, I can only answer questions.")

	while user_input != "quit":
		user_input = input("What is your question?")
=======

answer_list = ["It is certain","It is decidedly so","Without a doubt","Yes definitely", "You may rely on it","As I see it, yes","Most likely","Outlook good","Yes","Signs point to yes","Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now","Concentrate and ask again", "Don't count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful"]
answer = answer_list[randrange(len(answer_list))]
>>>>>>> master
