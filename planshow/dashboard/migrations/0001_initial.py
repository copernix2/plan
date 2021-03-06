# Generated by Django 3.2.4 on 2021-06-11 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('domain', models.TextField(blank=True, null=True)),
                ('caseid', models.TextField(blank=True, null=True)),
                ('adresse', models.TextField(blank=True, db_column='Adresse', null=True)),
                ('cpn1', models.TextField(blank=True, db_column='CPN1', null=True)),
                ('cpn1_date', models.TextField(blank=True, db_column='CPN1_date', null=True)),
                ('cpn2', models.TextField(blank=True, db_column='CPN2', null=True)),
                ('accompagnantcpn', models.TextField(blank=True, db_column='accompagnantCPN', null=True)),
                ('age_cal', models.TextField(blank=True, null=True)),
                ('age_femme', models.TextField(blank=True, null=True)),
                ('age_grossesse_mois', models.TextField(blank=True, null=True)),
                ('age_grossesse_semaine', models.TextField(blank=True, null=True)),
                ('complication', models.TextField(blank=True, null=True)),
                ('complication_precedent', models.TextField(blank=True, null=True)),
                ('connaissance_date', models.TextField(blank=True, null=True)),
                ('date_accouchement', models.TextField(blank=True, null=True)),
                ('date_dernier_regle', models.TextField(blank=True, null=True)),
                ('depistagevih', models.TextField(blank=True, db_column='depistageVIH', null=True)),
                ('enceinte', models.TextField(blank=True, null=True)),
                ('enfant_vivant', models.TextField(blank=True, null=True)),
                ('membre_ocb', models.TextField(blank=True, null=True)),
                ('moustiquaire', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('nb_cpn_visit', models.TextField(blank=True, null=True)),
                ('nb_visit', models.TextField(blank=True, null=True)),
                ('nom_mari', models.TextField(blank=True, null=True)),
                ('nombre_grossesse', models.TextField(blank=True, null=True)),
                ('poste_sante', models.TextField(blank=True, null=True)),
                ('prime_grossesse', models.TextField(blank=True, null=True)),
                ('prochain_cpn', models.TextField(blank=True, null=True)),
                ('prochain_rv', models.TextField(blank=True, null=True)),
                ('raison_manqcpn', models.TextField(blank=True, db_column='raison_manqCPN', null=True)),
                ('reference', models.TextField(blank=True, null=True)),
                ('respect_cpn', models.TextField(blank=True, null=True)),
                ('sous_moustiquaire', models.TextField(blank=True, null=True)),
                ('telephone', models.TextField(blank=True, null=True)),
                ('closed', models.BooleanField(blank=True, null=True)),
                ('last_modified_by_user_username', models.TextField(blank=True, null=True)),
                ('opened_by_username', models.TextField(blank=True, null=True)),
                ('opened_date', models.DateTimeField(blank=True, null=True)),
                ('owner_name', models.TextField(blank=True, null=True)),
                ('case_link', models.TextField(blank=True, null=True)),
                ('cpn2_date', models.TextField(blank=True, db_column='CPN2_date', null=True)),
                ('cpn3', models.TextField(blank=True, db_column='CPN3', null=True)),
                ('cpn3_date', models.TextField(blank=True, db_column='CPN3_date', null=True)),
                ('cpn4', models.TextField(blank=True, db_column='CPN4', null=True)),
                ('cpn4_date', models.TextField(blank=True, db_column='CPN4_date', null=True)),
                ('sp1', models.TextField(blank=True, db_column='SP1', null=True)),
                ('sp2', models.TextField(blank=True, db_column='SP2', null=True)),
                ('sp3', models.TextField(blank=True, db_column='SP3', null=True)),
                ('bilan', models.TextField(blank=True, null=True)),
                ('connaissance_gsh', models.TextField(blank=True, null=True)),
                ('donneur', models.TextField(blank=True, null=True)),
                ('groupe_soutien', models.TextField(blank=True, null=True)),
                ('gsh', models.TextField(blank=True, null=True)),
                ('ident_donneur', models.TextField(blank=True, null=True)),
                ('is_accomp', models.TextField(blank=True, null=True)),
                ('kit', models.TextField(blank=True, null=True)),
                ('lieu_acc', models.TextField(blank=True, null=True)),
                ('marainne', models.TextField(blank=True, null=True)),
                ('note_bilan', models.TextField(blank=True, null=True)),
                ('num_donneur', models.TextField(blank=True, null=True)),
                ('tel_maraine', models.TextField(blank=True, null=True)),
                ('transport', models.TextField(blank=True, null=True)),
                ('avisespacement', models.TextField(blank=True, null=True)),
                ('methonde', models.TextField(blank=True, null=True)),
                ('souhait_pf', models.TextField(blank=True, null=True)),
                ('accompagne_accouche', models.TextField(blank=True, null=True)),
                ('accouche', models.TextField(blank=True, null=True)),
                ('accouchement_effectue', models.TextField(blank=True, null=True)),
                ('affiche_viste', models.TextField(blank=True, null=True)),
                ('complication_accouche', models.TextField(blank=True, null=True)),
                ('consultation_postnat1', models.TextField(blank=True, null=True)),
                ('consultation_postnat2', models.TextField(blank=True, null=True)),
                ('consultation_postnat3', models.TextField(blank=True, null=True)),
                ('date_cpon1', models.TextField(blank=True, db_column='date_CPON1', null=True)),
                ('date_cpon2', models.TextField(blank=True, db_column='date_CPON2', null=True)),
                ('date_cpon3', models.TextField(blank=True, db_column='date_CPON3', null=True)),
                ('faire_cpon1', models.TextField(blank=True, null=True)),
                ('femme_vivant', models.TextField(blank=True, null=True)),
                ('lait_maternel', models.TextField(blank=True, null=True)),
                ('lieu_daccouchement', models.TextField(blank=True, null=True)),
                ('nb_passagecpon', models.TextField(blank=True, db_column='nb_passageCPON', null=True)),
                ('nbr_enfants_nes', models.TextField(blank=True, null=True)),
                ('pas_accouche_poste', models.TextField(blank=True, null=True)),
                ('transfusion', models.TextField(blank=True, null=True)),
                ('typ_accouche', models.TextField(blank=True, null=True)),
                ('bien_accueilli', models.TextField(blank=True, null=True)),
                ('covid_fait', models.TextField(blank=True, null=True)),
                ('date_de_naissance', models.TextField(blank=True, null=True)),
                ('non_consultation_postnat2', models.TextField(blank=True, null=True)),
                ('non_consultation_postnat3', models.TextField(blank=True, null=True)),
                ('note_felicita', models.TextField(blank=True, null=True)),
                ('pourquoi_case', models.TextField(blank=True, null=True)),
                ('sinon_raison', models.TextField(blank=True, null=True)),
                ('temps_rest_structure', models.TextField(blank=True, null=True)),
                ('respect_rdv', models.TextField(blank=True, null=True)),
                ('accompagne', models.TextField(blank=True, null=True)),
                ('accompagne1', models.TextField(blank=True, null=True)),
                ('aller_poste_sante', models.TextField(blank=True, null=True)),
                ('aller_poste_sante1', models.TextField(blank=True, null=True)),
                ('autres_motifs', models.TextField(blank=True, null=True)),
                ('date_ref', models.TextField(blank=True, null=True)),
                ('montant_transport', models.TextField(blank=True, null=True)),
                ('motif', models.TextField(blank=True, null=True)),
                ('motif_depist', models.TextField(blank=True, null=True)),
                ('motifs_de_rfrence', models.TextField(blank=True, null=True)),
                ('moyen_transport', models.TextField(blank=True, null=True)),
                ('moyen_transport1', models.TextField(blank=True, null=True)),
                ('nbr_jours_symptome', models.TextField(blank=True, null=True)),
                ('non_consultation_postnat1', models.TextField(blank=True, null=True)),
                ('note_soins_femme', models.TextField(blank=True, null=True)),
                ('soins_femme', models.TextField(blank=True, null=True)),
                ('statut', models.TextField(blank=True, null=True)),
                ('type_ref', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Cases',
                'managed': False,
            },
        ),
    ]
