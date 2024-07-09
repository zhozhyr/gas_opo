from datetime import datetime
from django.utils.timezone import make_aware, is_naive, get_current_timezone, now
from django.shortcuts import render, get_object_or_404, redirect

from .forms import FilterForm, ReportViewForm, DeleteConfirmForm, TUForm, OPOForm, CertificateForm
from .models import Report_view, TU, OPO, Setup, Certificate


def filter_view(request):
    current_year = now().year
    current_year_plus_2 = current_year + 2
    context = {
        'form': FilterForm(request.GET if request.method == 'GET' else None),
        'current_year': current_year,
        'current_year_plus_2': current_year_plus_2,
    }

    if request.method == 'GET':
        form = context['form']
        queryset = Report_view.objects.all()

        if form.is_valid():
            naimenovanie_strukturnogo_podrazdeleniya = form.cleaned_data.get('naimenovanie_strukturnogo_podrazdeleniya')
            cb_onControl = form.cleaned_data.get('cb_onControl')

            if naimenovanie_strukturnogo_podrazdeleniya:
                queryset = queryset.filter(
                    naimenovanie_strukturnogo_podrazdeleniya=naimenovanie_strukturnogo_podrazdeleniya)

            if cb_onControl:
                queryset = queryset.filter(cb_onControl=1)  # Assuming 1 means true for cb_onControl

        context['queryset'] = queryset

    return render(request, 'main.html', context)


def create_tu(request):
    if request.method == 'POST':
        form = ReportViewForm(request.POST)
        if form.is_valid():
            # Сохранение данных в соответствующие таблицы
            form.save()
            return redirect('display_data')
    else:
        form = ReportViewForm()
    return render(request, 'create_tu.html', {'form': form})


def delete_view(request, pk):
    item = get_object_or_404(TU, pk=pk)

    if request.method == 'POST':
        form = DeleteConfirmForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            try:
                # Удаление из main_tu
                TU.objects.filter(id_tu=item.id_tu).delete()

                # Удаление из main_opo (если требуется)
                # OPO.objects.filter(id_opo=item.id_opo).delete()

                # Удаление из main_certificate (если требуется)
                # Certificate.objects.filter(id_tu=item.id_tu).delete()

                return redirect('display_data')  # Замените на ваш URL успеха
            except Exception as e:
                print(f"Ошибка при удалении записи: {e}")
    else:
        form = DeleteConfirmForm()

    return render(request, 'delete_confirm.html', {'form': form, 'item': item})


def edit_view(request, pk):
    item = get_object_or_404(Report_view, pk=pk)
    tu_instance = get_object_or_404(TU, id_tu=item.ID_TU)
    opo_instance = get_object_or_404(OPO, id_opo=item.id_opo)
    certificates = Certificate.objects.filter(id_tu=item.ID_TU)

    if request.method == 'POST':
        tu_form = TUForm(request.POST, instance=tu_instance)
        opo_form = OPOForm(request.POST, instance=opo_instance)
        cert_forms = [CertificateForm(request.POST, prefix=str(cert.pk), instance=cert) for cert in certificates]

        if tu_form.is_valid() and opo_form.is_valid() and all([cf.is_valid() for cf in cert_forms]):
            tu_form.save()
            opo_form.save()
            for cert_form in cert_forms:
                cert_form.save()

            return redirect('display_data')
    else:
        tu_form = TUForm(instance=tu_instance)
        opo_form = OPOForm(instance=opo_instance)
        cert_forms = [CertificateForm(prefix=str(cert.pk), instance=cert) for cert in certificates]

    context = {
        'tu_form': tu_form,
        'opo_form': opo_form,
        'cert_forms': cert_forms,
        'item': item,
    }

    return render(request, 'edit_form.html', context)


def export_to_excel(request):
    # Получаем данные для экспорта из базы данных
    data = Report_view.objects.all()

    # Создаем Excel файл с помощью xlwt
    import xlwt
    from django.http import HttpResponse

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="report.xls"'

    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('Report')

    # Заголовки столбцов
    columns = [
        'Название подразделения',
        'Название типа ОПО',
        'Регистрационный номер ОПО',
        'Название класса опасности',
        'Краткое название типа ОПО',
        'Название ТУ',
        'Название завода',
        'ID структурного подразделения',
        'ID типа ОПО',
        'ID ОПО',
        'Название типа ТУ',
        'ID типа ТУ',
        'ID вида ТУ',
        'Название вида ТУ',
        'ID ТУ',
        'Регистрационный номер оборудования ТУ',
        'Серийный номер ТУ',
        'Государственный регистрационный номер',
        'Заводской номер',
        'Марка ТУ',
        'Краткие технические характеристики ТУ',
        'Регистрационный номер ГТТ',
        'Номер ТУ по технической схеме',
        'Год изготовления',
        'Нормативный срок эксплуатации (лет)',
        'Год ввода в эксплуатацию',
        'Год окончания эксплуатации',
        'Процент износа',

        'Дата последней проверки (ЕПБ)',
        'Дата следующей проверки (ЕПБ)',
        'Дата очередной проверки',
        'Дата следующей проверки',

        'Разрешенный срок эксплуатации',
        'Наличие предохранительного устройства',
        'Тип предохранительного устройства',
        'Объем (м3)',
        'Объект давление (МПа)',
        'Диаметр (мм)',
        'Тип',
        'Подтип',
        'Грузоподъемность (т)',
        'Объем (т)',
        'Давление оборудования (МПа)',
        'Год модернизации',
        'Проведенные мероприятия',
        'Номер разрешения РТН',
        'Номер заключения ЕПБ',
        'Наличие паспорта ТУ',
        'Информация о ТУ (сведения ОПО)',
        'Информация о ТУ (РТН)',
        'Наличие сертификата соответствия',
        'Наличие сертификата РТН',
        'Примечание',
        'Тип сертификата',
        'Номер сертификата',
        'Срок действия сертификата',
        'Орган, выдавший сертификат',
        'Примечание',
        'Примечание2',
        'Примечание3',

        'Дата обновления',
        'Логин обновления',

        'Срок окончания эксплуатации',
        'Выведено из эксплуатации',
    ]

    # Записываем заголовки столбцов
    for col_num, column_title in enumerate(columns):
        worksheet.write(0, col_num, column_title)

    tz = get_current_timezone()

    def to_aware_string(date_input, date_formats=['%Y-%m-%d', '%y.%m.%d', '%d.%m.%y']):
        if date_input:
            # Если входное значение уже является объектом datetime
            if isinstance(date_input, datetime):
                date_obj = date_input
            else:
                date_obj = None
                # Пробуем все форматы даты
                for date_format in date_formats:
                    try:
                        date_obj = datetime.strptime(date_input, date_format)
                        break
                    except ValueError:
                        continue
                if date_obj is None:
                    raise ValueError(f"Date input '{date_input}' does not match any of the formats: {date_formats}")

            # Если дата наивная, делаем ее осведомленной
            if is_naive(date_obj):
                date_obj = make_aware(date_obj, timezone=tz)

            # Возвращаем строковое представление даты
            return date_obj.strftime('%Y-%m-%d %H:%M:%S')
        return None

    # Записываем данные
    row_num = 1
    for obj in data:
        # Убедимся, что строковые представления дат преобразованы в datetime объекты
        date_upd = to_aware_string(obj.Date_upd, ['%Y-%m-%d %H:%M:%S', '%y.%m.%d', '%d.%m.%y', '%y.%m.%d', '%Y-%m-%d'])
        data_posl_epb = to_aware_string(obj.data_posl_epb, ['%y.%m.%d', '%d.%m.%y', '%Y-%m-%d'])
        data_sled_epb = to_aware_string(obj.data_sled_epb, ['%y.%m.%d', '%d.%m.%y', '%Y-%m-%d'])
        data_ocherednoy_proverki = to_aware_string(obj.data_ocherednoy_proverki, ['%y.%m.%d', '%d.%m.%y', '%Y-%m-%d'])
        data_sled_proverki = to_aware_string(obj.data_sled_proverki, ['%y.%m.%d', '%d.%m.%y', '%Y-%m-%d'])

        worksheet.write(row_num, 0, obj.naimenovanie_strukturnogo_podrazdeleniya)
        worksheet.write(row_num, 1, obj.naimenovanie_tipa_opo)
        worksheet.write(row_num, 2, obj.registracionniy_nomer_opo)
        worksheet.write(row_num, 3, obj.naimenovanie_classa_opasnosti)
        worksheet.write(row_num, 4, obj.kratkoe_naimenovanie_tipa_opo)
        worksheet.write(row_num, 5, obj.naimenovanie_tu)
        worksheet.write(row_num, 6, obj.naimenovanie_zavoda)
        worksheet.write(row_num, 7, obj.id_strukturn_podrazd)
        worksheet.write(row_num, 8, obj.id_tipa_opo)
        worksheet.write(row_num, 9, obj.id_opo)
        worksheet.write(row_num, 10, obj.naimenovanie_tipa_tu)
        worksheet.write(row_num, 11, obj.id_type_tu)
        worksheet.write(row_num, 12, obj.id_kind_tu)
        worksheet.write(row_num, 13, obj.naimenovanie_vida_tu)
        worksheet.write(row_num, 14, obj.ID_TU)
        worksheet.write(row_num, 15, obj.registr_nomer_oborudovaniya_tu)
        worksheet.write(row_num, 16, obj.seriyniy_nomer_tu)
        worksheet.write(row_num, 17, obj.gos_registracionniy_nomer)
        worksheet.write(row_num, 18, obj.zavodskoy_nomer)
        worksheet.write(row_num, 19, obj.marka_tu)
        worksheet.write(row_num, 20, obj.kratkie_tehn_haract_tu)
        worksheet.write(row_num, 21, obj.registr_nomer_gtt)
        worksheet.write(row_num, 22, obj.nomer_tu_po_tehn_sheme)
        worksheet.write(row_num, 23, obj.god_izgotovleniya)
        worksheet.write(row_num, 24, obj.norm_srok_ekspluat_let)
        worksheet.write(row_num, 25, obj.god_vvoda_v_ekspluat)
        worksheet.write(row_num, 26, obj.god_okonchaniya_ekspluat)
        worksheet.write(row_num, 27, obj.procent_iznosa)
        worksheet.write(row_num, 28, data_posl_epb)
        worksheet.write(row_num, 29, data_sled_epb)
        worksheet.write(row_num, 30, data_ocherednoy_proverki)
        worksheet.write(row_num, 31, data_sled_proverki)
        worksheet.write(row_num, 32, obj.razresh_srok_ekspluat)
        worksheet.write(row_num, 33, obj.nalichie_predohr_ustroystva)
        worksheet.write(row_num, 34, obj.tip_predohr_ustr)
        worksheet.write(row_num, 35, obj.obyom_m3)
        worksheet.write(row_num, 36, obj.object_davlenie_mpa)
        worksheet.write(row_num, 37, obj.dy_mm)
        worksheet.write(row_num, 38, obj.tip)
        worksheet.write(row_num, 39, obj.podtip)
        worksheet.write(row_num, 40, obj.gruzopodyomnost_t)
        worksheet.write(row_num, 41, obj.obyom_t)
        worksheet.write(row_num, 42, obj.oborudovanie_davlenie_mpa)
        worksheet.write(row_num, 43, obj.god_modernizacii)
        worksheet.write(row_num, 44, obj.provedennie_meropriyatiya)
        worksheet.write(row_num, 45, obj.nomer_razresheniya_rtn)
        worksheet.write(row_num, 46, obj.nomer_zaklyucheniya_epb)
        worksheet.write(row_num, 47, obj.nalichie_pasporta_tu)
        worksheet.write(row_num, 48, obj.inf_tu_svedeniya_opo)
        worksheet.write(row_num, 49, obj.inf_tu_rtn)
        worksheet.write(row_num, 50, obj.nalichie_sertificata_sootvetstviya)
        worksheet.write(row_num, 51, obj.nalichie_sertificata_rtn)
        worksheet.write(row_num, 52, obj.cb_onControl)
        worksheet.write(row_num, 53, obj.certificate_type)
        worksheet.write(row_num, 54, obj.certificate_number)
        worksheet.write(row_num, 55, obj.certificate_expiration_date)
        worksheet.write(row_num, 56, obj.certificate_issued_by)
        worksheet.write(row_num, 57, obj.primechanie)
        worksheet.write(row_num, 58, obj.Primechanie2)
        worksheet.write(row_num, 59, obj.Primechanie3)
        worksheet.write(row_num, 60, date_upd)
        worksheet.write(row_num, 61, obj.Login_upd)
        worksheet.write(row_num, 62, obj.srok_okonch_ekpl)
        worksheet.write(row_num, 63, obj.isdel)

        row_num += 1

    workbook.save(response)
    return response
