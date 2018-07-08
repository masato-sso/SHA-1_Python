#! /usr/bin/python
# -*- coding: utf-8 -*-
import hashlib

text="Hello world"

print("MD5    {}".format(hashlib.md5(text.encode('utf-8')).hexdigest()))
print("SHA1   {}".format(hashlib.sha1(text.encode('utf-8')).hexdigest()))
print("SHA224 {}".format(hashlib.sha224(text.encode('utf-8')).hexdigest()))
print("SHA256 {}".format(hashlib.sha256(text.encode('utf-8')).hexdigest()))
print("SHA384 {}".format(hashlib.sha384(text.encode('utf-8')).hexdigest()))
print("SHA512 {}".format(hashlib.sha512(text.encode('utf-8')).hexdigest()))
