from slacker import Slacker
import pprint

pp = pprint.PrettyPrinter(indent=4)

slack = Slacker('ADD_SLACK_API_TOKEN')

###########
## USERS ##
###########


response = slack.users.list()
users = response.body['members']

#pp.pprint(users)

for user in users:
	print user['real_name']
	print user['name']
	print user['id']
	print "\n"



##############
## CHANNELS ##
##############

slack_channels = slack.channels.list()
channels = slack_channels.body['channels']

# pp.pprint(channels)
# print "\n"

for c in channels:
	print c['name']
	print c['num_members']
	print c['members']
	print c['id']
	print '\n'



##############
## HISTORY ###
##############


#This part is for history

# slack_history = slack.channels.history('ADD_SLACK_CHANNEL_ID',count=1000)
# history = slack_history.body 

# pp.pprint(history)

# has_more = history['has_more']
# print 'has_more',has_more

# messages = history['messages']

# for m in messages:
# 	# pp.pprint(m)
# 	# print "\n"



# 	print m['text']
	
# 	try:
# 		print m['user']
# 	except:
# 		pass
	
# 	try:
# 		print m['reactions']
# 	except:
# 		pass

# 	try:
# 		print m['file']['reactions']
# 		print m['file']['initial_comment']['reactions']
# 	except:
# 		pass

# 	print "\n"
