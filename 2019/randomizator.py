import random

import random
from operator import itemgetter


def score(slide1, slide2):
    diff_tags = slide1.difference(slide2)
    intersection_tags = slide1.intersection(slide2)
    diff2_tags = slide2.difference(intersection_tags)
    return min(map(lambda x: len(x), [diff_tags, diff2_tags, intersection_tags]))


# Input
numPhotos = int(input())

photos = []

for i in range(numPhotos):
    name, tags = input().split('|')
    tags = set(tags.split(" "))

    photos.append({'name': name, 'tags': tags})

current_id = random.randint(0, len(photos) - 1)
current = photos[current_id]
photos.pop(current_id)

slideshow = [current]

while photos:
    nxt = random.randint(0, len(photos) - 1)
    slideshow.append(photos[nxt])
    photos.pop(nxt)

# Output
numSlidesInSlideshow = len(slideshow)
print(numSlidesInSlideshow)

for slide in slideshow:
    print(slide['name'])
