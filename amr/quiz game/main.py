#create quizes
#create answers
#create amount of tries
#get answer and see if its right 
#get number of tries see if its below the limit
#create loop to retry the wrong quiz
#get the final score

quiz1 ="whats one plus one "
quiz2 ="whats the color of the sun? "
quiz3 ="are you human? "
actual_answer1 ="2"
answer1 ="" 
actual_answer2 ="yellow"
answer2 =""
actual_answer3 = "yes"
answer3 =""
limit_of_tries = 10
number_of_tries = 0
answer =""
out_of_tries = False
score =0

print("welcome to the quiz, you have only " + str(limit_of_tries) +" tries")
#first quiz
while answer1 !=actual_answer1 and not out_of_tries:
  if number_of_tries<limit_of_tries:
    answer1 = input(quiz1)
    number_of_tries += 1
  else:
    out_of_tries = True
    print("you lost,out of tries")
  if answer1 == actual_answer1:
    print("correct answer")
    score+=1
  else:
    print("try again")

#second quiz
while answer2 !=actual_answer2 and not out_of_tries:
  if number_of_tries<limit_of_tries:
    answer2 = input(quiz2)
    number_of_tries += 1
  else:
    out_of_tries = True
    print("you lost,out of tries")
  if answer2 == actual_answer2:
    print("correct answer")
    score+=1
  else:
    print("try again")

#third quiz
while answer3 !=actual_answer3 and not out_of_tries :
  if number_of_tries<limit_of_tries:
    answer3 = input(quiz3)
    number_of_tries += 1
  else:
    out_of_tries = True
    print("you lost,out of tries")
  if answer3 == actual_answer3:
    print("correct answer")
    score+=1
  else:
    print("try again")


print( "you got "+str(limit_of_tries-number_of_tries+score)+" of "+str(limit_of_tries))

