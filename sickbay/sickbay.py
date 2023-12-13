class Patient:
    def __init__(self, sex, blood_cell_white, blood_cell_red, platelets, hemoglobin, hematocrit,
                 neutrophiles, eosinophils, bazophiles, lymphocites, monocytes, mcv, mch, mchc, rdw, esr):
        self.sex = sex
        self.is_male = True
        self.pronoun = "Sir"
        if sex == "F":
            self.is_male = False
            self.pronoun = "Madame"
        self.blood_cell_white = blood_cell_white
        self.blood_cell_red = blood_cell_red
        self.platelets = platelets
        self.hemoglobin = hemoglobin
        self.hematocrit = hematocrit
        self.neutrophiles = neutrophiles
        self.eosinophils = eosinophils
        self.bazophiles = bazophiles
        self.lymphocites = lymphocites
        self.monocytes = monocytes
        self.mcv = mcv
        self.mch = mch
        self.mchc = mchc
        self.rdw = rdw
        self.esr = esr



bartek = Patient("M",   #.is_male
                 2,  #.blood_cell_white
                 2,    #.blood_cell_red
                 2,   #.platelets
                 2,   #.hemoglobin
                 2,  #.hematocrit
                 2,  #.neutrophiles
                 2,   #.eosinophils
                 2,   #.bazophiles
                 2,  #.lymphocites
                 2,   #.monocytes
                 2,    #.mcv
                 2,  #.mch
                 2,  #.mchc
                 2,  #.rdw
                 2,      #.esr
                 )
#bartek = Patient("M",   #.is_male
#                 7800,  #.blood_cell_white
#                 47,    #.blood_cell_red
#                 200,   #.platelets
#                 149,   #.hemoglobin
#                 44.2,  #.hematocrit
#                 33.3,  #.neutrophiles
#                 8.7,   #.eosinophils
#                 0.5,   #.bazophiles
#                 48.8,  #.lymphocites
#                 8.3,   #.monocytes
#                 94,    #.mcv
#                 31.7,  #.mch
#                 33.7,  #.mchc
#                 12.4,  #.rdw
#                 2      #.esr
#                 )


msg_crit = 'CRITICAL VALUE - seek medical assistance immediately!'
msg_alarm_low = "alarmingly low"
msg_mod_low = "moderately lowered"
msg_border_low = "borderline lower healthy range"
msg_low_healthy = "lower 25% of healthy range"
msg_mid = "middle 50% of healthy range"
msg_up_healthy = "upper 25% of healthy range"
msg_border_up = "borderline upper healthy range"
msg_mod_elev = "moderately elevated"
msg_alarm_elev = "alarmingly elevated"
error_msg ='ERROR'

def evaluator(val_l, val_h, crit_val_low, crit_val_hi, user_val):
    percentage = 0
    eval_msg = msg_alarm_low
    panic_level_low = crit_val_low
    panic_level_hi = crit_val_hi
    ranges = {
        range(0, 15): msg_border_low,
        range(15, 25): msg_low_healthy,
        range(25, 75): msg_mid,
        range(75, 85): msg_up_healthy,
        range(85, 100): msg_border_up,
    }

    if user_val >= val_l and user_val <= val_h:
        percentage = round((user_val - val_l)/(val_h - val_l)*100)
        for key, value in ranges.items():
            if percentage in key:
                eval_msg = value

    elif user_val < val_l:
        eval_msg = msg_alarm_low
        if round(user_val/val_l*100) >= 90:
            eval_msg = msg_mod_low
        elif panic_level_low == None:
            pass
        elif user_val <= panic_level_low:
            eval_msg = msg_crit

    elif user_val > val_h:
        eval_msg = msg_alarm_elev
        if round(user_val / val_h * 100) <= 111:
            eval_msg = msg_mod_elev
        elif panic_level_hi == None:
            pass
        elif user_val >= panic_level_hi:
            eval_msg = msg_crit

    else:
        percentage = round(user_val/val_h * 100)
    return eval_msg


class White_cells_norm:
    #in thousands/μL

    lowered = 4500
    elevated = 11000
    crit_val_low = 500
    crit_val_hi = 50000

class Red_cells_norm:
    def __init__(self, is_male = True):
        self.is_male = is_male
        self.lowered = 46
        self.elevated = 59
        self.crit_val_low = 4
        self.crit_val_hi = 500

        if not is_male:
            self.lowered = 35
            self.elevated = 55
            self.crit_val_low = 4
            self.crit_val_hi = 500

class Platelets_norm:
    #in thousand/μL dla US MULTIPLY BY 1000!!!
    lowered = 150
    elevated = 400
    crit_val_low = 10
    crit_val_hi = 1000

class Hemoglobin_norm:
    #in g/dL MULTIPLIED BY 10!
    def __init__(self, is_male = True):
        self.is_male = True
        self.lowered = 135
        self.elevated = 175
        self.crit_val_low = 71
        self.crit_val_hi = 250

        if not is_male:
            self.lowered = 120
            self.elevated = 160
            self.crit_val_low = 71
            self.crit_val_hi = 250



class Hematocrit_norm:
    #in %
    def __init__(self, is_male = True):
        self.is_male = True
        self.lowered = 41
        self.elevated = 53
        self.crit_val_low = 22
        self.crit_val_hi = 65
        self.test = {
            range(0, 22): 'CRITICAL VALUE - seek medical assistance immediately!',
            range(22, 36): msg_alarm_low,
            range(36, 41): "moderately lowered",
            range(41, 42): "borderline lower healthy range",
            range(42, 44): "lower 25% of healthy range",
            range(44, 50): "middle 50% of healthy range",
            range(50, 52): "upper 25% of healthy range",
            range(52, 53): "borderline upper healthy range",
            range(53, 65): "alarming",
            range(65, 5000): 'CRITICAL VALUE - seek medical assistance immediately!',
        }
        if not is_male:
            self.lowered = 36
            self.elevated = 46
            self.crit_val_low = 22
            self.crit_val_hi = 65
            self.test = {
                range(0, 22): 'CRITICAL VALUE - seek medical assistance immediately!',
                range(22, 34): msg_alarm_low,
                range(34, 36): "moderately lowered",
                range(36, 37): "borderline lower healthy range",
                range(37, 38): "lower 25% of healthy range",
                range(38, 42): "middle 50% of healthy range",
                range(42, 44): "upper 25% of healthy range",
                range(44, 46): "borderline upper healthy range",
                range(46, 53): "moderately elevated",
                range(53, 65): "alarming",
                range(65, 5000): 'CRITICAL VALUE - seek medical assistance immediately!',
            }
    def range_description(self, tested_value):
        for key, value in self.test.items():
            if tested_value in key:
                print(tested_value)
                return value


class NeutrophilsPercent:
    # in %
    lowered = 40
    elevated = 70
    crit_val_low = None
    crit_val_hi = None
class EosinophilsPercent:
    # in %
    lowered = 1
    elevated = 6
    crit_val_low = None
    crit_val_hi = None
class BazophilesPercent:
    # in %
    lowered = 0
    elevated = 1
    crit_val_low = None
    crit_val_hi = None
class LymphocytesPercent:
    # in %
    lowered = 20
    elevated = 45
    crit_val_low = None
    crit_val_hi = None
class MonocytesPercent:
    # in %
    lowered = 3
    elevated = 8
    crit_val_low = None
    crit_val_hi = None


class MCV:
    #in μm3 (mean corpuscular volume)

    lowered = 80
    elevated = 92
    crit_val_low = None
    crit_val_hi = None
class MCH:
    #in pg (picogram, mean corpuscular hemoglobin)

    lowered = 27
    elevated = 32
    crit_val_low = None
    crit_val_hi = None

class MCHC:
    #in g/dl (mean corpuscular hemoglobin concentration)

    lowered = 32
    elevated = 36
    crit_val_low = None
    crit_val_hi = None

class RDW:
    #in %  (red cell distribution width)

    lowered = 11
    elevated = 14
    crit_val_low = None
    crit_val_hi = None
class ESR: #erythrocyte sedimentation rate Odczyn Biernackiego OB
    def __init__(self, is_male=True):
        self.is_male = True
        self.lowered = 2
        self.elevated = 12
        self.crit_val_low = None
        self.crit_val_hi = None
        if not is_male:
            self.lowered = 2
            self.elevated = 18
            self.crit_val_low = None
            self.crit_val_hi = None
def checker(patient):
    wc_status = "ok"
    if patient.blood_cell_white > White_cells_norm.elevated:
        wc_status = "elevated"
    elif patient.blood_cell_white < White_cells_norm.lowered:
        wc_status = "lowered"

    rc_status = "ok"
    if patient.blood_cell_red > Red_cells_norm(patient.is_male).elevated:
        rc_status = "elevated"
    elif patient.blood_cell_red < Red_cells_norm(patient.is_male).lowered:
        rc_status = "lowered"

    platelets_status = "ok"
    if patient.platelets > Platelets_norm.elevated:
        platelets_status = "elevated"
    elif patient.platelets < Platelets_norm.lowered:
        platelets_status = "lowered"

    hemoglobin_status = "ok"
    if patient.hemoglobin > Hemoglobin_norm(patient.is_male).elevated:
        hemoglobin_status = "elevated"
    elif patient.hemoglobin < Hemoglobin_norm(patient.is_male).lowered:
        hemoglobin_status = "lowered"

    hematocrit_status = "ok"
    if patient.hematocrit > Hematocrit_norm(patient.is_male).elevated:
        hematocrit_status = "elevated"
    elif patient.hematocrit < Hematocrit_norm(patient.is_male).lowered:
        hematocrit_status = "lowered"

    final_assesment = {"wc": wc_status, "rc": rc_status, "plat": platelets_status,
                       "hemo": hemoglobin_status, "hemat": hematocrit_status}
    return final_assesment


def assesment(patient):
    if checker(patient).get('wc') == None:
        return f" "
    wbc_rep = evaluator(White_cells_norm.lowered,
              White_cells_norm.elevated,
              White_cells_norm.crit_val_low,
              White_cells_norm.crit_val_hi,
              patient.blood_cell_white)
    rbc_rep = evaluator(Red_cells_norm(patient.is_male).lowered,
              Red_cells_norm(patient.is_male).elevated,
              Red_cells_norm(patient.is_male).crit_val_low,
              Red_cells_norm(patient.is_male).crit_val_hi,
              patient.blood_cell_red)
    plat_rep = evaluator(Platelets_norm.lowered,
              Platelets_norm.elevated,
              Platelets_norm.crit_val_low,
              Platelets_norm.crit_val_low,
              patient.platelets)
    hemo_rep = evaluator(Hemoglobin_norm(patient.is_male).lowered,
              Hemoglobin_norm(patient.is_male).elevated,
              Hemoglobin_norm(patient.is_male).crit_val_low,
              Hemoglobin_norm(patient.is_male).crit_val_hi,
              patient.hemoglobin)
    hemato_rep = evaluator(Hematocrit_norm(patient.is_male).lowered,
              Hematocrit_norm(patient.is_male).elevated,
              Hematocrit_norm(patient.is_male).crit_val_low,
              Hematocrit_norm(patient.is_male).crit_val_hi,
              patient.hematocrit)
    #msg_crit = "CRITICAL VALUE - seek medical assistance immediately!"

    final_assesment = f'''
    <b>Dear {patient.pronoun}, analysing Your main blood components:</b><br>
    <br>
    White cell count is {checker(patient).get("wc")} {"<b>" if wbc_rep == msg_crit else ''} ({wbc_rep}), </b><br>
    Red cell count is {checker(patient).get("rc")} {"<b>" if rbc_rep == msg_crit else ''} ({rbc_rep}), </b><br>
    Platelets count is {checker(patient).get("plat")} {"<b>" if plat_rep == msg_crit else ''} ({plat_rep}), </b><br>
    Hemoglobin count is {checker(patient).get("hemo")} {"<b>" if hemo_rep == msg_crit else ''} ({hemo_rep}), </b><br>
    Hematocrit count is {checker(patient).get("hemat")} {"<b>" if hemato_rep == msg_crit else ''} ({hemato_rep})</b> <br>
    <br>
               '''
    return final_assesment
def assesment2(patient):
    if checker(patient).get('wc') == None:
        return f" "
    neutro_rep = evaluator(NeutrophilsPercent.lowered,
              NeutrophilsPercent.elevated,
              NeutrophilsPercent.crit_val_low,
              NeutrophilsPercent.crit_val_hi,
              patient.neutrophiles)
    eoz_rep = evaluator(EosinophilsPercent.lowered,
              EosinophilsPercent.elevated,
              EosinophilsPercent.crit_val_low,
              EosinophilsPercent.crit_val_hi,
              patient.eosinophils)
    bazo_rep = evaluator(BazophilesPercent.lowered,
              BazophilesPercent.elevated,
              BazophilesPercent.crit_val_low,
              BazophilesPercent.crit_val_low,
              patient.bazophiles)
    lymp_rep = evaluator(LymphocytesPercent.lowered,
              LymphocytesPercent.elevated,
              LymphocytesPercent.crit_val_low,
              LymphocytesPercent.crit_val_hi,
              patient.lymphocites)
    mono_rep = evaluator(MonocytesPercent.lowered,
              MonocytesPercent.elevated,
              MonocytesPercent.crit_val_low,
              MonocytesPercent.crit_val_hi,
              patient.monocytes)

    mcv_rep = evaluator(MCV.lowered,
              MCV.elevated,
              MCV.crit_val_low,
              MCV.crit_val_hi,
              patient.mcv)
    mch_rep = evaluator(MCH.lowered,
              MCH.elevated,
              MCH.crit_val_low,
              MCH.crit_val_hi,
              patient.mch)
    mchc_rep = evaluator(MCHC.lowered,
              MCHC.elevated,
              MCHC.crit_val_low,
              MCHC.crit_val_hi,
              patient.mchc)
    rdw_rep = evaluator(RDW.lowered,
              RDW.elevated,
              RDW.crit_val_low,
              RDW.crit_val_hi,
              patient.rdw)
    esr_rep = evaluator(ESR(patient.is_male).lowered,
              ESR(patient.is_male).elevated,
              ESR(patient.is_male).crit_val_low,
              ESR(patient.is_male).crit_val_hi,
              patient.esr)
    #msg_crit = "CRITICAL VALUE - seek medical assistance immediately!"

    final_assesment2 = f'''
        \n<br>
        <br>
    Take into consideration:<br>
    <br>
    White cell Neutrophils {patient.neutrophiles} %  is <b>{neutro_rep}</b> (should be between {NeutrophilsPercent.lowered} and {NeutrophilsPercent.elevated} %),<br>
    White cell Eozynophils {patient.eosinophils} % is <b>{eoz_rep}</b> (should be between {EosinophilsPercent.lowered} and {EosinophilsPercent.elevated} %),<br>
    White cell Bazophils {patient.bazophiles} % is <b>{bazo_rep}</b> (should be between {BazophilesPercent.lowered} and {BazophilesPercent.elevated} %),<br>
    White cell Lymphocites {patient.lymphocites} % is <b>{lymp_rep}</b> (should be between {LymphocytesPercent.lowered} and {LymphocytesPercent.elevated} %),<br>
    White cell Monocytes {patient.monocytes} % is <b>{mono_rep}</b> (should be between {MonocytesPercent.lowered} and {MonocytesPercent.elevated} %),<br>

    Red cell mean corpuscular volume (MCV) {patient.mcv} μm3  is <b>{mcv_rep}</b> (should be between {MCV.lowered} and {MCV.elevated} μm3),<br>
    Red cell mean corpuscular hemoglobin (MCH) of {patient.mch} pg is <b>{mch_rep}</b> (should be between {MCH.lowered} and {MCH.elevated} picograms),<br>
    Red cell mean corpuscular hemoglobin concentration (MCHC) of {patient.mchc} g/dl is <b>{mchc_rep}</b> (should be between {MCHC.lowered} and {MCHC.elevated} g/dl),<br>
    Red cell distribution width (RDW) of {patient.rdw}% is <b>{rdw_rep}</b> (should be between {RDW.lowered} and {RDW.elevated} %),<br>
    Erythrocyte sedimentation rate (ESR) of {patient.esr} mm/h is <b>{esr_rep}</b> (should be between {ESR(patient.is_male).lowered} and {ESR(patient.is_male).elevated} mm/h),<br>


    <br>
               '''
    return final_assesment2


def compiler(patient):
    patient_status = "all values are in reference ranges\n "
    for value in checker(patient).values():
        if value != "ok":
            patient_status = f'''
Abnormal level of any component requires further investigation \n 
'''
    return patient_status

def auto_doc(patient):
    #test1 = checker(patient)
    test2 = assesment(patient)
    test3 = compiler(patient)
    test4 = assesment2(patient)
    possible_diagnosis = str(test2)+ str(test3)+ str(test4)

    return possible_diagnosis



print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(auto_doc(bartek))
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
diseases_dictionary = {
    "Infection": ["elevated", "ok", "ok", "ok", "ok"],
    "Inflammation": ["elevated", 'ok', "ok", "ok", "ok"],
    "Stress or Anxiety": ["ok", "ok", "ok", "ok", "ok"],
    "Autoimmune Diseases": ["elevated/lowered", "possibly elevated", "possibly elevated", "possibly elevated", "possibly elevated"],
    "Allergies": ["elevated", "ok", "ok", "ok", "ok"],
    "Corticosteroid Medication": ["elevated", "ok", "ok", "ok", "ok"],
    "Hematologic Disorders": ["elevated/lowered", "possibly elevated", "possibly elevated", "possibly elevated", "possibly elevated"],
    "Trauma or Tissue Damage": ["elevated", "ok", "ok", "ok", "ok"],
    "Polycythemia Vera": ["elevated", "elevated", "elevated", "elevated", "elevated"],
    "Lymphoma": ["elevated/lowered", "possibly elevated", "possibly elevated", "possibly elevated", "possibly elevated"],
    "Leukocytosis": ["elevated", "ok", "ok", "ok", "ok"],
    "Aplastic Anemia": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "HIV": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Chemotherapy and Radiation Exposure": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Systemic Lupus Erythematosus": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Immunosuppressant Medication": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Nutritional Deficiencies (especially B12 and Folic Acid)": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Rheumatoid Arthritis": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Leukemia": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Congenital Neutropenia": ["elevated/lowered", "ok", "ok", "ok", "ok"],
    "Myelofibrosis": ["elevated/lowered", "possibly elevated", "possibly elevated", "possibly elevated", "possibly elevated"],
    "Dehydration": ["ok", "ok", "elevated", "elevated", "ok"],
    "Chronic Hypoxia": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "ok"],
    "High Altitude": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "ok"],
    "Congenital Heart Disease": ["elevated/lowered", "ok", "ok", "ok", "ok"],
    "Kidney Disease": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Secondary Polycythemia": ["elevated", "elevated", "elevated", "elevated", "ok"],
    "Steroid Medication": ["elevated", "ok", "ok", "ok", "ok"],
    "High Testosterone Levels": ["elevated", "elevated", "elevated", "elevated", "ok"],
    "Congenital Polycythemia": ["elevated", "elevated", "elevated", "elevated", "ok"],
    "Smoking": ["elevated", "ok", "ok", "ok", "ok"],
    "Iron-Deficiency Anemia": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Chronic Kidney Diseases": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Myelodysplastic Syndromes": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Hemolysis": ["elevated/lowered", "elevated/lowered", "ok", "ok", "ok"],
    "Hemorrhage": ["elevated/lowered", "elevated/lowered", "ok", "ok", "ok"],
    "Medications": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Thalassemia": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Sickle Cell Anemia": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Malnutrition": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Inflammatory Bowel Disease": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Essential Thrombocythemia": ["ok", "elevated", "ok", "ok", "ok"],
    "Splenectomy": ["elevated/lowered", "ok", "ok", "ok", "ok"],
    "Antibiotic Medication": ["ok", "ok", "ok", "ok", "ok"],
    "Myeloproliferative Disorders": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Sickle Cell Disease": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Tuberculosis": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Surgical Procedure Recuperation": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Asplenia": ["elevated", "ok", "possibly elevated", "ok", "ok"],
    "Vasculitis": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Endocarditis": ["ok", "ok", "ok", "ok", "ok"],
    "Idiopathic Thrombocytopenic Purpura": ["ok", "elevated/lowered", "ok", "ok", "ok"],
    "Epstein-Barr Virus Infection": ["ok", "elevated/lowered", "ok", "ok", "ok"],
    "Alcohol Abuse": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Drug Abuse": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Wiskott-Aldrich Syndrome": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "May-Hegglin Anomaly": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Hepatic Cirrhosis": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Tick-Borne Illnesses": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Heparin-Induced Thrombocytopenia": ["ok", "elevated/lowered", "ok", "ok", "ok"],
    "Systemic Sclerosis": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Erythrocytosis": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Chronic Heart and Lung Conditions": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Congenital Erythrocytosis": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Steroid Abuse": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Chronic Kidney Disease": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Congenital Methemoglobinemia": ["ok", "ok", "ok", "ok", "ok"],
    "Androgen Medications": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "ok"],
    "Obstructive Sleep Apnea": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "ok"],
    "Myelodysplastic Syndrome": ["elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered", "elevated/lowered"],
    "Hemolytic Anemia": ["elevated/lowered", "elevated/lowered", "ok", "ok", "ok"],
    "Acute Blood Loss": ["elevated/lowered", "elevated/lowered", "ok", "ok", "ok"]
}




def is_patient_healthy(patient):
    patient_is_healthy = True
    for value in checker(patient).values():
        if value != "ok":
            patient_is_healthy = False
    return patient_is_healthy

print(is_patient_healthy(bartek))

def automatic_diagnosis(patient):
    healthy_message = "See You in 3 months"
    if not is_patient_healthy(patient):
        patient_to_check = list(checker(patient).values())
        disease_library = diseases_dictionary.items()
        likely = []
        possible = []
        worth_considering = []
        for key, values in disease_library:
            counter = 0
            possibility_check = 0
            for value in values:
                if value == patient_to_check[counter]:
                    possibility_check += 2
                elif value == "elevated/lowered" and patient_to_check[counter] == "elevated" or patient_to_check[
                    counter] == "lowered":
                    possibility_check += 1
                elif value != patient_to_check[counter]:
                    possibility_check -= 5
                counter += 1
            if possibility_check > 8:
                likely.append(key)
            elif possibility_check in range(4, 8):
                possible.append(key)
            elif possibility_check in range(0, 4):
                worth_considering.append(key)
        if likely == []:
            likely.append('nothing')
        if possible == []:
            possible.append('nothing')
        if worth_considering == []:
            worth_considering.append('nothing')
        return likely, possible, worth_considering
    # all in one solution without division for 3 lists:
    #       final_assesment = f'''
    #       likely (more than 75% chance):
    #       {", ".join(map(str, likely))}
    #       moderately likely (more than 50% chance):
    #       {", ".join(map(str, possible))}
    #       also worth considering:
    #       {", ".join(map(str, worth_considering))}
    #'''
    #       return final_assesment

    else:
        return healthy_message


print('$$$$$$$$$$$$$$$%$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
