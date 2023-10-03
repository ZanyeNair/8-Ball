from ball import Ball


class Board:
        # TODO: Add ball locations
        locations = [(), (), (), (), (), (), (), (), (), (), (), (), (), (), (), ()]
        def __init__(self) -> None:
                # Numbers 1-15
                for i in range(1, 16):
                        self.balls.append(Ball(i, self.locations[i]))
                # Cue ball
                self.balls.append(Ball(0, self.locations[0]))