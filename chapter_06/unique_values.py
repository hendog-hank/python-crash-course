favorite_languages = {
    "henry": "python",
    "mike": "java",
    "sarah": "python",
    "alex": "go",
 }

#set() keeps unique values
for language in set(favorite_languages.values()):
    print(language.title())

#set removes duplicates --perfect for: 
#seeing unique countries in a data set
#finding all unique game types
#summarizing survey responses