import hashlib

def get_SHA_1_digest(message):
    SHA1_obj=hashlib.sha1(message.encode())
    return SHA1_obj
