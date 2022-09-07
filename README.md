# Elite101PreWork
This repository contains my pre-work for the Elite 101 course at Code2College. 
This program uses Python to create a simple joke bot. 

# Flow
The joke bot asks the user if they want to hear a joke. If the user says yes, a random Chuck Norris joke is printed out, followed by a random comment on that joke. The joke bot will continue to ask the user if they'd like to hear another one. If the user says anything other than yes, the bot will insist and tell another joke anyway. The only way to turn off the joke bot and stop the program is by pressing "q", the quit key. 


# Documentation
I followed this example for the basic setup: https://repl.it/@lagrassom/chatbot01

Before importing the pyjokes library, I installed it in the shell using "pip install pyjokes". I left the import of the random library to use random selection later on.
On line 5, I left the defined generate_response() function and removed the parameter, since it won't need any additional information. Inside this function, the get_joke() method is stored in the variable "joke" and printed out. On the next line, a list of comments the bot can use to respond to the joke is assigned to the variable "followUp". A random response is selected, using random.choice(), and printed out. 

On line 23, I used the previously defined init_chat() function, which will initiate the conversation with the user. Inside this function, the string "q" is assigned to the quit_character variable. I liked this from the example so that if the user chose not to "hear a joke", the joke bot has the opportunity to insist. The user_input variable stores the input() function that asks the user if they want to hear a joke. 

A list of responses the bot can say anytime the user doesn't say yes, is assigned to the sarcastic_reply variable. 

A while loop is created inside the init_chat() function, as well, so the quit_character can be used as the condition being tested. While the user does not input "q", the quit character, the joke bot will continue to tell jokes. The if statement inside the loop checks if the user said anything other than yes when they are originally asked if they want to hear a joke. If true, a random response from the sarcastic_reply list will print out. The generate_response() function is called and then the user is prompted again to hear another joke. 

Finally, on line 45, I used the same condition from the example that checks if the name of the file is the main file. If true, the program will call the init_chat() function. 



