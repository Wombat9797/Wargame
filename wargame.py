# <チャレンジ_chapter19>
# 問題1
# Wargame(戦争)
from random import shuffle

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