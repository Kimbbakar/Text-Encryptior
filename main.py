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

front="""
	<div>
	<b>
	<h1>Welcome to Word encryptor !</h1>
	</div>

	<form methom="post">
		<h3>Post your text here </h3>
		<input type="text" name="text" value="%(text)s">

	</form>

"""

def enprypt(self,s):
  s=s.lower();
  s=list(s);
  for i in range(len(s)):
    if (s[i].isalpha()==True):
      s[i]=chr( ( (ord(s[i])-97)+13)%26+97 );

  x=chr(ord(s[0])-32);
  s[0]=x;
  s="".join(s)
  return s

def escape_html(s):
  s=s.replace("&","&amp;")
  s=s.replace(">","&gt;")
  s=s.replace("<","&lt;")
  s=s.replace('"',"&quot;")
  return s;


class MainHandler(webapp2.RequestHandler):
  def get(self):
    self.response.out.write(front%{"text":"" } )
  def post(self):
  	text=self.requst.get('text')
  	self.response.out.write(text)
#    self.response.out.write(front%{"text":(text ) } )

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
