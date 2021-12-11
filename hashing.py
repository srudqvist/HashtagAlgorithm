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
#   - 2021.12.10 - LG & SR - Implemented __init__, hash, and add_tweet
#                            methods for the Hashing class.


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
  #     self - Instance of the object.
  #     tweet - String for the text of the tweet.
  #     hashtag - String for the hashtag for this tweet.
  def __init__(self, tweet, hashtag):
    self.tweet = tweet
    self.hashtag = hashtag
    self.next_pointer = None

# Hashing - A class to operate the hashing algorithm.
#
# Properties:
#   table - The hashed table for the open hashing algorithm.
class Hashing:
  
  # __init__() - Initializer for the object of this class.
  #
  #   Parameters:
  #     self - Instance for the object.
  #     input_file - The .CSV file that is used for input.
  def __init__(self, input_file):
    # Create the self.table with the mod number of spaces.
    for i in range(MOD):
      self.table.append(None)
    
    # Opens the file and pulls all lines out to put into the hash table.
    with open(input_file, "r") as file:
      lines = file.readLines()
      
      # For each of the lines in the file, add them to the hash table. 
      for line in lines:
        hashtag, tweet = line.split(",")
        self.add_tweet(tweet, hashtag)
  
  # hash() - Creates the modded hash value for the hashtag so that
  #          it can be stored in the right place.
  #
  #   Parameters:
  #     self - Instance for the object.
  #     hashtag - The hashtag from the tweet.
  def hash(self, hashtag):
    # Start the accumulator.
    hashed_val = 0
    # For every character in the hashtag,
    for character in hashtag:
      #Add it's unicode value to the accumulator.
      hashed_val += ord(character)
    # Mod the final accumulator value.
    hashed_val %= MOD
    #Return the final value.
    return hashed_val

  # add_tweet() - Adds the tweet_text and the hashtag parameters to the 
  #               correct position in the singly linked list.
  #
  #   Parameters:
  #     self - Instance for the object.
  #     tweet_text - The text from the tweet.
  #     hashtag - The hashtag from the tweet.
  def add_tweet(self, tweet_text, hashtag):
    # Calculate the hash table position.
    position = self.hash(hashtag)
    
    #Check to see if the table position is already taken. 
    if self.table[position] == None:
      # Find the next open position in this column of the table
      item = self.table[position]
      while item.next_pointer != None:
        item = item.next_pointer
        # Assign the open pointer to the new tweet.
      item.next_pointer = HashedItem(tweet_text, hashtag)
    else:  
      # Nothing is in the table at the position so add the tweet there.
      self.table[position] = HashedItem(tweet_text, hashtag)
      
  # TODO: Searching the hash table
  # TODO: Adding to hash table

# user_interface() - This is what the user will interact with when 
#                    using this application.
def user_interface(restarted=False):
  #Initialize hashing class
  if(restarted == False):
    twitter = Hashing(INPUT_FILE)

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
      user_interface(True)
    else:
      print("\nEnding Execution")

if __name__ == "__main__":
  user_interface()