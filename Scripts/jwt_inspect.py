import jwt
import json

token = input("Enter JWT: ")

decoded = jwt.decode(token, options={"verify_signature": False})
print(json.dumps(decoded, indent=2))
