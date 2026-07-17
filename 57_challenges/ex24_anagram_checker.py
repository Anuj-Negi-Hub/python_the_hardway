'''
Create a program that compares two strings and determines if the two strings are anagrams.
The program should prompt for both input strings and display the output as shown in the example that follows.

Example Output
Enter two strings and I'll tell you if they are anagrams:
Enter the first string: note
Enter the second string: tone
"note" and "tone" are anagrams.
'''

def isAnagram(word1, word2):
    sorted_word1 = "".join(sorted(word1))
    sorted_word2 = "".join(sorted(word2))
    
    if sorted_word1 == sorted_word2:
        print(f"{word1} and {word2} are anagrams.")
    else:
        print(f"{word1} and {word2} are not anagrams.")

word1 = input("Type the first word: ")
word2 = input("Type the second word: ")
isAnagram(word1, word2)