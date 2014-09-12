abase.sql - MySQL dump for fast creation of DB for the articles info

scan.py - script for visiting web-pages, parsing them and getting names of authors

collect_info_for_lda.py - reads the file logdile.txt and gets authors names and their publications

sample.py - main script, when being called as script calls computing function for a "text"

logfile.txt - results of scannong all known from DB webpages

authors.list - serialized author and all text tokens list

hse_model.lda - serialized tfid lda model for eliminationg building it online

hse_model.lda.state			|DO NOT REMOVE
sample.mm.index 			|service files

sample.mm - serialized mmCorpus

sample.dict - serialized corpora.Dictionaty for lda model