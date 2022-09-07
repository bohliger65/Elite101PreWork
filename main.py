import random 
import pyjokes


def generate_response():
  joke = pyjokes.get_joke(language="en", category="chuck")
  print("\n"+joke)
  followUp = [
    "Funny, right?",
    "Hilarious!",
    "They can't all be winners.",
    "Hahahahahaha",
    "Not my best...",
    "Knee-slapping!",
    "...crickets...",
    "LOL",
    "heheheheheh",
    "I saw that eyeroll..."
  ]
  
  return print("\n" + random.choice(followUp))

def init_chat():
  quit_character = 'q'
  user_input = input("Wanna hear a joke?\n")
  sarcastic_reply = [ #list of responses anytime the user doesn't say yes
    "I insist. ",
    "That means yes in my mind.",
    "Don't care, telling you anyway.",
    "In life, things are sometimes unfair. Here's your joke:",
    "I heard yes...",
    "This one might change your mind.",
  ]

  while user_input != quit_character:
    if user_input != 'yes':
      print("\n" + random.choice(sarcastic_reply)) 
    generate_response()
    user_input = input("\nReady for another? ")





if __name__ == "__main__":
  init_chat()