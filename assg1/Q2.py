'''
print output in given format
'''

title = input("Enter the movie title: ")
director = input("Enter the director's name: ")
release_year = int(input("Enter the release year: "))

output = f"{title} ({release_year}), directed by {director}"
print(output)