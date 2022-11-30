import base64

class Authorization():
    
    def interceptor(secret):
        baseSecret = base64.b64decode(secret)
        if (baseSecret.decode('utf-8') == "mock-root"):
            return True
        else:
            return False