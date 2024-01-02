# Import necessary components from oTree
from otree.api import *

doc = """
Credit Worthiness Assessment Experiment
"""


class Constants(BaseConstants):
    name_in_url = 'credit_worthiness'
    players_per_group = 2
    num_rounds = 1
    BUDGET = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    give = models.CurrencyField(
        min=0,
        max=Constants.BUDGET,
        label="How much do you want to give?"
    )


class Player(BasePlayer):
    age_group = models.StringField(
        choices=["18-30", "31-45", "46-60", "61+"],
        label="Select your age group:"
    )
    health_insurance = models.BooleanField(label="Do you have health insurance?")
    dues_payment = models.BooleanField(label="Do you pay your dues on time?")
    marital_status = models.StringField(
        choices=["Single", "Married", "Divorced", "Widowed"],
        label="Select your marital status:"
    )
    family_members = models.IntegerField(min=1, label="Number of family members:")
    total_assets = models.FloatField(min=0, max=999999, label="Total assets (in dollars):")
    other_income_sources = models.BooleanField(label="Do you have any other sources of income?")
    payment_history = models.BooleanField(label="Do you have a good payment history/previous credit owed?")
    credit_score = models.IntegerField()

    def calculate_credit_score(self):
        score = 600

        # add points for good payment history
        if self.payment_history:
            score += 50

        # substract/add points based on age
        if self.age_group == "18-30":
            score += 20
        elif self.age_group == "31-45":
            score = score
        elif self.age_group == "46-60":
            score -= 10
        elif self.age_group == "61+":
            score -= 20

        # add points for health insurance
        if self.health_insurance:
            score += 30

        # subtract points for dues not paid on time
        if not self.dues_payment:
            score -= 20

        # marital status points
        if self.marital_status == "Married":
            score += 10
        elif self.marital_status in ["Divorced", "Widowed"]:
            score -= 10

        # substract points for more family members
        score -= (self.family_members - 1) * 5

        # add points for total assets
        score += int(self.total_assets / 10000)

        # other income sources
        if self.other_income_sources:
            score += 15

        self.credit_score = max(300, min(850, score))


def set_payoffs(group: Group):
    for player in group.get_players():
        player.payoff = Constants.BUDGET + player.credit_score / 10 + group.give


class Welcome(Page):
    pass


class Instructions(Page):
    pass


class Decision(Page):
    form_model = 'group'
    form_fields = ['give']


class Response(Page):
    form_model = 'player'
    form_fields = ['age_group', 'health_insurance', 'dues_payment', 'marital_status', 'family_members', 'total_assets',
                   'other_income_sources', 'payment_history']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.calculate_credit_score()


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    pass


page_sequence = [Welcome, Instructions, Decision, Response, ResultsWaitPage, Results]
