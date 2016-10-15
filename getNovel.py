import urllib2
from pyquery import PyQuery as pq

def main():
	f = open("nanfengruwohuai.txt",'w')
	for i in range(1,78):
		url = "http://www.sto.cc/149054-" + str(i) + "/"
		response = urllib2.urlopen(url)
		html = response.read()
		content = pq(html).find('#BookContent')
		detail = content.contents()
		text = ""
		for c in detail:
			if type(c)==type(detail[2]):
				text += c + '\n'
		f.write(text.encode('utf8'))
	f.close()

if __name__ == "__main__":
	main()
