def number_needed(a, b):
    count = 0
    first = dict((letter,a.count(letter)) for letter in set(a))
    second = dict((letter,b.count(letter)) for letter in set(b))
    
    for letter in first:
        if letter in second:
            count += abs(first.get(letter) - second.get(letter))
            first[letter] = 0
            second[letter] = 0
        else:
            count += first.get(letter)
            
    for letter in second:
        if letter in first:
            count += abs(second.get(letter) - first.get(letter))
        else:
            count += second.get(letter)
            
    return count
    
        

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)