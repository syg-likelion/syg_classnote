from flask import Flask
import os

# Create Flask Instance (application)
app = Flask('application')

# Import Every function in 'views' directory
for base, dirs, names in os.walk(os.path.join('application', 'views')):
	for name in filter(lambda s: s.endswith('.py') and s != '__init__.py', names) :
		exec('from application.views.' + name[:-3] + ' import *')

# Import application config (setting)
import config