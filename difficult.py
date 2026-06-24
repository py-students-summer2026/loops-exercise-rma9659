def get_prime_factors(n):
    factors = []
    temp = n
    
    for i in range(2, n + 1):
        if temp % i == 0:
            factors.append(i)
           
            while temp % i == 0:
                temp //= i
        if temp == 1:
            break  
            
    return factors


num = 12
print(f"The prime factors of {num} are: {get_prime_factors(num)}")

def fibonacci_nth(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
        
    a, b = 0, 1
    count = 2
    
    while count < n:
        a, b = b, a + b
        count += 1
        
    return b


n_term = 9
print(f"The {n_term}th term of the Fibonacci sequence is: {fibonacci_nth(n_term)}")

def is_anagram(str1, str2):
    
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if len(str1) != len(str2):
        return False
        
    char_count = {}
    
    
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1
        
   
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False
            
    
    for key in char_count:
        if char_count[key] != 0:
            return False
            
    return True


word1 = "Listen"
word2 = "Silent"
print(f"Are '{word1}' and '{word2}' anagrams?: {is_anagram(word1, word2)}")

def print_arithmetic_sequence(start_term, common_difference, n):
    count = 0
    current_term = start_term
    sequence = []
    
    while count < n:
        sequence.append(current_term)
        current_term += common_difference
        count += 1
        
    print(", ".join(map(str, sequence)))


print_arithmetic_sequence(2, 2, 10)

def find_median(numbers):
    if not numbers:
        return None
        
    n = len(numbers)
    
  
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                

    if n % 2 == 1:
        return numbers[n // 2]
    else:
        middle1 = numbers[(n // 2) - 1]
        middle2 = numbers[n // 2]
        return (middle1 + middle2) / 2

nums = [7, 3, 1, 4, 2, 6]
print(f"The median of the list is: {find_median(nums)}")

def is_perfect_number(n):
    if n <= 1:
        return False
        
    divisor_sum = 0
    i = 1
    
    while i <= n // 2:
        if n % i == 0:
            divisor_sum += i
        i += 1
        
    return divisor_sum == n


num = 28
print(f"Is {num} a perfect number?: {is_perfect_number(num)}")

def sum_digits(number):
    number_str = str(abs(number))
    total_sum = 0
    
    for digit in number_str:
        total_sum += int(digit)
        
    return total_sum


num = 12345
print(f"The sum of the digits in {num} is: {sum_digits(num)}")

def find_longest_word(sentence):
    for punc in ",.!?":
        sentence = sentence.replace(punc, "")
        
    words = sentence.split()
    if not words:
        return ""
        
    longest = ""
    index = 0
    
    while index < len(words):
        if len(words[index]) > len(longest):
            longest = words[index]
        index += 1
        
    return longest

sentence = "The magnificent structure stood tall against the Horizon."
print(f"The longest word is: '{find_longest_word(sentence)}'")

def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for char in alphabet:
        if char not in sentence:
            return False
            
    return True


test_sentence = "The quick brown fox jumps over the lazy dog"
print(f"Is it a pangram?: {is_pangram(test_sentence)}")

def print_primes_to_1000():
    current_num = 2
    prime_list = []
    
    while current_num <= 1000:
        is_prime = True
        divisor = 2
        
        while divisor * divisor <= current_num:
            if current_num % divisor == 0:
                is_prime = False
                break
            divisor += 1
            
        if is_prime:
            prime_list.append(current_num)
            
        current_num += 1
        
    print(", ".join(map(str, prime_list)))


print_primes_to_1000()