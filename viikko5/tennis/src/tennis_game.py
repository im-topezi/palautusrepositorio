from player import TennisPlayer,player_evaluater



class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1=TennisPlayer(player1_name)
        self.player2=TennisPlayer(player2_name)
        self.players={player1_name:self.player1,player2_name:self.player2}

    def won_point(self, player_name):
        self.players.get(player_name).won_point()

    def get_score(self):
        score = ""
        player1_score_name=self.player1.get_score_name()
        player2_score_name=self.player2.get_score_name()

        if self.player1.score == self.player2.score:
            if player1_score_name and player1_score_name!="Forty":
                score=player1_score_name+"-All"
            else:
                score="Deuce"

        elif not player1_score_name or not player2_score_name:
            scores_difference=self.player1.score-self.player2.score
            leading_player=player_evaluater(self.player1,self.player2)

            if abs(scores_difference) == 1:
                score = f"Advantage {leading_player}"
            else:
                score = f"Win for {leading_player}"
        else:
            score=player1_score_name+"-"+player2_score_name

        return score
    

