from flask import Flask
from flask import request
from router import router
app = Flask(__name__)


class main():
    @app.route("/getTemperature")
    def getTemperature():
        return router.Router.getTemperature()
    
    @app.route("/timelineTemp")
    def timelineTemp():
        return router.Router.timelineTemp()
    app.run()
main()