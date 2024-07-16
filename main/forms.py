from django import forms
from .models import Report_view, OPO, TU, Certificate, NameTU, Setup


class FilterForm(forms.Form):
    choices_list = Report_view.objects.values_list('naimenovanie_strukturnogo_podrazdeleniya',
                                                   flat=True).distinct().order_by(
        'naimenovanie_strukturnogo_podrazdeleniya')

    choices = [(choice, choice) for choice in choices_list]

    naimenovanie_strukturnogo_podrazdeleniya = forms.ChoiceField(
        choices=[('', 'Все')] + choices,
        label='Подразделение',
        required=False
    )

    cb_onControl = forms.BooleanField(label='ТУ на контроле', required=False)


class ReportViewForm(forms.ModelForm):
    class Meta:
        model = TU
        exclude = []
        labels = {
            'id_classa_opasnosti': 'Класс опасности',
            'zavod_izgotovitel_txt': 'Завод-изготовитель',
            'zavodskoy_nomer': 'Заводской номер',
            'seriyniy_nomer_tu': 'Серийный номер ТУ',
            'gos_registracionniy_nomer': 'Государственный регистрационный знак',
            'marka_tu': 'Марка ТУ',
            'kratkie_tehn_haract_tu': 'Краткие тех.характеристики',
            'registr_nomer_gtt': 'Регистрационный номер ГГТ',
            'nomer_tu_po_tehn_sheme': 'Номер по тех.схеме',
            'god_izgotovleniya': 'Год изготовления',
            'primechanie': 'Примечание',
            'primechanie2': 'Примечание №2',
            'primechanie3': 'Примечание №3',

            'norm_srok_ekspluat_let': 'Нормативный срок эксплуатации, лет',
            'god_vvoda_v_ekspluat': 'Год ввода в эксплуатацию',
            'god_okonchaniya_ekspluat': 'Год окончания срока эксплуатации',
            'procent_iznosa': 'Процент износа',
            'data_posl_epb': 'Дата проведения ЭПБ',
            'data_sled_epb': 'Дата следующей ЭПБ',
            'data_ocherednoy_proverki': 'Дата очередной проверки (технического освидетельствования)',
            'data_sled_proverki': 'Дата следующей проверки (технического освидетельствования)',
            'razresh_srok_ekspluat': 'Разрешенный срок эксплуатации, лет',

            'nalichie_predohr_ustroystva': 'Предохранительное устройство',
            'tip_predohr_ustr': 'Тип предохранительного устройства',
            'obyom_m3': 'Объём, м3',
            'object_davlenie_mpa': 'Давление, МПа',
            'dy_mm': 'Dy, MM',
            'oborudovanie_davlenie_mpa': 'Давление, МПа',
            'obyom_t': 'Объём, м3',
            'god_modernizacii': 'Год модернизации',
            'provedennie_meropriyatiya': 'Проведенные мероприятия',
            'tip': 'Тип',
            'podtip': 'Подтип',
            'gruzopodyomnost_t': 'Грузоподъемность, т',

            'nomer_razresheniya_rtn': 'Номер разрешения РТН',
            'nomer_zaklyucheniya_epb': 'Номер заключения ЭПБ',
            'nalichie_pasporta_tu': 'Паспорт ТУ',
            'inf_tu_svedeniya_opo': 'Информация о включении ТУ в Сведения, характеризующие ОПО',
            'inf_tu_rtn': 'Информация о вкючении ТУ в отчет PTН',
            'nalichie_sertificata_sootvetstviya': 'Сертификат (декларация)соответствия',
            'nalichie_sertificata_rtn': 'Разрешение РТН на применение',
            'certificate_type': 'Тип сертификата',
            'certificate_number': '№',
            'certificate_expiration_date': 'Дата сертификата',
            'issued_by': 'Кем выдан',

        }

    naimenovanie_strukturnogo_podrazdeleniya = forms.CharField(max_length=255, label='Cтруктурное подразделение')
    naimenovanie_tipa_opo = forms.CharField(max_length=255, label='ОПО')
    registracionniy_nomer_opo = forms.CharField(max_length=255, label='Регистрационный номер ОПО')
    kratkoe_naimenovanie_tipa_opo = forms.CharField(max_length=255, label='Краткое наименование ОПО')
    naimenovanie_tu = forms.CharField(max_length=255, label='Наименование ТУ')

    certificate_type = forms.CharField(label='Тип сертификата')
    certificate_number = forms.CharField(label='Номер сертификата')
    issued_by = forms.CharField(label='Кем выдан')
    certificate_expiration_date = forms.CharField(label='Дата сертификата')

    def save(self, commit=True):
        report_view_instance = super().save(commit=False)
        report_view_instance.naimenovanie_strukturnogo_podrazdeleniya = self.cleaned_data[
            'naimenovanie_strukturnogo_podrazdeleniya']
        report_view_instance.naimenovanie_tipa_opo = self.cleaned_data['naimenovanie_tipa_opo']
        report_view_instance.registracionniy_nomer_opo = self.cleaned_data['registracionniy_nomer_opo']
        report_view_instance.kratkoe_naimenovanie_tipa_opo = self.cleaned_data['kratkoe_naimenovanie_tipa_opo']
        report_view_instance.naimenovanie_tu = self.cleaned_data['naimenovanie_tu']

        if commit:
            report_view_instance.save()

        return report_view_instance


class DeleteConfirmForm(forms.Form):
    confirm = forms.BooleanField(label='Подтвердите удаление', required=True)


class TUForm(forms.ModelForm):
    class Meta:
        model = TU
        fields = '__all__'
        labels = {
            'registr_nomer_oborudovaniya_tu': 'Регистрационный номер оборудования ТУ',
            'seriyniy_nomer_tu': 'Серийный номер ТУ',
            'gos_registracionniy_nomer': 'Гос. регистрационный знак',
            'zavodskoy_nomer': 'Заводской номер',
            'marka_tu': 'Марка ТУ',
            'kratkie_tehn_haract_tu': 'Краткие тех. характеристики ТУ',
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

            'obyom_m3': 'Объём, м3',
            'object_davlenie_mpa': 'Давление, МПа',
            'dy_mm': 'Dy, MM',
            'oborudovanie_davlenie_mpa': 'Давление, МПа',
            'obyom_t': 'Объём, м3',
            'god_modernizacii': 'Год модернизации',
            'provedennie_meropriyatiya': 'Проведенные мероприятия',
            'tip': 'Тип',
            'podtip': 'Подтип',
            'gruzopodyomnost_t': 'Грузоподъемность, т',

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


class OPOForm(forms.ModelForm):
    class Meta:
        model = OPO
        fields = '__all__'
        labels = {
            'txt': 'Наименование типа ОПО',
            'reg_number': 'Регистрационный номер ОПО',
            'id_strukturn_podrazd': 'Структурное подразделение ID',
            'txt_short': 'Краткое наименование типа ОПО',

        }


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = '__all__'

        labels = {
            'type': 'Тип сертификата',
            'number': 'Номер сертификата',
            'expiration_date': 'Дата истечения сертификата',
            'issued_by': 'Кем выдан'
        }


class NameTuForm(forms.ModelForm):
    class Meta:
        model = NameTU
        fields = '__all__'

        labels = {
            'id': 'ID Наименования ТУ',
            'description': 'Наименование ТУ',
        }


class SetupForm(forms.ModelForm):
    class Meta:
        model = Setup
        fields = '__all__'

        labels = {
            'name': 'Структурное подразделение',
        }
