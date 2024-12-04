# 1. print("welcome to python programming".upper())

#2.  sum 2 numbers
# "a = int(input("enter a: " ))
#b = int(input("enter b: "))
#total = a + b
#print(total)

# 3.converting from f to c  
#def Fahrenheit_to_Celsuis(Fahrenheit):
 #   return(Fahrenheit - 32)*(5/9)
#f = int(input("enter temperature in Fahrenheit: "))
#c = Fahrenheit_to_Celsuis(f)
#print(f"temperature in Celsuis: {c:.2f}")
        #  OR this is my own attempt
#def f_to_c(f):
 #   return(c)
#f = int(input("enter temperature in f: "))
#c = ((f - 32) * (5/9))
#print(f"temperatuer is: {c}c")

# 4. find the square of a number
#number =int(input("enter a number: "))
#Square = int(number**2)
#print(Square)
#print(f"the square is: {square} is the square of 2")

# 5. even or odd numbers
#def even_or_odd(num):
 #   return "even" if num % 2 == 0 else "odd"
#num = int(input("enter a number: "))
#print(f"the number is {even_or_odd(num)}")
     # OR
#num = int(input("enter a num: "))
#if num % 2 == 0:
#    print(" this number is an even number")
#else:
 #   print("this number is an odd number")
    


# 6.finding the interest
#principal = int(input("enter principal: "))
#rate = int(input("enter rate: "))
#time = int(input("enter time: "))
#interest = ((principal*rate*time)/100)
#print(f"{interest} frs")

# *7. sum of lists
#def sum_of_list(numbers):
 #   return sum(numbers)
#numbers_list = [1,2,3,4]
#print("sum of the list is:", sum_of_list(numbers_list))

#8.count vowels, revisit this
#def count_vowels(string):
    #vowels = "aeiou"
   # return sum(1 for char in string if char in vowels)
#input_string = input("Enter a string: ") 
#print("number of vowels:", count_vowels(input_string))
 

#10 def reverse_string(s):
   #return s[::-1]
#string = input("enter a string: ")
#print("reversed string:", reverse_string(string))

#11 find largest number
#list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#print("the largest number is:", max(list))

#12 remove duplicates
#def remove_duplicate(lst):
  #  return list(set(lst))
#my_list = [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 9, 10]
#print("list after removing duplicates:", remove_duplicate(my_list))

# *13 factorial
#def factorial(n):
  # if n == 0:
   #   return 1
   #else:
      #return n * factorial(n -1)
#num = int(input("enter a number: "))
#print("factorial:", factorial(num))
#OR
#n = int(input("enter a num: "))
#def factorial(n):
 # if n == 0: 
  #    return 1
  #for i in range(1, n+1):
   #     fac *= i
    #    return fac
  #print(factorial(n))

#14 multiplication table
#number =int(input("enter a number: ")) 
#for i in range (1, 11):
 #   print(f"{number} * {i} = {number * i} ")
    
#1*5 length of list
#list = [2, 4, 6, 8, 10]
#print(len(list))
 
 #15 count words in a sentence
#def count_words(sentence):
 #  return sum(1 for char in sentence)
#sentence = input("write a sentence: ")
#print("number of words in sentence:", count_words(sentence))

#18 range of numbers
#def print_range(start, end):
  # for number in range(start, end + 1):
  #    print(number, end=' ')
  # print()
#start = int(input("enter start number: "))
#end = int(input("enter end number: "))
#print(print_range(start, end))

#19 sum of integer
#a = int(input("enter a number: "))
#b = int(input("enter b number: "))
#c = int(input("enter c number: "))
#sum = a + b + c
#print(sum)

#20 replace word
#def replace_word(sentence, old_word, new_word):
 #  return sentence.replace(old_word, new_word)
#sentence = input("enter a sentence: ")
#old_word = input("enter the word to replace: ")
#new_word = input("enter the new word: ")
#print("updated sentence:", replace_word(sentence, old_word, new_word))

# *21 sort list 
#def sort_list(list):
 #  return sorted(list)
#list = [2, 4, 10, 3, 7, 6, 9, 8, 1]
#print("sorted_list:", sort_list(list))

#22 POWER of a number
#def power_of_a_number(base, exponent):
 #  return base ** exponent
#base = int(input("enter base: "))
#exponent  = int(input("enter exponent: "))
#print("result:",power_of_a_number(base, exponent))

#23 count occurence of character
##  return string.count(character)
#string = input("enter a string: ")
#character = input("enter a character: ")
#print(f"the character {character} appears {count_occurence_of_char(string, character)} times.")

#24 leapyear
#def is_leap_year(year):
 # return(year % 400 == 0)
#year = int(input("enter a year: "))
#print(f"{year} is {'a leap year' if is_leap_year(year) else 'not a leap year'}.")

#25 combine a list
#def combine_lists(list1, list2):
 #  return [val for pair in zip(list1, list2) for val in pair]
#list1 = [1, 2, 3]
#list2 = [4, 5, 6] 
#print("combined list:", combine_lists(list1, list2))

#26 sum of even numbers
#even_sum = sum(i for i in range(1, 51) if i % 2 == 0)
#print("sum of even numbers between 1 and 51:", even_sum)

#27 dictionary
#my_dict = {'name': 'orny', 'age': '26', 'gender': 'female'}
##if key:
  # print(my_dict.get(key))
#else:
 #  print("key not found")

#28 list of squares
#def list_of_squares(n):
 #  return [i ** 2 for i in range(1, n+1)]
#n = int(input("enter a number:"))
#print("list of squares:", list_of_squares(n))

#29 check if elements are unique
#def all_unique(list):
 #  return list == list
#list = [1, 2, 3, 4]
#if list == list:
 #  print("all elements are unique:", all_unique(list))
   


#30 merge lists
#def merged_sorted_lists(list1, list2):
 #  return sorted(list1 + list2)
#list1 = [1, 2, 3]
#list2 = [4, 5, 6]
#print("merged sorted list:",  merged_sorted_lists(list1, list2))

