from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,

)
import random

class Constants(BaseConstants):
    name_in_url = 'income_expectation'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for player in self.get_players():
            player.identity= random.randint(3,4)   #这里random的究竟是什么




class Group(BaseGroup):
    pass


class Player(BasePlayer):

    #age = models.IntegerField(label='What is your age?', min=13, max=125)
    time = models.StringField(
        choices=[['2022年', '2022年'], ['2023年', '2023年'],['2024年','2024年'],['2025年','2025年']],
        label='1、请问你的研究生毕业年份是',
        widget=widgets.RadioSelect,
    )

    factor1 = models.LongStringField(
        label='2、现在，请你预估一下硕士研究生毕业后你的第一份工作的收入。（如果你不打算就业，也请预估硕士研究生毕业就业时的薪酬水平）首先，请陈述一下你是如何预估的，有考虑到哪些因素？（至少要填10个字符以上）',

    )

    expectation1 = models.IntegerField(
        label='''3、你对自己硕士研究生毕业后的第一份工作的收入水平预期是多少?（单位为元/月，请务必根据真实信息填写，实验最后将通过人工检查数据合理性，若数据不合理，填写者将不会被支付整个实验的报酬。）''', min=0, max=50000
    )
    #要限制min和max.

#--------------这里有分页-------------------------
    #这里有一张图片（是random给的）---这是分到不同的group.
#random 显示
#<img src="{% static "undergraduate_identity/undergraduate_master.jpg" %}"/>
#<img src="{% static "undergraduate_identity/master.jpg" %}"/>
    # identity1 = models.StringField()
    # identity2 = models.StringField()
    # identity=models.IntegerField()
    # def creating_session(self):    #是写到subsession里面的
    #     for player in self.get_players():
    #         player.identity = random.choice([3,4])   #这里还是不对
    #         #用is_displayed来check:
    #         def is_displayed(player):    #这里也不对
    #             return player.identiity == 3

    identity = models.IntegerField()

    undergraduate_type = models.StringField(
        choices=[['985/211类院校', '985/211类院校'], ['非985/211类院校', '非985/211类院校'], ['其他', '其他']],
        label='5、你的本科学校毕业类型为？',
        widget=widgets.RadioSelect,
    )

    factor2 = models.LongStringField(
        label='''6、现在，请你对自己硕士研究生毕业后的第一份工作的收入水平进行再次预期（如果你不打算就业，也请预估硕士研究生毕业就业时的薪酬水平）请陈述一下你是如何预估的，有考虑到哪些因素？（至少要填10个字符以上）'''

    )

    expectation2 = models.IntegerField(
        label='''7、你对自己硕士研究生毕业后的第一份工作的收入水平的再次预期是（如果你不打算就业，也请预估研究生毕业就业时的薪酬水平）：（单位为元/月，请务必根据真实信息填写，实验最后将通过人工检查数据合理性，若数据不合理，填写者将不会被支付整个实验的报酬。）'''

    )



