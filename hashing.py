# hashing.py
# Authors: John Thomas, Levi Graham, Riley Nichols, Sam Rudqvist
# Date: 12/09/21
# Course: CSCI 262: Algorithms
# Purpose: To implement an open hashing algorithm for the broadband
#          upgrade final project.
# Modification Log:
#   - 2021.12.09 - LG & JT - Added header and started design.
#   - 2021.12.09 - RN - Started on hash function.
#   - 2021.12.10 - LG - Added the HashedItem class and documentation
#                       for the class. Also added constants.
#   - 2021.12.10 - SR - Started user interface. 
#   - 2021.12.10 - LG & SR - Implemented __init__, hash, and 
#                            add_tweet.
#                            methods for the Hashing class.
#   - 2021.12.11 - RN & LG - Debug and cleaning up UI
#   - 2021.12.11 - RN - Implemented tweet_search method.
#   - 2021.12.11 - RN & SR - Finished tweet_search method.
#   - 2021.12.11 - RN, SR & JT - Added error handling for empty 
#                            hashtag, removes the hashtag from 
#                            the input.
#   - 2021.12.11 - RN & SR - Fixed issue of searching for 
#                            nonexistent hashtag when list exists.
#   - 2021.12.12 - SR & JT - Implemented testing for adding a tweet.
#   - 2021.12.12 - LG & JT - Updated and added comments.
#
# Constants
MOD = 11 # Mod factor for the hashing algorithm.
INPUT_FILE = 'long_input_20000.csv' # Input file for tweets.

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
    self.table = []
    for i in range(MOD):
      self.table.append(None)
    
    # Opens the file and pulls all lines out to put into the hash 
    # table.
    with open(input_file, "r") as file:
      # For each of the lines in the file, add them to the hash 
      # table. 
      for line in file:
        hashtag, tweet = line.rstrip().split(",")
        self.add_tweet(tweet, hashtag.upper())
  
  # hash() - Creates the modded hash value for the hashtag so that
  #          it can be stored in the right place.
  #
  #   Parameters:
  #     self - Instance for the object.
  #     hashtag - The hashtag from the tweet.
  #   
  #   Return - The hashed value for the hashtag.
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

  # add_tweet() - Adds the tweet_text and the hashtag parameters to 
  #               the correct position in the singly linked list.
  #
  #   Parameters:
  #     self - Instance for the object.
  #     tweet_text - The text from the tweet.
  #     hashtag - The hashtag from the tweet.
  def add_tweet(self, tweet_text, hashtag):
    # Calculate the hash table position.
    position = self.hash(hashtag)
    #Check to see if the table position is already taken. 
    if self.table[position] != None:
      # Find the next open position in this column of the table
      previous = self.table[position - 1]
      item = self.table[position]
      # Loop through the linked list.
      while item != None:
        previous = item
        item = item.next_pointer
        # Assign the open pointer to the new tweet.
      previous.next_pointer = HashedItem(tweet_text, hashtag)
    else:  
      # Nothing is in the table at the position so add the tweet 
      # there.
      self.table[position] = HashedItem(tweet_text, hashtag)
      
  # tweet_search() - Searches the hash table for the input hashtag.
  #
  #   Parameters:
  #     self - Instance for the object.
  #     hashtag - The hashtag from the tweet
  # 
  #   Return - A list of all tweets matching the hashtag.
  def tweet_search(self, hashtag):
    # Placeholder for list of hashtags
    list_hold = []
    # Finds mod value for hashtag searched
    hashtag_val = self.hash(hashtag)
    # Finds the area where the hashtag looks and adds every hashtag and its pointer to the list.
    count = 1
    item = self.table[hashtag_val]
    if item != None:
      while item.next_pointer != None:
        count += 1
        if item.hashtag == hashtag:
          list_hold.append(item)
        item = item.next_pointer
      if item.hashtag == hashtag:
        list_hold.append(item)
    #return list of hashtag items
    if list_hold == []:
      print("No results found")
    return list_hold, count


# user_interface() - This is what the user will interact with when 
#                    using this application.
#
#   Parameters:
#     twitter - Initializing the application.
#     restarted - Bool for whether or not the interface is being
#                 restarted or not. Defaults to false.
def user_interface(twitter, restarted=False):
  # Prints welcome if first booted.
  if(restarted == False):
    print("\nWelcome to Open Hashed Twitter")
  # Prints options.
  print("\nFunctions availble:\n\tAdd new tweet (A)\n\tSearch for hashtag (S)\n")
  # Ask user for input.
  user_input = input("What would you like to do? (A/S) ").upper()
  # If the user wants to add a tweet.
  if user_input == "A":
    new_tweet_input = str(input("What text would you like? "))
    new_hashtag_input = str(input("What hashtag would you like? ")).upper()
    # If the new tweet or hashtag is empty, skip. 
    if new_hashtag_input == "#" or new_hashtag_input == "":
      print("The hashtag must have characters in it.")
    elif new_tweet_input == '':
      print("The tweet must contain characters")
    # Remove the hashtag to not interfer with mod val.
    elif "#" in new_hashtag_input:
      splitted = new_hashtag_input.split('#')
      new_hashtag_input = str(splitted[1])
      twitter.add_tweet(new_tweet_input, new_hashtag_input)
    # If everything is good, just run function.
    else:
      twitter.add_tweet(new_tweet_input, new_hashtag_input)

  #If the user trys to search, take a input for the hashtag.
  elif user_input == "S":
    hashtag_input = str(input("What would you like to search? ")).upper()
    # Skips function if there is only a poundsign or its empty.
    if hashtag_input == "#" or hashtag_input == "":
      print("The hashtag must have charaters in it.")
    # Removes # in input
    elif "#" in hashtag_input:
      splitted = hashtag_input.split('#')
      hashtag_input = str(splitted[1])
      tweet_list, count = twitter.tweet_search(hashtag_input)
      for tweet in tweet_list:
        print(tweet.tweet)
      print(f"For empirical analysis: Count = {count}")
    # If everything is fine, run function and print every tweet.
    else:
      tweet_list, count = twitter.tweet_search(hashtag_input)
      for tweet in tweet_list:
        print(tweet.tweet)
      print(f"For empirical analysis: count = {count}")
  # If user does not use A or S, print an error.
  else:
    print("\nIncorrect input.")
    
  # Restart function with saved memeory.
  restart = input("\nWould you like to restart? (Y/N) ")
  if restart.upper() == "Y":
    user_interface(twitter, True)
  else:
    certain = input("\n\tAre you sure? (Y/N) ")
    if certain.upper() == "Y":
      print("\nEnding Execution")
    else:
      user_interface(twitter, True)
    
    


# test_case() - Tests the add tweet function by making a list of  
#               the current tweets with the hashtag, adding the   
#               tweet and then searching for it again. For use with 
#               the small input.
#
#   Parameters: 
#     test_number - The number of the test that is tested.
#     test_tweet - The contents of the tweet being added.
#     test_hashtag - The hashtag of the tweet being added.
def test_case(test_number, test_tweet, test_hashtag):
  before_list, count = twitter.tweet_search(test_hashtag)
  twitter.add_tweet(test_tweet, test_hashtag)
  after_list, count = twitter.tweet_search(test_hashtag)

  if len(before_list) < len(after_list):
    print(f"Test {test_number} passed.")
  else:
    print(f"Test {test_number} failed.")

  for tweet in after_list:
    print(tweet.tweet)


# test() - Runs the different test cases with the small input.
#
#   Parameters:
#     twitter - Initializing the application.
def test(twitter):
  print("\nTesting the application.\n")
  test_case(1, "This is a test tweet", "TESTHASHTAG")
  test_case(2, "Test tweet in #myhashtag", "MYHASHTAG")
  test_case(3, "Second tweet in #myhashtag", "MYHASHTAG")
  test_case(4, "Third tweet in #myhashtag", "MYHASHTAG")

# test2() - Prints the contents of all the positions in the hashtable.
#
#   Parameters:
#     twitter - Initializing the application.
def test2(twitter):
  for x in range(len(twitter.table)):
    item = twitter.table[x]
    print(f"Hash Value: {x}")
    if item != None:
      while item.next_pointer != None:
        print(f"\t#{item.hashtag} {item.tweet}")
        item = item.next_pointer
      print(f"\t#{item.hashtag} {item.tweet}")



if __name__ == "__main__":
  # Preprocess the input.
  twitter = Hashing(INPUT_FILE)
  
  # Run test() for testing with the small input.
  #test(twitter)
  #test2(twitter)

  # Run the user interface. 
  user_interface(twitter)