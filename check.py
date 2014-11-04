import shelve

d = shelve.open('authors.list')

print d['uri2author']