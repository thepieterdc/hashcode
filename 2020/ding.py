from collections import Counter
from sys import stdout, stderr


class Library:
    def __init__(self, books_in_j, num_days_finish_libary_j, books_shipped_per_day, i, book_ids):
        self.books_in_j = books_in_j
        self.opstarttijd = num_days_finish_libary_j
        self.books_shipped_per_day = books_shipped_per_day
        self.i = i
        self.book_ids = list(book_ids)
        self.book_ids.sort(key=lambda i:book_scores[i],reverse = True)
        self.possscore = sum(book_scores[b] for b in book_ids)

    def update(self,datesleft,books):
        for b in books:
            if b in self.book_ids:
                self.book_ids.remove(b)
        n = min(len(self.book_ids), (datesleft-self.opstarttijd) * self.books_shipped_per_day)
        self.possscore = sum(book_scores[b] for b in self.book_ids[:n])



num_books, num_libraries, num_days = tuple(map(int, input().split(" ")))
book_scores = list(map(int, input().split(" ")))

libraries = list()
library_book_1 = list()
for library in range(num_libraries):
    books_in_j, num_days_finish_libary_j, num_books_shipped_from_j_per_day = tuple(map(int, input().split(" ")))
    book_ids = tuple(map(int, input().split(" ")))
    library_book_1.append(book_ids[0])
    libraries.append(Library(books_in_j, num_days_finish_libary_j, num_books_shipped_from_j_per_day, library, book_ids))


library_scores = list(libraries)

tijd = num_days
printtijd = tijd
libraries.sort(key=lambda l: l.opstarttijd)
while tijd > 0:
    if tijd/100 < printtijd:
        printtijd -= 100
        print(printtijd,file=stderr,flush=True)
    minlibrary = max(libraries,key=lambda l:l.possscore / l.opstarttijd)

    libraries.remove(minlibrary)

    books = minlibrary.book_ids
    libraries = list(filter(lambda l:l.possscore>0 ,libraries))

    tijd -= minlibrary.opstarttijd

    for l in libraries:
        l.update(tijd,books)

    print(f"{minlibrary.i} {len(minlibrary.book_ids)}")
    print(" ".join(map(str,minlibrary.book_ids)))


# print()
# #
# print(f"numbooks: {num_books}")
# print(f"num_libraries: {num_libraries}")
# s = [len(l.book_ids) for l in libraries]
# print(f"max,avg,min {max(s)} {sum(s)/len(s)} {min(s)}")
# print(f"avgbookoccurence {sum(s)/num_books}")
#
# dagennodigtotaal = [l.num_days_finish_library_j + l.books_in_j/l.books_shipped_per_day for l in libraries]
# dagennodigopstart = [l.num_days_finish_library_j for l in libraries]
# print(num_days)
# print("max,avg,min dagen nodig totaal:", max(dagennodigtotaal),sum(dagennodigtotaal)/len(dagennodigtotaal), min(dagennodigtotaal))
# # print("max,avg,min dagen nodig opstart:", max(dagennodigopstart),sum(dagennodigopstart)/len(dagennodigopstart), min(dagennodigopstart))
# #
# print("max,avg,min boekscores",max(book_scores),sum(book_scores)/len(book_scores), min(book_scores))

# print(num_libraries)
# for l in sorted(libraries, key=lambda li: li.num_days_finish_library_j):
#     print(f"{l.i} {l.books_in_j}")
#     print(" ".join(map(str, l.book_ids)))
