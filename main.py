import diffbot as df
import randomnews as rn

def main():
	article = rn.get_articles('politics', True)
	text = df.retrieve_from_url(article[0], df.get_token())
	
	print(article[1], text, article[2])


if __name__ == "__main__":
	main()
	
