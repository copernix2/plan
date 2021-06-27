from django.db import models
from accounts.models import Profil

class Cases(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    domain = models.TextField(blank=True, null=True)
    caseid = models.TextField(blank=True, null=True)
    adresse = models.TextField(db_column='Adresse', blank=True, null=True)  # Field name made lowercase.
    cpn1 = models.TextField(db_column='CPN1', blank=True, null=True)  # Field name made lowercase.
    cpn1_date = models.TextField(db_column='CPN1_date', blank=True, null=True)  # Field name made lowercase.
    cpn2 = models.TextField(db_column='CPN2', blank=True, null=True)  # Field name made lowercase.
    accompagnantcpn = models.TextField(db_column='accompagnantCPN', blank=True, null=True)  # Field name made lowercase.
    age_cal = models.TextField(blank=True, null=True)
    age_femme = models.TextField(blank=True, null=True)
    age_grossesse_mois = models.TextField(blank=True, null=True)
    age_grossesse_semaine = models.TextField(blank=True, null=True)
    complication = models.TextField(blank=True, null=True)
    complication_precedent = models.TextField(blank=True, null=True)
    connaissance_date = models.TextField(blank=True, null=True)
    date_accouchement = models.TextField(blank=True, null=True)
    date_dernier_regle = models.TextField(blank=True, null=True)
    depistagevih = models.TextField(db_column='depistageVIH', blank=True, null=True)  # Field name made lowercase.
    enceinte = models.TextField(blank=True, null=True)
    enfant_vivant = models.TextField(blank=True, null=True)
    membre_ocb = models.TextField(blank=True, null=True)
    moustiquaire = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    nb_cpn_visit = models.TextField(blank=True, null=True)
    nb_visit = models.TextField(blank=True, null=True)
    nom_mari = models.TextField(blank=True, null=True)
    nombre_grossesse = models.TextField(blank=True, null=True)
    poste_sante = models.TextField(blank=True, null=True)
    prime_grossesse = models.TextField(blank=True, null=True)
    prochain_cpn = models.TextField(blank=True, null=True)
    prochain_rv = models.TextField(blank=True, null=True)
    raison_manqcpn = models.TextField(db_column='raison_manqCPN', blank=True, null=True)  # Field name made lowercase.
    reference = models.TextField(blank=True, null=True)
    respect_cpn = models.TextField(blank=True, null=True)
    sous_moustiquaire = models.TextField(blank=True, null=True)
    telephone = models.TextField(blank=True, null=True)
    closed = models.BooleanField(blank=True, null=True)
    last_modified_by_user_username = models.TextField(blank=True, null=True)
    opened_by_username = models.ForeignKey("MobileUser", on_delete=models.DO_NOTHING,
                                   null=True, db_column='opened_by_username', related_name='femme', verbose_name='poste')    
    opened_date = models.DateTimeField(blank=True, null=True)
    cpn2_date = models.TextField(db_column='CPN2_date', blank=True, null=True)  # Field name made lowercase.
    cpn3 = models.TextField(db_column='CPN3', blank=True, null=True)  # Field name made lowercase.
    cpn3_date = models.TextField(db_column='CPN3_date', blank=True, null=True)  # Field name made lowercase.
    cpn4 = models.TextField(db_column='CPN4', blank=True, null=True)  # Field name made lowercase.
    cpn4_date = models.TextField(db_column='CPN4_date', blank=True, null=True)  # Field name made lowercase.
    sp1 = models.TextField(db_column='SP1', blank=True, null=True)  # Field name made lowercase.
    sp2 = models.TextField(db_column='SP2', blank=True, null=True)  # Field name made lowercase.
    sp3 = models.TextField(db_column='SP3', blank=True, null=True)  # Field name made lowercase.
    bilan = models.TextField(blank=True, null=True)
    connaissance_gsh = models.TextField(blank=True, null=True)
    donneur = models.TextField(blank=True, null=True)
    groupe_soutien = models.TextField(blank=True, null=True)
    gsh = models.TextField(blank=True, null=True)
    ident_donneur = models.TextField(blank=True, null=True)
    is_accomp = models.TextField(blank=True, null=True)
    kit = models.TextField(blank=True, null=True)
    lieu_acc = models.TextField(blank=True, null=True)
    marainne = models.TextField(blank=True, null=True)
    note_bilan = models.TextField(blank=True, null=True)
    num_donneur = models.TextField(blank=True, null=True)
    tel_maraine = models.TextField(blank=True, null=True)
    transport = models.TextField(blank=True, null=True)
    avisespacement = models.TextField(blank=True, null=True)
    methonde = models.TextField(blank=True, null=True)
    souhait_pf = models.TextField(blank=True, null=True)
    accompagne_accouche = models.TextField(blank=True, null=True)
    accouche = models.TextField(blank=True, null=True)
    accouchement_effectue = models.TextField(blank=True, null=True)
    affiche_viste = models.TextField(blank=True, null=True)
    complication_accouche = models.TextField(blank=True, null=True)
    consultation_postnat1 = models.TextField(blank=True, null=True)
    consultation_postnat2 = models.TextField(blank=True, null=True)
    consultation_postnat3 = models.TextField(blank=True, null=True)
    date_cpon1 = models.TextField(db_column='date_CPON1', blank=True, null=True)  # Field name made lowercase.
    date_cpon2 = models.TextField(db_column='date_CPON2', blank=True, null=True)  # Field name made lowercase.
    date_cpon3 = models.TextField(db_column='date_CPON3', blank=True, null=True)  # Field name made lowercase.
    faire_cpon1 = models.TextField(blank=True, null=True)
    femme_vivant = models.TextField(blank=True, null=True)
    lait_maternel = models.TextField(blank=True, null=True)
    lieu_daccouchement = models.TextField(blank=True, null=True)
    nb_passagecpon = models.TextField(db_column='nb_passageCPON', blank=True, null=True)  # Field name made lowercase.
    nbr_enfants_nes = models.TextField(blank=True, null=True)
    pas_accouche_poste = models.TextField(blank=True, null=True)
    transfusion = models.TextField(blank=True, null=True)
    typ_accouche = models.TextField(blank=True, null=True)
    bien_accueilli = models.TextField(blank=True, null=True)
    date_de_naissance = models.TextField(blank=True, null=True)
    note_felicita = models.TextField(blank=True, null=True)
    respect_rdv = models.TextField(blank=True, null=True)
    accompagne = models.TextField(blank=True, null=True)
    accompagne1 = models.TextField(blank=True, null=True)
    aller_poste_sante = models.TextField(blank=True, null=True)
    aller_poste_sante1 = models.TextField(blank=True, null=True)
    autres_motifs = models.TextField(blank=True, null=True)
    covid_fait = models.TextField(blank=True, null=True)
    date_ref = models.TextField(blank=True, null=True)
    montant_transport = models.TextField(blank=True, null=True)
    motif = models.TextField(blank=True, null=True)
    motif_depist = models.TextField(blank=True, null=True)
    motifs_de_rfrence = models.TextField(blank=True, null=True)
    moyen_transport = models.TextField(blank=True, null=True)
    moyen_transport1 = models.TextField(blank=True, null=True)
    nbr_jours_symptome = models.TextField(blank=True, null=True)
    non_consultation_postnat1 = models.TextField(blank=True, null=True)
    note_soins_femme = models.TextField(blank=True, null=True)
    soins_femme = models.TextField(blank=True, null=True)
    statut = models.TextField(blank=True, null=True)
    temps_rest_structure = models.TextField(blank=True, null=True)
    type_ref = models.TextField(blank=True, null=True)
    danger_grossesse = models.TextField(blank=True, null=True)
    pourquoi_case = models.TextField(blank=True, null=True)
    sinon_raison = models.TextField(blank=True, null=True)
    non_consultation_postnat2 = models.TextField(blank=True, null=True)
    non_consultation_postnat3 = models.TextField(blank=True, null=True)
    autre_raison_arret = models.TextField(blank=True, null=True)
    confirmation = models.TextField(blank=True, null=True)
    raison_arret = models.TextField(blank=True, null=True)
    survi_enfant = models.TextField(blank=True, null=True)
    closed_date = models.DateTimeField(blank=True, null=True)
    date_deces = models.TextField(blank=True, null=True)
    laits = models.TextField(blank=True, null=True)
    raison_non_allaitement = models.TextField(blank=True, null=True)
    type_lait = models.TextField(blank=True, null=True)
    danger_accouchement = models.TextField(blank=True, null=True)
    accompagnant = models.TextField(blank=True, null=True)
    accouchement_vous = models.TextField(blank=True, null=True)
    autre_raison_accouche = models.TextField(blank=True, null=True)
    bebe_vivant = models.TextField(blank=True, null=True)
    date_dece = models.TextField(blank=True, null=True)
    femme_mort = models.TextField(blank=True, null=True)
    eval_sympt = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cases'

class MobileUser(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    username = models.TextField(blank=True, null=True)
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    user_category = models.TextField(blank=True, null=True)
    poste = models.ForeignKey("accounts.Profil", on_delete=models.DO_NOTHING,
                                   null=True, db_column='poste', related_name='agentCom', verbose_name='poste')
    district = models.TextField(db_column='District', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mobile_user'

class Reference(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    domain = models.TextField(blank=True, null=True)
    caseid = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    date_ref = models.TextField(blank=True, null=True)
    statut = models.TextField(blank=True, null=True)
    indices_femme = models.TextField(db_column='indices.femme', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    closed = models.BooleanField(blank=True, null=True)
    last_modified_by_user_username = models.TextField(blank=True, null=True)
    opened_by_username = models.ForeignKey("MobileUser", on_delete=models.DO_NOTHING,
                                   null=True, db_column='opened_by_username', related_name='reference', verbose_name='poste')
    opened_date = models.DateTimeField(blank=True, null=True)
    owner_name = models.TextField(blank=True, null=True)
    case_link = models.TextField(blank=True, null=True)
    conseil_ipc = models.TextField(blank=True, null=True)
    consulte_ref = models.TextField(blank=True, null=True)
    date_vis_ref = models.TextField(blank=True, null=True)
    retours_sur_la_visite = models.TextField(blank=True, null=True)
    type_de_conseils = models.TextField(blank=True, null=True)
    type_ref = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reference'