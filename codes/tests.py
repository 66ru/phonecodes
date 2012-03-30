# -*- coding: utf-8 -*-
import json
from django.test.client import Client as HTTPClient
from django.utils import unittest
from models import Operator
from utils.exceptions import *

class GetOperatorTestCase(unittest.TestCase):
    def setUp(self):
        self.client = HTTPClient()
        Operator(
            name=u"МагаданТелеком",
            region_code=560,
            number_start_range=2000000,
            number_end_range=3999999,
            mobile=False,
            region=u"Магадан"
        ).save()
        Operator(
            name=u"КроссТелеком",
            region_code=530,
            number_start_range=1000000,
            number_end_range=1999999,
            mobile=True,
            region=u"Владивосток"
        ).save()
        Operator(
            name=u"Магаданские Телесистемы",
            region_code=560,
            number_start_range=4000000,
            number_end_range=8999999,
            mobile=False,
            region=u"Магадан"
        ).save()

    def tearDown(self):
        Operator.objects.all().delete()

    def test_get_operator_ok(self):
        resp = self.client.post('/', {'phone': '85602234567'})
        self.assertEqual(resp.status_code, 200)
        json_resp = json.loads(resp.content)
        self.assertEqual(json_resp['operator'], u'МагаданТелеком')
        self.assertEqual(json_resp['mobile'], False)
        self.assertEqual(json_resp['region'], u'Магадан')

        resp = self.client.get('/', {'phone': '+7 (530) 123-45-67'})
        self.assertEqual(resp.status_code, 200)
        json_resp = json.loads(resp.content)
        self.assertEqual(json_resp['operator'], u'КроссТелеком')
        self.assertEqual(json_resp['mobile'], True)
        self.assertEqual(json_resp['region'], u'Владивосток')

        resp = self.client.get('/', {'phone': '8-560-5-23-45-67'})
        self.assertEqual(resp.status_code, 200)
        json_resp = json.loads(resp.content)
        self.assertEqual(json_resp['operator'], u'Магаданские Телесистемы')
        self.assertEqual(json_resp['mobile'], False)
        self.assertEqual(json_resp['region'], u'Магадан')

    def test_get_operator_fail(self):
        resp = self.client.post('/', {'phone': '85609080808'})
        self.assertEqual(resp.status_code, 200)
        json_resp = json.loads(resp.content)
        self.assertEqual(json_resp['status'], 1)
        self.assertEqual(json_resp['message'], OperatorNotFoundException.msg)

        resp = self.client.post('/', {'phone': '85601080808'})
        self.assertEqual(resp.status_code, 200)
        json_resp = json.loads(resp.content)
        self.assertEqual(json_resp['status'], 1)
        self.assertEqual(json_resp['message'], OperatorNotFoundException.msg)

    def test_wrong_number(self):
        resp = self.client.post('/', {'phone': '85601080808879475230345'})
        self.assertEqual(resp.status_code, 200)
        json_resp = json.loads(resp.content)
        self.assertEqual(json_resp['status'], 1)
        self.assertEqual(json_resp['message'], InvalidNumberException.msg)

        resp = self.client.post('/', {'phone': 'PhoneNumber'})
        self.assertEqual(resp.status_code, 200)
        json_resp = json.loads(resp.content)
        self.assertEqual(json_resp['status'], 1)
        self.assertEqual(json_resp['message'], InvalidNumberException.msg)