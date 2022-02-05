from modules.HotelRooms import HotelRooms
from modules.RoomStatus import RoomStatus
class BoutiqueHotel:
    def __init__(self, floorCount, roomCountOnEachFloor):
        self.HotelsRoomsList, self.AvailableRoomsPriorityQueue = HotelRooms(floorCount, roomCountOnEachFloor).InitializeHotelRooms()
        self.OccupiedRoomsQueue = {}
        self.VacantRoomsQueue = {}
        self.RoomsToRepairQueue = {}
    
    def AssignRoom(self):
        availableRoomId = self.AvailableRoomsPriorityQueue.GetAvailableRoomId()
        if not availableRoomId:
            return "No Room Available !!"
        ##Change Room Status
        self.HotelsRoomsList[availableRoomId].RoomStatus = RoomStatus.Occupied
        assignedRoom = self.HotelsRoomsList[availableRoomId]
        self.OccupiedRoomsQueue[assignedRoom.RoomNumber] =  availableRoomId
        return assignedRoom.RoomNumber
    
    def CheckOutRoom(self, roomNumber):
        if roomNumber not in self.OccupiedRoomsQueue:
            return "Invalid Room Number, Please provide correct room Number."
        roomId = self.OccupiedRoomsQueue[roomNumber]
        return roomId
    
    def MarkRoomAvailable(self, roomNumber):
        pass

    def MarkRoomForRepair(self, roomNumber):
        pass

    def ListAvailableRooms(self):
        availableRooms = []
        for room in self.AvailableRoomsPriorityQueue.AvailableRooms[1:]:
            availableRooms.append(self.HotelsRoomsList[room].RoomNumber)

        return (',').join(availableRooms)
    



if __name__ == '__main__':
    objBoutiqueHotel = BoutiqueHotel(4,5)
    # roomNumber = objBoutiqueHotel.AssignRoom()
    # roomId = objBoutiqueHotel.CheckOutRoom(roomNumber + 'A')
    # print(roomNumber, roomId)
    objBoutiqueHotel.ListAvailableRooms()