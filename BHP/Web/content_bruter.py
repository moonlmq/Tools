import urllib2
import threading
import Queue
import urllib

threads = 1
target_url = "http://testphp.vulnweb.com"
wordlist_file = "all.txt"
resume = None
user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) " +\
"Gecko/20100101Firefox/19.0"

def build_wordlist(wordlist_file):
	fd = open(wordlist_file,"r")
	raw_words = fd.readlines()
	fd.close()

	found_resume = False

	words = Queue.Queue()

	for word in raw_words:
		word = word.rstrip()

		if resume is not None:
			if found_resume:
				words.put(word)
			else:
				if word == resume:
					found_resume = True
					print "Resuming wordlist from: %s" % resume

		else:
			words.put(word)

	return words

def dir_bruter(word_queue,extensions = None):
	while not word_queue.empty():
		attempt = word_queue.get()

		attempt_list = []

		# check to see if there is a file extension; if not
		# it's a directory path 
		if "." not in attempt:
			attempt_list.append("/%s/" % attempt)
			print attempt_list
		else:
			attempt_list.append("/%s" % attempt)
			print attempt_list

		#if want to bruteforce extensions
		if extensions:
			for extension in extensions:
				attempt_list.append("/%s%s" % (attempt,extension))
				print attempt_list

		#iterate over list of attempts
		for brute in attempt_list:

			url = "%s%s" %(target_url,urllib.quote(brute))

			try:
				headers = {}
				headers["User-Agent"] = user_agent
				r = urllib2.Request(url, headers = headers)

				response = urllib2.urlopen(r)

				if len(response.read()):
					print "[%d] => %s" % (response.code, url)

			except urllib2.URLError,e:

				if hasattr(e,'code') and e.code !=404:
					print "!!! %d => %s" % (e.cde,url)
				pass


word_queue =build_wordlist(wordlist_file)
extensions = [".php",".bak",".orig",".inc"]

for i in range(threads):
	t = threading.Thread(target=dir_bruter,args=(word_queue,extensions,))
	t.start()



