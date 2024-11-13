import os
import random

print("chat or cmd?")
c = input('')
if c == 'cmd':
  pass
elif c == 'chat':
  os.system('clear')
  greetings = ["hello", "how are you doing today", "hi"]
  goodbyes = ["have a nice day", "Bye", "Bye, have a good time"]
  status = 'on'

  # Open keywords and responses files for reading and writing
  with open("keywords.txt", "a+") as k:
    k.seek(0)
    keywords = k.read().splitlines()

  with open("responses.txt", "a+") as r:
    r.seek(0)
    responses = r.read().splitlines()
###-------------------------------------------------------###
  
  print(random.choice(greetings))
  
  user = input("type music or food (or type bye to quit): ")
  user = user.lower()

  while status == 'on':
    while user.strip() == "":
      user = input("COME ON MAN USE YOUR GROWN UP WORDS: ")
      user = user.lower()
      pass

    if user == "bye":
      os.system('clear')
      print(random.choice(goodbyes))
      status = 'off'
    elif user != "bye":
      keyword_found = False

      for index in range(len(keywords)):
        if keywords[index] in user.strip().replace(" ", ""):
          print("Bot: " + responses[index])
          keyword_found = True

      if not keyword_found:
        new_response = input("what do I say to " + user + "? \n")
        keywords.append(user.strip().replace(" ", ""))
        responses.append(new_response)

        with open("keywords.txt", "w") as k:
          k.write("\n".join(keywords))

        with open("responses.txt", "w") as r:
          r.write("\n".join(responses))

    if status == 'on':
      user = input("type music or food (or type bye to quit): ")
      user = user.lower()
