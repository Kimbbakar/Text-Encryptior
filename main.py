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
	<!--
		Want to add some emotional text here . But I can't.
		Rak1, SI and ATC must watch this and bring out something to crack new jokes.  :(
	-->

<div>
  <b>
  <h1>Welcome to Word encryptor !</h1>
</div>

<form method="post">
  <select name="ROT">
    <option value="13">13 Rotation</option>
    <option value="2">2 Rotation</option>
    <option value="15">15 Rotation</option>
  </select>

  <br>
  <br>
<div style="color: red">
<b>
%(error)s
</div>

  <br>
  <input type="submit">



</form>


"""

rot13="""

<div>
  <b>
  <h1>Rotation 13</h1>
</div>


<form method="post">


<form method="post">
  <!--
  <input type="text" name='text' value="%(text)s" style="height: 100px; width: 400px;"> -->

<textarea name="text" 
              style="height: 100px; width: 400px;">%(text)s</textarea>
  <br><br>
  <input type="submit" name="submit">

</form>


"""

def encrypt(s,val):
  s=s.lower();
  s=list(s);
  for i in range(len(s)):
    if (s[i].isalpha()==True):
      s[i]=chr( ( (ord(s[i])-97)+val)%26+97 );

  #x=chr(ord(s[0])-32);
  #s[0]=x;
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
    self.response.out.write(front%{"error":""} )
  def post(self):
    ROT=self.request.get('ROT')
#    self.response.out.write(ROT)

    if(ROT=="13"):
      self.redirect('/rot13')
    else:
      self.response.out.write(front%{"error":"That page is under construction.Please try another option !"} )

class ROT13(webapp2.RequestHandler):
  def get(self):
    self.response.out.write(rot13%{"text":"Enter your text here..." } )
  def post(self):
    text=self.request.get('text')
 #   if(reset=="Home"):
#    self.redirect('/')    
#    else
    self.response.out.write(rot13%{"text":escape_html( encrypt(text,13) ) } )

app = webapp2.WSGIApplication([
    ('/', MainHandler),('/rot13',ROT13)
], debug=True)

