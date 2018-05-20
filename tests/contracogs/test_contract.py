import pendulum
import pytest
from django.test import RequestFactory
from mixer.backend.django import mixer

'''
pytestmark = pytest.mark.django_db

from friend_app import forms


def get_contract_form(seller_name='seller_name',
                      country='ID',
                      date_start='12/12/2017',
                      date_end='12/13/2017',
                      brand,
                      seller_contact_name,
                      seller_contact_email,
                      currency,
                      contract_level,
                      contract_type,
                      lump_sum_amount,
                      agreement_type,
                      payment_schedule,
                      start_date,
                      end_date,
                      payment_date,
                      payment_method,
                      backmargin_unit_type,
                      base_price_type,
                      cap_total_item,
                      cap_total_value,
                      quantity_final_backmargin,
                      final_backmargin,
                      actual_backmargin,
                      backmargin_l1_fixed_amount,
                      backmargin_l2_fixed_amount,
                      backmargin_l3_fixed_amount,
                      backmargin_l1_fixed_percentage,
                      backmargin_l2_fixed_percentage,
                      backmargin_l3_fixed_percentage,
                      target_l1_number_item,
                      target_l2_number_item,
                      target_l3_number_item,
                      target_l1_value,
                      target_l2_value,
                      target_l3_value,
                      allocation_start_datetime,
                      allocation_end_datetime,
                      allocation_backmargin_per_unit_contract,
                      multi_payment_start_datetime,
                      multi_payment_end_datetime
                      ):

    return forms.CampaignForm({
        "seller_name": seller_name,
        "country": country,
        "campaign_group": '1',
        "date_start": date_start,
        "date_end": date_end,
        "date_archive": date_archive,
    })


class TestOneTimePaymentContract:
'''


class TestMonthlyPaymentContract:

    def test_multiple_contract_creation_with_monthly_payment(self):
        pass

    def test_wrong_date_insert_to_create_monthly_payment(self):
        pass

    def test_multiple_contract_creation_with_quarterly_payment(self):
        pass

    def test_wrong_date_insert_to_create_quarterly_payment(self):
        pass

    def test_number_of_contracts_created_with_given_date(self):
        pass

    def test_cloned_contract_field_info(self):
        pass

    def test_edit_cloned_contract_field_info(self):
        pass
