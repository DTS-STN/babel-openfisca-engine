clean:
	rm -rf build dist
	find . -name '*.pyc' -exec rm \{\} \;

build-run-dev:
	docker-compose up --build --detach --force-recreate

test:
	docker exec openfisca_dev_babel openfisca test -c openfisca_canada_babel openfisca_canada_babel/tests
