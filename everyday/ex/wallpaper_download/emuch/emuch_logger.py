# -*- coding: utf-8 -*-
import re
from logger_base import *
import time
from bs4 import BeautifulSoup

class EmuchLogger(Logger):
	def __init__(self, url):
		Logger.__init__(self, url)
		self._log_str = {
					'update_form_data'  : ('there has been \'${form_name} = ${old_value}\','
								  			'update to \'${form_name} = ${new_value}\''),
					'get_credit_succeed': 'today\'s credit get√, current coin number:${credit_num}',
					'get_credit_fail'   : 'failed (´-ι_-｀) , have got today\'s coin,current coin number:${credit_num}'
					}
		self.form_data_dict = self.load_form_data(filename='formdata.txt')
		self.credit_url = 'http://emuch.net/bbs/memcp.php?action=getcredit'
		self.log_file = './emuch.log'

#	def log(self, event, **kwargs):
#		file_obj = open('./emuch.log','a')
#		#append new log infomation
#		message_template = Template(self._log_str[event])
#		message = message_template.substitute(kwargs)
#		append_ctnt = self._log_format % (message, '['+time.ctime()+']')
#		file_obj.write(append_ctnt)
#		file_obj.close()

	def post_with_cookie(self):
		"post data with cookie setting, return page string and cookie tuple"
		#get formhash
		url_login = self.url_login
		formhash = self.get_hash_code_BSoup('formhash', url_login)
		#update form_data_dict
		self.add_form_data({'formhash':formhash})
		#set cookie
		cj = cookielib.CookieJar()
		form_data = self.form_data_dict
		try:
			opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
			urllib2.install_opener(opener)
			req=urllib2.Request(url_login,urllib.urlencode(form_data))
			u=urllib2.urlopen(req)
			cookie_list = []
#			for index, cookie in enumerate(cj):
#				print '['+index+']:'+cookie
#				cookie_list.append(cookie)
#			if not cookie_list:
#				print 'Warning : failed to set cookies'
			return u.read(), tuple(cookie_list)
		except:
			print "Ooops! Failed to log in !>_< there may be a problem."
			return

	@staticmethod
	def get_hash_code(tag_name, response):
		hash_regex = r'(<input.+name=")(' + tag_name + r')(" value=")([\d\w]+)(">)'
		m = re.search(hash_regex, response)
		#retrun tag_name, hash_code
		return m.group(2), m.group(4) 

	@staticmethod
	def get_hash_code_BSoup(hash_name, url):
		login_page = urllib.urlopen(url).read()
		login_soup = BeautifulSoup(login_page)
		formhash_tag = login_soup.find('input',attrs = {'name':hash_name})
#		if formhash_tag:
		return formhash_tag['value']
#		else:
#			return

	def log_in(self):
		"""
		Method to pass values by POST 2 times to log in emuch.net,
		return cookie tuple.
		"""
		num1, num2, operation = 0, 0, ''
		qustion_regex = r'(\xce\xca\xcc\xe2\xa3\xba)(\d+)(.+)(\d+)'+\
					r'(\xb5\xc8\xd3\xda\xb6\xe0\xc9\xd9?)'

		while not (num1 and num2 and operation):
			response = self.post_with_cookie()[0]
			match_obj = re.search(qustion_regex, response)
			#get question parts
			try:
				num1, num2, operation = match_obj.group(2), match_obj.group(4),\
												match_obj.group(3)
				#return num1, num2, operation
			except:
				#print "failed to get question"
				#time.sleep(6)
				pass

		#further log in
		#calculate verify question
		#division
		if operation == '\xb3\xfd\xd2\xd4':
			answer = str(int(num1) / int(num2))
		#multiplication
		if operation == '\xb3\xcb\xd2\xd4':
			answer = str(int(num1) * int(num2))

		#get formhash value
		formhash = self.get_hash_code('formhash',response)[1]
		#get post_sec_hash value
		post_sec_hash = self.get_hash_code('post_sec_hash',response)[1]

		#update form_data_dict
		self.add_form_data({'formhash':formhash,
							'post_sec_code':answer,
							'post_sec_hash':post_sec_hash
							})

		#login_response = self.post_with_cookie()
		cookies_tup = self.post_with_cookie()[1]

		return cookies_tup

	def get_credit(self):
		"""get today's credit, 
		if get, return page content, else return None"""
		#get formhash value
		req_1 = urllib2.Request(self.credit_url, 
								urllib.urlencode({'getmode':'1'}))
		response_1 = urllib2.urlopen(req_1).read()
		credit_soup = BeautifulSoup(response_1)
		formhash_tag = credit_soup.find('input',attrs = {'name':'formhash'})
		if formhash_tag:
			formhash = formhash_tag['value']
			#formhash = self.get_hash_code_BSoup('formhash', credit_url)
			credit_form_data = {'getmode':'1', 'creditsubmit':'领取红包'}
			credit_form_data['formhash'] = formhash
			setattr(self, 'credit_form_data', credit_form_data)

			#post values to get credit
			data = urllib.urlencode(credit_form_data)
			req_2 = urllib2.Request(self.credit_url, data)
			response_2 = urllib2.urlopen(req_2).read()
			if response_2:
				credit_num = self.get_credit_number(response_2)
				self.log(event='get_credit_succeed', credit_num=credit_num)

			return response_2
		else:
			#print 'got!'
			credit_num = self.get_credit_number(self.send_post(self.credit_url,self.form_data_dict))
			self.log(event='get_credit_fail', credit_num=credit_num)
			return

	@staticmethod
	def get_credit_number(response):
		regex = r'(<u>\xbd\xf0\xb1\xd2: )(\d\d\.\d)(</u>)'
		m = re.search(regex, response)
		credit_num_str = m.group(2)
		return credit_num_str
