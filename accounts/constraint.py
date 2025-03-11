BLOOD_GROUP = [ 
    ("A+","A+"),
    ("A-","A-"), 
    ("B+","B+"),
    ("B-","B-"),
    ("AB+","AB+"),
    ("AB-","AB-"), 
    ("O+","O+"),
    ("O-","O-"), 
]

GENDER = [
    ('Male','Male'),
    ('Female','Female')
]
COUNTRY = [
    ('Bangladesh','Banglades'),
]



# # utils.py
# import requests
# from django.core.cache import cache

# def fetch_divisions_from_api():
#     # Check if divisions are already cached
#     cached_divisions = cache.get('divisions')
#     if cached_divisions:
#         return cached_divisions

#     # If not cached, make a request to the API
#     url = 'https://bdapi.vercel.app/api/v.1/district'
#     response = requests.get(url)
#     divisions = []

#     if response.status_code == 200:
#         divisions_data = response.json()
#         divisions = [(division, division) for division in divisions_data]

#         # Cache the divisions for 1 hour
#         cache.set('divisions', divisions, timeout=3600)

#     return divisions
