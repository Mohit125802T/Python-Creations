square_number = int(input("Enter your square number: "))
print("")
if pow(pow(square_number,1/2),2) != pow(round(pow(square_number,1/2)),2):
    print("\033[31mThe given number is not a perfect square of any Number.\033[0m")
else:
    root_of_number = pow(square_number,1/2)
    next_square_number = pow(root_of_number+1,2)
    print("\033[32mNext square number is:\033[0m\033[4m",round(next_square_number),"\033[0m")
print("")
print("")
print("\033[35mThank you for using \033[1mNext Square Finder\033[0m")
print("\033[35mMade by\033[0m \033[97m\033[1mMohit Kumar\033[0m \033[35mwith\033[0m \033[91m\033[1mLove <3\033[0m")
