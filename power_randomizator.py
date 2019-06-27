import random

import random
import time
from operator import itemgetter


def score(slide1, slide2):
    diff_tags = slide1.difference(slide2)
    intersection_tags = slide1.intersection(slide2)
    diff2_tags = slide2.difference(intersection_tags)
    return min(map(lambda x: len(x), [diff_tags, diff2_tags, intersection_tags]))


# Input
numPhotos = int(input())

photos_orig = []

for i in range(numPhotos):
    name, tags = input().split('|')
    tags = set(tags.split(" "))

    photos_orig.append({'name': name, 'tags': tags})

best_show = []
best_score = 0

start = time.time()
while time.time() - start < 2300:
    total_score = 0

    photos = list(photos_orig)
    current_id = random.randint(0, len(photos) - 1)
    current = photos[current_id]
    photos.pop(current_id)

    slideshow = [current]

    while photos:
        nxt = random.randint(0, len(photos) - 1)
        slideshow.append(photos[nxt])
        total_score += score(current['tags'], photos[nxt]['tags'])
        current_id = nxt
        current = photos[current_id]
        photos.pop(nxt)

    if total_score > best_score:
        best_show = list(slideshow)

# Output
numSlidesInSlideshow = len(best_show)
print(numSlidesInSlideshow)

for slide in best_show:
    print(slide['name'])
