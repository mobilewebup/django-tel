PACK = django-tel.tar.gz
CLEAN_ITEMS = \
  $(PACK) \
  src/django_tel.egg-info \
  build

test:
	nosetests

clean:
	rm -rf $(CLEAN_ITEMS)

pack:
	git archive --format=tar HEAD | gzip > $(PACK)

