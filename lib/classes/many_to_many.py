class Game:
    def __init__(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise ValueError("title must be a non-empty string")
        self._results = []

    @property
    def title(self):
        """Returns the game's immutable title"""
        return self._title

    @title.setter
    def title(self, value):
        self._title = self._title

    def add_result(self, result):
        if not isinstance(result, Result):
            raise TypeError("result must be a Result object")
        self._results.append(result)

    def results(self):
        return list(self._results)

    def players(self):
        players_played_game = set()
        unique_players = []
        for result in self._results:
            player = result.player
            if player not in players_played_game:
                players_played_game.add(player)
                unique_players.append(player)
        return unique_players

    def average_score(self, player):
        player_scores = [result.score for result in self._results if result.player == player]
        if not player_scores:
            return 0
        return sum(player_scores) / len(player_scores)


class Player:
    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._username = value
        else: 
            raise ValueError("username must be a string between 2 and 16 characters")

    def results(self):
        return list(self._results)

    def games_played(self):
        unique_games = []
        for result in self._results:
            game = result._game
            if game not in unique_games:
                unique_games.append(game)
        return unique_games 

    def played_game(self, game):
        for result in self._results:
            if result.game == game:
                return True
        return False

    def num_times_played(self, game):
        count = 0
        for result in self._results:
            if result.game == game:
                count += 1
        return count

    def average_score(self, game):
        scores = [result._score for result in self._results if result._game == game]
        if scores:
            return sum(scores) / len(scores)
        return 0

    @classmethod
    def highest_scored(cls, game):
        if not cls.all:
            return None

        top_player = None
        top_avg = 0

        for player in cls.all:
            avg = player.average_score(game)
            if avg > top_avg:
                top_avg = avg
                top_player = player
        return top_player

class Result:
    all = []

    def __init__(self, player, game, score):
        if not isinstance(player, Player):
            raise TypeError("player must be a Player object")
        if not isinstance(game, Game):
            raise TypeError("game must be a Game object")
        if not isinstance(score, int):
            raise ValueError("score must be an integer")

        self._player = player
        self._game = game
        self._score = score

        Result.all.append(self)

        player._results.append(self)
        game._results.append(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        return 

    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game