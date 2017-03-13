class hand(object):
    def __init__(self,dealer_card,*cards):
        self.dealer_card = dealer_card
        self.cards = list(cards)

    def __str__(self):
        return ", ".join(map(str,self.cards))

    def __repr__(self):
        return "{__class__.__name__}({dealer_card!r},{_cards_str})".format(__class__=self.__class__,_cards_str=", ".join(map(repr,self.cards)),**self.__dict__)

    def __format__(self, format_specification):
        if format_specification == "":
            return str(self)
        return ", ".join("{0:{fs}}".format(c,fs=format_specification) for c in self.cards)



zjw = hand('zjw','zzz','cbb','ceb','zyc')



