#this is my first code........

print ("HI")
print ("welcome to Prithviquiz 1")
print ("respond with (yes or no)")
score=0
answer=input('so ready to play the game?')
total_questions=3
 
if answer.lower()=='yes':
     answer=input('Question 1: who is Albert einstein:')
     if answer.lower()=='scientist':
        score += 1
        print("nice, correct")
     else:
         print("wrong....")   

     answer=input('Question 2: When was albert einstain born ??:')
     if answer.lower=='March 14':
         score += 1
         print("nice,correct")
     else:
         print("Wrong....")  

     answer=input('what do we use to type in a computer/laptop??:')
     if answer.lower=='keyboard':
         score += 1
         print("nice") 
     else:
         print("Wrong.....")
         print("Thanks for playing :)....") 

         print("you scored",score,"Marks, BYE BYE")     
elif answer.lower()=='no':
      print("i hate you, bye bye")

else:
    print("the answer you gave is incorrect, restart the program and respond with (yes or no)")

#done
