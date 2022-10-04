class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # ex1: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
        #      return: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
        
        n = len(buildings)
        # base case
        if n == 1:
            building_n = buildings[0]
            return [[building_n[0], building_n[2]], [building_n[1], 0]]

        skyline = self.getSkyline(buildings[:n-1])

        building_n = buildings[n-1]
        Li, Ri, Hi = building_n[0], building_n[1], building_n[2]

        # assume we know n-1, now n is [5,26,9] ([Li, Ri, Hi]):
        for index, line in enumerate(skyline): 
            if index == len(skyline) -1:
                if (line[0] > Li and line[0] > Ri) or line[0] == Ri:  # buildingn before line[0] or line[0] equal Ri
                    break

                if (line[0] > Li and line[0] < Ri):  # line[0] between buildingn
                    skyline.append([Ri, 0])

                if line[0] == Li:  # skylinebuildingn
                    skyline[index] = [Li, Hi]
                    skyline.append([Ri,0])

                if line[0] < Li and line[0] < Ri:  # skyline ___ buildingn
                    skyline.append([Li, Hi])
                    skyline.append([Ri, 0])
            else: 

                if line[0] > Ri:
                    break

                if line[0] < Li and skyline[index+1][0] > Li:
                    if line[1] >= Hi:
                        continue
                    else:
                        skyline.insert(index + 1, [Li, Hi])  # insert [Li, Hi] to skyline

                if line[0] >= Li and line[0] <= Ri:
                    if line[1] >= Hi:
                        continue
                    else:
                        skyline[index] = [line[0], Hi]  # repalce this (x, height) with (x, Hi)

        # after this -> modify skyline -> same height differnt x process
        return skyline

