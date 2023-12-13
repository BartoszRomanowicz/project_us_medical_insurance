from sickbay import Patient, checker


class Disease:
    def __init__(self, name, sex, blood_cell_white, blood_cell_red, platelets, hemoglobin, hematocrit):
        self.name = name
        self.sex = sex
        self.is_male = None #none for both male and female
        if sex == "F":
            self.is_male = False
        if sex == "M":
            self.is_male = True
        self.blood_cell_white = blood_cell_white
        self.blood_cell_red = blood_cell_red
        self.platelets = platelets
        self.hemoglobin = hemoglobin
        self.hematocrit = hematocrit


#1 name##, #2is_male=None##, #3white blood cellls##, #4red blood cellls##,#5plats##, #6hemoglobin##, #7hematocrit##,
dis1 = Disease('lymphi', None,  range(1,66664), range(1,100), range(1,2), range(1,100), range(1,100))
dis2 = Disease('sdfmphi', "M",  [range(1,44), range(10,20)], range(1,100), range(1,100), range(1,100), range(1,100))
dis3 = Disease('disses3', "M",  [range(1,3), range(10,20)], range(1,100), range(1,100), range(1,100), range(1,100))

diseases_list = [dis1, dis2, dis3]

print("55555555555555555555555555555555555555555555")
print(type(dis1.hematocrit))
bartek = Patient("M", 7800, 47, 300, 149, 44.2)
print(bartek.blood_cell_red)
print(dis1.blood_cell_white)
if bartek.blood_cell_white in dis1.blood_cell_white:
    print('yes')
else:
    print("NOOOOOOO")
for item in diseases_list:
    print(item.platelets)
#########
#def automatic_diagnosis2(patient):
#    healthy_message = "See You in 3 months"
#
#    patient_to_check = list(checker(patient).values())
#    disease_library = diseases_list
#
#    likely = []
#    possible = []
#    worth_considering = []
#
#    for disease in disease_library:
#        possibility_check = 0
#        if patient.blood_cell_white in disease.blood_cell_white:
#            possibility_check+= 5
for item in range(1,11):
    print(item)

a = 101

print(f'ossssk { "10" if a == 10 else "11" }')
print("55555555555555555555555555555555555555555555")

val1 = 0
val2 = 0
val3 = 0
val4 = 0
val5 = 0
print("55555555555555555555555555555555555555555555")
if bartek.blood_cell_white in dis1.blood_cell_white:
    val1 = bartek.blood_cell_white
    print(val1)
print("55555555555555555555555555555555555555555555")

#
def automatic_diagnosis2(patient):
    healthy_message = "See You in 3 months"
    patient_to_check = list(checker(patient).values())
    disease_library = diseases_list.items()
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


