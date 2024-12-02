from hashlib import md5

def day5(key):
    passwd = ""
    passwd2 = ['_']*8
    i = 0
    print("".join(passwd2))
    while '_' in passwd2:
        tmp = md5(bytes(key + str(i),encoding='ascii')).hexdigest()
        if tmp[:5] == '00000':
            passwd += tmp[5]
            pos = int(tmp[5], 16)
            if pos < 8 and passwd2[pos] == '_':
                passwd2[pos] = tmp[6]
                print("".join(passwd2))
        i += 1
    return passwd[:8], "".join(passwd2)

if __name__ == "__main__":
    key = 'ugkcyxxp'
    p1, p2 = day5(key)
    print("Part 1:", p1)
    print("Part 2:", p2)