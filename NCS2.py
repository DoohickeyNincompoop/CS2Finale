#!/usr/bin/python

import cgi

def htmlTop():
        print '''Content-type:text/html\n\n
        <!DOCTYPE html>
        <html>
        <head>
                <link rel="stylesheet" type="text/css" href="finalprojectstyle2.css">
                <meta charset="utf-8">
                <title>mAd LiBs</title>
        </head>
        </body>
        '''

def htmlTail():
        print '''</body>
        </html>'''

def main():
        formData = cgi.FieldStorage()
        htmlTop()
        print '''My "Dream Man" should, first of all be very <em>{}</em> and <em>{}</em>.
        He should have a physique like <em>{}</em>, a profile like <em>{}</em>, and the intelligence of a/an <em>{}</em>.
        He must be polite and must always remember to <em>{}</em> my <em>{}</em>, to tip his <em>{}</em> and to take my <em>{}</em> when crossing the street.
        He should move <em>{}</em>, have a/an <em>{}</em> voice, and should always dress <em>{}</em>.
        I would also like him to be a/an <em>{}</em> dancer, and when we are alone he should whisper <em>{}</em> nothings into my <em>{}</em> and hold my <em>{}</em>.
        I know the perfect man is hard to find.
        In fact, the only one I can think of is <em>{}</em>.
        '''.format(formData.getvalue("1"),formData.getvalue("2"),formData.getvalue("3"),formData.getvalue("4"),formData.getvalue("5"),formData.getvalue("6"),formData.getvalue("7"),formData.getvalue("8"),formData.getvalue("9"),formData.getvalue("10"),formData.getvalue("11"),formData.getvalue("12"),formData.getvalue("13"),formData.getvalue("14"),formData.getvalue("15"),formData.getvalue("16"),formData.getvalue("17"))
        htmlTail()

if __name__=='__main__':
        try:
                main()
        except:
                cgi.print_exception()
