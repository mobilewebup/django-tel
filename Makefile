PACK = django-tel
CLEAN_ITEMS = \
  $(PACK) \
  $(PACK).tar.gz \
  src/django_tel.egg-info \
  build

test:
	nosetests

clean:
	rm -rf $(CLEAN_ITEMS)
	rm $$(find . -name '*.pyc' -o -name '*~')

pack: clean
	git checkout-index -a --prefix=$(PACK)/
	tar zcf $(PACK).tar.gz $(PACK)
