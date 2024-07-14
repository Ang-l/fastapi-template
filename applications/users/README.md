# 简介

```
简单的用户相关

1、 数据库相关  用户名、密码字段
2、 加入了登录、注册接口
```


## 调用、以及使用
### 密钥生成
```python
## Suggest executing the following function yourself to generate the project key

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

```

### token生成
```python

### secret_key 由上方代码生成

import jwt

def encryption(payload) -> str:
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token


payload = {
    'user_id': user.id, 
    'username': user.username,
    "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * 60 * 24)
}

token = encryption(payload)

```

### token 解密、 异常可以自己捕获
```python
def decryption(token):
    decoded_payload = jwt.decode(token, secret_key, algorithms=['HS256'])
    return decoded_payload

payload = decryption(token)

```