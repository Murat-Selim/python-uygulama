import math

points = [(0,0), (1,2), (4,4), (5,7), (8,10), (11,13)]
distances = []

def euclidean_distance(point1, point2):
    distance = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    return distance

# Tüm mesafeleri hesaplayıp distances listesine ekleyelim
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        x = euclidean_distance(points[i], points[j])
        distances.append(x)

# Minimum mesafeyi bulalım
minMes = min(distances)

print("Minimum uzaklık:", minMes)




