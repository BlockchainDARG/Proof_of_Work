#!/bin/python

import sys
import time
import hashlib
from struct import unpack, pack

timestamp = str(time.time()) 		# Work timestamp
message = "This is a random message." 	# Plaintext message
nonce = 0				# 
guess = 99999999999999999999
payload = timestamp + message
throttle = 10000000
target = 2**64 / throttle

payloadHash = hashlib.sha512(payload).digest()

start = time.time()
while guess > target:
	nonce += 1
	guess, = unpack('>Q',hashlib.sha512(hashlib.sha512(pack('>Q',nonce) + payloadHash).digest()).digest()[0:8])
end = time.time()

print "%s:%s:%s:%s:%s:%s:%s" % (timestamp, message, nonce, guess, payload, target, end-start)
