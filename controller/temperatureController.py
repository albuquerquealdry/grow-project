from service import temperatureService

class temperatureController():

    def getTemperature():
        return temperatureService.temperatureService.getTemperature()
    
    def timelineTemp():
        return ("chegou tambem")