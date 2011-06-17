#Imports
import telnetlib
import ircbot_handler

#Variables
HOST = 'irc.unilang.org'
PORT = 6667
nick = "Allu2_Bot"
realname = "IrcBot by allu2"
IDENT = "allu2bot"
#Make connection to server
tn = telnetlib.Telnet(HOST,PORT)
tn.write("NICK %s\n" %nick)#Send nick to irc server
tn.write("USER %(IDENT)s %(HOST)s Allu2:'%(realname)s'\n" % locals())

#Main loop
while True:
	line = tn.read_until('\n')
	#Manage Pings here
	if "PING :" in line:
		tn.write("PONG %s\n" %HOST)
		print "PONG :%s\n" % HOST
	#Reload  handler if asked
	if "!Reload" in line:
		print "Reloading!!"
		try:
			reload(ircbot_handler)	
		#In case of errors in handler annonce emergency mode and wait till its fixed and reloaded
		except:
			print "Error!!"
			tn.write("PRIVMSG " +'#linux '+ ":" + "Emergency mode activated, fix the bugs and reload!" + "\n\r" )
	#Print all server messages for debugging observing etc.
	print line
	#Start up the Handler for commands :)
	ircbot_handler.handler(tn,HOST,nick,realname,IDENT,line)#handler(tn,HOST,nick,realname,IDENT,line)
#	handler(tn,HOST,nick,realname,IDENT,line)



