from django.http import HttpResponse
from django.utils.timezone import now
from django.shortcuts import render, get_object_or_404

from .forms import FilterForm, ReportViewForm, DeleteConfirmForm, TUForm, OPOForm, CertificateForm, NameTuForm, \
    SetupForm
from .models import Report_view, TU, OPO, Setup, Certificate, NameTU


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
                queryset = queryset.filter(cb_onControl=1)

        context['queryset'] = queryset

    return render(request, 'main.html', context)


def create_tu(request):
    if request.method == 'POST':
        form = ReportViewForm(request.POST)
        if form.is_valid():

            report_view_instance = form.save()


            certificate_data = {
                'certificate_type': form.cleaned_data['certificate_type'],
                'certificate_number': form.cleaned_data['certificate_number'],
                'certificate_expiration_date': form.cleaned_data['certificate_expiration_date'],
                'issued_by': form.cleaned_data['issued_by'],
                'id_tu': report_view_instance.id_tu,
            }
            certificate_form = CertificateForm(certificate_data)
            if certificate_form.is_valid():
                certificate_form.save()

            name_tu_data = {
                'naimenovanie_tu': form.cleaned_data['naimenovanie_tu'],
            }
            name_tu_form = NameTuForm(name_tu_data)
            if name_tu_form.is_valid():
                name_tu_form.save()

            return HttpResponse('<script>window.close();</script>')
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

                return HttpResponse('<script>window.close();</script>')
            except Exception as e:
                print(f"Ошибка при удалении записи: {e}")
    else:
        form = DeleteConfirmForm()

    return render(request, 'delete_confirm.html', {'form': form, 'item': item})


import logging
logger = logging.getLogger(__name__)

def edit_view(request, pk):
    item = get_object_or_404(Report_view, pk=pk)
    tu_instance = get_object_or_404(TU, id_tu=item.ID_TU)
    opo_instance = get_object_or_404(OPO, id_opo=item.id_opo)
    certificates = Certificate.objects.filter(id_tu=item.ID_TU)
    name_instance = get_object_or_404(NameTU, id=tu_instance.id_naimenovanie_tu)
    setup_instance = get_object_or_404(Setup, id_firm=opo_instance.id_strukturn_podrazd)

    if request.method == 'POST':
        tu_form = TUForm(request.POST, instance=tu_instance)
        opo_form = OPOForm(request.POST, instance=opo_instance)
        cert_forms = [CertificateForm(request.POST, prefix=str(cert.pk), instance=cert) for cert in certificates]

        new_cert_forms = [CertificateForm(request.POST, prefix=f'new_{i}') for i in range(5)]

        name_form = NameTuForm(request.POST, instance=name_instance)
        setup_form = SetupForm(request.POST, instance=setup_instance)

        all_cert_forms = cert_forms + new_cert_forms

        if tu_form.is_valid() and opo_form.is_valid() and all([cf.is_valid() for cf in all_cert_forms]):
            tu_form.save()
            opo_form.save()
            name_form.save()
            for cert_form in all_cert_forms:
                if cert_form.cleaned_data.get('certificate_type') or cert_form.cleaned_data.get('certificate_number') or cert_form.cleaned_data.get('certificate_expiration_date') or cert_form.cleaned_data.get('issued_by'):
                    cert_instance = cert_form.save(commit=False)
                    cert_instance.id_tu = tu_instance.id_tu  # Ensure the ID is set
                    cert_instance.save()

            return HttpResponse('<script>window.close();</script>')
    else:
        tu_form = TUForm(instance=tu_instance)
        opo_form = OPOForm(instance=opo_instance)
        cert_forms = [CertificateForm(prefix=str(cert.pk), instance=cert) for cert in certificates]

        new_cert_forms = [CertificateForm(prefix=f'new_{i}') for i in range(5)]

        name_form = NameTuForm(instance=name_instance)
        setup_form = SetupForm(instance=setup_instance)

        all_cert_forms = cert_forms + new_cert_forms

    context = {
        'tu_form': tu_form,
        'opo_form': opo_form,
        'cert_forms': all_cert_forms,
        'name_form': name_form,
        'setup_form': setup_form,
        'item': item,
    }

    return render(request, 'edit_form.html', context)






