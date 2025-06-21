

from selenium import webdriver
from selenium.webdriver.common.by import  By

def test_one():
    driver = webdriver.chrome()
    driver.get("https://www.google.com/")
    element = driver.find_element(by=By.XPATH, value = "//*[@class= "Gdd5U"]"))
    element.click()








#
# class testing():
#
#     def __int__(self,one,two):
#         self.one = one
#         self.two = two
#
#
#
#     def test_one(self):
#         driver.get("https://www.devpropvivo.com")
#         driver.find_element(by=By.XPATH, value="test").click()
#
#
#
#
# variable = testing()
#
#
#





# basic python programs  related to string and list give more programs
# ChatGPT said:
# ChatGPT
# Here are some basic Python programs related to strings and lists. These examples will help you understand how to manipulate and work with these data types.
#
# 1. Reverse a String
# python
# Copy code
# def reverse_string(s):
#     return s[::-1]
#
# # Example usage
# string = "Hello, World!"
# print(reverse_string(string))  # Output: !dlroW ,olleH
# 2. Check if a String is a Palindrome
# A palindrome is a word that reads the same backward as forward.
#
# python
# Copy code
# def is_palindrome(s):
#     return s == s[::-1]
#
# # Example usage
# word = "madam"
# print(is_palindrome(word))  # Output: True
# 3. Count the Number of Vowels in a String
# python
# Copy code
# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in s:
#         if char in vowels:
#             count += 1
#     return count
#
# # Example usage
# sentence = "This is an example sentence."
# print(count_vowels(sentence))  # Output: 8
# 4. Remove All Vowels from a String
# python
# Copy code
# def remove_vowels(s):
#     vowels = "aeiouAEIOU"
#     return ''.join([char for char in s if char not in vowels])
#
# # Example usage
# sentence = "This is an example sentence."
# print(remove_vowels(sentence))  # Output: Ths s n xmpl sntnc.
# 5. Find the Length of a List
# python
# Copy code
# def list_length(lst):
#     return len(lst)
#
# # Example usage
# numbers = [1, 2, 3, 4, 5]
# print(list_length(numbers))  # Output: 5
# 6. Sum All Elements in a List
# python
# Copy code
# def sum_list(lst):
#     return sum(lst)
#
# # Example usage
# numbers = [1, 2, 3, 4, 5]
# print(sum_list(numbers))  # Output: 15
# 7. Find the Largest Element in a List
# python
# Copy code
# def max_in_list(lst):
#     return max(lst)
#
# # Example usage
# numbers = [1, 2, 3, 4, 5]
# print(max_in_list(numbers))  # Output: 5
# 8. Find the Smallest Element in a List
# python
# Copy code
# def min_in_list(lst):
#     return min(lst)
#
# # Example usage
# numbers = [1, 2, 3, 4, 5]
# print(min_in_list(numbers))  # Output: 1
# 9. Remove Duplicates from a List
# python
# Copy code
# def remove_duplicates(lst):
#     return list(set(lst))
#
# # Example usage
# numbers = [1, 2, 3, 4, 5, 3, 2, 1]
# print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4, 5]
# 10. Find the Second Largest Element in a List
# python
# Copy code
# def second_largest(lst):
#     unique_lst = list(set(lst))
#     unique_lst.sort()
#     return unique_lst[-2]
#
# # Example usage
# numbers = [10, 20, 4, 45, 99, 99]
# print(second_largest(numbers))  # Output: 45
# 11. Check if a String Contains Only Digits
# python
# Copy code
# def is_digit(s):
#     return s.isdigit()
#
# # Example usage
# string = "12345"
# print(is_digit(string))  # Output: True
#
# string = "123a5"
# print(is_digit(string))  # Output: False
# 12. Sort a List of Strings Alphabetically
# python
# Copy code
# def sort_strings(lst):
#     return sorted(lst)
#
# # Example usage
# words = ["banana", "apple", "cherry"]
# print(sort_strings(words))  # Output: ['apple', 'banana', 'cherry']
# 13. Count the Frequency of Each Element in a List
# python
# Copy code
# from collections import Counter
#
# def frequency(lst):
#     return Counter(lst)
#
# # Example usage
# numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# print(frequency(numbers))  # Output: Counter({4: 4, 3: 3, 2: 2, 1: 1})
# 14. Concatenate Two Lists
# python
# Copy code
# def concatenate_lists(lst1, lst2):
#     return lst1 + lst2
#
# # Example usage
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# print(concatenate_lists(list1, list2))  # Output: [1, 2, 3, 4, 5, 6]
# 15. Find Common Elements Between Two Lists
# python
# Copy code
# def common_elements(lst1, lst2):
#     return list(set(lst1) & set(lst2))
#
# # Example usage
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
# print(common_elements(list1, list2))  # Output: [3, 4]
# 16. Check if a List is Empty
# python
# Copy code
# def is_empty(lst):
#     return len(lst) == 0
#
# # Example usage
# empty_list = []
# print(is_empty(empty_list))  # Output: True
#
# non_empty_list = [1]
# print(is_empty(non_empty_list))  # Output: False
# 17. Join a List of Strings into a Single String
# python
# Copy code
# def join_strings(lst):
#     return ' '.join(lst)
#
# # Example usage
# words = ["Hello", "World", "from", "Python"]
# print(join_strings(words))  # Output: Hello World from Python
# 18. Split a String into a List of Words
# python
# Copy code
# def split_string(s):
#     return s.split()
#
# # Example usage
# sentence = "Hello World from Python"
# print(split_string(sentence))  # Output: ['Hello', 'World', 'from', 'Python']
# 19. Remove All Occurrences of an Element in a List
# python
# Copy code
# def remove_all_occurrences(lst, value):
#     return [x for x in lst if x != value]
#
# # Example usage
# numbers = [1, 2, 2, 3, 4, 2]
# print(remove_all_occurrences(numbers, 2))  # Output: [1, 3, 4]
# 20. Check if All Characters in a String are Unique
# python
# Copy code
# def all_unique(s):
#     return len(s) == len(set(s))
#
# # Example usage
# string = "abcdef"
# print(all_unique(string))  # Output: True
#
# string = "abcdea"
# print(all_unique(string))  # Output: False
# These programs cover a variety of basic string and list operations in Python. They can be used as building blocks for more complex programs and help you get comfortable with handling these data types.
#
#
#
#
#
# You said:
# give the more programs for strings
# ChatGPT said:
# ChatGPT
# Memory updated
# Here are some more Python programs focused on string manipulation:
#
# 1. Count the Number of Words in a String
# python
# Copy code
# def count_words(s):
#     words = s.split()
#     return len(words)
#
# # Example usage
# sentence = "This is a simple sentence."
# print(count_words(sentence))  # Output: 5
# 2. Convert a String to Title Case
# python
# Copy code
# def to_title_case(s):
#     return s.title()
#
# # Example usage
# sentence = "this is a title case example."
# print(to_title_case(sentence))  # Output: This Is A Title Case Example.
# 3. Find the Most Frequent Character in a String
# python
# Copy code
# def most_frequent_char(s):
#     frequency = {}
#     for char in s:
#         if char in frequency:
#             frequency[char] += 1
#         else:
#             frequency[char] = 1
#     most_frequent = max(frequency, key=frequency.get)
#     return most_frequent
#
# # Example usage
# string = "sample string"
# print(most_frequent_char(string))  # Output: s
# 4. Check if a String is an Anagram
# Two strings are anagrams if they contain the same characters in a different order.
#
# python
# Copy code
# def is_anagram(s1, s2):
#     return sorted(s1) == sorted(s2)
#
# # Example usage
# string1 = "listen"
# string2 = "silent"
# print(is_anagram(string1, string2))  # Output: True
# 5. Replace All Spaces in a String with Hyphens
# python
# Copy code
# def replace_spaces(s):
#     return s.replace(' ', '-')
#
# # Example usage
# sentence = "Replace spaces with hyphens."
# print(replace_spaces(sentence))  # Output: Replace-spaces-with-hyphens.
# 6. Check if a String is a Pangram
# A pangram is a sentence containing every letter of the alphabet at least once.
#
# python
# Copy code
# import string
#
# def is_pangram(s):
#     alphabet = set(string.ascii_lowercase)
#     return alphabet <= set(s.lower())
#
# # Example usage
# sentence = "The quick brown fox jumps over the lazy dog."
# print(is_pangram(sentence))  # Output: True
# 7. Remove Punctuation from a String
# python
# Copy code
# import string
#
# def remove_punctuation(s):
#     return s.translate(str.maketrans('', '', string.punctuation))
#
# # Example usage
# sentence = "Hello, world! This is an example."
# print(remove_punctuation(sentence))  # Output: Hello world This is an example
# 8. Find the Longest Word in a String
# python
# Copy code
# def longest_word(s):
#     words = s.split()
#     longest = max(words, key=len)
#     return longest
#
# # Example usage
# sentence = "Find the longest word in this sentence."
# print(longest_word(sentence))  # Output: sentence
# 9. Swap the Case of All Characters in a String
# python
# Copy code
# def swap_case(s):
#     return s.swapcase()
#
# # Example usage
# sentence = "This is a Test Sentence."
# print(swap_case(sentence))  # Output: tHIS IS A tEST sENTENCE.
# 10. Reverse Each Word in a String
# python
# Copy code
# def reverse_words(s):
#     words = s.split()
#     reversed_words = [word[::-1] for word in words]
#     return ' '.join(reversed_words)
#
# # Example usage
# sentence = "Reverse each word in this sentence."
# print(reverse_words(sentence))  # Output: esreveR hcae drow ni siht .ecnetnes
# 11. Count the Number of Uppercase and Lowercase Letters in a String
# python
# Copy code
# def count_case(s):
#     upper_count = sum(1 for c in s if c.isupper())
#     lower_count = sum(1 for c in s if c.islower())
#     return upper_count, lower_count
#
# # Example usage
# sentence = "This is a Test Sentence."
# upper, lower = count_case(sentence)
# print(f"Uppercase: {upper}, Lowercase: {lower}")  # Output: Uppercase: 4, Lowercase: 15
# 12. Remove All Duplicate Characters from a String
# python
# Copy code
# def remove_duplicates(s):
#     seen = set()
#     result = []
#     for char in s:
#         if char not in seen:
#             result.append(char)
#             seen.add(char)
#     return ''.join(result)
#
# # Example usage
# string = "programming"
# print(remove_duplicates(string))  # Output: progamin
# 13. Check if a String is a Substring of Another String
# python
# Copy code
# def is_substring(s1, s2):
#     return s1 in s2
#
# # Example usage
# substring = "test"
# string = "This is a test string."
# print(is_substring(substring, string))  # Output: True
# 14. Find All Substrings of a String
# python
# Copy code
# def all_substrings(s):
#     length = len(s)
#     substrings = [s[i:j+1] for i in range(length) for j in range(i,length)]
#     return substrings
#
# # Example usage
# string = "abc"
# print(all_substrings(string))  # Output: ['a', 'ab', 'abc', 'b', 'bc', 'c']
# 15. Find the First Non-Repeating Character in a String
# python
# Copy code
# def first_non_repeating_char(s):
#     frequency = {}
#     for char in s:
#         if char in frequency:
#             frequency[char] += 1
#         else:
#             frequency[char] = 1
#     for char in s:
#         if frequency[char] == 1:
#             return char
#     return None
#
# # Example usage
# string = "swiss"
# print(first_non_repeating_char(string))  # Output: w













