# Source1: https://www.azion.com/en/blog/the-experts-speak-cybersecurity-quotes-about-zero-trust-waf-social-engineering/
# Source2: https://digitaldefynd.com/IQ/inspirational-cybersecurity-quotes/

import random

def random_line(text):
    with open(text, 'r', encoding='UTF-8') as file:
        line = file.readlines()
        return random.choice(line)

def main():
    print(random_line('quotes.txt'))

if __name__ == "__main__":
    main()
