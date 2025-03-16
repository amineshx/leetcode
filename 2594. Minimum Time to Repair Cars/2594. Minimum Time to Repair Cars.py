from typing import List
from math import sqrt
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def canRepaireCarInTime(time):
            totale_cars = 0
            for rank in ranks:
                totale_cars += int(sqrt(time // rank))
                if totale_cars>=cars:
                    return True
            return totale_cars >=cars

        lower_time=0
        higher_time=max(ranks)*cars**2

        while lower_time<higher_time:
            mid = (lower_time+higher_time)//2
            if canRepaireCarInTime(mid):
                higher_time=mid
            else: lower_time=mid+1
        
        return lower_time