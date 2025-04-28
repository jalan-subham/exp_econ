from otree.api import *

doc = """
Volunteer's dilemma, 1 round, no group income reveal, standard (not altruistic) version.
"""

class C(BaseConstants):
    NAME_IN_URL = 'volunteer_dilemma_v7'
    PLAYERS_PER_GROUP = 4
    GENERAL_BENEFIT = cu(10)
    VOLUNTEER_COST = cu(5)  # standard: cost < benefit
    NO_VOLUNTEER_PAYOFF = cu(-2)

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    num_volunteers = models.IntegerField()

class Player(BasePlayer):
    volunteer = models.BooleanField(
        label='Do you wish to volunteer?', doc="""Whether player volunteers"""
    )
    name = models.StringField(
        label='Enter your name', doc="""Name of the player"""
    )

def set_payoffs(group: Group):
    players = group.get_players()
    group.num_volunteers = sum([p.volunteer for p in players])
    if group.num_volunteers > 0:
        baseline_amount = C.GENERAL_BENEFIT
    else:
        baseline_amount = C.NO_VOLUNTEER_PAYOFF
    for p in players:
        p.payoff = baseline_amount
        if p.volunteer:
            p.payoff -= C.VOLUNTEER_COST

class Introduction(Page):
    form_model = 'player'
    form_fields = ['name']

class Decision(Page):
    form_model = 'player'
    form_fields = ['volunteer']
    def vars_for_template(player):
        return {}

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs

class Results(Page):
    pass
class ThankYou(Page):
    pass

page_sequence = [
    Introduction, Decision, ResultsWaitPage, Results, ThankYou
]