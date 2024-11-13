import random
import time, os

print("chat or cmd?")
c = input('')
if c == 'cmd':
  pass
elif c == 'chat':
  os.system('clear')
  greetings = ["hello", "how are you doing today", "hi"]
  goodbyes = ["have a nice day", "Bye"]
  status = 'on'
  keywords = ["music", "food", "bombs", "you too"]
  responses = [
    "My favorite music is counray", "yes food", "USA USA USA", "Thank you"
  ]

  print(random.choice(greetings))

  user = input("type music or food (or type bye to quit): ")
  user = user.lower()

  while (status == 'on'):
    if user == "bye":
      print(random.choice(goodbyes))
      status = 'off'
    if (user != "bye"):
      keyword_found = False

      for index in range(len(keywords)):
        if (keywords[index] in user):
          print("Bot: " + responses[index])
          keyword_found = True

      if (keyword_found == False):
        keywords.append(user)
        new_response = input("what do i say to " + user + "?")
        responses.append(new_response)
    if status == 'on':
      user = input("type music or food (or type bye to quit): ")
      user = user.lower()
