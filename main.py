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
    <option value="13 forward backward">13 forward backward Rotation</option>
    <option value="13 backward forward">13 forward backward Rotation</option>
  </select>

  <br>
  <br>
<div style="color: red">
<b>
%(error)s
</div>

  <br>
  <button type="submit" > Submit </button>



</form>


"""

rot="""

<div>
  <b>
  <h1>Rotation %(rotation)s</h1>
</div>


<form method="post">


<form method="post">
  <!--
  <input type="text" name='text' value="%(text)s" style="height: 100px; width: 400px;"> -->

<textarea name="text" 
              style="height: 100px; width: 400px;">%(text)s</textarea>
  <br><br>
  <button type="submit" value="Submit" >Submit </button>  
</form>

<form action="./" >
    <input type="submit" name="Home" value="Home">
</form>

"""

def encrypt(s,type):
  s=s.lower();
  s=list(s);
  for i in range(len(s)):
    if (s[i].isalpha()==True):
      if(type==0):
        s[i]=chr( ( (ord(s[i])-97)+13+26)%26+97 );

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

    if(ROT=="13"):
      self.redirect('/rot13')
    elif(ROT=="13 forward backward"):
      self.redirect('/rot13FB')
#    else:

#      self.response.out.write(front%{"error":"That page is under construction.Please try another option !"} )

class ROT13(webapp2.RequestHandler):
  def get(self):
    self.response.out.write(rot%{"text":"Enter your text here...","rotation":"13" } )
  def post(self):
    text=self.request.get('text')
    self.response.out.write(rot%{"text":escape_html( encrypt(text,0) ),"rotation":"13" } )

class ROT13FB(webapp2.RequestHandler):
  def get(self):
    self.response.out.write(rot%{"text":"Enter your text here...","rotation":"13 forward backward" } )
  def post(self):
    text=self.request.get('text')
    self.response.out.write(rot%{"text":escape_html( encrypt(text,1) ),"rotation":"13 forward backward" } )

app = webapp2.WSGIApplication([
    ('/', MainHandler),('/rot13',ROT13),('/rot13FB',ROT13FB)
], debug=True)

