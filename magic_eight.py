def ask_user():
	user_input = input("What is your question?")

	if user_input[-1] != "?":
		print("I'm sorry, I can only answer questions.")

	while user_input != "quit":
		user_input = input("What is your question?")