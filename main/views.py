from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from .forms import FilterForm
from .models import Report_view
import xlwt


def filter_view(request):
    if request.method == 'GET':
        form = FilterForm(request.GET)
        if form.is_valid():
            naimenovanie_strukturnogo_podrazdeleniya = form.cleaned_data.get('naimenovanie_strukturnogo_podrazdeleniya')

            # Фильтрация queryset по выбранному значению
            if naimenovanie_strukturnogo_podrazdeleniya:
                queryset = Report_view.objects.filter(
                    naimenovanie_strukturnogo_podrazdeleniya=naimenovanie_strukturnogo_podrazdeleniya)
            else:
                queryset = Report_view.objects.all()

            # Возвращаем данные на страницу
            return render(request, 'main.html', {'form': form, 'queryset': queryset})

    else:
        form = FilterForm()

    return render(request, 'main.html', {'form': form})


from django.utils.timezone import make_naive, get_current_timezone, make_aware


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
        # 'Дата последней проверки (ЕПБ)',
        # 'Дата следующей проверки (ЕПБ)',
        # 'Дата очередной проверки',
        # 'Дата следующей проверки',
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
        'cb_onControl',
        'Примечание2',
        'Примечание3',
        # 'Дата обновления',
        # 'Логин обновления',
        'Срок окончания эксплуатации',
        'isdel',
    ]

    # Записываем заголовки столбцов
    for col_num, column_title in enumerate(columns):
        worksheet.write(0, col_num, column_title)

    # Записываем данные
    row_num = 1
    for obj in data:
        # Преобразуем строки в datetime объекты, если это необходимо
        # data_posl_epb = datetime.strptime(obj.data_posl_epb, '%y.%m.%d') if obj.data_posl_epb else None
        # data_sled_epb = datetime.strptime(obj.data_sled_epb, '%y.%m.%d') if obj.data_sled_epb else None
        # data_ocherednoy_proverki = datetime.strptime(obj.data_ocherednoy_proverki,
        #                                              '%y.%m.%d') if obj.data_ocherednoy_proverki else None
        # data_sled_proverki = datetime.strptime(obj.data_sled_proverki, '%y.%m.%d') if obj.data_sled_proverki else None
        #
        # # Преобразуем в aware datetime объекты, если они еще не в этом формате
        # tz = get_current_timezone()
        # data_posl_epb = make_aware(data_posl_epb, timezone=tz) if data_posl_epb else None
        # data_sled_epb = make_aware(data_sled_epb, timezone=tz) if data_sled_epb else None
        # data_ocherednoy_proverki = make_aware(data_ocherednoy_proverki,
        #                                       timezone=tz) if data_ocherednoy_proverki else None
        # data_sled_proverki = make_aware(data_sled_proverki, timezone=tz) if data_sled_proverki else None

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
        # worksheet.write(row_num, 28, data_posl_epb)
        # worksheet.write(row_num, 29, data_sled_epb)
        # worksheet.write(row_num, 30, data_ocherednoy_proverki)
        # worksheet.write(row_num, 31, data_sled_proverki)
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
        worksheet.write(row_num, 52, obj.primechanie)
        worksheet.write(row_num, 53, obj.certificate_type)
        worksheet.write(row_num, 54, obj.certificate_number)
        worksheet.write(row_num, 55, obj.certificate_expiration_date)
        worksheet.write(row_num, 56, obj.certificate_issued_by)
        worksheet.write(row_num, 57, obj.cb_onControl)
        worksheet.write(row_num, 58, obj.Primechanie2)
        worksheet.write(row_num, 59, obj.Primechanie3)
        # worksheet.write(row_num, 60, obj.Date_upd)
        # worksheet.write(row_num, 61, obj.Login_upd)
        worksheet.write(row_num, 62, obj.srok_okonch_ekpl)
        worksheet.write(row_num, 63, obj.isdel)

        row_num += 1

    workbook.save(response)
    return response

