from django.test import TestCase
from lending_site.service import (
    get_queryset_company,
    get_queryset_vacancy,
    get_context,
    save_applicants
    )
from lending_site.models import (
    Company,
    Contacts,
    Vacancy,
    Applicants
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
        cls.data = {"full_name":'x',"phone":'34343',"email":'mr@mail.ru',"comment":'sfssfsf',"file":'files.docx'}
        cls.con_title = 'ssss'
        cls.con_phone = '9529529592'
        cls.con_email = 'mmmmm@gmail.com'
        cls.adress = 'Mk-rn Orbit'

        Company.objects.create(
            name=cls.c_name,
            description= cls.c_description,
            image = cls.c_image,
        )

        Contacts.objects.create(
            contact_id = cls.pk,
            title = cls.con_title,
            phone = cls.con_phone,
            email = cls.con_email,
            adress = cls.adress
        )


        Vacancy.objects.create(
            id = cls.pk,
            name = cls.name,
            salary = cls.salary,
            description = cls.v_description,
            activated = cls.activated
        )


    def test_views_get(self):
        data = get_context()
        response = self.client.get('',data)
        resp_status = response.status_code
        self.assertEqual(resp_status,200)

    def test_views_post(self):
        save_dict = {"saved":True}
        context = get_context() | save_dict
        response = self.client.post('',data=context)
        resp_status = response.status_code
        self.assertEqual(resp_status,200)

        

    def test_cquery_is_true(self):
        valid_dict = {
          "name": self.c_name,
          "description": self.c_description,
          "image": self.c_image
        }
        invalid_dict = {
            "description": self.c_description,
            "image": 'pnx',
            "name": self.c_name,
        }
        company_queryset = get_queryset_company()
        self.assertEqual(valid_dict, company_queryset, msg=company_queryset)
        self.assertNotEqual(company_queryset, invalid_dict, msg=company_queryset)


    def test_vquery_is_true(self):
        valid_dict = {
            'id':self.pk,
            'name':self.v_name,
            'salary':self.salary,
            'description':self.v_description,
        }
        invalid_dict = {
            'name':self.v_name,
            'id':2,
            'salary':self.salary,
            'description':self.v_description,
        }
        vacancy_queryset = get_queryset_vacancy()
        print(vacancy_queryset)
        self.assertEqual(vacancy_queryset, valid_dict, msg=vacancy_queryset)
        self.assertNotEqual(vacancy_queryset, invalid_dict, msg=vacancy_queryset)



    
