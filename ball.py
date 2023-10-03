class Ball: 

        # Initialize a ball with a number and location
        def __init__(self, number: int, location:tuple) -> None:
                self.value = number;
                self.location = location
                self.x = location[0]
                self.y = location[1]
                self.r = 5;
        
        # Move to a new location
        def move(self, x: int, y: int) -> None:
                self.x = x
                self.y = y
                self.location = (x, y)