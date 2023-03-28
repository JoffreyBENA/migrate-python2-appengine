from google.appengine.ext import vendor
import os

# Set PATH to your libraries folder.
PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')

# Add libraries installed in the PATH folder.
vendor.add(PATH)