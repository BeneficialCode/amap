import xxtea
import base64
import string
import Crypto.Cipher.AES as AES
from Crypto.Util.Padding import unpad

def decrypt_user_info():
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

def decrypt_girf_sync_db(encrypted_db,decrypted_db):
    with open(decrypted_db,"a+b") as file:
        header = b"SQLite format 3\0"
        file.write(header)

        with open(encrypted_db,"rb") as rfile:
            rfile.seek(0)
            array = bytearray(16)
            rfile.seek(8)
            array[:8] = rfile.read(8)
            key = b"a4a11bb9ef4b2f4c"
            cipher = AES.new(key, AES.MODE_ECB)
            try:
                data = array[:8]
                rfile.seek(24)
                # append the data
                data += rfile.read(8)
                # decrypt the data
                decrypted = cipher.decrypt(data)
                file.write(decrypted)

                while True:
                    chunk = rfile.read(16)
                    if not chunk:
                        break
                    decrypted = cipher.decrypt(chunk)
                    file.write(decrypted)
                
            except Exception as e:
                print(e)
            finally:
                cipher = None
            file.close()
            rfile.close()

def main():
   decrypt_user_info()
   decrypt_girf_sync_db("girf_sync.db","girf_sync_dec.db")

if __name__ == '__main__':
    main()