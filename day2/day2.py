from dataclasses import dataclass

@dataclass
class Game:
    game_id: int
    red: int
    blue: int
    green: int

    def valid(self, red_limit: int, green_limit: int, blue_limit:int ) -> bool:
        if red_limit < self.red:
            return False
        if green_limit < self.green:
            return False
        if blue_limit < self.blue:
            return False
        return True

    @property
    def power(self):
        return self.red * self.blue * self.green

    @classmethod
    def create_game(cls, game_line:str):
        # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        game_id, pulls = game_line.split(": ")
        game_id = int(game_id.split(" ")[-1])
        red, blue, green = 0, 0, 0
        for pull in pulls.split("; "):
            for _color in pull.split(", "):
                count, color = _color.split(" ")
                count = int(count)
                if color == "red":
                    red = max([red, count])
                elif color == "green":
                    green = max([green, count])
                elif color == "blue":
                    blue = max([blue, count])
                else:
                    print(f"Unknown color: {color}")
        return cls(game_id, red, blue, green)
    

def main():
    data = [_.strip() for _ in open('input.txt', 'r').readlines()]
    games = []
    for game in data:
        g = Game.create_game(game)
        games.append(g)
    #part 1
    valid_games = []
    for game in games:
        if game.valid(12, 13, 14):
            valid_games.append(game.game_id)
    print("Part 1:", sum(valid_games))
    #part 2
    powers = []
    for game in games:
        powers.append(game.power)
    print("Part 2:", sum(powers))
    

if __name__ == '__main__':
    main()