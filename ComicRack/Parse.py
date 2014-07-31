import re
def ParseComicPath (path, proposed):
	splitpath = path.split('\\')
	dirname = splitpath[len(splitpath) - 2]
	filename = splitpath[len(splitpath) - 1]
	
	proposed.Series = dirname
		
	string = filename
	
	expr1 = re.compile("^([0-9]+|HS[0-9]?|INT[0-9]?|OS)( - .*)\\.cbz")

	expr2 = re.compile("^[0-9]+\\.cbz")
	
	expr3   = re.compile("^.* (V[0-9]+ )?#([0-9]+(\\.[0-9])?|HS[0-9]?|INT[0-9]?|OS|One [Ss]hot) (\\(of [0-9]+\\) )?\\([0-9]+\\)\\.cbz")
	expr3s  = re.compile("(V[0-9]+ )?#([0-9]+(\\.[0-9])?|HS[0-9]?|INT[0-9]?|OS|One [Ss]hot) (\\(of [0-9]+\\) )?\\([0-9]+\\)\\.cbz")
	expr3of = re.compile("\\(of [0-9]+\\)")
	expr3y  = re.compile("\\([0-9]+\\)")
	
	# First format : Serie/01 - Title.cbz
	if(expr1.match(string)):
		split = string.split('-', 1)
		
		num = split[0].lstrip().rstrip()
		title = split[1][:-4].lstrip().rstrip()
		
		proposed.Title = title
		
		if(num != "OS"):
			proposed.Number = num
		else:
			proposed.Series = title
			proposed.Number = ""
	
	# Second format : Serie/01.cbz
	elif(expr2.match(string)):
		num = string[:-4]
		proposed.Number = num
		
	elif(expr3.match(string)):
		firstChar = expr3s.search(string).span()[0]
		title = string[0:firstChar].lstrip().rstrip()
		print title
		
		data = expr3s.search(string).group(0)
		print data
		result = re.split(r"\s+(?=[^()]*(?:\(|$))", data)
		print result
		
		for elt in result:
		# Volume (facultatif)
			if elt[0] == 'V':
				volume = elt[1:len(elt)]
				proposed.Volume = int(volume)
				continue
			
		# Issue (obligatoire sauf pour OS)
			if elt[0] == '#':
				issue = elt[1:len(elt)]
				if issue == "One" or issue == "OS":
					issue = ""
					proposed.Number = ""
					proposed.Title = title
					proposed.Series = title
					
				continue
		
		# Max issue (facultatif)
			if expr3of.match(elt):
				maxvol = re.search("[0-9]+", elt).group(0)
				
				proposed.Count = int(maxvol)
				continue
		
		# Annee (obligatoire)
			if expr3y.match(elt):
				year = re.search("[0-9]+", elt).group(0)
				proposed.Year = int(year)
				continue
