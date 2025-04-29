from os import environ


SESSION_CONFIGS = [
    # dict(
    #     name='vd_v1',
    #     display_name="Modified version of Volunteer's Dilemma by AHRSS - v1",
    #     app_sequence=['volunteer_dilemma_v1'],
    #     num_demo_participants=20,
    # ),
    # dict(
    #     name='vd_v2',
    #     display_name="Modified version of Volunteer's Dilemma by AHRSS - v2",
    #     app_sequence=['volunteer_dilemma_v2'],
    #     num_demo_participants=8,
    # ),
    # dict(
    #     name='vd_v3',
    #     display_name="Modified version of Volunteer's Dilemma by AHRSS - v3",
    #     app_sequence=['volunteer_dilemma_v3'],
    #     num_demo_participants=4,
    # ),
    dict(
        name='volunteer_dilemma_v4',
        display_name='Experimental Economics Experiment 1 (Altruism: ON, Random Balances: ON)',
        app_sequence=['volunteer_dilemma_v4'],
        num_demo_participants=4,
 
    ),
    dict(
        name='volunteer_dilemma_v5',
        display_name='Experimental Economics Experiment 2 (Altruism: ON, Random Balances: OFF)',
        app_sequence=['volunteer_dilemma_v5'],
        num_demo_participants=4,
     
    ),
    dict(
        name='volunteer_dilemma_v6',
        display_name='Experimental Economics Experiment 3 (Altruism: OFF, Random Balances: ON)',
        app_sequence=['volunteer_dilemma_v6'],
        num_demo_participants=4,
    ),
    dict(
        name='volunteer_dilemma_v7',
        display_name='Experimental Economics Experiment 4 (Altruism: OFF, Random Balances: OFF)',
        app_sequence=['volunteer_dilemma_v7'],
        num_demo_participants=4,
    
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'INR'
USE_POINTS = True

ROOMS = [
    # dict(
    #     name='econ101',
    #     display_name='Econ 101 class',
    #     participant_label_file='_rooms/econ101.txt',
    # ),
    dict(name='data_collection', display_name='Room for data collection.'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
"""


SECRET_KEY = '7002691907422'

INSTALLED_APPS = ['otree']
