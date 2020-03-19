from tagList import Tags

def getTags(list_of_keywords):
	tags = Tags['common']

	for key in list_of_keywords:
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
  with open ("detected.txt", "r") as fileHandler: 
    for line in fileHandler:
      print(line.strip())
      print (hashes(getTags(line)))
