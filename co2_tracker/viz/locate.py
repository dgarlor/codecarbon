import requests

# TODO: Make these sets
US = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado', \
'Connecticut','Delaware', 'Florida','Georgia','Hawaii','Idaho', \
'Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana', \
'Maine','Maryland','Massachusetts','Michigan','Minnesota', \
'Mississippi','Missouri','Montana','Nebraska','Nevada', \
'New Hampshire','New Jersey','New Mexico','New York', \
'North Carolina','North Dakota','Ohio','Oklahoma','Oregon', \
'Pennsylvania', 'Rhode Island','South Carolina','South Dakota', \
'Tennessee','Texas','Utah','Vermont','Virginia','Washington', \
'West Virginia','Wisconsin','Wyoming']

EUROPE = ['Albania','Andorra','Armenia','Austria','Azerbaijan', \
          'Belarus','Belgium','Bosnia and Herzegovina','Bulgaria', \
          'Croatia','Cyprus','Czech Republic','Denmark','Estonia','Finland', \
          'France','Georgia','Germany','Greece','Hungary','Iceland', \
          'Ireland','Italy','Kazakhstan','Kosovo','Latvia','Liechtenstein', \
          'Lithuania','Luxembourg','Malta','Moldova','Monaco','Montenegro', \
          'Netherlands','Macedonia','Norway','Poland','Portugal','Romania', \
          'Russia','San Marino','Serbia','Slovakia','Slovenia','Spain', \
          'Sweden','Switzerland','Turkey','Ukraine','United Kingdom','Vatican City']

CANADA = ['British Columbia', 'Newfoundland and Labrador', 'Saskatchewan',
            'Prince Edward Island', 'Ontario', 'Nova Scotia', 'Quebec',
            'Alberta', 'Manitoba', 'Northwest Territories', 'New Brunswick',
            'Nunavut', 'Yukon']

""" LOCATION UTILS """

def in_US(location):
    return (location in US)

def in_Europe(location):
    return (location in EUROPE)

def in_Canada(location):
    return (location in CANADA)
