from controller import temperatureController

class Router():
    def getTemperature():
        return temperatureController.temperatureController.getTemperature()
    
    def timelineTemp():
        return temperatureController.temperatureController.timelineTemp()
