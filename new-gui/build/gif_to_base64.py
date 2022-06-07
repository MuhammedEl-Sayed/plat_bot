import base64

with open('bg.gif', 'rb') as f:
    encoded_string = base64.b64encode(f.read())
    print(encoded_string)