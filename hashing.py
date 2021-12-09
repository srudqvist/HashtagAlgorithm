# hashing.py
# Authors: John Thomas, Levi Graham, Riley Nichols, Sam Rudqvist
# Date: 12/09/21
# Course: CSCI 262: Algorithms
# Purpose: To implement an open hashing algorithm for the broadband
#          upgrade final project.
# Modification Log:
#   - 2021.12.09 - LG - Added header and started design.


def test_input():
  file = open("short_input.csv", "r", encoding='utf-8-sig')
  for line in file:
    print(line)

  file.close()


if __name__ == "__main__":
  test_input()