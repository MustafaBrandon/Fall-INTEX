from django.db import models
from django.db.models.deletion import DO_NOTHING

class Drug(models.Model):
    drugid = models.IntegerField(default=0)
    drugname = models.CharField(max_length=30)
    isopioid = models.CharField(max_length=5)

    class Meta:
        db_table = "pd_drugs"
    
    def __str__(self):
        return (self.drugname)

    
class Prescriber(models.Model):
    npi = models.IntegerField(default=0)
    fname = models.CharField(max_length=11)
    lname = models.CharField(max_length=11)
    gender = models.CharField(max_length=1)
    state = models.CharField(max_length=2)
    credentials = models.CharField(max_length=20)
    specialty = models.CharField(max_length=62)
    isopioidprescriber = models.CharField(max_length=5)
    totalprescriptions = models.IntegerField(default=0)
    abilify = models.IntegerField(default=0)
    acetaminophencodeine = models.IntegerField(default=0)
    acyclovir = models.IntegerField(default=0)
    advairdiskus = models.IntegerField(default=0)
    aggrenox = models.IntegerField(default=0)
    alendronatesodium = models.IntegerField(default=0)
    allopurinol = models.IntegerField(default=0)
    alprazolam = models.IntegerField(default=0)
    amiodaronehcl = models.IntegerField(default=0)
    amitriptylinehcl = models.IntegerField(default=0)
    amlodipinebesylate = models.IntegerField(default=0)
    amlodipinebesylatebenazepril = models.IntegerField(default=0)
    amoxicillin = models.IntegerField(default=0)
    amoxtrpotassiumclavulanate = models.IntegerField(default=0)
    amphetaminesaltcombo = models.IntegerField(default=0)
    atenolol = models.IntegerField(default=0)
    atorvastatincalcium = models.IntegerField(default=0)
    avodart = models.IntegerField(default=0)
    azithromycin = models.IntegerField(default=0)
    baclofen = models.IntegerField(default=0)
    bdultrafinepenneedle = models.IntegerField(default=0)
    benazeprilhcl = models.IntegerField(default=0)
    benicar = models.IntegerField(default=0)
    benicarhct = models.IntegerField(default=0)
    benztropinemesylate = models.IntegerField(default=0)
    bisoprololhydrochlorothiazide = models.IntegerField(default=0)
    brimonidinetartrate = models.IntegerField(default=0)
    bumetanide = models.IntegerField(default=0)
    bupropionhclsr = models.IntegerField(default=0)
    bupropionxl = models.IntegerField(default=0)
    buspironehcl = models.IntegerField(default=0)
    bystolic = models.IntegerField(default=0)
    carbamazepine = models.IntegerField(default=0)
    carbidopalevodopa = models.IntegerField(default=0)
    carisoprodol = models.IntegerField(default=0)
    cartiaxt = models.IntegerField(default=0)
    carvedilol = models.IntegerField(default=0)
    cefuroxime = models.IntegerField(default=0)
    celebrex = models.IntegerField(default=0)
    cephalexin = models.IntegerField(default=0)
    chlorhexidinegluconate = models.IntegerField(default=0)
    chlorthalidone = models.IntegerField(default=0)
    cilostazol = models.IntegerField(default=0)
    ciprofloxacinhcl = models.IntegerField(default=0)
    citalopramhbr = models.IntegerField(default=0)
    clindamycinhcl = models.IntegerField(default=0)
    clobetasolpropionate = models.IntegerField(default=0)
    clonazepam = models.IntegerField(default=0)
    clonidinehcl = models.IntegerField(default=0)
    clopidogrel = models.IntegerField(default=0)
    clotrimazolebetamethasone = models.IntegerField(default=0)
    colcrys = models.IntegerField(default=0)
    combiventrespimat = models.IntegerField(default=0)
    crestor = models.IntegerField(default=0)
    cyclobenzaprinehcl = models.IntegerField(default=0)
    dexilant = models.IntegerField(default=0)
    diazepam = models.IntegerField(default=0)
    diclofenacsodium = models.IntegerField(default=0)
    dicyclominehcl = models.IntegerField(default=0)
    digox = models.IntegerField(default=0)
    digoxin = models.IntegerField(default=0)
    diltiazem24hrcd = models.IntegerField(default=0)
    diltiazem24hrer = models.IntegerField(default=0)
    diltiazemer = models.IntegerField(default=0)
    diltiazemhcl = models.IntegerField(default=0)
    diovan = models.IntegerField(default=0)
    diphenoxylateatropine = models.IntegerField(default=0)
    divalproexsodium = models.IntegerField(default=0)
    divalproexsodiumer = models.IntegerField(default=0)
    donepezilhcl = models.IntegerField(default=0)
    dorzolamidetimolol = models.IntegerField(default=0)
    doxazosinmesylate = models.IntegerField(default=0)
    doxepinhcl = models.IntegerField(default=0)
    doxycyclinehyclate = models.IntegerField(default=0)
    duloxetinehcl = models.IntegerField(default=0)
    enalaprilmaleate = models.IntegerField(default=0)
    escitalopramoxalate = models.IntegerField(default=0)
    estradiol = models.IntegerField(default=0)
    exelon = models.IntegerField(default=0)
    famotidine = models.IntegerField(default=0)
    felodipineer = models.IntegerField(default=0)
    fenofibrate = models.IntegerField(default=0)
    fentanyl = models.IntegerField(default=0)
    finasteride = models.IntegerField(default=0)
    floventhfa = models.IntegerField(default=0)
    fluconazole = models.IntegerField(default=0)
    fluoxetinehcl = models.IntegerField(default=0)
    fluticasonepropionate = models.IntegerField(default=0)
    furosemide = models.IntegerField(default=0)
    gabapentin = models.IntegerField(default=0)
    gemfibrozil = models.IntegerField(default=0)
    glimepiride = models.IntegerField(default=0)
    glipizide = models.IntegerField(default=0)
    glipizideer = models.IntegerField(default=0)
    glipizidexl = models.IntegerField(default=0)
    glyburide = models.IntegerField(default=0)
    haloperidol = models.IntegerField(default=0)
    humalog = models.IntegerField(default=0)
    hydralazinehcl = models.IntegerField(default=0)
    hydrochlorothiazide = models.IntegerField(default=0)
    hydrocodoneacetaminophen = models.IntegerField(default=0)
    hydrocortisone = models.IntegerField(default=0)
    hydromorphonehcl = models.IntegerField(default=0)
    hydroxyzinehcl = models.IntegerField(default=0)
    ibandronatesodium = models.IntegerField(default=0)
    ibuprofen = models.IntegerField(default=0)
    insulinsyringe = models.IntegerField(default=0)
    ipratropiumbromide = models.IntegerField(default=0)
    irbesartan = models.IntegerField(default=0)
    isosorbidemononitrateer = models.IntegerField(default=0)
    jantoven = models.IntegerField(default=0)
    janumet = models.IntegerField(default=0)
    januvia = models.IntegerField(default=0)
    ketoconazole = models.IntegerField(default=0)
    klorcon10 = models.IntegerField(default=0)
    klorconm10 = models.IntegerField(default=0)
    klorconm20 = models.IntegerField(default=0)
    labetalolhcl = models.IntegerField(default=0)
    lactulose = models.IntegerField(default=0)
    lamotrigine = models.IntegerField(default=0)
    lansoprazole = models.IntegerField(default=0)
    lantus = models.IntegerField(default=0)
    lantussolostar = models.IntegerField(default=0)
    latanoprost = models.IntegerField(default=0)
    levemir = models.IntegerField(default=0)
    levemirflexpen = models.IntegerField(default=0)
    levetiracetam = models.IntegerField(default=0)
    levofloxacin = models.IntegerField(default=0)
    levothyroxinesodium = models.IntegerField(default=0)
    lidocaine = models.IntegerField(default=0)
    lisinopril = models.IntegerField(default=0)
    lisinoprilhydrochlorothiazide = models.IntegerField(default=0)
    lithiumcarbonate = models.IntegerField(default=0)
    lorazepam = models.IntegerField(default=0)
    losartanhydrochlorothiazide = models.IntegerField(default=0)
    losartanpotassium = models.IntegerField(default=0)
    lovastatin = models.IntegerField(default=0)
    lovaza = models.IntegerField(default=0)
    lumigan = models.IntegerField(default=0)
    lyrica = models.IntegerField(default=0)
    meclizinehcl = models.IntegerField(default=0)
    meloxicam = models.IntegerField(default=0)
    metforminhcl = models.IntegerField(default=0)
    metforminhcler = models.IntegerField(default=0)
    methadonehcl = models.IntegerField(default=0)
    methocarbamol = models.IntegerField(default=0)
    methotrexate = models.IntegerField(default=0)
    methylprednisolone = models.IntegerField(default=0)
    metoclopramidehcl = models.IntegerField(default=0)
    metolazone = models.IntegerField(default=0)
    metoprololsuccinate = models.IntegerField(default=0)
    metoprololtartrate = models.IntegerField(default=0)
    metronidazole = models.IntegerField(default=0)
    mirtazapine = models.IntegerField(default=0)
    montelukastsodium = models.IntegerField(default=0)
    morphinesulfate = models.IntegerField(default=0)
    morphinesulfateer = models.IntegerField(default=0)
    mupirocin = models.IntegerField(default=0)
    nabumetone = models.IntegerField(default=0)
    namenda = models.IntegerField(default=0)
    namendaxr = models.IntegerField(default=0)
    naproxen = models.IntegerField(default=0)
    nasonex = models.IntegerField(default=0)
    nexium = models.IntegerField(default=0)
    niaciner = models.IntegerField(default=0)
    nifedicalxl = models.IntegerField(default=0)
    nifedipineer = models.IntegerField(default=0)
    nitrofurantoinmonomacro = models.IntegerField(default=0)
    nitrostat = models.IntegerField(default=0)
    nortriptylinehcl = models.IntegerField(default=0)
    novolog = models.IntegerField(default=0)
    novologflexpen = models.IntegerField(default=0)
    nystatin = models.IntegerField(default=0)
    olanzapine = models.IntegerField(default=0)
    omeprazole = models.IntegerField(default=0)
    ondansetronhcl = models.IntegerField(default=0)
    ondansetronodt = models.IntegerField(default=0)
    onglyza = models.IntegerField(default=0)
    oxcarbazepine = models.IntegerField(default=0)
    oxybutyninchloride = models.IntegerField(default=0)
    oxybutyninchlorideer = models.IntegerField(default=0)
    oxycodoneacetaminophen = models.IntegerField(default=0)
    oxycodonehcl = models.IntegerField(default=0)
    oxycontin = models.IntegerField(default=0)
    pantoprazolesodium = models.IntegerField(default=0)
    paroxetinehcl = models.IntegerField(default=0)
    phenobarbital = models.IntegerField(default=0)
    phenytoinsodiumextended = models.IntegerField(default=0)
    pioglitazonehcl = models.IntegerField(default=0)
    polyethyleneglycol3350 = models.IntegerField(default=0)
    potassiumchloride = models.IntegerField(default=0)
    pradaxa = models.IntegerField(default=0)
    pramipexoledihydrochloride = models.IntegerField(default=0)
    pravastatinsodium = models.IntegerField(default=0)
    prednisone = models.IntegerField(default=0)
    premarin = models.IntegerField(default=0)
    primidone = models.IntegerField(default=0)
    proairhfa = models.IntegerField(default=0)
    promethazinehcl = models.IntegerField(default=0)
    propranololhcler = models.IntegerField(default=0)
    propranololhcl = models.IntegerField(default=0)
    quetiapinefumarate = models.IntegerField(default=0)
    quinaprilhcl = models.IntegerField(default=0)
    raloxifenehcl = models.IntegerField(default=0)
    ramipril = models.IntegerField(default=0)
    ranexa = models.IntegerField(default=0)
    ranitidinehcl = models.IntegerField(default=0)
    restasis = models.IntegerField(default=0)
    risperidone = models.IntegerField(default=0)
    ropinirolehcl = models.IntegerField(default=0)
    seroquelxr = models.IntegerField(default=0)
    sertralinehcl = models.IntegerField(default=0)
    simvastatin = models.IntegerField(default=0)
    sotalol = models.IntegerField(default=0)
    spiriva = models.IntegerField(default=0)
    spironolactone = models.IntegerField(default=0)
    sucralfate = models.IntegerField(default=0)
    sulfamethoxazoletrimethoprim = models.IntegerField(default=0)
    sumatriptansuccinate = models.IntegerField(default=0)
    symbicort = models.IntegerField(default=0)
    synthroid = models.IntegerField(default=0)
    tamsulosinhcl = models.IntegerField(default=0)
    temazepam = models.IntegerField(default=0)
    terazosinhcl = models.IntegerField(default=0)
    timololmaleate = models.IntegerField(default=0)
    tizanidinehcl = models.IntegerField(default=0)
    tolterodinetartrateer = models.IntegerField(default=0)
    topiramate = models.IntegerField(default=0)
    toprolxl = models.IntegerField(default=0)
    torsemide = models.IntegerField(default=0)
    tramadolhcl = models.IntegerField(default=0)
    travatanz = models.IntegerField(default=0)
    trazodonehcl = models.IntegerField(default=0)
    triamcinoloneacetonide = models.IntegerField(default=0)
    triamterenehydrochlorothiazid = models.IntegerField(default=0)
    valacyclovir = models.IntegerField(default=0)
    valsartan = models.IntegerField(default=0)
    valsartanhydrochlorothiazide = models.IntegerField(default=0)
    venlafaxinehcl = models.IntegerField(default=0)
    venlafaxinehcler = models.IntegerField(default=0)
    ventolinhfa = models.IntegerField(default=0)
    verapamiler = models.IntegerField(default=0)
    vesicare = models.IntegerField(default=0)
    voltaren = models.IntegerField(default=0)
    vytorin = models.IntegerField(default=0)
    warfarinsodium = models.IntegerField(default=0)
    xarelto = models.IntegerField(default=0)
    zetia = models.IntegerField(default=0)
    ziprasidonehcl = models.IntegerField(default=0)
    zolpidemtartrate = models.IntegerField(default=0)

    class Meta:
        db_table = "pd_prescriber"

    def __str__(self):
        return (self.full_name)

    @property
    def full_name(self):
        return '%s %s' % (self.fname, self.lname)  


class Credential(models.Model):
    npi = models.ForeignKey(Prescriber, on_delete=DO_NOTHING)
    cred_pa = models.CharField(max_length=5)
    cred_phd = models.CharField(max_length=5)
    cred_md = models.CharField(max_length=5)
    cred_dds = models.CharField(max_length=5)
    cred_do = models.CharField(max_length=5)
    cred_np = models.CharField(max_length=5)    
    cred_dpm = models.CharField(max_length=5)
    cred_od = models.CharField(max_length=5)

    class Meta:
        db_table = "pd_credentials"

    def __str__(self):
        return (self.npi) 