import functools
import random
import sys
from operator import itemgetter


def sort(photos):
    return list(sorted(photos, key=lambda photo: len(photo['tags'])))


def score(slide1, slide2):
    slide1, slide2 = set(slide1), set(slide2)
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

photos = sort(photos)

current_id = random.randint(0, len(photos) - 1)
current = photos[current_id]
photos.pop(current_id)

slideshow = [current]

while photos:
    this_tags = current['tags']
    next_tags = max(((i, score(this_tags, photos[i]['tags'])) for i in range(len(photos))),
                    key=itemgetter(1))

    print(next_tags)

    slideshow.append(photos[next_tags[0]])
    current = photos[next_tags[0]]
    photos.pop(next_tags[0])
    if len(photos) % 1000 == 0:
        print(len(photos), file=sys.stderr)

# Output
numSlidesInSlideshow = len(slideshow)
print(numSlidesInSlideshow)

for slide in slideshow:
    print(slide['name'])
