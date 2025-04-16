import os
import secrets
import sys
from hashlib import sha1
from binascii import hexlify, unhexlify

secret_key = '1'

def hash_(a):
    print(secret_key.encode())
    print(secret_key.encode() + a)
    print(sha1(secret_key.encode() + a))
    print(sha1(secret_key.encode() + a).hexdigest())
    return sha1(secret_key.encode() + a).hexdigest()


def get_session_from_username(username):
    print('-----------------')
    print(username)
    print(username + '|')
    print(username + '|' + hash_(username.encode()))
    for_session = username + '|' + hash_(username.encode())
    print(hexlify(for_session.encode()).decode())
    print('-----------------')
    return hexlify(for_session.encode()).decode()
    
def get_username_from_session(session):
    try:
        parts = unhexlify(session.encode())
        print('AAAAAAAAA')
        print(parts)
        data, sym, sign = parts.rpartition(b'|')
        print(sign)

        is_verified = hash_(data) == sign.decode()

        username = parts.split(b'|')[-2].decode()
        print(username)
        print('AAAAAAAAA')
        return username, is_verified

    except:
        return "", False
    
print(get_session_from_username('ara'))

print(get_username_from_session('6172617c34653439366564323433343532653164666166313732616330306637613836613761666561633064'))