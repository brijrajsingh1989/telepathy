from modules.RoomStatus import RoomStatus
class HotelRooms:
    def __init__(self, floorCount, roomCountOnEachFloor):
        self.HotelRooms = []
        self.floorCount = floorCount
        self.roomCountOnEachFloor = roomCountOnEachFloor
        self.ASCIICodeForCharA = 65
    
    def InitiateHotelRooms(self):
        for floorCount in range(1, self.floorCount + 1):
            for roomCount in range(1, self.roomCountOnEachFloor + 1):
                if floorCount % 2 == 0:
                    self.HotelRooms.append(str(floorCount) + chr(self.ASCIICodeForCharA + self.roomCountOnEachFloor - roomCount))
                else:
                    self.HotelRooms.append(str(floorCount) + chr(self.ASCIICodeForCharA + roomCount - 1))
        return self.HotelRooms
