from otree.api import *



doc = """
Each player decides if to free ride or to volunteer from which all will
benefit.
See: Diekmann, A. (1985). Volunteer's dilemma. Journal of Conflict
Resolution, 605-610.

This is single round, no balances, no name reveal, no min-max balance reveal, altruistic version.
"""


class C(BaseConstants):
    NAME_IN_URL = 'volunteer_dilemma_v2'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 1
    NUM_OTHER_PLAYERS = PLAYERS_PER_GROUP - 1
    # """Payoff for each player if at least one volunteers"""
    GENERAL_BENEFIT = cu(5)
    # """Cost incurred by volunteering player"""
    VOLUNTEER_COST = cu(7)
    # payoff if no one volunteers
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



# FUNCTIONS
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


# PAGES
class Introduction(Page):
    form_model = 'player'
    form_fields = ['name']


class Decision(Page):
    form_model = 'player'
    form_fields = ['volunteer']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    pass

class ThankYou(Page):
    pass

page_sequence = [Introduction, Decision, ResultsWaitPage, Results, ThankYou]
