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

class Events:
	def debug(self, msg):
		print "[DEBUG]: " + msg
	def msg_found(self, msg, message):
		if msg in message:
			return True
		else:
			return False
	def conversation(self, line):
		
		test = line.split(' ')[2]#[0] host] [1] PRIVMSG] [2] NICK] [3] :message
		name = line.split('!')[0].lstrip(':')
		message_list = line.split(' ')[3:]
		message = ' '.join(message_list).lstrip(':')
		channel = ''
		if "#" in test:
			channel = line.split(' ')[2] + ' '
		info = {"Nick": name, "Channel":channel, "Msg":message}
		return info
	
	

