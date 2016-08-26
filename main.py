#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar
import cgi

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>Rot13</title>
</head>
<body>
    <h1>
        Enter some text to Rot13
    </h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""
rot_form ="""
    <form method="post">
    <label> Rotate by:</label>
    <input type="text" name="rot" value="0">
    <br>
    <textarea name ="ROTtext" style="height: 100px; width:400px;">{}</textarea>
    <br>
    <input type="submit">
    </form>
"""
class Index(webapp2.RequestHandler):


    def get(self):

        response = page_header + rot_form.format("") + page_footer
        self.response.write(response)

    def post(self):
        ROT_text = self.request.get("ROTtext")
        rot_number = self.request.get("rot")
        rot_number = int(rot_number)
        rotate = caesar.encrypt(ROT_text,rot_number)
        ROT_text = cgi.escape(rotate, quote=True)

        response = page_header + rot_form.format(ROT_text) + page_footer
        self.response.write(response)



app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
