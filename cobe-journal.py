#!/usr/bin/env python

# Require cobe. See https://github.com/pteichman/cobe

from cobe.brain import Brain

# main loop 
def main():
    f= open("journal.txt","a")
    b = Brain("cobe.brain")
    while True:
	try:
	    question_Asked = raw_input("User> ").lower()
	except EOFError:
	    print
	    break
        if question_Asked in ("#quit", "#bye","#exit"):
          break
        else:
	  msg = b.reply(question_Asked)
	  print "AI> "+msg
	  b.learn(question_Asked)
	  f.write("User> "+question_Asked+"\n")
	  f.write("AI> "+msg+"\n")
    f.close()
    return
    
if __name__ == '__main__': main() 
