from __future__ import print_function	# For Py2/3 compatibility
import eel

# Set web files folder
eel.init('web')

@eel.expose                         # Expose this function to Javascript
def say_hello_py(x):
    print('Hello from %s' % x)

# say_hello_py('edgar')
eel.say_hello_js('edgar')   # Call a Javascript function

eel.start('hello.html', size=(500, 500))    # Start
