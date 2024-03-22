def flip_case(phrase, to_swap):
    return ''.join([char.swapcase() if char.lower() == to_swap.lower() else char for char in phrase])
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
