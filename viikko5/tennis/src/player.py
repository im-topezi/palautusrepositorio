class TennisPlayer:
    def __init__(self,player_name,score=0):
        self.name=player_name
        self.score=score

    def won_point(self):
        self.score+=1

    def get_score_name(self):
        scores={0:"Love",1:"Fifteen",2:"Thirty",3:"Forty"}
        try:
            return scores[self.score]
        except:
            return ""
        
def player_evaluater(player1,player2):
    if player1.score>player2.score:
        return player1.name
    else:
        return player2.name