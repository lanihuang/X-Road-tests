CERTIFICATION_SERVICES_TABLE_ID = 'cas'
INTERMEDIATE_CA_TAB_XPATH = '//a[@href="#intermediate_cas_tab"]'
INTERMEDIATE_CA_ADD_BTN_ID = 'intermediate_ca_add'
INTERMEDIATE_CA_CERT_UPLOAD_INPUT_ID = 'ca_cert_file'
INTERMEDIATE_CA_OCSP_TAB_XPATH = '//a[@href="#intermediate_ca_ocsp_responders_tab"]'
INTERMEDIATE_CA_OCSP_ADD_BTN_ID = 'intermediate_ca_ocsp_responder_add'
INTERMEDIATE_CA_BY_NAME_XPATH = '//table[@id="intermediate_cas"]//td[text()="{}"]'
INTERMEDIATE_CA_TR_BY_NAME_XPATH = '//table[@id="intermediate_cas"]//td[text()="{}"]/..'
INTERMEDIATE_CA_DELETE_BTN_ID = 'intermediate_ca_delete'
INTERMEDIATE_CA_TRS_CSS = '#intermediate_cas tbody tr'
INTERMEDIATE_CA_EDIT_BTN_ID = 'intermediate_ca_edit'
INTERMEDIATE_CA_SUBJECT_DN_ID = 'intermediate_ca_cert_subject_dn'
INTERMEDIATE_CA_ISSUER_DN_ID = 'intermediate_ca_cert_issuer_dn'
INTERMEDIATE_CA_VALID_FROM_ID = 'intermediate_ca_cert_valid_from'
INTERMEDIATE_CA_VALID_TO_ID = 'intermediate_ca_cert_valid_to'

DELETE_BTN_ID = 'ca_delete'
ADD_BTN_ID = 'ca_add'
DETAILS_BTN_ID = 'ca_details'
DATE_REGEX = '(\d{4}[-]?\d{1,2}[-]?\d{1,2})'
DATE_TIME_REGEX = '\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'

CA_DETAILS_SUBJECT_DISTINGUISHED = 'top_ca_cert_subject_dn'
CA_DETAILS_ISSUER_DISTINGUISHED = 'top_ca_cert_issuer_dn'
CA_DETAILS_VALID_FROM = 'top_ca_cert_valid_from'
CA_DETAILS_VALID_TO = 'top_ca_cert_valid_to'
CA_DETAILS_VIEW_CERT = 'top_ca_cert_view'
CA_DETAILS_VIEW_CERT_SHA1 = 'cert_details_hash'
CA_DETAILS_VIEW_CERT_DUMP = 'cert_details_dump'

# Timestamp buttons
TSDELETE_BTN_ID = 'tsp_delete'
TSADD_BTN_ID = 'tsp_add'
TSEDIT_BTN_ID = 'tsp_details'

TS_SETTINGS_POPUP = '//div[@aria-describedby="tsp_url_and_cert_dialog"]'
TS_SETTINGS_POPUP_CANCEL_BTN_XPATH = TS_SETTINGS_POPUP + '//div[@class="ui-dialog-buttonset"]//button[span="Cancel"]'

IMPORT_TS_CERT_BTN_ID = 'tsp_cert_button'
SUBMIT_TS_CERT_BTN_ID = 'tsp_url_and_cert_submit'
TIMESTAMP_SERVICES_URL_ID = 'tsp_url'

IMPORT_CA_CERT_BTN_ID = 'ca_cert_button'
ADD_CA_AUTH_ONLY_CHECKBOX_XPATH = '//div[@id="ca_settings_dialog"]//input[@name="authentication_only"]'
EDIT_CA_AUTH_ONLY_CHECKBOX_XPATH = '//div[@id="ca_settings_tab"]//input[@name="authentication_only"]'
CA_SETTINGS_TAB_XPATH = '//li[@aria-controls="ca_settings_tab"]'


SUBMIT_CA_CERT_BTN_ID = 'ca_cert_submit'

# Timestamp view certificate
VIEW_CERTIFICATE = 'tsp_cert_view'

CERTIFICATE_PROFILE_INFO_AREA_CSS = '.cert_profile_info'
ADD_CERTIFICATE_PROFILE_INFO_AREA_XPATH = '//div[@id="ca_settings_dialog"]//input[@name="cert_profile_info"]'
EDIT_CERTIFICATE_PROFILE_INFO_AREA_XPATH = '//div[@id="ca_settings_tab"]//input[@name="cert_profile_info"]'
SUBMIT_CA_SETTINGS_BTN_ID = 'ca_settings_submit'
SAVE_CA_SETTINGS_BTN_ID = 'ca_settings_save'

OCSP_RESPONSE_TAB = '//li[@aria-controls="ocsp_responders_tab"]'
OCSP_RESPONDER_ADD_BTN_ID = 'ocsp_responder_add'
OCSP_RESPONDER_EDIT_BTN_ID = 'ocsp_responder_edit'
OCSP_RESPONDER_DELETE_BTN_ID = 'ocsp_responder_delete'


INTERMEDIATE_CA_TAB = '//li[@aria-controls="intermediate_cas_tab"]'


IMPORT_OCSP_CERT_BTN_ID = 'ocsp_responder_cert_button'
OCSP_RESPONDER_URL_AREA_ID = 'ocsp_responder_url'

SUBMIT_OCSP_CERT_AND_URL_BTN_ID = 'ocsp_responder_url_and_cert_submit'

OCSP_SETTINGS_POPUP = '//div[@aria-describedby="ocsp_responder_url_and_cert_dialog"]'
OCSP_SETTINGS_POPUP_OK_BTN_XPATH = OCSP_SETTINGS_POPUP + '//div[@class="ui-dialog-buttonset"]//button[span="OK"]'
OCSP_SETTINGS_POPUP_CANCEL_BTN_XPATH = OCSP_SETTINGS_POPUP + '//div[@class="ui-dialog-buttonset"]//button[span="Cancel"]'

LAST_ADDED_CERT_XPATH = '//table[@id="cas"]//tbody//tr[last()]'


def get_ca_by_td_text(text):
    return '//table[contains(@id, "cas")]//tr//td[contains(text(), \"' + text + '\")]'


# timestamp id
def ts_get_ca_by_td_text(text):
    return '//table[contains(@id, "tsps")]//tr//td[contains(text(), \"' + text + '\")]'


def get_ocsp_by_td_text(text):
    return '//table[contains(@id, "ocsp_responders")]//tr//td[contains(text(), \"' + text + '\")]'


def get_ocsp_responders(self):
    responders = self.by_xpath(
        '(//table[contains(@id, "ocsp_responders")]//tr//td[1])[not(contains(@class,"dataTables_empty"))]',
        multiple=True)
    result = []
    for responder in responders:
        result.append(responder.text)

    return result
