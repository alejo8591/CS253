#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain ax copy of the License at
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
form = """
           <form method="post">
             What is your birthday?
             <br>
             <label> Month
                <input type="text" name="month" value="%(month)s">
             </label>
             <label> Day
                <input type="text" name="day" value="%(day)s">
            </label>
             <label> Year
                <input type="text" name="year" value="%(year)s">
            </label>
             <br>
             <div style="color : red">%(error)s</div>
             <input type="submit">
           </form>
       """

class MainHandler(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):
        self.response.out.write(form % {"error":error,
                                        "month": month,
                                        "day": day,
                                        "year":year})
        
    def valid_month(self, month):
        months = ['January',
              'February',
              'March',
              'April',
              'May',
              'June',
              'July',
              'August',
              'September',
              'October',
              'November',
              'December']
        month = month.capitalize()
        if(month in months): return month
     
    def valid_day(self, day):
        days = range(1,32)
        day = int(day)
        if(day in days): return day
    
    def valid_year(self, year):
        years = range(1900, 2021)
        year = int(year)
        if(year in years): return year
        
    def get(self):
           self.write_form()
        
    def post(self):
        
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')
        
        month = self.valid_month(self.request.get('month'))
        day = self.valid_day(self.request.get('day'))
        year = self.valid_year(self.request.get('year'))
        
        if not (month and day and year):
            self.write_form("That dosen't look valid to me, friend.",
                            user_month, user_day, user_year)
        else:
            self.response.out.write('Thanks!')
        

app = webapp2.WSGIApplication([('/', MainHandler)],
                              debug=True)