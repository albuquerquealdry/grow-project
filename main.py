from flask import Flask
from flask import request
from router import router
from flask import request
from auth import auth
app = Flask(__name__)

class main():
    @app.route("/getTemperature")
    def getTemperature():
        secret = request.headers.get('secret') 
        validUser = auth.Authorization.interceptor(secret)
        if (validUser == True):
            return router.Router.getTemperature()
        else:
            return ("erro credentials")
    
    @app.route("/timelineTemp")
    def timelineTemp():
        return router.Router.timelineTemp()
    app.run()

main()