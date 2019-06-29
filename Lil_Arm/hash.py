from pwn import *
import re
import string
import time

"""
https://ughe.github.io/2018/07/19/qemu-aarch64

sudo mv ld-linux-aarch64.so.1 /lib/ld-linux-aarch64.so.1
sudo mv libc.so.6 /lib64/libc.so.6
"""


flag = "shellter{"
HASH = "b5a7adbec4cd12410c1751871691b01a51a91961ac1de1e021f1fc1f826024f2a82ce2a631d2e72ee362347"
TMP_HASH = ""
while HASH != TMP_HASH:
	for x in string.printable:
		io = process(['hash.bin',flag +str(x)])
		s = io.recvline()
		match = re.findall(r"'(.*)'", str(s))
		hash = match[0]
		if HASH[0: len(hash)] == hash:
			print hash
			print HASH[0: len(hash)]
			print("NUMERO "+ str(x))
			flag += str(x)
			TMP_HASH = hash
			time.sleep(2)
		io.close()
print(flag)