from emuch_logger import *
url = 'http://muchong.com/bbs/logging.php?action=login'
emuch_logger = EmuchLogger(url)
try:
	cookies = emuch_logger.log_in()
	#get credit
	response = emuch_logger.get_credit()
	#check
	#credit_soup = BeautifulSoup(response_1)
	#formhash_tag = credit_soup.find('input',attrs = {'name':'formhash'})
	if response:
		print "Today's credit -> get!"
	else:
		print 'Wait for tomorrow ~'
except TypeError:
	print "A exception is detected, check your internet connection."
finally:
	raw_input('Press Enter to exit...')