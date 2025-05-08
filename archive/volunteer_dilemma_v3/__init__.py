from otree.api import *
import random


doc = """
Each player decides if to free ride or to volunteer from which all will
benefit.
See: Diekmann, A. (1985). Volunteer's dilemma. Journal of Conflict
Resolution, 605-610.

This is 3 rounds, random balances, name reveal, min-max balance reveal, altruistic version.
"""


class C(BaseConstants):
    NAME_IN_URL = 'volunteer_dilemma_v3'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 1
    NUM_OTHER_PLAYERS = PLAYERS_PER_GROUP - 1
    # """Payoff for each player if at least one volunteers"""
    GENERAL_BENEFIT = cu(5)
    # """Cost incurred by volunteering player"""
    VOLUNTEER_COST = cu(7)
    # payoff if no one volunteers
    NO_VOLUNTEER_PAYOFF = cu(-2)

    BALANCE_LOW = 0 
    BALANCE_HIGH = 10


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    num_volunteers = models.IntegerField()
    min_balance = models.CurrencyField()
    max_balance = models.CurrencyField()


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
    # randomly assign a balance between low and high
    player.balance = random.randint(C.BALANCE_LOW, C.BALANCE_HIGH)
    print(f"Player {player.id_in_group} initialized with balance: {player.balance}")
def set_initial_min_max_balance(group: Group):
    players = group.get_players()
    min_balance = min([p.balance for p in players])
    max_balance = max([p.balance for p in players])
    group.min_balance = min_balance
    group.max_balance = max_balance

# FUNCTIONS
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

    min_balance = min([p.balance for p in players])
    max_balance = max([p.balance for p in players])
    group.min_balance = min_balance
    group.max_balance = max_balance


# PAGES
class Introduction(Page):
    form_model = 'player'
    form_fields = ['name']

    def before_next_page(player, timeout_happened):
        initialize_balance(player)

class Decision(Page):
    form_model = 'player'
    form_fields = ['volunteer']

class InitWaitPage(WaitPage):
    after_all_players_arrive = set_initial_min_max_balance

    def before_next_page(player, timeout_happened):
        initialize_balance(player)
class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs_and_balances


class Results(Page):
    pass
class ThankYou(Page):
    pass


page_sequence = [Introduction, InitWaitPage, Decision, ResultsWaitPage, Results, Decision, ResultsWaitPage, Results, Decision, ResultsWaitPage, Results, ThankYou]
