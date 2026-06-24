def find_largest_number (numbers):
    if not numbers:
        return None
    
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

nums = [23, 78, 45, 92, 56, 12]
print(f"The largest number in the list is: {find_largest_number(nums)}")

def calculate_average(numbers):
    if not numbers:
        return 0
    
    total = 0
    index = 0
    length = len(numbers)
    
    while index < length:
        total += numbers[index]
        index += 1
        
    return total / length


nums = [10, 20, 30, 40, 50]
print(f"The average is: {calculate_average(nums)}")

def is_palindrome(text):
   
    text = text.lower()
    length = len(text)
    
    for i in range(length // 2):
        if text[i] != text[length - 1 - i]:
            return False
            
    return True


test_word = "Racecar"
print(f"Is '{test_word}' a palindrome?: {is_palindrome(test_word)}")

def print_geometric_sequence(start_term, ratio, n):
    count = 0
    current_term = start_term
    sequence = []
    
    while count < n:
        sequence.append(current_term)
        current_term *= ratio
        count += 1
        
    print(", ".join(map(str, sequence)))


print_geometric_sequence(2, 2, 10)

def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    result = 1
    original_n = n
    
    while n > 1:
        result *= n
        n -= 1
        
    return result

num = 5
print(f"The factorial of {num} is: {calculate_factorial(num)}")

def is_perfect_square(n):
    if n < 0:
        return False
    if n in (0, 1):
        return True
        
    for i in range(1, (n // 2) + 1):
        if i * i == n:
            return True
        if i * i > n:
            break  
            
    return False

num = 64
print(f"Is {num} a perfect square?: {is_perfect_square(num)}")


def sum_primes_to_100():
    total_sum = 0
    current_num = 2
    
    while current_num <= 100:
        is_prime = True
        divisor = 2
        
        while divisor * divisor <= current_num:
            if current_num % divisor == 0:
                is_prime = False
                break
            divisor += 1
            
        if is_prime:
            total_sum += current_num
            
        current_num += 1
        
    return total_sum

print(f"The sum of primes between 1 and 100 is: {sum_primes_to_100()}")

def count_words(sentence):
    
    punctuations = ",.!?"
    for punc in punctuations:
        sentence = sentence.replace(punc, " ")
        
    
    words_list = sentence.split()
    word_count = 0
    
    for _ in words_list:
        word_count += 1
        
    return word_count


sentence = "Hello, world! This is a test... is it working?"
print(f"Word count: {count_words(sentence)}")

def find_common_elements(list1, list2):
    common_list = []
    index = 0
    
    while index < len(list1):
        item = list1[index]
        if item in list2 and item not in common_list:
            common_list.append(item)
        index += 1
        
    return common_list


a = [1, 2, 3, 4, 5, 5]
b = [4, 5, 6, 7, 5, 8]
print(f"Common elements: {find_common_elements(a, b)}")

