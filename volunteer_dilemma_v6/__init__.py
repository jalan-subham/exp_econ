from otree.api import *
import random

doc = """
Volunteer's dilemma, ALTRUISM: OFF, RANDOM BALANCES: ON.
"""

class C(BaseConstants):
    NAME_IN_URL = 'volunteer_dilemma_v6'
    PLAYERS_PER_GROUP = 5
    NUM_OTHER_PLAYERS = PLAYERS_PER_GROUP - 1
    GENERAL_BENEFIT = cu(5)
    VOLUNTEER_COST = cu(3)  # altruism: cost = benefit
    NO_VOLUNTEER_PAYOFF = cu(-2)
    BALANCE_LOW = 50
    BALANCE_HIGH = 100 # random balances
    # We could not get NUM_ROUNDS to work while persisting the computed variables, so we hardcoded the page sequence
    NUM_ROUNDS = 1 # number of rounds

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
    balance = models.CurrencyField(
        label='Balance',
        doc="""The player's balance after the round"""
    )

def initialize_balance(player: Player):
    player.balance = random.randint(BALANCE_LOW, BALANCE_HIGH)

def set_payoffs_and_balances(group: Group):
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
    for p in players:
        p.balance += p.payoff

class Introduction(Page):
    form_model = 'player'
    form_fields = ['name']
    def before_next_page(player, timeout_happened):
        initialize_balance(player)

class Decision(Page):
    form_model = 'player'
    form_fields = ['volunteer']
    def vars_for_template(player):
        group_incomes = sorted([p.balance for p in player.group.get_players()])
        return {
            "group_incomes": ', '.join([str(x) for x in group_incomes]),
        }

class InitWaitPage(WaitPage):
    def before_next_page(player, timeout_happened):
        initialize_balance(player)

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs_and_balances

class Results(Page):
    pass
class ThankYou(Page):
    pass

page_sequence = [
    Introduction, InitWaitPage, Decision, ResultsWaitPage, Results,
    Decision, ResultsWaitPage, Results,
    Decision, ResultsWaitPage, Results,
    ThankYou
]