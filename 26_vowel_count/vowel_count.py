def vowel_count(phrase):
    vowels = 'aeiou'
    return {char: phrase.lower().count(char) for char in phrase.lower() if char in vowels}
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """