#ABCDEFGHIJKLMNOPQRSTUVWXYZ
#DCHEZKIBOXS
from pwn import *

def longest_substring_with_allowed_chars(s, allowed_chars):
    char_set = set(allowed_chars)
    left = 0
    max_length = 0
    max_substring = ""

    for right in range(len(s)):
        if s[right] in char_set:
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
                max_substring = s[left:right + 1]
        else:
            left = right + 1
    
    return max_substring

p = remote("103.181.183.216", 19001)

output = p.recvuntil(b"\n").decode()
allowed_characters = "DCHEZKIBOXS"
result = longest_substring_with_allowed_chars(output, allowed_characters)
print(result)
p.recv()
p.sendline(result.encode())
p.interactive()