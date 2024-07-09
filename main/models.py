from django.db import models


class UserInfo(models.Model):
    group_account = models.CharField(max_length=255, null=True, verbose_name="Group Account")
    full_name = models.CharField(max_length=255, null=True, verbose_name="Full Name")
    position = models.CharField(max_length=255, null=True, verbose_name="Position")
    specialist_exploitation = models.CharField(max_length=255, null=True,
                                               verbose_name="Specialist of Exploitation Department")
    head_exploitation = models.CharField(max_length=255, null=True, verbose_name="Head of Exploitation Department")
    specialist_it_service = models.CharField(max_length=255, null=True, verbose_name="Specialist of IT Service")
    head_it_service = models.CharField(max_length=255, null=True, verbose_name="Head of IT Service")
    production_department = models.CharField(max_length=255, null=True,
                                             verbose_name="Production Department of Diagnostic Works")
    corporate_supervision = models.CharField(max_length=255, null=True, verbose_name="Corporate Supervision")
    email = models.CharField(max_length=255, null=True, verbose_name="Email")
    access_rights = models.CharField(max_length=255, null=True, verbose_name="Access Rights")
    active_account = models.CharField(max_length=255, null=True, verbose_name="Active Account")

    class Meta:
        verbose_name = "Информация"
        verbose_name_plural = "Информация"

    def __str__(self):
        return self.full_name if self.full_name else "UserInfo object"


class Tree(models.Model):
    id_tree = models.AutoField(primary_key=True)
    parent_structure = models.IntegerField(null=True, verbose_name="Parent Structure")
    structure_code = models.IntegerField(null=True, verbose_name="Structure Code")
    level = models.SmallIntegerField(null=True, verbose_name="Level")
    firm_id = models.IntegerField(null=True, verbose_name="Firm ID")
    branch_number = models.IntegerField(null=True, verbose_name="Branch Number")
    branch_id = models.IntegerField(null=True, verbose_name="Branch ID")

    class Meta:
        verbose_name = "Дерево"
        verbose_name_plural = "Деревья"

    def __str__(self):
        return f"Tree {self.id_tree}"


class Administrators(models.Model):
    auto_card = models.IntegerField(null=True)

    class Meta:
        verbose_name = "Администратор"
        verbose_name_plural = "Администраторы"


class Appointments(models.Model):
    code_appoint = models.AutoField(primary_key=True)
    name_appoint = models.CharField(max_length=250, null=True)
    name_appoint_acc = models.CharField(max_length=250, null=True)

    class Meta:
        verbose_name = "Назначение"
        verbose_name_plural = "Назначения"

    def __str__(self):
        return self.name_appoint if self.name_appoint else "Appointment object"


class ClassOpasnosti(models.Model):
    id = models.AutoField(primary_key=True)
    txt = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = "Класс опасности"
        verbose_name_plural = "Классы опасности"

    def __str__(self):
        return self.txt if self.txt else "ClassOpasnosti object"


class ControlNotes(models.Model):
    id = models.AutoField(primary_key=True)
    id_tu = models.IntegerField(null=True)
    auto_card = models.IntegerField(null=True)
    note_txt = models.CharField(max_length=5000, null=True)
    date_note = models.DateTimeField(null=True)

    class Meta:
        verbose_name = "Примечание контроля"
        verbose_name_plural = "Примечания контроля"

    def __str__(self):
        return self.note_txt[:50] if self.note_txt else "ControlNote object"


# Должности
class Position(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    description = models.CharField(max_length=200, null=True, verbose_name="Description")

    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Positions"

    def __str__(self):
        return self.description if self.description else "Position object"


# Журналы ЭПБ
class EPBJournal(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    epb_date = models.DateTimeField(null=True, verbose_name="EPB Date")
    tu_id = models.IntegerField(null=True, verbose_name="TU ID")
    epb_conclusion = models.CharField(max_length=200, null=True, verbose_name="EPB Conclusion")

    class Meta:
        verbose_name = "EPB Journal"
        verbose_name_plural = "EPB Journals"

    def __str__(self):
        return f"EPB Journal {self.epb_date} - {self.epb_conclusion}"


class InspectionJournal(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    inspection_date = models.DateTimeField(null=True, verbose_name="Inspection Date")
    tu_id = models.IntegerField(null=True, verbose_name="TU ID")

    class Meta:
        verbose_name = "Inspection Journal"
        verbose_name_plural = "Inspection Journals"

    def __str__(self):
        return f"Inspection Journal {self.inspection_date}"


class LogActions(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=500, null=True)

    class Meta:
        verbose_name = "Лог действий"
        verbose_name_plural = "Логи действий"

    def __str__(self):
        return self.description[:50] if self.description else "LogAction object"


# Наличие
class Availability(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    description = models.CharField(max_length=20, null=True, verbose_name="Description")

    class Meta:
        verbose_name = "Availability"
        verbose_name_plural = "Availability"

    def __str__(self):
        return self.description if self.description else "Availability object"


# Наличие паспорта ТУ
class PassportAvailability(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    description = models.CharField(max_length=20, null=True, verbose_name="Description")

    class Meta:
        verbose_name = "Passport Availability"
        verbose_name_plural = "Passport Availability"

    def __str__(self):
        return self.description if self.description else "PassportAvailability object"


class NameTU(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = "Наименование ТУ"
        verbose_name_plural = "Наименования ТУ"

    def __str__(self):
        return self.description if self.description else "NameTU object"


class OPO(models.Model):
    id_opo = models.BigAutoField(primary_key=True)
    id_type_opo = models.BigIntegerField()
    id_strukturn_podrazd = models.BigIntegerField(null=True, blank=True, default=None)
    txt = models.CharField(max_length=200, null=True)
    txt_short = models.CharField(max_length=200, null=True)
    reg_number = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = "ОПО"
        verbose_name_plural = "ОПО"

    def __str__(self):
        return self.txt if self.txt else "OPO object"


# Сертификаты
class Certificate(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="ID")
    type = models.CharField(max_length=500, verbose_name="Type", blank=True)
    number = models.CharField(max_length=200, verbose_name="Number", blank=True)
    issue_date = models.DateField(blank=True, null=True ,verbose_name="Issue Date")
    expiration_date = models.DateField(null=True, verbose_name="Expiration Date", blank=True)
    issued_by = models.CharField(max_length=500, verbose_name="Issued By", blank=True, null=True)
    id_tu = models.BigIntegerField(verbose_name="ID TU")
    scan = models.BinaryField(null=True, verbose_name="Scan", blank=True)

    class Meta:
        verbose_name = "Certificate"
        verbose_name_plural = "Certificates"

    def __str__(self):
        return self.number if self.number else "Certificate object"


class Setup(models.Model):
    id_firm = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    short_name = models.CharField(max_length=100, null=True)
    id_struct_parent = models.IntegerField(null=True)

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"

    def __str__(self):
        return self.name if self.name else "Setup object"


class TypeOPO(models.Model):
    id = models.AutoField(primary_key=True)
    txt = models.CharField(max_length=200, null=True)
    txt_short = models.CharField(max_length=200, null=True)
    reg_number = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = "Тип ОПО"
        verbose_name_plural = "Типы ОПО"

    def __str__(self):
        return self.txt if self.txt else "TipOPO object"


class TypeTU(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    description = models.CharField(max_length=200, null=True, verbose_name="Description")

    class Meta:
        verbose_name = "TU Type"
        verbose_name_plural = "TU Types"

    def __str__(self):
        return self.description if self.description else "TUType object"


class TypeTU_J(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="ID")
    description = models.CharField(max_length=200, null=True, verbose_name="Description")

    class Meta:
        verbose_name = "TU Type (j)"
        verbose_name_plural = "TU Types (j)"

    def __str__(self):
        return self.description if self.description else "TUTypeJ object"


class TU(models.Model):
    registr_nomer_oborudovaniya_tu = models.CharField(max_length=200, null=True, blank=True)
    seriyniy_nomer_tu = models.CharField(max_length=200, null=True, blank=True)
    gos_registracionniy_nomer = models.CharField(max_length=200, null=True, blank=True)
    zavodskoy_nomer = models.CharField(max_length=200, null=True, blank=True)
    marka_tu = models.CharField(max_length=500, null=True, blank=True)
    kratkie_tehn_haract_tu = models.CharField(max_length=200, null=True, blank=True)
    registr_nomer_gtt = models.CharField(max_length=200, null=True, blank=True)
    nomer_tu_po_tehn_sheme = models.CharField(max_length=200, null=True, blank=True)
    god_izgotovleniya = models.CharField(max_length=200, null=True, blank=True)
    norm_srok_ekspluat_let = models.SmallIntegerField(null=True, blank=True)
    god_vvoda_v_ekspluat = models.SmallIntegerField(null=True, blank=True)
    god_okonchaniya_ekspluat = models.SmallIntegerField(null=True, blank=True)
    procent_iznosa = models.FloatField(null=True, blank=True)
    data_posl_epb = models.DateField(null=True, blank=True)
    data_sled_epb = models.DateField(null=True, blank=True)
    data_ocherednoy_proverki = models.DateField(null=True, blank=True)
    data_sled_proverki = models.DateField(null=True, blank=True)
    razresh_srok_ekspluat = models.SmallIntegerField(null=True, blank=True)
    nalichie_predohr_ustroystva = models.IntegerField(null=True, blank=True)
    tip_predohr_ustr = models.CharField(max_length=200, null=True, blank=True)
    obyom_m3 = models.FloatField(null=True, blank=True)
    object_davlenie_mpa = models.FloatField(null=True, blank=True)
    dy_mm = models.FloatField(null=True, blank=True)
    tip = models.CharField(max_length=200, null=True, blank=True)
    podtip = models.CharField(max_length=200, null=True, blank=True)
    gruzopodyomnost_t = models.FloatField(null=True, blank=True)
    obyom_t = models.FloatField(null=True, blank=True)
    oborudovanie_davlenie_mpa = models.FloatField(null=True, blank=True)
    god_modernizacii = models.SmallIntegerField(null=True, blank=True)
    provedennie_meropriyatiya = models.CharField(max_length=200, null=True, blank=True)
    nomer_razresheniya_rtn = models.CharField(max_length=200, null=True, blank=True)
    nomer_zaklyucheniya_epb = models.CharField(max_length=200, null=True, blank=True)
    nalichie_pasporta_tu = models.IntegerField(null=True, blank=True)
    inf_tu_svedeniya_opo = models.CharField(max_length=200, null=True, blank=True)
    inf_tu_rtn = models.CharField(max_length=200, null=True, blank=True)
    nalichie_sertificata_sootvetstviya = models.IntegerField(null=True, blank=True)
    nalichie_sertificata_rtn = models.IntegerField(null=True, blank=True)
    primechanie = models.TextField(null=True, blank=True)
    id_opo = models.BigIntegerField()
    id_classa_opasnosti = models.BigIntegerField(null=True, blank=True)
    id_zavod_izgotovitel = models.BigIntegerField(null=True, blank=True)
    id_vid_tu = models.BigIntegerField()
    id_tip_tu = models.BigIntegerField(null=True, blank=True)
    id_naimenovanie_tu = models.BigIntegerField(default=None)

    id_tu = models.IntegerField(primary_key=True, db_column='ID_TU')
    id_rtn = models.IntegerField(db_column='id_RTN', blank=True, null=True)
    strana_proizvoditel = models.CharField(db_column='Strana_proizvoditel', max_length=200, blank=True,
                                           null=True)
    vivod_epb = models.CharField(db_column='Vivod_EPB', max_length=200, blank=True,
                                 null=True)  # Field name made lowercase.
    kol_ciklov = models.IntegerField(db_column='Kol_ciklov', blank=True, null=True)
    kol_ciklov_fact = models.IntegerField(db_column='Kol_ciklov_fact', blank=True,
                                          null=True)
    id_nalichie_sr_kontr = models.IntegerField(blank=True, null=True)
    id_tu_zamen = models.IntegerField(db_column='id_TU_Zamen', blank=True, null=True)
    nn_tu_zamen = models.CharField(db_column='NN_TU_Zamen', max_length=200, blank=True,
                                   null=True)
    id_vid_tu_j = models.IntegerField(db_column='id_Vid_TU_j', blank=True, null=True)
    id_tip_tu_j = models.IntegerField(db_column='id_Tip_TU_j', blank=True, null=True)
    cb_oncontrol = models.IntegerField(db_column='cb_onControl', blank=True, null=True)
    primechanie2 = models.CharField(db_column='Primechanie2', blank=True, null=True)
    primechanie3 = models.CharField(db_column='Primechanie3', blank=True, null=True)
    zavod_izgotovitel_txt = models.CharField(db_column='Zavod_Izgotovitel_txt', max_length=500, blank=True,
                                             null=True)
    date_upd = models.DateTimeField(db_column='Date_upd', blank=True, null=True)
    login_upd = models.CharField(db_column='Login_upd', max_length=100, blank=True,
                                 null=True)  # Field name made lowercase.
    isdeleted = models.IntegerField(db_column='isDeleted', blank=True, null=True)

    class Meta:
        verbose_name = "ТУ"
        verbose_name_plural = "ТУ"

    def __str__(self):
        return self.registr_nomer_oborudovaniya_tu if self.registr_nomer_oborudovaniya_tu else "TU object"


class TU_RTN(models.Model):
    id = models.IntegerField(primary_key=True)
    txt = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = "ТУ РТН"
        verbose_name_plural = "ТУ РТН"

    def __str__(self):
        return self.txt if self.txt else "TU_RTN object"


class UserRoles(models.Model):
    id = models.AutoField(primary_key=True)
    txt = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = "Роль пользователя"
        verbose_name_plural = "Роли пользователей"

    def __str__(self):
        return self.txt if self.txt else "UserRoles object"


class UserSettings(models.Model):
    id = models.AutoField(primary_key=True)
    net_name = models.CharField(max_length=30, null=True)
    auto_card = models.IntegerField(null=True)
    ini_file = models.BinaryField(null=True)
    ini_file_name = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = "Настройка пользователя"
        verbose_name_plural = "Настройки пользователей"

    def __str__(self):
        return self.net_name if self.net_name else "UserSettings object"


class UsersList(models.Model):
    id = models.AutoField(primary_key=True)
    auto_card = models.IntegerField(null=True)
    id_role = models.ForeignKey(UserRoles, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Список пользователей"
        verbose_name_plural = "Списки пользователей"

    def __str__(self):
        return str(self.auto_card) if self.auto_card else "UsersList object"


class KindTU(models.Model):
    id = models.AutoField(primary_key=True)
    txt = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = "Вид ТУ"
        verbose_name_plural = "Виды ТУ"

    def __str__(self):
        return self.txt if self.txt else "VidTU object"


class KindTU_J(models.Model):
    id = models.IntegerField(primary_key=True)
    txt = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = "Вид ТУ (j)"
        verbose_name_plural = "Виды ТУ (j)"

    def __str__(self):
        return self.txt if self.txt else "VidTUJ object"


class YesNo(models.Model):
    id = models.IntegerField(primary_key=True)
    txt = models.CharField(max_length=50, null=True)


# Завод-изготовитель
class Manufacturer(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    description = models.CharField(max_length=200, null=True, verbose_name="Description")

    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturers"

    def __str__(self):
        return self.description if self.description else "Manufacturer object"


class Report_view(models.Model):
    naimenovanie_strukturnogo_podrazdeleniya = models.CharField(max_length=255)
    naimenovanie_tipa_opo = models.CharField(max_length=255)
    registracionniy_nomer_opo = models.CharField(max_length=255)
    naimenovanie_classa_opasnosti = models.CharField(max_length=255)
    kratkoe_naimenovanie_tipa_opo = models.CharField(max_length=255)
    naimenovanie_tu = models.CharField(max_length=255)
    naimenovanie_zavoda = models.CharField(max_length=255)
    id_strukturn_podrazd = models.IntegerField()
    id_tipa_opo = models.IntegerField()
    id_opo = models.IntegerField()  # Assuming 'id_opo' is unique and can be used as a primary key
    naimenovanie_tipa_tu = models.CharField(max_length=255)
    id_type_tu = models.IntegerField()
    id_kind_tu = models.IntegerField()
    naimenovanie_vida_tu = models.CharField(max_length=255)
    ID_TU = models.IntegerField(primary_key=True)
    registr_nomer_oborudovaniya_tu = models.CharField(max_length=255)
    seriyniy_nomer_tu = models.CharField(max_length=255)
    gos_registracionniy_nomer = models.CharField(max_length=255)
    zavodskoy_nomer = models.CharField(max_length=255)
    marka_tu = models.CharField(max_length=255)
    kratkie_tehn_haract_tu = models.CharField(max_length=255)
    registr_nomer_gtt = models.CharField(max_length=255)
    nomer_tu_po_tehn_sheme = models.CharField(max_length=255)
    god_izgotovleniya = models.IntegerField()
    norm_srok_ekspluat_let = models.IntegerField()
    god_vvoda_v_ekspluat = models.IntegerField()
    god_okonchaniya_ekspluat = models.IntegerField()
    procent_iznosa = models.FloatField()

    data_posl_epb = models.CharField(max_length=255)
    data_sled_epb = models.CharField(max_length=255)
    data_ocherednoy_proverki = models.CharField(max_length=255)
    data_sled_proverki = models.CharField(max_length=255)

    razresh_srok_ekspluat = models.CharField(max_length=255)
    nalichie_predohr_ustroystva = models.CharField(max_length=255)
    tip_predohr_ustr = models.CharField(max_length=255)
    obyom_m3 = models.FloatField()
    object_davlenie_mpa = models.FloatField()
    dy_mm = models.FloatField()
    tip = models.CharField(max_length=255)
    podtip = models.CharField(max_length=255)
    gruzopodyomnost_t = models.FloatField()
    obyom_t = models.FloatField()
    oborudovanie_davlenie_mpa = models.FloatField()
    god_modernizacii = models.IntegerField()
    provedennie_meropriyatiya = models.CharField(max_length=255)
    nomer_razresheniya_rtn = models.CharField(max_length=255)
    nomer_zaklyucheniya_epb = models.CharField(max_length=255)
    nalichie_pasporta_tu = models.CharField(max_length=255)
    inf_tu_svedeniya_opo = models.CharField(max_length=255)
    inf_tu_rtn = models.CharField(max_length=255)
    nalichie_sertificata_sootvetstviya = models.CharField(max_length=255)
    nalichie_sertificata_rtn = models.CharField(max_length=255)
    primechanie = models.CharField(max_length=255)
    certificate_type = models.CharField(max_length=255)
    certificate_number = models.CharField(max_length=255)
    certificate_expiration_date = models.CharField(max_length=255)
    certificate_issued_by = models.CharField(max_length=255)
    cb_onControl = models.IntegerField()
    Primechanie2 = models.CharField(max_length=255)
    Primechanie3 = models.CharField(max_length=255)

    Date_upd = models.CharField(max_length=255)
    Login_upd = models.CharField(max_length=255)

    srok_okonch_ekpl = models.IntegerField()
    isdel = models.CharField(max_length=255)

    class Meta:
        managed = False  # No migrations will be created
        db_table = 'report_view'  # Replace with the actual name of your view