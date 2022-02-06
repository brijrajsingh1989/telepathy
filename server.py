from modules.HotelRooms import HotelRooms
from modules.RoomStatus import RoomStatus
from flask import Flask, jsonify, request

app = Flask(__name__)
BoutiqueHotelObj = None

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
    
    def MarkRoomVacant(self, roomNumber):
        if roomNumber not in self.OccupiedRoomsQueue and roomNumber not in self.RoomsToRepairQueue:
            return "Invalid Room Number, Please provide correct room Number."
        roomId = -1
        if roomNumber in self.OccupiedRoomsQueue:
            roomId = self.OccupiedRoomsQueue[roomNumber]
            del self.OccupiedRoomsQueue[roomNumber]
        elif roomNumber in self.RoomsToRepairQueue:
            roomId = self.RoomsToRepairQueue[roomNumber]
            del self.RoomsToRepairQueue[roomNumber]
        self.VacantRoomsQueue[roomNumber] = roomId
        self.HotelsRoomsList[roomId].RoomStatus = RoomStatus.Vacant
        return "Room Number {} vacated.".format(roomNumber)
    
    def MarkRoomAvailable(self, roomNumber):
        if roomNumber not in self.VacantRoomsQueue:
            return "This room is not ready to be available."
        roomId = self.VacantRoomsQueue[roomNumber]
        self.AvailableRoomsPriorityQueue.InsertAvailableRoomId(roomId)
        self.HotelsRoomsList[roomId].RoomStatus = RoomStatus.Available
        del self.VacantRoomsQueue[roomNumber]
        return "Room Number {} is available now.".format(roomNumber)

    def MarkRoomToRepair(self, roomNumber):
        if roomNumber not in self.VacantRoomsQueue:
            return "Invalid Room Number, Please provide correct room Number."
        roomId = self.VacantRoomsQueue[roomNumber]
        self.RoomsToRepairQueue[roomNumber] = roomId
        self.HotelsRoomsList[roomId].RoomStatus = RoomStatus.Repair
        del self.VacantRoomsQueue[roomNumber]
        return "Room Number {} has been marked to repair.".format(roomNumber)

    def ListAvailableRooms(self):
        availableRooms = []
        for room in self.AvailableRoomsPriorityQueue.AvailableRooms[1:]:
            availableRooms.append(self.HotelsRoomsList[room].RoomNumber)
        return "Availabel Rooms: {} ".format((',').join(availableRooms))

@app.route('/Ping')
def Ping():
    return jsonify({'response':'ok'})

@app.route('/GetAllAvailableRooms', methods=['GET'])
def GetAllAvailableRooms():
    global BoutiqueHotelObj
    return jsonify({'result':BoutiqueHotelObj.ListAvailableRooms()})

@app.route('/AssignRoom', methods=['GET'])
def AssignRoom():
    global BoutiqueHotelObj
    return jsonify({'result':BoutiqueHotelObj.AssignRoom()})

@app.route('/VacateRoom', methods=['POST'])
def VacateRoom():
    global BoutiqueHotelObj
    if not request.json and 'roomNumber' not in request.json:
        return jsonify({'result', 'Invalid Room Number, This room can not be vacate at the movement.'})
    roomNumber = request.json['roomNumber']
    return jsonify({'result':BoutiqueHotelObj.MarkRoomVacant(roomNumber)})

@app.route('/MarkRoomAvailable', methods=['POST'])
def MarkRoomAvailable():
    global BoutiqueHotelObj
    if not request.json and 'roomNumber' not in request.json:
        return jsonify({'result', 'Invalid Room Number, This room can not be vacate at the movement.'})
    roomNumber = request.json['roomNumber']
    return jsonify({'result':BoutiqueHotelObj.MarkRoomAvailable(roomNumber)})

@app.route('/MarkRoomToRepair', methods=['POST'])
def MarkRoomToRepair():
    global BoutiqueHotelObj
    if not request.json and 'roomNumber' not in request.json:
        return jsonify({'result', 'Invalid Room Number, This room can not be vacate at the movement.'})
    roomNumber = request.json['roomNumber']
    return jsonify({'result':BoutiqueHotelObj.MarkRoomToRepair(roomNumber)})

if __name__ == '__main__':
    floorCount = 4
    roomCountOnEachFloor = 5
    BoutiqueHotelObj = BoutiqueHotel(floorCount, roomCountOnEachFloor)
    app.run(host='0.0.0.0', port=8000)
