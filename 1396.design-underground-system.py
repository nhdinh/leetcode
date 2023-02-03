# 1396. Design Underground System

class UndergroundSystem:
    def __init__(self):
        self.check_in = {}
        self.timer = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:        
        self.check_in[id] = (stationName, t)       
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_in[id]

        _timer = self.timer.get(start_station)
        if _timer is None:
            self.timer[start_station] = {stationName: [t - start_time]}
        else:
            _timer = _timer.get(stationName)
            if _timer is None:
                self.timer[start_station][stationName] = [t - start_time]
            else:
                _timer.append(t - start_time)
            
        # delete from db
        del self.check_in[id]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        _timer = self.timer[startStation][endStation]
        if _timer is None:
            return 0
        else:
            return sum(_timer)/ len(_timer)
        
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)