CLEAN_ITEMS = \
  src/django_tel.egg-info \
  build

test:
	nosetests
clean:
	rm -rf $(CLEAN_ITEMS)
