from django.db import models

class Card(models.Model):
    SUITS = [
        ('H', 'Hearts'),
        ('D', 'Diamonds'),
        ('C', 'Clubs'),
        ('S', 'Spades'),
    ]
    RANKS = [
        ('A', 'Ace'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
        ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'),
        ('J', 'Jack'), ('Q', 'Queen'), ('K', 'King'),
    ]
    suit = models.CharField(max_length=1, choices=SUITS)
    rank = models.CharField(max_length=2, choices=RANKS)
    face_up = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.get_rank_display()} of {self.get_suit_display()}"

class Deck(models.Model):
    cards = models.ManyToManyField(Card)

    def shuffle(self):
        """Shuffle the deck."""
        self.cards.set(list(self.cards.order_by('?')))

    def deal(self):
        """Deal a card from the deck."""
        return self.cards.first()