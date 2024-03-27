import base64

original_string = "nimda"  # Replace this with the string you want to encode

# Encode the string 20 times
encoded_string = original_string.encode('utf-8')
for _ in range(20):
    encoded_string = base64.b64encode(encoded_string)

decode_id = encoded_string.decode('utf-8')

decode_id = decode_id.replace("8", ")")
decode_id = decode_id.replace("7", "(")
decode_id = decode_id.replace("6", "*")
decode_id = decode_id.replace("5", "&")
decode_id = decode_id.replace("4", "^")
decode_id = decode_id.replace("3", "$")
decode_id = decode_id.replace("2", "@")
decode_id = decode_id.replace("1", "!")

print(decode_id)  # This will print the decoded string
