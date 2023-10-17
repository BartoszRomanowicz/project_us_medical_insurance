class Patient:
    def __init__(self, sex, blood_cell_white, blood_cell_red, platelets, hemoglobin, hematocrit):
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


patient_anne = Patient("F",10000,5,40,15,60)
patient1 = Patient("F",10000,4,40,15,60)
patient2 = Patient("M", 100000, 4, 0, 1000, 1000)
bartek = Patient("M", 7800, 4.7, 200, 14.9, 44.2)


class White_cells_norm:
    lowered = 4500
    hightened = 11000


class Red_cells_norm:
    def __init__(self, is_male = True):
        self.is_male = is_male
        self.lowered = 4.3
        self.hightened = 5.9
        if not is_male:
            self.lowered = 3.5
            self.hightened = 5.5


class Platelets_norm:
    lowered = 150
    hightened = 400


class Hemoglobin_norm:
    def __init__(self, is_male = True):
        self.is_male = True
        self.lowered = 13.5
        self.hightened = 17.5
        if not is_male:
            self.lowered = 12
            self.hightened = 16


class Hematocrit_norm:
    def __init__(self, is_male = True):
        self.is_male = True
        self.lowered = 41
        self.hightened = 53
        if not is_male:
            self.lowered = 36
            self.hightened = 46

def checker(patient):
    wc_status = "ok"
    if patient.blood_cell_white > White_cells_norm.hightened:
        wc_status = "hightened"
    elif patient.blood_cell_white < White_cells_norm.lowered:
        wc_status = "lowered"

    rc_status = "ok"
    if patient.blood_cell_red > Red_cells_norm(patient.is_male).hightened:
        rc_status = "hightened"
    elif patient.blood_cell_red < Red_cells_norm(patient.is_male).lowered:
        rc_status = "lowered"

    platelets_status = "ok"
    if patient.platelets > Platelets_norm.hightened:
        platelets_status = "hightened"
    elif patient.platelets < Platelets_norm.lowered:
        platelets_status = "lowered"

    hemoglobin_status = "ok"
    if patient.hemoglobin > Hemoglobin_norm(patient.is_male).hightened:
        hemoglobin_status = "hightened"
    elif patient.hemoglobin < Hemoglobin_norm(patient.is_male).lowered:
        hemoglobin_status = "lowered"

    hematocrit_status = "ok"
    if patient.hematocrit > Hematocrit_norm(patient.is_male).hightened:
        hematocrit_status = "hightened"
    elif patient.hematocrit < Hematocrit_norm(patient.is_male).lowered:
        hematocrit_status = "lowered"

    final_assesment = {"wc": wc_status, "rc": rc_status, "plat": platelets_status,
                       "hemo": hemoglobin_status, "hemat": hematocrit_status}
    return final_assesment


def assesment(patient):
    final_assesment = f'''
Dear {patient.pronoun}:
your white cell count is {checker(patient).get("wc")}, 
red cell count is {checker(patient).get("rc")}, 
platelets count is {checker(patient).get("plat")}, 
hemoglobin count is {checker(patient).get("hemo")}, 
hematocrit count is {checker(patient).get("hemat")} 
           '''
    return final_assesment


def compiler(patient):
    patient_status = "all is good, stay fit and healthy"
    for value in checker(patient).values():
        if value != "ok":
            patient_status = f'''
Abnormal levels of these components may indicate:\n
-nutritional deficiencies, such as vitamin B6 or B12
-anemia (iron deficiency)
-clotting problems
-blood cancer
-infection
-immune system disorders \n
Based on your results, your doctor will order follow-up tests to confirm abnormal levels and a possible diagnosis.
'''
    return patient_status

def auto_doc(patient):
    #test1 = checker(patient)
    test2 = assesment(patient)
    test3 = compiler(patient)
    possible_diagnosis = str(test2) + "\n" + str(test3)

    return possible_diagnosis

#rint(checker(bartek))
#rint(assesment(bartek))
print(auto_doc(bartek))
print("")

#new_patient = Patient(input("M or F?").upper(), int(input(">")), float(input(">")), int(input(">")), int(input(">")), int(input(">")))
#print(checker(new_patient))
#print(assesment(new_patient))
#print(compiler(new_patient))

#