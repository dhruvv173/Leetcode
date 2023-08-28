class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev_seat = None
        dist = float('-inf')
        for idx in range(len(seats)):
            if seats[idx] == 1:
                if prev_seat == None:
                    dist = idx
                else:
                    dist = max(dist, (idx-prev_seat) // 2)
                prev_seat = idx
            
        dist = max(dist, len(seats) - 1 - prev_seat)
        return dist