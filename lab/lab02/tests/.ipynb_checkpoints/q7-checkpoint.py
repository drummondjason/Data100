# +
OK_FORMAT = True

test = {   'name': 'q7',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> elections_with_first_name.shape\n(182, 7)', 'hidden': False, 'locked': False},
                                   {   'code': '>>> elections_with_first_name[elections_with_first_name["Candidate"] == "Andrew Jackson"].iloc[0]["First Name"]\n\'Andrew\'',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> elections_with_first_name[elections_with_first_name["Candidate"] == "Jo Jorgensen"].iloc[0]["First Name"]\n\'Jo\'', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
