# <チャレンジ_chapter19>
# 問題1
# Wargame(戦争)
from random import shuffle

#カード
class Card():
    #カード基本情報(クラス変数)
    suits = ["spades", "hearts", "diamonds", "culbs"]
    values = [None, None,
    "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "Juck", "Queen", "King", "Ace"]

    #カード単体を作成(インスタンスオブジェクトを作成)
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    #カード番号とマークを「<」演算子で比較(__lt__特殊メソッドをオーバーライド)
    def __lt__(self, player2):
        if self.value < player2.value:
            return True
        if self.value == player2.value:
            return self.suit < player2.suit
        return False
    
    #カード番号とマークを「>」演算子で比較(__gt__特殊メソッドをオーバーライド)
    def __gt__(self, player2):
        if  self.value > player2.value:
            return True
        if self.value == player2.value:
            return self.suit > player2.suit
        return False
    
    #カード番号とマークを文字列として出力(__repr__特殊メソッドをオーバーライド)
    def __repr__(self):
        return self.values[self.value] + " of " + self.suits[self.suit]
"""
card1 = Card(10, 1)
card2 = Card(13, 3)
print(card1)
#⇒card1.__repr__()
print(card2)
#⇒card2.__repr__()
print(card1 < card2)
#⇒card1.__lt__(card2)
print(card1 > card2)
#⇒card1.__gt__(card2)
"""

#デッキ
class Deck():
    #カードデッキの入れ物を作成(クラス変数)
    card_deck = []

    #５２枚のカードデッキを作成(インスタンスオブジェクトを作成)
    def __init__(self):
        for i in range(2, 15):
            for j in range(4):
                self.card_deck.append(Card(i, j))
        shuffle(self.card_deck)
    
    #デッキ内のカード枚数を判定して１枚以上の場合は１枚減らして、そのカードの番号とマークを取得
    def draw(self):
        if len(self.card_deck) == 0:
            return None
        else:
            return self.card_deck.pop()
"""
deck = Deck()
for card in deck.card_deck:
    print(card)
print(len(deck.card_deck))
card = deck.draw()
print(card)
print(len(deck.card_deck))
"""

#プレイヤー
class Player():
    #プレイヤー初期情報を作成(インスタンスオブジェクトを作成)
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name
"""
player1 = Player("Yuto")
print(player1.wins, player1.card, player1.name)
"""

#ゲーム
class Game():
    #カードデッキとプレイヤー基本情報を作成(インスタンスオブジェクトを作成)
    def __init__(self):
        self.deck = Deck()
        name1 = input("Enter player1's name: ")
        name2 = input("Enter player2's name: ")
        self.player1 = Player(name1)
        self.player2 = Player(name2)
    
    #ラウンド毎の勝利プレイヤーを表示(入力値にコンポジションを利用)
    def print_winner(self, winner):
        print("The winner of this round is {}!!".format(winner.name))
    
    #プレイヤーの手札を表示(入力値にコンポジションを利用)
    def print_draw(self, player1, player2):
        print("{}'s card is {}, {}'s card is {}!!".format(player1.name, player1.card, player2.name, player2.card))
    
    #ラウンドの勝利回数から勝利プライヤーを決定(入力値にコンポジションを利用)
    def game_winner(self, player1, player2):
        if player1.wins > player2.wins:
            print("The winner is {}!".format(player1.name))
        elif player1.wins < player2.wins:
            print("The winner is {}!!".format(player2.name))
        else:
            print("This game is draw!!")
    
    #ゲームを制御
    def play_game(self):
        #カードデッキを用意
        player_deck = self.deck.card_deck
        print("Let's play wargame!!")

        #ゲームの開始終了を制御(whileループを使用)
        while len(player_deck) >= 1:
            request = input("Enter q to quit, another to continue: ")
            if  request == "q":
                break
            #プレイヤーの手札と名前を表示
            self.player1.card = self.deck.draw()
            self.player2.card = self.deck.draw()
            self.print_draw(self.player1, self.player2)
            #ラウンド毎の勝利プレイヤーを表示
            if self.player1.card > self.player2.card:
                self.player1.wins += 1
                self.print_winner(self.player1)
            else:
                self.player2.wins += 1
                self.print_winner(self.player2)
        
        #ゲーム勝利プレイヤーを表示
        self.game_winner(self.player1, self.player2)

game = Game()
game.play_game()