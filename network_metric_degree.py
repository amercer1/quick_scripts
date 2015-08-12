from __future__ import division
from collections import Counter, defaultdict

def users_print():
  for user in users:
    print(user)

def number_of_friends(user):
  return len(user["friends"])

def friends_of_friend_ids_bad(user):
  # "foaf" is short for friend of friend
  return [x["id"] for y in user["friends"] for x in y["friends"]] 

def not_the_same(user, other_user):
  """two users are not the same if they have different id"""
  return user["id"] is not other_user["id"]

def not_friends(user, other_user):
  """other_user is not a friend if he's not in user["friends"];
  that is, if he's not_the_same as all the people in the user["friends"]"""

  return all(not_the_same(friend, other_user) for friend in user["friends"])

def friends_of_friend_ids(user):
  return Counter(foaf["id"]
                 for friend in user["friends"]  # for each of my friends
                 for foaf in friend["friends"]  # count "their" friends
                 if not_the_same(user, foaf)    # who are not me
                 and not_friends(user, foaf))   # and aren't my friends

def data_scientists_who_like(target_interest):
  return [user_id
          for user_id, user_interest in interests
          if user_interest == target_interest] 

def most_common_interests_with(user):
  return Counter(interested_user_id
      for interest in interests_by_user_id[user["id"]]
      for interested_user_id in user_ids_by_interest[interest]
      if interested_user_id != user["id"])

users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

friendships = [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4),
               (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)] 


interests = [
       (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
       (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
       (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
       (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
       (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
       (3, "statistics"), (3, "regression"), (3, "probability"),
       (4, "machine learning"), (4, "regression"), (4, "decision trees"),
       (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
       (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
       (6, "probability"), (6, "mathematics"), (6, "theory"),
       (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
       (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
       (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
       (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

for user in users:
  user["friends"] = []

for x, y in friendships:
  users[x]["friends"].append(users[y])
  users[y]["friends"].append(users[x])

"""how many total connections are there"""
total_connections = sum(number_of_friends(user) for user in users)
print(total_connections)                                              #24

"""what is the average connections among users"""
avg_connections = total_connections / len(users)
print(avg_connections)                                                #2.4

"""find the most connected people"""
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users] #[(0, 2), (1, 3), (2, 3), (3, 3), (4, 2), (5, 3), (6, 2), (7, 2), (8, 3), (9, 1)]


num_friends_by_id_sorted = sorted(num_friends_by_id, 
                                  key=lambda x: x[1],
                                  reverse=True)

# keys are interest, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)



print(num_friends_by_id_sorted)  #[(1, 3), (2, 3), (3, 3), (5, 3), (8, 3), (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)] 
print(friends_of_friend_ids_bad(users[0]))
print(not_the_same(users[0],users[0]))
print(not_friends(users[0], users[4]))
print(friends_of_friend_ids(users[3]))
print(most_common_interests_with(users[0]))
