import re

def match(text):
    m = re.search("^<img=\"[http|ftp]\S+\">", text)

if __name__ == "__main__":
    match('<img="/img/aa.png"')    



max()