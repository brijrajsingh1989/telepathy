from modules.HeapStore import HeapStore
from modules.Room import Room
from modules.RoomStatus import RoomStatus
class HotelRooms:
    def __init__(self, floorCount, roomCountOnEachFloor):
        self.HotelRooms = {}
        self.floorCount = floorCount
        self.roomCountOnEachFloor = roomCountOnEachFloor
        self.ASCIICodeForCharA = 65
        self.HeapStore = HeapStore()
        self.InitialRoomId = 1000
    
    def InitializeHotelRooms(self):
        for floorCount in range(1, self.floorCount + 1):
            for roomCount in range(1, self.roomCountOnEachFloor + 1):
                roomNumber = None
                if floorCount % 2 == 0:
                    roomNumber = str(floorCount) + chr(self.ASCIICodeForCharA + self.roomCountOnEachFloor - roomCount)
                else:
                    roomNumber = str(floorCount) + chr(self.ASCIICodeForCharA + roomCount - 1)
                self.InitialRoomId += 1
                self.HotelRooms[self.InitialRoomId] = Room(roomNumber, RoomStatus.Available, self.InitialRoomId)
                self.HeapStore.InsertAvailableRoomId(self.InitialRoomId)
        return self.HotelRooms, self.HeapStore
