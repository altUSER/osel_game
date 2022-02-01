from classes import User
from classes import Session


if __name__ == "__main__":

    session = Session()

    print(session.addUser("first"))
    print(session.addUser("second"))

    print(session.users[0].name)
    session.giveCards(0, 13)
    print (session.users[0].countCards())