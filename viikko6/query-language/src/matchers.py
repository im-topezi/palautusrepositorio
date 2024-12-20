class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value
    
class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value
    

class Not:
    def __init__(self,matcher):
        self.matcher=matcher
    def test(self, player):
        if self.matcher.test(player):
            return False
        
        return True
        
class All:
    def __init__(self):
        pass

    def test(self,player):
        return True
    
class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True

        return False
    
    
class QueryBuilder:
    def __init__(self,query=All()):
        self.query=query
    def build(self):
        return QueryBuilder(self.query)
    def one_of(self,*matchers):
        return QueryBuilder(Or(*matchers))
    def plays_in(self,team):
        return QueryBuilder(And(self.query,PlaysIn(team)))
    def has_at_least(self,amount,type_of_score):
        return QueryBuilder(And(self.query,HasAtLeast(amount,type_of_score)))
    def has_fewer_than(self,amount,type_of_score):
        return QueryBuilder(And(self.query,HasFewerThan(amount,type_of_score)))
    def test(self,player):
        return self.query.test(player)
        