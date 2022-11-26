from django.test import TestCase
from lending_site.service import (
    get_queryset_company,
    get_queryset_vacancy,
    )


class ServiceTestCase():
    def test_gqc(self):
        print(get_queryset_company)

    def test_gqv(self):
        print(get_queryset_vacancy.name)