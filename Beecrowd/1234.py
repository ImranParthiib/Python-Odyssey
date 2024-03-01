import sys

def is_upper(c):
    return 'A' <= c <= 'Z'

def is_lower(c):
    return 'a' <= c <= 'z'

def main():
    for line in sys.stdin:
        new_line = ''
        upper_case = True
        for char in line:
            if char == ' ':
                new_line += ' '
                continue
            if upper_case:
                if is_lower(char):
                    char = char.upper()
                upper_case = False
            else:
                if is_upper(char):
                    char = char.lower()
                upper_case = True
            new_line += char
        print(new_line, end='')

if __name__ == "__main__":
    main()
