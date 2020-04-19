import re

def namen(bestandsnaam):

    """
    >>> namen('data.nl.txt')
    ['Monty Python', 'Flying Circus', 'Graham Chapman', 'John\\nCleese', 'Terry Gilliam', 'Eric Idle', 'Terry Jones', 'Michael Palin', 'Monty Python', 'Holy Grail', 'The Meaning', 'Noord Amerika', 'Saturday Night Live']
    """

    patroon = re.compile(r'\b([A-Z][a-z]*(\s+[A-Z][a-z]*)+)\b')
    return [mo[0] for mo in patroon.findall(open(bestandsnaam).read())]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
