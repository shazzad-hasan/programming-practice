import pickle
import json


class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def position(self):
        print(self.x, self.y, sep = ", ")

if __name__ == '__main__':
    c1: Coordinate = Coordinate(5, 10)
    # c1.position()

    # c1.y = 150
    # with open('data.json', 'w') as file:
    #     data = {'x': c1.x, 'y':c1.y}
    #     json.dump(data, file)

    # with open('data.json', 'r') as file:
    #     data = json.load(file)
    #     print(data)

    c1.y = 150
    with open("data.pickle", "wb") as file:
        pickle.dump(c1, file)

    with open("data.pickle", "rb") as file:
        c1: Coordinate = pickle.load(file)

    c1.position()
    c1.y = 200
    c1.position()