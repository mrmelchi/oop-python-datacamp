class Player:
    MAX_POSITION = 10
    MAX_SPEED = 10
    
    def __init__(self):
        self.position = 0

    # Add a move() method with steps parameter
    def move(self, steps):
        if self.position + steps < Player.MAX_POSITION:
            self.position += steps
        else:
            self.position = Player.MAX_POSITION
           
    # This method provides a rudimentary visualization in the console    
    def draw(self):
        drawing = "-" * self.position + "|" +"-"*(Player.MAX_POSITION - self.position)
        print(drawing)


if __name__ == "__main__":
    p = Player(); p.draw()
    p.move(4); p.draw()
    p.move(5); p.draw()
    p.move(3); p.draw()

    # changing max speed
    print(p.MAX_SPEED)
    Player.MAX_SPEED = 7
    print(p.MAX_SPEED)