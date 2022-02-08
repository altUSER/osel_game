import random

class User():
    def __init__(self, name):
        self.name = name
        self.hand = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
        self.score = 0


class Session():
    def __init__(self):
        self.users = {}
        self.deck = {0: 1, 1: 8, 2: 8, 3: 8, 4: 8, 5: 8, 6: 8, 7: 8, 8: 8, 9: 8, 10: 8, 11: 8, 12: 8, 13: 8, 14: 5}
        self.table = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
        self.sbros = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}

    def countCards(self, cards):
        count = 0
        for i in cards.keys():
            count += cards[i]

        return count

    def addUser(self, username):
        id = len(self.users)
        self.users.update({id: User(username)})

        return id

    def giveRandomCard(self, uid):

        availableCardsId = []
        for card in range(1, 15):
            availableCardsId.append(card)

        card = random.choice(availableCardsId)
        self.users[uid].hand[card]+=1
        self.deck[card]-=1

    def giveCardsToUsers(self, uid, count):
        for i in range(count):
            self.giveRandomCard(uid)

    def giveCardsToAllUsers(self, handSize):
        if handSize*len(self.users)>self.countCards(self.deck):
            raise ValueError('Too many cards in hand')
        osel = random.randint(len(self.users)-1)
        self.users[osel].hand[0] = 1
        self.deck[0] = 0

        for uid in self.users.keys():
            self.giveRandomCardsToUser
