# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 13:34:34 2020

@author: RebekahDSK
"""


def main():

#user selection and displays choice
   user_choice = int(input("How many numbers?"))
   #print("User Choice:" + user_choice)

#conditionals; what happens when a number has been chosen
   if user_choice == 0:
        print("Fine, nothing for you then")
   elif user_choice == 1:
            print("0, ah ah ah")
   elif user_choice == 2:
                print("0, 1, ah ah ah")
   elif user_choice == 3:
                    print("0, 1, 2, ah ah ah")
   elif user_choice == 4:
                        print("0, 1, 2, 3, ah ah ah")
   elif user_choice == 5:
                            print("0, 1, 2, 3, 4, ah ah ah")
    
#after results have printed, ask the user if they would like to continue playing
   keep_playing = input("Would you like to keep playing? Yes or No")
   print("You've answered:" + keep_playing)

   if keep_playing == "Yes":
       main()
   else:
        print("Thanks for playing. Goodbye")
        exit()
main ()