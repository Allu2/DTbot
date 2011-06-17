#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       untitled.py
#       
#       Copyright 2011 Aleksi Joakim Palomäki <aleksi@gami>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
#  
     
def msg(q, channel, tn):
	tn.write ("PRIVMSG " + channel + " :" + q + "\n\r" )

def handler(tn,HOST,nick,realname,IDENT,line):
	try:
		#from ircbot_Events import Events
		import ircbot_Events
		x = ircbot_Events.Events()
		lineinfo = x.conversation(line)
		channel = lineinfo["Channel"]
		nick = lineinfo["Nick"]
		message = lineinfo["Msg"]
		print "%(channel)s%(nick)s: %(message)s" %locals()
		if x.msg_found("Hello", message) == True:
			Reply = "Hello " + nick
			msg(Reply, channel, tn)
		if x.msg_found("!Reload", message) == True:
			reload(ircbot_Events)
			#reload(ircbot_handler)
			
		
		if "+x" in line:
			tn.write("JOIN #linux\n")
	except:
		print "Error!!!"
