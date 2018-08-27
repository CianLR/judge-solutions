import sys
import string

DELIM_CHARS = '"\'!@#$%^&*' + string.ascii_letters
DELIM_SET   = set(DELIM_CHARS)
DELIM_SPECIAL = '\'"'

def unescape_string(code):
    orig_delim = code[0]
    if code.startswith("Q="):
        orig_delim = code[2]
        code = code[2:]
    # Cut off delims and replace any escaped ones.
    unesc = code[1:-1].replace('\\' + orig_delim, orig_delim)
    # Find the next unused delim
    used_chars = set(unesc)
    new_delim = None
    for d in DELIM_CHARS:
        if d not in used_chars:
            new_delim = d
            break
    # Pop in the new delim, with Q= if neccessary.
    new_code = new_delim + unesc + new_delim
    if new_delim not in DELIM_SPECIAL:
        new_code = "Q=" + new_code
    return new_code

def extract_string(code, start):
    delim = code[start]
    i = start + 1
    last_escape = False
    while code[i] != delim or last_escape:
        if code[i] == '\\' and not last_escape:
            last_escape = True
        else:
            last_escape = False
        i += 1
    return i, code[start:i + 1]

def process_code(code):
    processed_code = ''
    str_start = None
    last_escape = False
    last_q = False
    i = 0
    while i < len(code):
        if i + 1 < len(code) and code[i:i + 2] == "Q=":
            i, raw_str = extract_string(code, i + 2)
            processed_code += unescape_string(raw_str)
        elif code[i] in DELIM_SPECIAL:
            i, raw_str = extract_string(code, i)
            processed_code += unescape_string(raw_str)
        else:
            processed_code += code[i]
        i += 1
    return processed_code

def main():
    sys.stdout.write(process_code(sys.stdin.read()))

if __name__ == '__main__':
    main()

