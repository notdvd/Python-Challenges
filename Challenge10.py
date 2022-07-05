word = input("Enter a word: ")
wordMap = reversed(list(map(str,word)))
reverse = "".join(wordMap)
if word == reverse:
    print("Palindrome!")
else:
    print("Not a Plaindrome!")