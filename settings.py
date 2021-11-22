from os import environ

#oTreeCodeReview
# Dear Chris,  I am a beginner on otree. I want to design an app that participants answer questions like a survey in this project, the logic may like:
#  Such as: Just give 1 minute for subjects to answer questions and we can calculate the ammount of questions they answer and the accuracy rate they have. And calculate their rank in a group or some people with same identity.
#
# The problem: 1. limited time 2. make sure the answer is right or wrong. 3. calculate the rank. I donot how the logic will be arranged using otree.
# do you know or have some similar packages like this? Or just remind me how to do it using otree?  Some details may better. Thank you in advance!!!
#
# Sincerely,
# Claire

# Chris, I donot know how to do it if things like this, would you be so kind to give me some clues or details better? My email is 943576333@qq.com / xinzeliu98@163.com. Thank you in advance!!!

SESSION_CONFIGS = [
    # dict(
    #     name='MPL',
    #     display_name='MPL',
    #     num_demo_participants=1,
    #     app_sequence=['MPL', 'payment_info'],
    # ),
    # dict(
    #     name='public_goods',
    #     display_name="Public Goods",
    #     num_demo_participants=3,
    #     app_sequence=['public_goods', 'payment_info'],
    # ),
    # dict(
    #     name='income_expectation',
    #     display_name="income_expectation",
    #     num_demo_participants=3,
    #     app_sequence=['income_expectation'],
    # )
    dict(
        name='part1_3',
        display_name="part1_3",
        num_demo_participants=3,
        app_sequence=['MPL','public_goods','income_expectation'],
    )
    # dict(
    #     name='survey',
    #     display_name="survey",
    #     num_demo_participants=3,
    #     app_sequence=['survey', 'payment_info'],
    # ),
    # dict(
    #     name='survey',
    #     display_name='survey',
    #     num_demo_participants=1,
    #     app_sequence=['survey', 'payment_info'],
    # ),
    # dict(
    #     name='MPL',
    #     display_name='MPL',
    #     num_demo_participants=1,
    #     app_sequence=['MPL', 'payment_info'],
    # )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = 'cxr4m(#mi$l86s)69%ovzd9y2c$)42j30h3va1zw4@vv^%hjgq'

INSTALLED_APPS = ['otree']
