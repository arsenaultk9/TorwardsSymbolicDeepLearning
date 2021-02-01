class Score:
    score = 1

    @classmethod
    def increment_score(cls):
        cls.score += 1
        print('score: ' + str(cls.score))

    @classmethod
    def decrement_score(cls):
        cls.score -= 1
        print('score: ' + str(cls.score))