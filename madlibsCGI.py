#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import cgi
 
def htmlTop():
	print '''Content-type:text/html\n\n
    	<!DOCTYPE html>
    	<html>
        	<head>
                        <link rel="stylesheet" type="text/css" href="finalprojectstyle.css">
                        <meta charset="utf-8">
                        <title> mAd LiBs </title>
        	</head>
        	<body>'''
 
def htmlTail():
	print '''</body>
    	</html>'''
 
 
def main():
	htmlTop()
	print '<h1>  Angry LIBs</h1>'
	print '''A gigantic contest in which you already may be a
      <form style = "display:inline;" action="NCS.py" method="get">
   	  <input type="text" name="1" placeholder = "noun, singular" style = "display:inline;">
    .
    Anyone, and we mean anyone, can enter this
   	  <input type="text" name="2" placeholder = "adjective" style = "display:inline;">  
    contest.
    Just follow these
    <input type="text" name="3" placeholder = "adjective" style = "display:inline;">
    rules.
    Write down in
    <input type="text" name="4" placeholder = "number" style = "display:inline;">
    words or less why you think
    <input type="text" name="5" placeholder = "your mother's name" style = "display:inline;">
    	should be elected
    <input type="text" name="6" placeholder = "noun" style = "display:inline;">
    	Of The Year. Remember she does not know that you think so
    <input type="text" name="7" placeholder = "adverb" style = "display:inline;">
    	of her.
    	First prize will be a deluxe, three-speed
    <input type="text" name="8" placeholder = "piece of technology" style = "display:inline;">
    	and a year’s supply of
    <input type="text" name="9" placeholder = "noun" style = "display:inline;">
        .
	Second prize will be a twenty one foot long
    <input type="text" name="10" placeholder = "noun" style = "display:inline;">
        .
 	Third prize will be a full-color
    <input type="text" name="11" placeholder = "noun" style = "display:inline;">
	plus a set of
    <input type="text" name="12" placeholder = "animal, plural" style = "display:inline;">
    	.
	Each entry must be accompanied by a stamped, self-addressed
    <input type="text" name="13" placeholder = "extraterrestrial being" style = "display:inline;">
    	.
    	The decision will be final and in the event of a tie, duplicate 
    <input type="text" name="14" placeholder = "noun, plural" style = "display:inline;">
    	will be awarded.
	
 <input type="submit" value="Submit">
    </form> '''
 
 
 
	htmlTail()
 
main()



 
