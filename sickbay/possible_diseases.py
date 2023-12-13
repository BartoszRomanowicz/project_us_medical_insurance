from sickbay import Patient

#ICD10
diseases = {
###########highened WC
"Infection" : ['elevated','elevated','elevated','elevated','elevated'],
"Inflammation" : ['elevated','ok','ok','ok','ok'],
"Stress or anxiety" : ['elevated','ok','ok','ok','ok'],
"Autoimmune diseases" : ['elevated','ok','ok','ok','ok'],
"Allergies" : ['elevated','ok','ok','ok','ok'],
"Corticosteroid meducation" : ['elevated','ok','elevated','ok','ok'],
"Hematologic disorders" : ['elevated','ok','ok','ok','ok'],
"Trauma or tissue damage" : ['elevated','ok','ok','ok','ok'],
"Polycythemia vera" : ['elevated','elevated','elevated','elevated','elevated'],
"Lymphoma" : ['elevated','ok','ok','ok','ok'],
"Leukocytosis" : ['elevated','elevated','ok','ok','ok'],
###########lowered WC
"Aplastic anemia" : ['lowered','lowered','lowered','lowered','ok'],
"HIV" : ['lowered','lowered','lowered','lowered','ok'],
"Chemotherapy and radiation exposure" : ['lowered','lowered','lowered','ok','ok'],
"Systemic lupus erythematosus" : ['lowered','ok','ok','ok','ok'],
"Immunosupressant medication" : ['lowered','ok','ok','ok','ok'],
"Nutritional deficiencies (especially B12 and follic acid)" : ['lowered','lowered','ok','lowered','ok'],
"Rheumatodi arthritis" : ['lowered','lowered','elevated','ok','ok'],
"Leukemia" : ['elevated','ok','lowered','ok','ok'],
"Congenital neutropenia" : ['lowered','ok','ok','ok','ok'],
"Myelofibrosis" : ['lowered','ok','elevated','ok','ok'],
###########highened RC
"Dehydration" : ['ok','elevated','ok','elevated','elevated'],
"Chronic hypoxia" : ['ok','elevated','ok','elevated','ok'],
"High altitude" : ['ok','elevated','ok','elevated','elevated'],
"Congenital heart disease" : ['ok','elevated','ok','ok','ok'],
"Kidney disease" : ['ok','elevated','ok','ok','ok'],
"Secondary lolycythemia" : ['ok','elevated','ok','ok','ok'],
"Steroid medication" : ['elevated','ok','ok','ok','ok'],
"High testosterone levels" : ['elevated','elevated','ok','ok','ok'],
"Congenital polycythemia" : ['ok','elevated','ok','ok','ok'],
"Smoking" : ['elevated','elevated','ok','elevated','elevated'],
###########lowered WC
"Iron-deficiency anemia" : ['ok','lowered','elevated','lowered','ok'],
"Chronic kidney diseases" : ['ok','lowered','ok','ok','ok'],
"Myelodysplastic syndromes" : ['ok','lowered','lowered','ok','ok'],
"Hemolysis" : ['ok','lowered','ok','ok','ok'],
"Hemorrhage" : ['ok','lowered','ok','ok','ok'],
"Medications" : ['ok','lowered','ok','ok','ok'],
"Hepatitis" : ['ok','lowered','lowered','lowered','ok'],
"Thalassemia" : ['ok','lowered','ok','lowered','ok'],
"Sickle cell anemia" : ['ok','lowered','ok','lowered','ok'],
"Malnutrition" : ['lowered','lowered','ok','lowered','ok'],
###########highened plat
"Inflammatory bowel disease" : ['ok','ok','elevated','ok','ok'],
"Essential thrombocythemia" : ['ok','ok','elevated','ok','ok'],
"Splenectomy" : ['ok','ok','ok','elevated','elevated'],
"Antibiotic medication" : ['elevated','ok','elevated','ok','ok'],
"Myeloproliferative disorders" : ['elevated','ok','elevated','ok','ok'],
"Sickle cell disease" : ['elevated','ok','elevated','ok','ok'],
"Tuberculosis" : ['elevated','ok','elevated','ok','ok'],
"Surgical procedure recuperation" : ['elevated','ok','elevated','ok','ok'],
"Asplenia" : ['elevated','elevated','elevated','ok','ok'],
"Vasculitis" : ['elevated','ok','elevated','ok','ok'],
"Endocarditis" : ['elevated','elevated','elevated','ok','ok'],
###########lowered plat 10
"Idiopathic thrombocytopenic purpura" : ['ok','ok','lowered','ok','ok'],
"Epstein-Barr virus infection" : ['ok','ok','lowered','ok','ok'],
"Systemic lupus erythematosus " : ['ok','ok','lowered','ok','ok'],
"Alcohol abuse" : ['ok','ok','lowered','ok','ok'],
"Drug abuse" : ['ok','ok','lowered','ok','ok'],
"Wiskott-Aldrich syndrome" : ['ok','ok','lowered','ok','ok'],
"May-Hegglin anomaly" : ['ok','ok','lowered','ok','ok'],
"Hepatic cirrhosis" : ['ok','ok','lowered','ok','ok'],
"Tick-borne illnesses" : ['ok','ok','lowered','ok','ok'],
"Heparin-Induced thrombocytopenia" : ['ok','ok','lowered','ok','ok'],
"Systemic sclerosis" : ['ok','ok','lowered','ok','ok'],
###########highened hemoglobin 7
"Erythrocytosis" : ['ok','ok','ok','elevated','ok'],
"Chronic heart and lung conditions" : ['ok','ok','ok','elevated','ok'],
"Congenital erythrocytosis" : ['ok','ok','ok','elevated','elevated'],
"Steroid abuse" : ['ok','ok','ok','elevated','ok'],
"Chronic kidney disease" : ['ok','ok','ok','elevated','elevated'],
"Congenital methemoglobinemia" : ['ok','ok','ok','elevated','ok'],
"Androgen medications" : ['ok','ok','ok','elevated','elevated'],
"Obstructive sleep apnea" : ['ok','ok','ok','elevated','ok'],
###########lowered hemoglobin 7
"Myelodysplastic syndrome" : ['ok','ok','ok','lowered','ok'],
"Hemolytic anemia" : ['ok','ok','ok','lowered','ok'],
"Acute blood loss" : ['ok','ok','ok','lowered','ok'],
"Menorrhagia" : ['ok','ok','ok','lowered','ok'],
"Pregnancy-associated anemia" : ['ok','ok','ok','lowered','ok'],
"Cirrhosis" : ['ok','ok','ok','lowered','ok'],
"Alpha-Thalassemia" : ['ok','ok','ok','lowered','ok'],
"Hereditary spherocytosis" : ['ok','ok','ok','lowered','ok'],
###########highened hematocrit
"Chronic obstructive pulmonary disease" : ['ok','ok','ok','elevated','elevated'],
"Primary erythrocytosis" : ['ok','elevated','ok','ok','elevated'],
"Hemochromatosis" : ['ok','ok','ok','ok','elevated'],
"Hemoglobin M disease" : ['ok','ok','ok','ok','elevated'],

            }

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


def evaluator(val_l, val_h, crit_val_low, crit_val_hi, user_val):
    percentage = 0
    eval_msg = msg_alarm_elev
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

        elif user_val <= panic_level_low:
            eval_msg = msg_crit

    elif user_val > val_h:
        eval_msg = msg_alarm_elev
        if round(user_val / val_h * 100) <= 111:
            eval_msg = msg_mod_elev

        elif user_val >= panic_level_hi:
            eval_msg = msg_crit

    else:
        percentage = round(user_val/val_h * 100)
    return eval_msg



#def alarm_val_low(lowered): #0 : -10%
#    val_l = lowered * 0.9
#    return range(0, int(val_l))
#
#
#def alarm_val_hi(elevated): #110% : 550%
#    val_h = elevated * 1.1
#    return range(int(val_h)+1, int(val_h)*5)


class White_cells_norm:
    #in thousands/μL

    lowered = 4500
    elevated = 11000
    crit_val_low = 500
    crit_val_hi = 50000

    #moderately_lowered = moderately_lowered(lowered)
    #border_low = border_low(lowered, elevated)
    #lower_good = lower_good(lowered, elevated)
#
    #median = median(lowered, elevated)
#
    #upper_good = upper_good(lowered, elevated)
    #border_hi = border_hi(lowered, elevated)
    #moderately_elevated = moderately_elevated(elevated)
#
    #panic_val_low = range(0, 500)#crit value @stanford medicine
    #alarm_val_low = range(max(panic_val_low)+1, min(moderately_lowered))
#
    #panic_val_hi = range(50_000, 150_001)#crit value @stanford medicine
    #alarm_val_hi = range(max(moderately_elevated)+1, min(panic_val_hi))
#
#
    #test = {
    #    range(0, 501): msg_crit,
    #    range(501, 4500): msg_alarm_low,
    #    range(4500, 5001): msg_border_low ,
    #    range(5001, 6125): msg_low_healthy,
    #    range(6125, 9375): msg_mid,
    #    range(9375, 9_999): msg_up_healthy,
    #    range(10_000, 11_001): msg_border_up,
    #    range(11_001, 21_001): msg_mod_elev,
    #    range(21_001, 50_000): msg_alarm_elev,
    #    range(50_000, 150_001): msg_crit,
    #}




class Red_cells_norm:
    def __init__(self, is_male = True):
        self.is_male = is_male
        self.lowered = 43
        self.elevated = 59
        #self.moderately_lowered = moderately_lowered(self.lowered)
        #self.border_low = border_low(self.lowered, self.elevated)
        #self.lower_good = lower_good(self.lowered, self.elevated)
#
        #self.median = median(self.lowered, self.elevated)
#
        #self.upper_good = upper_good(self.lowered, self.elevated)
        #self.border_hi = border_hi(self.lowered, self.elevated)
        #self.moderately_elevated = moderately_elevated(self.elevated)
        #self.test = {
        #    range(0, 38): msg_alarm_low,
        #    range(38, 43): "moderately lowered",
        #    range(43, 45): "borderline lower healthy range",
        #    range(45, 47): "lower 25% of healthy range",
        #    range(47, 55): "middle 50% of healthy range",
        #    range(55, 57): "upper 25% of healthy range",
        #    range(57, 60): "borderline upper healthy range",
        #    range(60, 75): "moderately elevated",
        #    range(75, 30000): "alarmingly",}

        if not is_male:
            self.lowered = 35
            self.elevated = 55
        #    self.test = {
        #        range(0, 35): msg_alarm_low,
        #        range(35, 37): "borderline lower healthy range",
        #        range(37, 40): "lower 25% of healthy range",
        #        range(40, 50): "middle 50% of healthy range",
        #        range(50, 53): "upper 25% of healthy range",
        #        range(53, 56): "borderline upper healthy range",
        #        range(56, 75): "moderately elevated",
        #        range(75, 30000): "alarmingly",
        #    }
    def range_description(self, tested_value):
        for key,value in self.test.items():
            if tested_value in key:
                return value


#print(White_cells_norm.panic_val_low)
#print(White_cells_norm.alarm_val_low)
#print(White_cells_norm.moderately_lowered)
#print(White_cells_norm.border_low)
#print(White_cells_norm.lower_good)
#print(White_cells_norm.median)
#print(White_cells_norm.upper_good)
#print(White_cells_norm.border_hi)
#print(White_cells_norm.moderately_elevated)
#print(White_cells_norm.alarm_val_hi)
#print(White_cells_norm.panic_val_hi)
#print(Red_cells_norm.panic_val_low)
#print(Red_cells_norm.alarm_val_low)




bartek = Patient("F", 13500, 35, 300, 149, 44.2)



print('TUTATAJTATUTATAJTATUTATAJTATUTATAJTATUTATAJTATUTATAJTATUTATAJTA')
#y = evaluator(
#    Red_cells_norm(bartek.is_male).lowered,
#    Red_cells_norm(bartek.is_male).elevated,
#
#    bartek.blood_cell_red)
#print(bartek.blood_cell_red)
#print(Red_cells_norm(bartek.is_male).lowered)
#print(Red_cells_norm(bartek.is_male).elevated)
#print(bartek.is_male)
#print(y)
y = evaluator(White_cells_norm.lowered,
              White_cells_norm.elevated,
              White_cells_norm.crit_val_low,
              White_cells_norm.crit_val_hi,
              bartek.blood_cell_white)
print(White_cells_norm.lowered)
print(White_cells_norm.elevated)
print(White_cells_norm.crit_val_low)
print(White_cells_norm.crit_val_hi)
print(bartek.blood_cell_white)

print(y)
print('TUTATAJTATUTATAJTATUTATAJTATUTATAJTATUTATAJTATUTATAJTATUTATAJTA')
def assesment(patient):
    if checker(patient).get('wc') == None:
        return f"check error "
    wbc_rep = evaluator(White_cells_norm.lowered,
              White_cells_norm.elevated,
              White_cells_norm.crit_val_low,
              White_cells_norm.crit_val_hi,
              patient.blood_cell_white)
    rbc_rep = Red_cells_norm(patient.is_male).range_description(patient.blood_cell_red)
    plat_rep = "".join(list(value for key,value in Platelets_norm.test.items() if patient.platelets in key))
    hemo_rep = Hemoglobin_norm(patient.is_male).range_description(patient.hemoglobin)
    hemato_rep = Hematocrit_norm(patient.is_male).range_description(patient.hematocrit)
    crit_msg = "CRITICAL VALUE - seek medical assistance immediately!"
    final_assesment = f'''
Dear {patient.pronoun}, Your:<br>
<br>
white cell count is {checker(patient).get("wc")} {"<b>" if wbc_rep == crit_msg else ''} ({wbc_rep}), </b><br>
red cell count is {checker(patient).get("rc")} {"<b>" if rbc_rep == crit_msg else ''} ({rbc_rep}), </b><br>
platelets count is {checker(patient).get("plat")} {"<b>" if plat_rep == crit_msg else ''} ({plat_rep}), </b><br>
hemoglobin count is {checker(patient).get("hemo")} {"<b>" if hemo_rep == crit_msg else ''} ({hemo_rep}), </b><br>
hematocrit count is {checker(patient).get("hemat")} {"<b>" if hemato_rep == crit_msg else ''} ({hemato_rep})</b> <br>
<br>
           '''
    return final_assesment

