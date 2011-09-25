#Imports
import telnetlib
import ircbot_handler

#Variables
HOST = '' #server here
PORT = 6667
nick = "Allu2_Bot"
realname = "IrcBot by allu2"
IDENT = "allu2bot"
#Make connection to server
tn = telnetlib.Telnet(HOST,PORT)
#Send nick to irc server
tn.write("NICK %s\n" %nick)
tn.write("USER %(IDENT)s %(HOST)s Allu2:'%(realname)s'\n" % locals())
s = True
#Main loop
while True:
	line = tn.read_until('\n')
	c = False
	#Manage Pings here
	if "PING :" in line:
		tn.write("PONG %s\n" %HOST)
		print "PONG :%s\n" % HOST
	#Reload  handler if asked
	if "!Reload" in line:
		print "Reloading!!"
		try:
			reload(ircbot_handler)	
			c = True
	#In case of errors in handler annonce emergency mode and wait till its fixed and reloaded
		except:
			print "Error!!"
			tn.write("PRIVMSG " +'#linux '+ ":" + "Emergency mode activated, fix the bugs and reload!" + "\n\r" )
	#Print all server messages for debugging observing etc.
	print line
	#Start up the Handler for commands :)

	ircbot_handler.handler(tn,HOST,nick,realname,IDENT,line, c, s)
	c = False
	s = False



