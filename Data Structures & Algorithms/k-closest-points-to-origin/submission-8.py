import heapq
class Solution:
    def euclideanFromOrigin(self, point):
        return (point[0]**2 + point[1]**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        pointsAtDistance = defaultdict(list)
        distanceMinHeap = []
        for point in points:
            distance = self.euclideanFromOrigin(point)
            pointsAtDistance[distance].append(point)
            heapq.heappush(distanceMinHeap, distance)
        while len(result)<k:
            result += pointsAtDistance[heapq.heappop(distanceMinHeap)]
        return result[:k]

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclideanPoints = [[self.euclideanFromOrigin(point), point[0], point[1]] for point in points]
        print(euclideanPoints)
        top_k = euclideanPoints[:k]
        heapq.heapify_max(top_k)
        print(top_k)
        for point in euclideanPoints[k:]:
            if point[0] < top_k[0][0]:
                heapq.heappush_max(top_k, point)
                heapq.heappop_max(top_k)
        return [[point[1], point[2]] for point in top_k]






        