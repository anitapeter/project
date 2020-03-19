from tagList import Tags
tags = Tags['common']
def getTags(list_of_keywords):
	

	key = list_of_keywords
	for tag in Tags[key]:
		tags.append(tag)

	return list(set(tags))

def hashes(list_of_tags):
	hashTagString = ""

	for tag in list_of_tags:
	 hashTagString += " #" + tag

	return hashTagString

if __name__ == '__main__':
  import sys
  with open ("result.txt", "r") as fileHandler: 
    for line in fileHandler:
      for word in line.split():
        getTags(word)
  print(hashes(tags))
