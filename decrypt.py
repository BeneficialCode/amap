import xxtea
import base64
import string

def decrypt(data, key):
    pass

def main():
    # read file
    with open('UserInfo875', 'r') as f:
        data = f.read()
    # decode base64
    data = base64.b64decode(data)
    # decrypt
    key = 'LXlvWaosMcJCJwVn'
    data = xxtea.decrypt(data, key)

    # decode utf-8
    data = data.decode('utf-8')

    # decode base64
    data = base64.b64decode(data)

    # convert to string
    data = data.decode('utf-8')

    print(data)

if __name__ == '__main__':
    main()