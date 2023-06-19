from machinetranslation import translator as tr

TEST1_FR = "Bonjour"
TEST2_FR = "Chien"
TEST1_EN = "Hi"
TEST2_EN = "Dog"

FR_TO_EN1 = tr.frenchToEnglish(TEST1_FR)
FR_TO_EN2 = tr.frenchToEnglish(TEST2_FR)
EN_TO_FR1 = tr.englishToFrench(TEST1_EN)
EN_TO_FR2 = tr.englishToFrench(TEST2_EN)

print(TEST1_FR + " in English is: " + FR_TO_EN1)    # print Test 1 French to English
print(TEST2_FR + " in English is: " + FR_TO_EN2)    # print Test 1 French to English
print(TEST1_EN + " in French is: " + EN_TO_FR1)    # print Test 1 French to English
print(TEST2_EN + " in French is: " + EN_TO_FR2)    # print Test 1 French to English