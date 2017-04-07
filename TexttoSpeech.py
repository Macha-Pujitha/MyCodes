'''
To install it on anaconda
pip install -i https://pypi.anaconda.org/pypi/simple pyttsx
'''

import pyttsx
engine = pyttsx.init()
engine.say('what are you doing')
engine.runAndWait()
