from django.test import TestCase
from lending_site.service import (
    get_context,
)
from lending_site.models import (
    Company,
    Contacts,
    Vacancy,
)


class ServiceTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.c_name = 'text'
        cls.c_description = 'text'
        cls.c_image = 'default.jpg'
        cls.name = 'Test2'
        cls.v_description = 'Testing2'
        cls.salary = '300'
        cls.activated = True
        cls.pk = 1
        cls.data = {"full_name": 'x', "phone": '34343',
                    "email": 'mr@mail.ru', "comment": 'sfssfsf', "file": 'files.docx'}
        cls.con_title = 'ssss'
        cls.con_phone = '9529529592'
        cls.con_email = 'mmmmm@gmail.com'
        cls.adress = 'Mk-rn Orbit'

        Company.objects.create(
            name=cls.c_name,
            description=cls.c_description,
            image=cls.c_image,
        )

        Contacts.objects.create(
            contact_id=cls.pk,
            title=cls.con_title,
            phone=cls.con_phone,
            email=cls.con_email,
            adress=cls.adress
        )

        Vacancy.objects.create(
            id=cls.pk,
            name=cls.name,
            salary=cls.salary,
            description=cls.v_description,
            activated=cls.activated
        )

    def test_views_get(self):
        data = get_context()
        response = self.client.get('', data)
        resp_status = response.status_code
        self.assertEqual(resp_status, 200)

    def test_views_post(self):
        save_dict = {"saved": True}
        context = get_context() | save_dict
        response = self.client.post('', data=context)
        resp_status = response.status_code
        self.assertEqual(resp_status, 200)
