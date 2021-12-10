# hashing.py
# Authors: John Thomas, Levi Graham, Riley Nichols, Sam Rudqvist
# Date: 12/09/21
# Course: CSCI 262: Algorithms
# Purpose: To implement an open hashing algorithm for the broadband
#          upgrade final project.
# Modification Log:
#   - 2021.12.09 - LG - Added header and started design.
#   - 2021.12.10 - LG - Added the HashedItem class and documentation
#                       for the class. Also added constants.
#   - 2021.12.10 - SR - Started user interface. 


# Constants
MOD = 11 # Mod factor for the hashing algorithm.
INPUT_FILE = 'short_input.csv' # Input file for tweets.

# HashedItem - A class to hold the text of a tweet, a hashtag, and
#              the pointer to the next hashedItem in the stack.
# 
# Properties:
#   tweet - String for the tweet that is held by an object of this
#           class. 
#   hashtag - Holds the string for the hashtag that is held by an
#             object of this class. 
#   next_pointer - Pointer to the next object in the hashed list.
class HashedItem:
  
  # __init__() - Initializer for the object of this class.
  #
  #   Parameters:
  #     tweet - String for the text of the tweet.
  #     hashtag - String for the hashtag for this tweet.
  def __init__(self, tweet, hashtag):
    self.tweet = tweet
    self.hashtag = hashtag
    self.next_pointer = None

# TODO: Add in read_file() method. 









# user_interface() - This is what the user will interact with when 
#                    using this application.
def user_interface():
  print("\nWelcome to Open Hashed Twitter\n\nFunctions availble: ")
  print("   Add new tweet (A)\n   Search for hashtag (S)\n")

  user_input = input("What would you like to do? (A/S) ").upper()

  if user_input == "A":
    pass
  elif user_input == "S":
    pass
  else:
    restart = input("\nIncorrect input.\nWould you like to restart? (Y/N) ")
    if restart.upper() == "Y":
      user_interface()
    else:
      print("\nEnding Execution")

if __name__ == "__main__":
  user_interface()