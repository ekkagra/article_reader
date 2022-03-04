import argparse
import requests
import markdownify
from bs4 import BeautifulSoup
import os
import webbrowser

def convert_to_markdown(link, **kwargs):
	req = requests.get(link)
	soup = BeautifulSoup(req.text, 'lxml')
	if kwargs:
		ht = str(soup.find(**kwargs))
	else:
		ht = str(soup.find("body"))
	h = markdownify.markdownify(ht, heading_style="ATX")
	file_name = os.path.basename(link).replace("-","_").replace(" ","_") + ".md"
	print(os.path.abspath(file_name))
	with open(file_name,"w", errors="replace") as f:
		f.write(h)
	webbrowser.open(os.path.abspath(file_name), new=2)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--link")
	args = parser.parse_known_args()
	keywords = [ele for ele in args[1] if ele.startswith("--")]
	parser2 = argparse.ArgumentParser()
	for ele in keywords:
		parser2.add_argument(ele)
	kwargs = parser2.parse_args(args[1])
	convert_to_markdown(args[0].link, **vars(kwargs))