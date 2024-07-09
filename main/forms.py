from django import forms
from .models import Report_view, OPO, TU, Certificate


class FilterForm(forms.Form):
    # Получаем список уникальных значений поля 'naimenovanie_strukturnogo_podrazdeleniya'
    choices_list = Report_view.objects.values_list('naimenovanie_strukturnogo_podrazdeleniya',
                                                   flat=True).distinct().order_by(
        'naimenovanie_strukturnogo_podrazdeleniya')
    # Преобразуем в список кортежей для ChoiceField
    choices = [(choice, choice) for choice in choices_list]

    naimenovanie_strukturnogo_podrazdeleniya = forms.ChoiceField(
        choices=[('', 'Выберите подразделение')] + choices,
        label='Подразделение',
        required=False
    )

    cb_onControl = forms.BooleanField(label='ТУ на контроле', required=False)


class ReportViewForm(forms.ModelForm):
    naimenovanie_tipa_opo = forms.CharField(max_length=255, label='Наименование типа ОПО')
    registracionniy_nomer_opo = forms.CharField(max_length=255, label='Регистрационный номер ОПО')
    naimenovanie_strukturnogo_podrazdeleniya = forms.CharField(max_length=255,
                                                               label='Наименование структурного подразделения')
    kratkoe_naimenovanie_tipa_opo = forms.CharField(max_length=255, label='Краткое наименование типа ОПО')

    certificate_type = forms.CharField(widget=forms.Textarea, label='Тип сертификата')
    certificate_number = forms.CharField(widget=forms.Textarea, label='Номер сертификата')
    certificate_expiration_date = forms.CharField(widget=forms.Textarea, label='Дата истечения сертификата')

    class Meta:
        model = TU
        fields = [
            'naimenovanie_tipa_opo',
            'registracionniy_nomer_opo',
            'naimenovanie_strukturnogo_podrazdeleniya',
            'kratkoe_naimenovanie_tipa_opo',
            'registr_nomer_oborudovaniya_tu',
            'seriyniy_nomer_tu',
            'gos_registracionniy_nomer',
            'zavodskoy_nomer',
            'marka_tu',
            'kratkie_tehn_haract_tu',
            'registr_nomer_gtt',
            'nomer_tu_po_tehn_sheme',
            'god_izgotovleniya',
            'norm_srok_ekspluat_let',
            'god_vvoda_v_ekspluat',
            'god_okonchaniya_ekspluat',
            'procent_iznosa',
            'data_posl_epb',
            'data_sled_epb',
            'data_ocherednoy_proverki',
            'data_sled_proverki',
            'razresh_srok_ekspluat',
            'nalichie_predohr_ustroystva',
            'tip_predohr_ustr',
            'obyom_m3',
            'object_davlenie_mpa',
            'dy_mm',
            'tip',
            'podtip',
            'gruzopodyomnost_t',
            'obyom_t',
            'oborudovanie_davlenie_mpa',
            'god_modernizacii',
            'provedennie_meropriyatiya',
            'nomer_razresheniya_rtn',
            'nomer_zaklyucheniya_epb',
            'nalichie_pasporta_tu',
            'inf_tu_svedeniya_opo',
            'inf_tu_rtn',
            'nalichie_sertificata_sootvetstviya',
            'nalichie_sertificata_rtn',
            'primechanie',
            'id_opo',
            'id_classa_opasnosti',
            'id_zavod_izgotovitel',
            'id_vid_tu',
            'id_tip_tu',
            'id_naimenovanie_tu',
            'id_tu',
            'id_rtn',
            'strana_proizvoditel',
            'vivod_epb',
            'kol_ciklov',
            'kol_ciklov_fact',
            'id_nalichie_sr_kontr',
            'id_tu_zamen',
            'nn_tu_zamen',
            'id_vid_tu_j',
            'id_tip_tu_j',
            'cb_oncontrol',
            'primechanie2',
            'primechanie3',
            'zavod_izgotovitel_txt',
            'date_upd',
            'login_upd',
            'isdeleted',
        ]
        labels = {
            'registr_nomer_oborudovaniya_tu': 'Регистрационный номер оборудования ТУ',
            'seriyniy_nomer_tu': 'Серийный номер ТУ',
            'gos_registracionniy_nomer': 'Государственный регистрационный номер',
            'zavodskoy_nomer': 'Заводской номер',
            'marka_tu': 'Марка ТУ',
            'kratkie_tehn_haract_tu': 'Краткие технические характеристики ТУ',
            'registr_nomer_gtt': 'Регистрационный номер ГТТ',
            'nomer_tu_po_tehn_sheme': 'Номер ТУ по технической схеме',
            'god_izgotovleniya': 'Год изготовления',
            'norm_srok_ekspluat_let': 'Нормативный срок эксплуатации (лет)',
            'god_vvoda_v_ekspluat': 'Год ввода в эксплуатацию',
            'god_okonchaniya_ekspluat': 'Год окончания эксплуатации',
            'procent_iznosa': 'Процент износа',
            'data_posl_epb': 'Дата последней проверки безопасности',
            'data_sled_epb': 'Дата следующей проверки безопасности',
            'data_ocherednoy_proverki': 'Дата очередной проверки',
            'data_sled_proverki': 'Дата следующей проверки',
            'razresh_srok_ekspluat': 'Разрешенный срок эксплуатации (лет)',
            'nalichie_predohr_ustroystva': 'Наличие предохранительного устройства',
            'tip_predohr_ustr': 'Тип предохранительного устройства',
            'obyom_m3': 'Объем, м³',
            'object_davlenie_mpa': 'Давление на объекте, МПа',
            'dy_mm': 'Диаметр трубы, мм',
            'tip': 'Тип',
            'podtip': 'Подтип',
            'gruzopodyomnost_t': 'Грузоподъемность, т',
            'obyom_t': 'Объем, т',
            'oborudovanie_davlenie_mpa': 'Давление оборудования, МПа',
            'god_modernizacii': 'Год модернизации',
            'provedennie_meropriyatiya': 'Проведенные мероприятия',
            'nomer_razresheniya_rtn': 'Номер разрешения РТН',
            'nomer_zaklyucheniya_epb': 'Номер заключения по безопасности',
            'nalichie_pasporta_tu': 'Наличие паспорта ТУ',
            'inf_tu_svedeniya_opo': 'Информация по ТУ (сведения ОПО)',
            'inf_tu_rtn': 'Информация по ТУ (РТН)',
            'nalichie_sertificata_sootvetstviya': 'Наличие сертификата соответствия',
            'nalichie_sertificata_rtn': 'Наличие сертификата РТН',
            'primechanie': 'Примечание',
            'id_opo': 'ID ОПО',
            'id_classa_opasnosti': 'ID класса опасности',
            'id_zavod_izgotovitel': 'ID завода изготовителя',
            'id_vid_tu': 'ID вида ТУ',
            'id_tip_tu': 'ID типа ТУ',
            'id_naimenovanie_tu': 'ID наименования ТУ',
            'id_tu': 'ID ТУ',
            'id_rtn': 'ID РТН',
            'strana_proizvoditel': 'Страна производитель',
            'vivod_epb': 'Вывод ЕПБ',
            'kol_ciklov': 'Количество циклов',
            'kol_ciklov_fact': 'Фактическое количество циклов',
            'id_nalichie_sr_kontr': 'ID наличия СР и контроля',
            'id_tu_zamen': 'ID ТУ замен',
            'nn_tu_zamen': 'NN ТУ замен',
            'id_vid_tu_j': 'ID вида ТУ (J)',
            'id_tip_tu_j': 'ID типа ТУ (J)',
            'cb_oncontrol': 'CB onControl',
            'primechanie2': 'Примечание 2',
            'primechanie3': 'Примечание 3',
            'zavod_izgotovitel_txt': 'Завод изготовитель (текст)',
            'date_upd': 'Дата обновления',
            'login_upd': 'Логин обновления',
            'isdeleted': 'Выведено из эксплуатации',
        }


class DeleteConfirmForm(forms.Form):
    confirm = forms.BooleanField(label='Подтвердите удаление', required=True)


class TUForm(forms.ModelForm):
    class Meta:
        model = TU
        fields = '__all__'


class OPOForm(forms.ModelForm):
    class Meta:
        model = OPO
        fields = '__all__'


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = '__all__'
