
"""
Suggest executing the following function yourself to generate the project key

import secrets

def generate_encryption_key(key_length: int = 32) -> bytes:

    # Generate a secure encryption key.
    
    # Args:
    #     key_length (int): Length of the encryption key in bytes. Default is 32 bytes.
    
    # Returns:
    #     bytes: Secure encryption key.
    
    return secrets.token_bytes(key_length)

# # Generate a 256-bit (32 bytes) encryption key
encryption_key = generate_encryption_key()
print("Encryption Key:", encryption_key.hex())      #### It will return a 32-bit key and store it properly
"""


import jwt


"""
### Call Example

ut = Ujwt()

### Retrieve tokens based on payload, and set exp to control expiration time : datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * 60 * 24)
token = ut.encryption({"user_id": 1})   

user_info = ut.decryption(token)    ### 根据token获取出 payload

### You can write functions and use interface injection to verify whether you are logged in or if you are an admin

async def get_current_user(request: Request) -> dict:

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token = request.headers.get("X-Token", None)

    # If no token is carried, throw an exception and return 401
    if not token:
        raise credentials_exception
    
    try:
        ut = Ujwt()
        user_info = ut.decryption(token)
        return user_info
    
    except jwt.ExpiredSignatureError:
        raise credentials_exception

    except jwt.InvalidTokenError:
        raise credentials_exception

### This function can be injected into the interface to verify login
async def get_current_active_user(current_user: User = Depends(get_current_user)):
    return current_user

### This function can be injected into the interface, and the administrator can be controlled based on the parameters of the payload
async def get_user_authority_is_admin(user_info = Depends(get_current_user)):

    if user_info.get("role") != "admin":
        credentials_exception = HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to operate this interface",
        )
        raise credentials_exception
    
    return user_info

"""

secret_key = '920decd2236c8cd7c36100a8e60e9506ebd1198be072a346bc13ae040b5b3805'


def encryption(payload) -> str:
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token


def decryption(token):
    decoded_payload = jwt.decode(token, secret_key, algorithms=['HS256'])
    return decoded_payload