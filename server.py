from modules.HotelRooms import HotelRooms

def InitiateRooms(floorCount, roomCountOnEachFloor):
    HotelRoomsObj = HotelRooms(floorCount, roomCountOnEachFloor)
    rooms = HotelRoomsObj.InitiateHotelRooms()
    print(rooms)

if __name__ == '__main__':
    InitiateRooms(40,26)