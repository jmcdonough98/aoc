from collections import Counter
import re

def parseRoom(room):
    name, r_id, checksum = re.findall(r"^(.*)-(\d+)\[(.*)\]$", room)[0]
    chars = Counter(c for c in name if c != '-')
    new_checksum = "".join(sorted(chars.keys(), key = lambda x: (chars[x],-ord(x)), reverse=True)[:5])

    return (int(r_id), name, new_checksum == checksum)

def decrypt(name, r_id):
    key = {c: chr((((c - 97) + r_id) % 26) + 97) for c in range(97,123)} | {45:' '}
    return "".join(key[ord(c)] for c in name)

def day4(lines):
    p1, p2 = 0, 0
    for line in lines:
        r_id, name, valid = parseRoom(line)
        if valid:
            p1 += r_id
            decoded_name = decrypt(name, r_id)
            if decoded_name == 'northpole object storage':
                p2 = r_id
    return p1, p2

if __name__ == "__main__":
    lines = open('input.txt','r').read().split('\n')    
    p1, p2 = day4(lines)
    print("Part 1:", p1)
    print("Part 2:", p2)