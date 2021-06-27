from django.shortcuts import render
from django.contrib.humanize.templatetags.humanize import intcomma
import locale

from dashboard.models import *
from accounts.models import Profil
from django.db.models.functions import  Concat, FirstValue
from django.db.models import Q,  Count, Case, When, F, Value, IntegerField, Sum
from datetime import timedelta, datetime
# Create your views here.

def indexDash(request):

    cases = Cases.objects.all()

    context={
        'cases': cases,
    }

    return render(request, 'dashboard/login.html', context)


def dashboard(request):
    # if User.Profil.user=="ICP" :
    #     utilisateur="Infirmier Chef de poste" 
    # else:
    #     utilisateur="Staff Plan"
   
    nb_ac=MobileUser.objects.filter(poste__poste=request.user.profil.poste).count()
    nb_femme=Cases.objects.filter(opened_by_username__poste=request.user.profil.poste, closed=False).count()
    grossseses=Cases.objects.filter(opened_by_username__poste=request.user.profil.poste, enceinte = 'oui').count()
    accouchement=Cases.objects.filter(opened_by_username__poste=request.user.profil.poste, accouche = 'oui').count()

    #nombre de reférence
    nb_ref=Reference.objects.filter(Q(opened_by_username__poste=request.user.profil.poste) 
    & Q(opened_date__gte= datetime.now() - timedelta(days=30))).count()
    nb_ref60=Reference.objects.filter(Q(opened_by_username__poste=request.user.profil.poste) 
    & Q(opened_date__gte= datetime.now() - timedelta(days=30))).count()

    if nb_ref60 - nb_ref ==0 :
        varRef= 100
    elif  nb_ref == 0 and nb_ref60==0: 
        varRef=0
    else:
        varRef =  100 * (2*nb_ref - nb_ref60)/(nb_ref60 - nb_ref)

    if varRef > 0 : 
        class_ref = "fa-caret-up text-success"
    elif varRef == 0 :
        class_ref =''
    else:
        class_ref = "fa-caret-down text-danger"


    cpn=Cases.objects.filter(Q(opened_by_username__poste=request.user.profil.poste) 
    & (Q(cpn4_date__gte= datetime.now() - timedelta(days=30)) |
    Q(cpn3_date__gte= datetime.now() - timedelta(days=30)) | 
    Q(cpn2_date__gte= datetime.now() - timedelta(days=30))  |
    Q(cpn1_date__gte= datetime.now() - timedelta(days=30)))).count()
    cpn60=Cases.objects.filter(Q(opened_by_username__poste=request.user.profil.poste) 
            & (Q(cpn4_date__gte= datetime.now() - timedelta(days=60)) |
            Q(cpn3_date__gte= datetime.now() - timedelta(days=60)) | 
            Q(cpn2_date__gte= datetime.now() - timedelta(days=60))  |
            Q(cpn1_date__gte= datetime.now() - timedelta(days=60)))).count()
    if cpn60 - cpn ==0 :
        varCPN= 100
    elif  cpn == 0 and cpn60==0: 
        varCPN=0
    else:
        varCPN =  100 * (2*cpn - cpn60)/(cpn60 - cpn)

    cpon=Cases.objects.filter(Q(opened_by_username__poste=request.user.profil.poste) 
    & (Q(date_cpon3__gte= datetime.now() - timedelta(days=30)) | 
    Q(date_cpon2__gte= datetime.now() - timedelta(days=30))  |
    Q(date_cpon1__gte= datetime.now() - timedelta(days=30)))).count()
    
    cpon60=Cases.objects.filter(Q(opened_by_username__poste=request.user.profil.poste) 
            & (Q(date_cpon3__gte= datetime.now() - timedelta(days=60)) | 
            Q(date_cpon2__gte= datetime.now() - timedelta(days=60))  |
            Q(date_cpon1__gte= datetime.now() - timedelta(days=60)))).count()
    
    if cpon60 - cpon ==0 :
        varcpon= 100
    elif  cpon == 0 and cpon60==0: 
        varcpon=0
    else:
        varcpon = 100 * (2*cpon - cpon60)/(cpon60 - cpon)
    
    #classe CPN
    if varCPN > 0 : 
        class_cpn = "fa-caret-up text-success"
    elif varCPN == 0 :
        class_cpn =''
    else:
        class_cpn = "fa-caret-down text-danger"

    if varcpon > 0 : 
        class_cpon="fa-caret-up text-success"
    elif varCPN == 0 :
        class_cpon =''
    else:
        class_cpon="fa-caret-down text-danger"

    statAgent=Cases.objects.filter(opened_by_username__poste=request.user.profil.poste).values('opened_by_username', 'opened_by_username__first_name', 'opened_by_username__last_name').annotate(femme=Count('closed',filter=Q(closed=False)), enceinte=Count('enceinte', 
        filter=Q(enceinte='oui')), accouchement=Count('accouche', filter=Q(accouche='oui')))
    
    
    statWomen=Cases.objects.filter(opened_by_username__poste=request.user.profil.poste).values('opened_by_username', 'opened_by_username__first_name', 'opened_by_username__last_name').annotate(femme=Count('closed',filter=Q(closed=False)), enceinte=Count('enceinte', 
        filter=Q(enceinte='oui')), accouchement=Count('accouche', filter=Q(accouche='oui')))

    context = {
        'nb_ac': nb_ac,
        'nb_femme': nb_femme,
        'grossseses' : grossseses,
        'accouchement' : accouchement,
        'cpn' :cpn,
        'varCPN' : varCPN,
        'cpon' :cpon,
        'varcpon' : varcpon, 
        'class_cpn' : class_cpn,
        'class_cpon': class_cpon,
        'nb_ref': nb_ref,
        'varRef': varRef,
        'class_ref': class_ref,
        'statAgent': statAgent,
        'statWomen': statWomen
    }
    return render(request, 'dashboard/index.html', context)

def acFolder(request, ac):
    nom_ac=MobileUser.objects.filter(id = ac).values('first_name', 'last_name')[0]
    femmes= Cases.objects.filter(opened_by_username=ac, 
        closed=False).values('id', 'name', 'age_cal', 'enceinte', 'accouche', 'telephone', 'nom_mari', 'groupe_soutien','marainne', 'tel_maraine','femme_vivant')
    context= {
        'ac': ac,
        'nom_ac' : nom_ac,
        'femmes': femmes
    }
    return render(request, 'dashboard/ac-folder.html', context)

def womanFolder (request, ac, femme):
     nom_ac=MobileUser.objects.filter(id = ac).values('first_name', 'last_name')[0]
     femmesd= Cases.objects.filter(id=femme,  closed=False).values('id', 'adresse',		'cpn1',	'cpn1_date',	'cpn2',	'cpn2_date',	
        'cpn3',	'cpn3_date',	'cpn4',	'cpn4_date',	'sp1',	'sp2',	'sp3',	'accompagnantcpn',	'accompagne',	'accompagne1',	'accompagne_accouche',	'accouche',	'accouchement_effectue',	
        'age_cal',	'age_femme',	'age_grossesse_mois',	'age_grossesse_semaine',	'aller_poste_sante',	'aller_poste_sante1',
        'avisespacement',	'bien_accueilli',	'bilan',		'complication',	'complication_accouche',	
        'complication_precedent',		'connaissance_date',	'connaissance_gsh',	'consultation_postnat1',	'consultation_postnat2',	'consultation_postnat3',	'covid_fait',	'danger_accouchement',
        'danger_grossesse',	'date_cpon1',	'date_cpon2',	'date_cpon3',	'date_accouchement',	'date_de_naissance',	'date_dece',	'date_deces',	'date_dernier_regle',	'date_ref',	'depistagevih',	'donneur',
        'enceinte',	'enfant_vivant', 'eval_sympt',	'faire_cpon1',	'femme_mort',	'femme_vivant',		'groupe_soutien',	'gsh',	'ident_donneur',	'is_accomp',	'kit',	'lait_maternel',	'laits',	'lieu_acc',	'lieu_daccouchement',	'marainne',	'membre_ocb',	'methonde',	'montant_transport',
        'motif',	'motif_depist',	 'moustiquaire',	'moyen_transport',	'moyen_transport1',	'name',	'nb_cpn_visit',	'nb_passagecpon',	'nb_visit',	'nbr_enfants_nes',	'nbr_jours_symptome',	'nom_mari',	'nombre_grossesse',	'non_consultation_postnat1',	'non_consultation_postnat2',	'non_consultation_postnat3',	'note_bilan',	'note_felicita',	'note_soins_femme',	'num_donneur',	'pas_accouche_poste',	'poste_sante',	'pourquoi_case',	'prime_grossesse',	'prochain_cpn',	'prochain_rv',
        		'raison_arret',	'raison_manqcpn',	'raison_non_allaitement',	'reference',	'respect_cpn',	'respect_rdv',		'soins_femme',		'souhait_pf',	'sous_moustiquaire',	'statut',	'survi_enfant',	'tel_maraine',	'telephone',	'temps_rest_structure',	'transfusion',	'transport',	'typ_accouche',	'type_lait',	'type_ref',	'nom_mari',	'closed',	'closed_date')[0]
     context= {
        'ac': ac,
        'femmesd': femmesd
     }
     return render(request, 'dashboard/femme-folder.html', context)

def search(request):
    if request.method == 'POST' :
        test = "ok"
    #nom_ac=MobileUser.objects.filter(id = '').values('first_name', 'last_name')[0]
    #femmes= Cases.objects.filter(opened_by_username='oumar', 
    #    closed=False).values('id', 'name', 'age_cal', 'enceinte', 'accouche', 'telephone', 'nom_mari', 'groupe_soutien','marainne', 'tel_maraine','femme_vivant')
    context= {
        #'nom_ac' : nom_ac,
        #'femmes': femmes
    }
    return render(request, "dashboard/search_woman.html", {'test' : test})