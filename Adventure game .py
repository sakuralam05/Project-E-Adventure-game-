name=input("type your name:")
print("Welcome", name,"to this adventure game!")

answer=input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you go ?").lower()


if answer=="left":
    answer=input("You have come to a river, you can walk around it or swim across, Which would you choose?")

if answer=="swim":
 print("You sawm across and were eaten by an alligator.")
 
elif answer== "walk":
 print("You walked for for 10hours and ran out of water. On top of that you ran out of water. You lose")    
       else:
           print("Not a valid option. You lose")

        
        
elif answer="right"
      answer=input("You have come to a bridge, it looks wobbly, do you want to cross it or head back?(cross/back)")
      
  if answer=="back":
 print("You have returned to the main road.")
 
elif answer== "cross":
 answer=input("You cross the bridge and meet a stranger. Approach them, yes or no ?(yes/no)")
    if answer=="yes":
        print("talk to stranger and recieve gold from the stranger. You win")
    elif answer=="no"
    print("You ignore the stranger and they get offended. You lose ")
else:
  print("Not a valid option. You lose")