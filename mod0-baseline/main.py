# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START mod0_baseline]
app = Flask(__name__)

import os
import webapp2
from flask import Flask, render_template, request
from google.appengine.ext import ndb

class Visit(ndb.Model):
    'Visit entity registers visitor IP address & timestamp'
    visitor   = ndb.StringProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)

def store_visit(remote_addr, user_agent):
    'create new Visit entity in Datastore'
    Visit(visitor='{}: {}'.format(remote_addr, user_agent)).put()

def fetch_visits(limit):
    'get most recent visits'
    return Visit.query().order(-Visit.timestamp).fetch(limit)

class MainHandler(webapp2.RequestHandler):
    'main application (GET) handler'
    def get(self):
        store_visit(self.request.remote_addr, self.request.user_agent)
        visits = fetch_visits(10)
        tmpl = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(tmpl, {'visits': visits}))

# [END mod0_baseline]
