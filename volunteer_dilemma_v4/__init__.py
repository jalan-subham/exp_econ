from otree.api import *
import random

doc = """
Volunteer's dilemma, ALTRUISM: OFF, RANDOM BALANCES: OFF.
"""

class C(BaseConstants):
    NAME_IN_URL = "VolunteerDilemma-4"
    PLAYERS_PER_GROUP = 3 # how many players per group? this variable can be changed.
    NUM_OTHER_PLAYERS = PLAYERS_PER_GROUP - 1
    GENERAL_BENEFIT = cu(5)
    VOLUNTEER_COST = cu(3)  # altruism: cost = benefit
    NO_VOLUNTEER_PAYOFF = cu(-2)
    BALANCE_LOW = 50
    BALANCE_HIGH = 50 # fixed balances
    # We could not get NUM_ROUNDS to work while persisting the computed variables, so we hardcoded the page sequence
    NUM_ROUNDS = 1 # number of rounds

class Subsession(BaseSubsession):
    round_index = models.IntegerField(initial=1) # round index for the current round

class Group(BaseGroup):
    num_volunteers = models.IntegerField()

class Player(BasePlayer): # player model/table
    volunteer = models.BooleanField(
        label='Do you wish to volunteer?', doc="""Whether player volunteers"""
    )
    name = models.StringField(
        label='Enter your name', doc="""Name of the player"""
    )
    initial_balance = models.CurrencyField(
        label='Initial Balance')
    
    balance = models.CurrencyField(
        label='Balance',
        doc="""The player's balance after the round"""
        
    )
    round1_volunteer = models.BooleanField(
        doc ="""Whether player volunteered in round 1""")
    balance1 = models.CurrencyField(
        label='Balance',
        doc="""The player's balance after round 1"""
    )
    round2_volunteer = models.BooleanField(
        doc ="""Whether player volunteered in round 2""")
    balance2 = models.CurrencyField(
        label='Balance',
        doc="""The player's balance after round 2"""
    )
    round3_volunteer = models.BooleanField(
        doc ="""Whether player volunteered in round 3""")
    balance3 = models.CurrencyField(
        label='Balance',
        doc="""The player's balance after round 3"""
    )

def initialize_balance(player: Player):
    player.balance = random.randint(C.BALANCE_LOW, C.BALANCE_HIGH)

def set_payoffs_and_balances(group: Group): # set the payoffs and balances of the players
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
        # Update the balance and round-specific fields
        p.balance += p.payoff
        round_index = group.subsession.round_index
        if round_index == 1:
            p.round1_volunteer = p.volunteer
            p.balance1 = p.balance
        elif round_index == 2:
            p.round2_volunteer = p.volunteer
            p.balance2 = p.balance
        elif round_index == 3:
            p.round3_volunteer = p.volunteer
            p.balance3 = p.balance
    group.subsession.round_index += 1

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
            "round_index": player.subsession.round_index,
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