#!/usr/bin/env python3
# Required:
# python3 -m pip install passlib --user

import getpass

from passlib.hash import sha512_crypt

if __name__ == "__main__":
    passwd = getpass.getpass('Password to hash: ')
    hash = sha512_crypt.encrypt(passwd)

    print(hash)
