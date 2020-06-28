import os
from dotenv import load_dotenv
load_dotenv()

from locations import get_locations
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
IP_PRE = os.getenv('IP_PRE')

# The range of endings to scan.
locations = get_locations()
minEnding = locations[0].ending
maxEnding = locations[len(locations) - 1].ending

######################
# Don't mess with code above this line.
#
# This is a comment ('#' = Comment)
#
# Settings below this line are meant to be user-editable (even if you don't know Python! :D)
######################

FROM_EMAIL = os.getenv('FROM_EMAIL')
TO_EMAIL = os.getenv('TO_EMAIL')
SUBJECT = os.getenv('SUBJECT')