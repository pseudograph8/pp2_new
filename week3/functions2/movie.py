movies = [ {
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
} ]

'''Write a function that takes a single movie and returns True if its IMDB score is above 5.5

Write a function that returns a sublist of movies with an IMDB score above 5.5.

Write a function that takes a category name and returns just those movies under that category.

Write a function that takes a list of movies and computes the average IMDB score.

Write a function that takes a category and computes the average IMDB score.'''

#1
def func1(movie):
    if movie["imdb"]>5.5:
        return True
    return False

print(func1(movies[0]))

#2
def func2(list_of_movies):
    sublist = []
    for i in range(len(list_of_movies)):
        if list_of_movies[i]['imdb']>5.5:
            sublist.append(list_of_movies[i])
    return sublist

print(func2(movies))

#3
def category(genre, movies):
    sublist = []
    for i in range(len(movies)):
        if movies[i]["category"] == genre:
            sublist.append(movies[i])
    return sublist

c = input()
print(category(c, movies))

#4
def average(list_of_movies):
    overall = 0
    for i in range(len(list_of_movies)):
        overall = overall + list_of_movies[i]['imdb']

    ave = overall/len(list_of_movies)
    return ave

print(average(movies))


#5
def category(genre, movies):
    sublist = []
    for i in range(len(movies)):
        if movies[i]["category"] == genre:
            sublist.append(movies[i])
    overall = 0
    for i in range(len(sublist)):
        overall = overall + sublist[i]['imdb']

    ave = overall/len(sublist)
    return ave

c = input()
print(category(c, movies))
'''
for i in range(len(movies)):
    print(movies[i])
'''
