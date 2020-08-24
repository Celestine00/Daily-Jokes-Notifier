import datetime
import random
import pyjokes
import time
from plyer import notification
joke = pyjokes.get_joke()
now = datetime.datetime.now()
hour = now.hour
def alert(text):    
        notification.notify(
            app_icon = 'ding.ico',
            title = 'Joke of the Day',
            message = text,
            timeout = 6,
        )
        time.sleep(7)
        
if hour < 12:
    alert("Good Morning, Here's a joke for you: \n" + joke)
else:
	alert('Jokes will be ready in the Morning')    
	



