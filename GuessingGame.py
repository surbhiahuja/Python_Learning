secret_word = "sur"
guess = ""

guess_count = 0
limit_of_guess = 3
is_limit_crossed = False

while guess!=secret_word and not(is_limit_crossed):
    if guess_count < limit_of_guess:
        guess = input("Enter guess number: ")
        guess_count +=1

    else:
        is_limit_crossed = True
    
if is_limit_crossed:
    print("you Loose the match")

else:
    print("you won the match: " + guess)