

def count_char(text):
        
    counts = {}
    for character in text: 
        if character not in counts:
            counts[character] = 1
        else: 
            counts[character] += 1

    for c, count in counts.items():
        print(c,count)

def count_char_insensitive(text):
    
    counts = {}
    for character in text:
    
        if character.isalpha():
            character = character.lower()
        if character not in counts:
            counts[character] = 1
        else:
            counts[character] += 1

    for char, count in counts.items():
        print(char, count)


def count_char_ordered(text):
    # TODO print the characters in the descending order of the count
    # HINT: lookup `sorted()` in the Python documentation
    
    # This task is quite difficult, so please feel free to make use of
    # resources online (Python docs, Stack Overflow, etc.)
    pass
