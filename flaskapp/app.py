#!/usr/bin/python3

# -*- coding: utf-8 -*-
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import json
import os
import requests
#from dotenv import load_dotenv
from flask import Flask, request, session, render_template, flash
from requests.auth import HTTPBasicAuth

app = Flask(__name__)
#@app.route("/")


class churnForm():

    @app.route('/', methods=['GET', 'POST'])
    def index():

        
         return render_template('input.html')


#load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
#port = os.environ.get('PORT', '5000')
#host = os.environ.get('HOST', '0.0.0.0')
if __name__ == "__main__":
#    app.run(host=host, port=int(port))

   app.run()

