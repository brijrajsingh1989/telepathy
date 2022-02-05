class HeapStore:
    def __init__(self):
        self.AvailableRooms = [0]
        self.CurrentChild = 0
 
    def ShiftUpIndex(self, i):
        while i // 2 > 0:
            if self.AvailableRooms[i] < self.AvailableRooms[i // 2]:
                self.AvailableRooms[i], self.AvailableRooms[i // 2] = self.AvailableRooms[i // 2], self.AvailableRooms[i]
            i = i // 2
 
    def InsertAvailableRoomId(self, k):
        self.AvailableRooms.append(k)
        self.CurrentChild += 1
        self.ShiftUpIndex(self.CurrentChild)
 
    def ShiftDownIndex(self, i):
        while (i * 2) <= self.CurrentChild:
            mc = self.MinChild(i)
            if self.AvailableRooms[i] > self.AvailableRooms[mc]:
                self.AvailableRooms[i], self.AvailableRooms[mc] = self.AvailableRooms[mc], self.AvailableRooms[i]
            i = mc
 
    def MinChild(self, i):
        if (i * 2)+1 > self.CurrentChild:
            return i * 2
        else:
            if self.AvailableRooms[i*2] < self.AvailableRooms[(i*2)+1]:
                return i * 2
            else:
                return (i * 2) + 1
 
    def GetAvailableRoomId(self):
        if len(self.AvailableRooms) == 1:
            return None
 
        root = self.AvailableRooms[1] 
        self.AvailableRooms[1] = self.AvailableRooms[self.CurrentChild]
        *self.AvailableRooms, _ = self.AvailableRooms
        self.CurrentChild -= 1
        self.ShiftDownIndex(1)
        return root
