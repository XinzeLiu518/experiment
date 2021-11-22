from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants
import random


class information1(Page):
    form_model = 'player'
    form_fields = ['time']

class expectation1(Page):
    form_model = 'player'
    form_fields = ['factor1', 'expectation1']

class identity1(Page):
    form_model = 'player'
    def is_displayed(self):
        player = self.player
        return player.identity==3

class identity2(Page):
    form_model = 'player'
    def is_displayed(self):
        player = self.player
        return player.identity==4

class information2(Page):
    form_model = 'player'
    form_fields = ['undergraduate_type']

class expectation2(Page):
    form_model = 'player'
    form_fields = ['factor2', 'expectation2']

page_sequence = [information1,expectation1,identity1,identity2, information2, expectation2]
