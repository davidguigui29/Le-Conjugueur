from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty, BooleanProperty
from kivy.lang import Builder

#Builder.load_file('thelab.kv')

personal_pronouns = ["Je ", "Tu ", "Il ", "Nous ", "Vous ", "Ils "]
present_tense_endings_for_first_group_verbs = ["e", "es", "e", "ons", "ez", "ent"]
simple_future_endings = ["rai", "ras", "ra", "rons", "rez", "ront"]
imparfait_endings = ["ais", "ais", "ait", "ions", "iez", "aient"]
etre_in_present_tense = ["suis", "es", "est", "sommes", "êtes", "sont"]
avoir_in_present_tense = ["ai", "as", "a", "avons", "avez", "ont"]
imparfait_endings_for_second_group_verbs = ["issais", "issais", "issait", "issions", "issiez", "issaient"]
simple_past_endings_for_first_group_verbs = ["ai", "as", "a", "âmes", "âtes", "èrent"]
simple_past_endings_for_second_group_verbs = ["is", "is", "it", "îmes", "îtes", "irent"]
present_tense_endings_for_second_group_verbs = ["is", "is", "it", "issons", "issez", "issent"]
present_tense_endings_for_third_group_verbs = ["s", "s", "", "ons", "ez", "ent"]
vowels = ["a", "e", "i", "o", "u", "y", "h", "é"]
first_group_verbs_past_participle = "é"
#conjugated_verbs = {"first": [], "second": [], "third": []}
third_group_endings = ["enir", "érir", "tir", "vrir", "frir", "llir", "mir", "rir",
                       "vir", "uir", "cevoir", "voir", "loir", "seoir", ]
real_third_group_endings = ["andre", "endre", "ondre", "erdre", "ordre", "attre", "ettre", "eindre", "oindre", "aindre", "aire",
                            "aitre", "oitre", "oire", "ore", "ure", "ivre", "ire", "uire"]
third_group_endings.extend(real_third_group_endings)
tuple_third_group_endings = tuple(third_group_endings)
string_tuple = tuple(third_group_endings)
irregular_endre_verbs_type1 = ["descendre", "défendre"]
irregular_endre_verbs_type2 = ["prendre", "apprendre", "comprendre"]
verbs_of_movement = ["aller", "arriver", "descendre", "entrer", "monter", "mourir", "naître", "partir", "passer", "rester", "sortir", "tomber", "venir"]
print(tuple_third_group_endings)

class Leconjugueur(BoxLayout):

    infinitif = ""

    indicatif_enabled = BooleanProperty(False)

    # Function that conjugate first group verb.
   



    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.modified_letter = "ç"
        self.vowels = vowels
        self.modified_letter_d_to_n = "n"

    def verb_to_conjugate(self):
        # Create variables for our widget
        name = self.ids.name_input.text
        self.infinitif = name
        # update the label
        self.ids.name_label.text = name
        # Store input into variable
        verb = self.ids.name_input.text

        # Clear input box
        #self.ids.name_input.text = ""
        return verb.lower().lstrip().rstrip()
    def infinitive(self):
        self.verb = self.infinitif
        self.ids.name_label.text = self.verb
        # name = self.ids.name_input.text
        # self.ids.name_label.text = name
        # verb = self.ids.name_input.text
        return self.verb.lower().strip()

    def formating(self):
        self.verb = self.verb_to_conjugate()
        self.is_infinitive = (self.verb[-2:])
        self.three_letters_ending_rules = (self.verb[-3:])
        self.four_letters_ending_rules = (self.verb[-4:])
        self.five_letters_ending_rules = (self.verb[-5:])
        self.get_root = self.verb[0:-2]
        self.root_of_simple_future = self.verb[0:-1]
        self.elements = [self.is_infinitive, self.three_letters_ending_rules, self.three_letters_ending_rules,
                         self.four_letters_ending_rules, self.modified_letter, self.modified_letter_d_to_n,
                         self.get_root, self.verb, self.root_of_simple_future]
        return self.elements

    def avoirInPresentTense(self):
        important_elements = self.formating()
        is_infinitive = important_elements[0]
        three_letters_ending_rules = important_elements[1]
        three_letters_ending_rules = important_elements[2]
        four_letters_ending_rules = important_elements[3]
        modified_letter = important_elements[4]
        modified_letter_d_to_n = important_elements[5]
        root = important_elements[6]
        verb = important_elements[7]
        self.verb = verb
        self.personal_pronouns = personal_pronouns
        self.get_root = root
        self.present_tense_endings_for_first_group_verbs = present_tense_endings_for_first_group_verbs
        self.conjugated_verbs = {"first": [], "second": [], "third": []}
        self.vow = ""
        conjugated_verb1 = self.personal_pronouns[0][0] + "'" + avoir_in_present_tense[0]
        conjugated_verb2 = self.personal_pronouns[1] + avoir_in_present_tense[1]
        conjugated_verb3 = self.personal_pronouns[2] + avoir_in_present_tense[2]
        conjugated_verb4 = self.personal_pronouns[3] + avoir_in_present_tense[3]
        conjugated_verb5 = self.personal_pronouns[4] + avoir_in_present_tense[4]
        conjugated_verb6 = self.personal_pronouns[5] + avoir_in_present_tense[5]
        return conjugated_verb1, conjugated_verb2, conjugated_verb3, conjugated_verb4, conjugated_verb5, conjugated_verb6

    def etreInPresentTense(self):
        important_elements = self.formating()
        is_infinitive = important_elements[0]
        three_letters_ending_rules = important_elements[1]
        three_letters_ending_rules = important_elements[2]
        four_letters_ending_rules = important_elements[3]
        modified_letter = important_elements[4]
        modified_letter_d_to_n = important_elements[5]
        root = important_elements[6]
        verb = important_elements[7]
        self.verb = verb
        self.personal_pronouns = personal_pronouns
        self.get_root = root
        self.present_tense_endings_for_first_group_verbs = present_tense_endings_for_first_group_verbs
        self.conjugated_verbs = {"first": [], "second": [], "third": []}
        self.vow = ""
        conjugated_verb1 = self.personal_pronouns[0] + etre_in_present_tense[0]
        conjugated_verb2 = self.personal_pronouns[1] + etre_in_present_tense[1]
        conjugated_verb3 = self.personal_pronouns[2] + etre_in_present_tense[2]
        conjugated_verb4 = self.personal_pronouns[3] + etre_in_present_tense[3]
        conjugated_verb5 = self.personal_pronouns[4] + etre_in_present_tense[4]
        conjugated_verb6 = self.personal_pronouns[5] + etre_in_present_tense[5]
        return conjugated_verb1, conjugated_verb2, conjugated_verb3, conjugated_verb4, conjugated_verb5, conjugated_verb6

    def avoirInImparfait(self):   
        important_elements = self.formating()
        is_infinitive = important_elements[0]
        three_letters_ending_rules = important_elements[1]
        three_letters_ending_rules = important_elements[2]
        four_letters_ending_rules = important_elements[3]
        modified_letter = important_elements[4]
        modified_letter_d_to_n = important_elements[5]
        root = important_elements[6]
        verb = important_elements[7]
        self.verb = verb
        self.personal_pronouns = personal_pronouns
        self.get_root = root
        self.present_tense_endings_for_first_group_verbs = present_tense_endings_for_first_group_verbs
        self.conjugated_verbs = {"first": [], "second": [], "third": []}
        self.vow = ""
        conjugated_verb1 = self.personal_pronouns[0][0] + "'" + self.get_root[:-1] + imparfait_endings[0]
        conjugated_verb2 = self.personal_pronouns[1] + self.get_root[:-1] + imparfait_endings[1]
        conjugated_verb3 = self.personal_pronouns[2] + self.get_root[:-1] + imparfait_endings[2]
        conjugated_verb4 = self.personal_pronouns[3] + self.get_root[:-1] + imparfait_endings[3]
        conjugated_verb5 = self.personal_pronouns[4] + self.get_root[:-1] + imparfait_endings[4]
        conjugated_verb6 = self.personal_pronouns[5] + self.get_root[:-1] + imparfait_endings[5]
        return conjugated_verb1, conjugated_verb2, conjugated_verb3, conjugated_verb4, conjugated_verb5, conjugated_verb6

    def etreInImparfait(self):   
        important_elements = self.formating()
        is_infinitive = important_elements[0]
        three_letters_ending_rules = important_elements[1]
        three_letters_ending_rules = important_elements[2]
        four_letters_ending_rules = important_elements[3]
        modified_letter = important_elements[4]
        modified_letter_d_to_n = important_elements[5]
        root = important_elements[6]
        verb = important_elements[7]
        self.verb = verb
        self.personal_pronouns = personal_pronouns
        self.get_root = root
        self.present_tense_endings_for_first_group_verbs = present_tense_endings_for_first_group_verbs
        self.conjugated_verbs = {"first": [], "second": [], "third": []}
        self.vow = ""
        conjugated_verb1 = self.personal_pronouns[0][0] + "'" + "ét" + imparfait_endings[0]
        conjugated_verb2 = self.personal_pronouns[1] + "ét" + imparfait_endings[1]
        conjugated_verb3 = self.personal_pronouns[2] + "ét" + imparfait_endings[2]
        conjugated_verb4 = self.personal_pronouns[3] + "ét" + imparfait_endings[3]
        conjugated_verb5 = self.personal_pronouns[4] + "ét" + imparfait_endings[4]
        conjugated_verb6 = self.personal_pronouns[5] + "ét" + imparfait_endings[5]
        return conjugated_verb1, conjugated_verb2, conjugated_verb3, conjugated_verb4, conjugated_verb5, conjugated_verb6

    def avoirInSimplePast(self):   
        important_elements = self.formating()
        is_infinitive = important_elements[0]
        three_letters_ending_rules = important_elements[1]
        three_letters_ending_rules = important_elements[2]
        four_letters_ending_rules = important_elements[3]
        modified_letter = important_elements[4]
        modified_letter_d_to_n = important_elements[5]
        root = important_elements[6]
        verb = important_elements[7]
        self.verb = verb
        self.personal_pronouns = personal_pronouns
        self.get_root = root
        self.present_tense_endings_for_first_group_verbs = present_tense_endings_for_first_group_verbs
        self.conjugated_verbs = {"first": [], "second": [], "third": []}
        self.vow = ""
        conjugated_verb1 = self.personal_pronouns[0][0] + "'" + "eus"
        conjugated_verb2 = self.personal_pronouns[1] + "eus"
        conjugated_verb3 = self.personal_pronouns[2] + "eut"
        conjugated_verb4 = self.personal_pronouns[3] + "eûmes"
        conjugated_verb5 = self.personal_pronouns[4] + "eûtes"
        conjugated_verb6 = self.personal_pronouns[5] + "eurent"
        return conjugated_verb1, conjugated_verb2, conjugated_verb3, conjugated_verb4, conjugated_verb5, conjugated_verb6

    
    def etreInSimplePast(self):   
        important_elements = self.formating()
        is_infinitive = important_elements[0]
        three_letters_ending_rules = important_elements[1]
        three_letters_ending_rules = important_elements[2]
        four_letters_ending_rules = important_elements[3]
        modified_letter = important_elements[4]
        modified_letter_d_to_n = important_elements[5]
        root = important_elements[6]
        verb = important_elements[7]
        self.verb = verb
        self.personal_pronouns = personal_pronouns
        self.get_root = root
        self.present_tense_endings_for_first_group_verbs = present_tense_endings_for_first_group_verbs
        self.conjugated_verbs = {"first": [], "second": [], "third": []}
        self.vow = ""
        conjugated_verb1 = self.personal_pronouns[0] + "fus"
        conjugated_verb2 = self.personal_pronouns[1] + "fus"
        conjugated_verb3 = self.personal_pronouns[2] + "fut"
        conjugated_verb4 = self.personal_pronouns[3] + "fûmes"
        conjugated_verb5 = self.personal_pronouns[4] + "fûtes"
        conjugated_verb6 = self.personal_pronouns[5] + "furent"
        return conjugated_verb1, conjugated_verb2, conjugated_verb3, conjugated_verb4, conjugated_verb5, conjugated_verb6

    def etreInSimpleFuture(self):   
        important_elements = self.formating()
        is_infinitive = important_elements[0]
        three_letters_ending_rules = important_elements[1]
        three_letters_ending_rules = important_elements[2]
        four_letters_ending_rules = important_elements[3]
        modified_letter = important_elements[4]
        modified_letter_d_to_n = important_elements[5]
        root = important_elements[6]
        verb = important_elements[7]
        self.verb = verb
        self.personal_pronouns = personal_pronouns
        self.get_root = root
        self.present_tense_endings_for_first_group_verbs = present_tense_endings_for_first_group_verbs
        self.conjugated_verbs = {"first": [], "second": [], "third": []}
        self.vow = ""
        conjugated_verb1 = self.personal_pronouns[0] + "se" + simple_future_endings[0]
        conjugated_verb2 = self.personal_pronouns[1] + "se" + simple_future_endings[1]
        conjugated_verb3 = self.personal_pronouns[2] + "se" + simple_future_endings[2]
        conjugated_verb4 = self.personal_pronouns[3] + "se" + simple_future_endings[3]
        conjugated_verb5 = self.personal_pronouns[4] + "se" + simple_future_endings[4]
        conjugated_verb6 = self.personal_pronouns[5] + "se" + simple_future_endings[5]
        return conjugated_verb1, conjugated_verb2, conjugated_verb3, conjugated_verb4, conjugated_verb5, conjugated_verb6

    
    def avoirInSimpleFuture(self):   
        important_elements = self.formating()
        is_infinitive = important_elements[0]
        three_letters_ending_rules = important_elements[1]
        three_letters_ending_rules = important_elements[2]
        four_letters_ending_rules = important_elements[3]
        modified_letter = important_elements[4]
        modified_letter_d_to_n = important_elements[5]
        root = important_elements[6]
        verb = important_elements[7]
        self.verb = verb
        self.personal_pronouns = personal_pronouns
        self.get_root = root
        self.present_tense_endings_for_first_group_verbs = present_tense_endings_for_first_group_verbs
        self.conjugated_verbs = {"first": [], "second": [], "third": []}
        self.vow = ""
        conjugated_verb1 = self.personal_pronouns[0][0] + "'" + "au" + simple_future_endings[0]
        conjugated_verb2 = self.personal_pronouns[1] + "au" + simple_future_endings[1]
        conjugated_verb3 = self.personal_pronouns[2] + "au" + simple_future_endings[2]
        conjugated_verb4 = self.personal_pronouns[3] + "au" + simple_future_endings[3]
        conjugated_verb5 = self.personal_pronouns[4] + "au" + simple_future_endings[4]
        conjugated_verb6 = self.personal_pronouns[5] + "au" + simple_future_endings[5]
        return conjugated_verb1, conjugated_verb2, conjugated_verb3, conjugated_verb4, conjugated_verb5, conjugated_verb6


    def conjugate_first_group_verbs_in_simple_present(self):  # vowels, root, personal_pronouns, present_tense_endings_for_first_group_verbs):
        # global root, important_elements, vowels, is_infinitive, three_letters_ending_rules, three_letters_ending_rules,
        # four_letters_ending_rules, modified_letter_d_to_n
        important_elements = self.formating()
        is_infinitive = important_elements[0]
        three_letters_ending_rules = important_elements[1]
        three_letters_ending_rules = important_elements[2]
        four_letters_ending_rules = important_elements[3]
        modified_letter = important_elements[4]
        modified_letter_d_to_n = important_elements[5]
        root = important_elements[6]
        verb = important_elements[7]
        self.verb = verb
        self.personal_pronouns = personal_pronouns
        self.get_root = root
        self.present_tense_endings_for_first_group_verbs = present_tense_endings_for_first_group_verbs
        self.conjugated_verbs = {"first": [], "second": [], "third": []}
        self.vow = ""
        
        # This for loop will check if the verb start with vowel or not
        # if self.verb == "avoir":
        #     self.avoir_in_present_tense()
        #     self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
        if self.verb == "avoir":            
            for verb in self.avoirInPresentTense():
                self.conjugated_verbs["third"].append(verb)
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["third"])
        if self.verb == "être" or self.verb == "etre":
            for verb in self.etreInPresentTense():
                self.conjugated_verbs["third"].append(verb)
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["third"])


        if is_infinitive == "er" and self.get_root != "all":
            self.conjugated_verbs["first"].append("First group verb")
            for vow in self.get_root[0]:
                if vow in self.vowels:
                    if four_letters_ending_rules == "oyer" or four_letters_ending_rules == "uyer":
                        self.get_root = root[:-1] + "i"
                    
                    conjugated_verb1 = self.personal_pronouns[0][0] + "'{}{}".format(self.get_root,
                                                                                    self.present_tense_endings_for_first_group_verbs[
                                                                                    0])
                    self.conjugated_verbs["first"].append(conjugated_verb1)
        
                    # if four_letters_ending_rules == "oyer":
                    #     
                elif vow not in self.vowels:
                    if four_letters_ending_rules == "oyer" or four_letters_ending_rules == "uyer":
                        self.get_root = root[:-1] + "i"
                    
                    conjugated_verb1 = self.personal_pronouns[0] + "{}{}".format(self.get_root, self.present_tense_endings_for_first_group_verbs[0])
                    self.conjugated_verbs["first"].append(conjugated_verb1)

            if four_letters_ending_rules == "oyer" or four_letters_ending_rules == "uyer":
                 self.get_root = root[:-1] + "i"
            
            
            conjugated_verb2 = self.personal_pronouns[1] + "{}{}".format(self.get_root, self.present_tense_endings_for_first_group_verbs[1])
            self.conjugated_verbs["first"].append(conjugated_verb2)

            conjugated_verb3 = self.personal_pronouns[2] + "{}{}".format(self.get_root, self.present_tense_endings_for_first_group_verbs[2])
            self.conjugated_verbs["first"].append(conjugated_verb3)

            # Handling verbs that end in "cer"
            if three_letters_ending_rules == "cer":
                conjugated_verb4 = self.personal_pronouns[3] + self.get_root[0: -1] + modified_letter + "{}".format(
                    self.present_tense_endings_for_first_group_verbs[3])
                self.conjugated_verbs["first"].append(conjugated_verb4)
            elif four_letters_ending_rules == "oyer" or four_letters_ending_rules == "uyer":
                conjugated_verb4 = self.personal_pronouns[3] + "{}{}".format(self.get_root[:-1] + "y" , self.present_tense_endings_for_first_group_verbs[3])
                self.conjugated_verbs["first"].append(conjugated_verb4)
            # Handling a verb ending in "ger"
            elif self.three_letters_ending_rules == "ger":
                conjugated_verb4 = self.personal_pronouns[3] + "{}e{}".format(self.get_root,
                                                                            self.present_tense_endings_for_first_group_verbs[
                                                                                3])
                self.conjugated_verbs["first"].append(conjugated_verb4)

            else:
                conjugated_verb4 = self.personal_pronouns[3] + "{}{}".format(self.get_root, self.present_tense_endings_for_first_group_verbs[3])
                self.conjugated_verbs["first"].append(conjugated_verb4)
            
            if four_letters_ending_rules == "oyer" or four_letters_ending_rules == "uyer":
                conjugated_verb5 = self.personal_pronouns[4] + "{}{}".format(self.get_root[:-1] + "y" , self.present_tense_endings_for_first_group_verbs[4])
            else:
                conjugated_verb5 = self.personal_pronouns[4] + "{}{}".format(self.get_root, self.present_tense_endings_for_first_group_verbs[4])
            self.conjugated_verbs["first"].append(conjugated_verb5)

            conjugated_verb6 = self.personal_pronouns[5] + "{}{}".format(self.get_root, self.present_tense_endings_for_first_group_verbs[5])
            self.conjugated_verbs["first"].append(conjugated_verb6)

            # else:
            #     conjugated_verb6 = self.personal_pronouns[5] + "{}{}".format(self.get_root, self.present_tense_endings_for_first_group_verbs[5])
            #     self.conjugated_verbs["first"].append(conjugated_verb6)
            self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])

        # Condition for second_group verbs
        elif self.get_root == "all" and self.is_infinitive == "er":
            form_infinitive = ("Third group verb")
            self.conjugated_verbs["first"].append(form_infinitive)
            conjugated_verb1 = self.personal_pronouns[0] + "vais"
            self.conjugated_verbs["first"].append(conjugated_verb1)

            conjugated_verb2 = self.personal_pronouns[1] + "vas"
            self.conjugated_verbs["first"].append(conjugated_verb2)

            conjugated_verb3 = self.personal_pronouns[2] + "va"
            self.conjugated_verbs["first"].append(conjugated_verb3)

            conjugated_verb4 = self.personal_pronouns[3] + "{}{}".format(self.get_root,
                                                                         self.present_tense_endings_for_first_group_verbs[
                                                                             3])
            self.conjugated_verbs["first"].append(conjugated_verb4)

            conjugated_verb5 = self.personal_pronouns[4] + "{}{}".format(self.get_root,
                                                                         self.present_tense_endings_for_first_group_verbs[
                                                                             4])
            self.conjugated_verbs["first"].append(conjugated_verb5)

            conjugated_verb6 = self.personal_pronouns[5] + "vont"
            self.conjugated_verbs["first"].append(conjugated_verb6)
            self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
        
        if is_infinitive == "ir" and self.verb != "avoir" and verb.endswith(string_tuple) and verb.endswith("ouir"):
            conjugated_verb1 = self.personal_pronouns[0] + "{}{}".format(self.get_root,
                                                                         present_tense_endings_for_second_group_verbs[
                                                                             0])
            self.conjugated_verbs["second"].append(conjugated_verb1)
            conjugated_verb2 = self.personal_pronouns[1] + "{}{}".format(self.get_root,
                                                                         present_tense_endings_for_second_group_verbs[
                                                                             1])
            self.conjugated_verbs["second"].append(conjugated_verb2)
            conjugated_verb3 = self.personal_pronouns[2] + "{}{}".format(self.get_root,
                                                                         present_tense_endings_for_second_group_verbs[
                                                                             2])
            self.conjugated_verbs["second"].append(conjugated_verb3)
            conjugated_verb4 = self.personal_pronouns[3] + "{}{}".format(self.get_root,
                                                                         present_tense_endings_for_second_group_verbs[
                                                                             3])
            self.conjugated_verbs["second"].append(conjugated_verb4)
            conjugated_verb5 = self.personal_pronouns[4] + "{}{}".format(self.get_root,
                                                                         present_tense_endings_for_second_group_verbs[
                                                                             4])
            self.conjugated_verbs["second"].append(conjugated_verb5)
            conjugated_verb6 = self.personal_pronouns[5] + "{}{}".format(self.get_root,
                                                                         present_tense_endings_for_second_group_verbs[
                                                                             5])
            self.conjugated_verbs["second"].append(conjugated_verb6)
            self.ids.name_label.text = "\n".join(self.conjugated_verbs["second"])
    
    def conjugate_first_group_verbs_in_imparfait(self):
        important_elements = self.formating()
        is_infinitive = important_elements[0]
        three_letters_ending_rules = important_elements[1]
        three_letters_ending_rules = important_elements[2]
        four_letters_ending_rules = important_elements[3]
        modified_letter = important_elements[4]
        modified_letter_d_to_n = important_elements[5]
        root = important_elements[8]
        verb = important_elements[7]
        self.verb = verb
        self.personal_pronouns = personal_pronouns
        self.get_root = root[:-1]
        self.imparfait_endings = imparfait_endings
        self.conjugated_verbs = {"first": [], "second": [], "third": []} 
        if self.verb == "avoir":
            for verb in self.avoirInImparfait():
                self.conjugated_verbs["third"].append(verb)
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["third"])

        if self.verb == "être" or self.verb == "etre":
            for verb in self.etreInImparfait():
                self.conjugated_verbs["third"].append(verb)
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["third"])
            
         # This for loop will check if the verb start with vowel or not
        if is_infinitive == "er" and three_letters_ending_rules != "cer" and three_letters_ending_rules != "ger":
            self.conjugated_verbs["first"].append("First group verb")
            for vow in self.get_root[0]:
                if vow in self.vowels:
                    conjugated_verb1 = self.personal_pronouns[0][0] + "'{}{}".format(self.get_root, self.imparfait_endings[0])
                    self.conjugated_verbs["first"].append(conjugated_verb1)
                elif vow not in self.vowels:
                    conjugated_verb1 = self.personal_pronouns[0] + "{}{}".format(self.get_root, self.imparfait_endings[0])
                    self.conjugated_verbs["first"].append(conjugated_verb1)

            conjugated_verb2 = self.personal_pronouns[1] + "{}{}".format(self.get_root,
                                                                         self.imparfait_endings[
                                                                             1])
            self.conjugated_verbs["first"].append(conjugated_verb2)

            conjugated_verb3 = self.personal_pronouns[2] + "{}{}".format(self.get_root, self.imparfait_endings[2])
            self.conjugated_verbs["first"].append(conjugated_verb3)

            conjugated_verb4 = self.personal_pronouns[3] + "{}{}".format(self.get_root, self.imparfait_endings[3])
            self.conjugated_verbs["first"].append(conjugated_verb4)

            conjugated_verb5 = self.personal_pronouns[4] + "{}{}".format(self.get_root, self.imparfait_endings[4])
            self.conjugated_verbs["first"].append(conjugated_verb5)

            conjugated_verb6 = self.personal_pronouns[5] + "{}{}".format(self.get_root, self.imparfait_endings[5])
            self.conjugated_verbs["first"].append(conjugated_verb6)
            self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])

        # Handling verbs that end in "cer"
        if three_letters_ending_rules == "cer" and three_letters_ending_rules != "ger":

            self.conjugated_verbs["first"].append("First group verb")
            for vow in self.get_root[0]:
                if vow in self.vowels:
                    conjugated_verb1 = self.personal_pronouns[0][0] + "'{}{}".format(self.get_root[:-1] + modified_letter, self.imparfait_endings[0])
                    self.conjugated_verbs["first"].append(conjugated_verb1)
                elif vow not in self.vowels:
                    conjugated_verb1 = self.personal_pronouns[0] + "{}{}".format(self.get_root[:-1] + modified_letter, self.imparfait_endings[0])
                    self.conjugated_verbs["first"].append(conjugated_verb1)

            conjugated_verb2 = self.personal_pronouns[1] + "{}{}".format(self.get_root[:-1] + modified_letter, self.imparfait_endings[1])
            self.conjugated_verbs["first"].append(conjugated_verb2)

            conjugated_verb3 = self.personal_pronouns[2] + "{}{}".format(self.get_root[:-1] + modified_letter, self.imparfait_endings[2])
            self.conjugated_verbs["first"].append(conjugated_verb3)

            conjugated_verb4 = self.personal_pronouns[3] + self.get_root +"{}".format(self.imparfait_endings[3])
            self.conjugated_verbs["first"].append(conjugated_verb4)

            conjugated_verb5 = self.personal_pronouns[4] + self.get_root +"{}".format(self.imparfait_endings[4])
            self.conjugated_verbs["first"].append(conjugated_verb5)

            conjugated_verb6 = self.personal_pronouns[5] + "{}{}".format(self.get_root[:-1] + modified_letter, self.imparfait_endings[5])
            self.conjugated_verbs["first"].append(conjugated_verb6)
            self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
    

        # Handling a verb ending in "ger"
        
        if self.three_letters_ending_rules == "ger":# and self.three_letters_ending_rules != "cer":

            self.conjugated_verbs["first"].append("First group verb")
            for vow in self.get_root[0]:
                if vow in self.vowels:
                    conjugated_verb1 = self.personal_pronouns[0][0] + "'{}e{}".format(self.get_root, self.imparfait_endings[0])
                    self.conjugated_verbs["first"].append(conjugated_verb1)
                elif vow not in self.vowels:
                    conjugated_verb1 = self.personal_pronouns[0] + "{}e{}".format(self.get_root, self.imparfait_endings[0])
                    self.conjugated_verbs["first"].append(conjugated_verb1)

            conjugated_verb2 = self.personal_pronouns[1] + "{}e{}".format(self.get_root, self.imparfait_endings[1])
            self.conjugated_verbs["first"].append(conjugated_verb2)

            conjugated_verb3 = self.personal_pronouns[2] + "{}e{}".format(self.get_root, self.imparfait_endings[2])
            self.conjugated_verbs["first"].append(conjugated_verb3)

            conjugated_verb4= self.personal_pronouns[3] + "{}{}".format(self.get_root, self.imparfait_endings[3])
            self.conjugated_verbs["first"].append(conjugated_verb4)

            conjugated_verb5 = self.personal_pronouns[4] + "{}{}".format(self.get_root, self.imparfait_endings[4])
            self.conjugated_verbs["first"].append(conjugated_verb5)

            conjugated_verb6 = self.personal_pronouns[5] + "{}e{}".format(self.get_root, self.imparfait_endings[5])
            self.conjugated_verbs["first"].append(conjugated_verb6)
    
            self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])

        # # Condition for second_group verbs
        # elif self.get_root == "all" and self.is_infinitive == "er":
        #     form_infinitive = ("Third group verb")
        #     self.conjugated_verbs["first"].append(form_infinitive)
        #     conjugated_verb1 = self.personal_pronouns[0] + "vais"
        #     self.conjugated_verbs["first"].append(conjugated_verb1)

        #     conjugated_verb2 = self.personal_pronouns[1] + "vas"
        #     self.conjugated_verbs["first"].append(conjugated_verb2)

        #     conjugated_verb3 = self.personal_pronouns[2] + "va"
        #     self.conjugated_verbs["first"].append(conjugated_verb3)

        #     conjugated_verb4 = self.personal_pronouns[3] + "{}{}".format(self.get_root,
        #                                                                  self.present_tense_endings_for_first_group_verbs[
        #                                                                      3])
        #     self.conjugated_verbs["first"].append(conjugated_verb4)

        #     conjugated_verb5 = self.personal_pronouns[4] + "{}{}".format(self.get_root,
        #                                                                  self.present_tense_endings_for_first_group_verbs[
        #                                                                      4])
        #     self.conjugated_verbs["first"].append(conjugated_verb5)

        #     conjugated_verb6 = self.personal_pronouns[5] + "vont"
        #     self.conjugated_verbs["first"].append(conjugated_verb6)
        #     self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])

        # elif is_infinitive == "ir" and not verb.endswith(string_tuple) or verb.endswith("ouir"):
        #     conjugated_verb1 = self.personal_pronouns[0] + "{}{}".format(self.get_root,
        #                                                                  present_tense_endings_for_second_group_verbs[
        #                                                                      0])
        #     self.conjugated_verbs["second"].append(conjugated_verb1)
        #     conjugated_verb2 = self.personal_pronouns[1] + "{}{}".format(self.get_root,
        #                                                                  present_tense_endings_for_second_group_verbs[
        #                                                                      1])
        #     self.conjugated_verbs["second"].append(conjugated_verb2)
        #     conjugated_verb3 = self.personal_pronouns[2] + "{}{}".format(self.get_root,
        #                                                                  present_tense_endings_for_second_group_verbs[
        #                                                                      2])
        #     self.conjugated_verbs["second"].append(conjugated_verb3)
        #     conjugated_verb4 = self.personal_pronouns[3] + "{}{}".format(self.get_root,
        #                                                                  present_tense_endings_for_second_group_verbs[
        #                                                                      3])
        #     self.conjugated_verbs["second"].append(conjugated_verb4)
        #     conjugated_verb5 = self.personal_pronouns[4] + "{}{}".format(self.get_root,
        #                                                                  present_tense_endings_for_second_group_verbs[
        #                                                                      4])
        #     self.conjugated_verbs["second"].append(conjugated_verb5)
        #     conjugated_verb6 = self.personal_pronouns[5] + "{}{}".format(self.get_root,
        #                                                                  present_tense_endings_for_second_group_verbs[
        #                                                                      5])
        #     self.conjugated_verbs["second"].append(conjugated_verb6)
        #     self.ids.name_label.text = "\n".join(self.conjugated_verbs["second"])      

    def conjugate_first_group_verbs_in_simple_past(self):
        important_elements = self.formating()
        is_infinitive = important_elements[0]
        three_letters_ending_rules = important_elements[1]
        three_letters_ending_rules = important_elements[2]
        four_letters_ending_rules = important_elements[3]
        modified_letter = important_elements[4]
        modified_letter_d_to_n = important_elements[5]
        root = important_elements[6]
        verb = important_elements[7]
        self.verb = verb
        self.personal_pronouns = personal_pronouns
        self.get_root = root
        #self.present_tense_endings_for_first_group_verbs = present_tense_endings_for_first_group_verbs
        self.simple_past_endings_for_first_group_verbs = simple_past_endings_for_first_group_verbs
        self.simple_past_endings_for_second_group_verbs = simple_past_endings_for_second_group_verbs
        
        self.conjugated_verbs = {"first": [], "second": [], "third": []}
        self.vow = ""

        if self.verb == "avoir":
            for verb in self.avoirInSimplePast():
                self.conjugated_verbs["third"].append(verb)
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["third"])

        if self.verb == "être" or self.verb == "etre":
            for verb in self.etreInSimplePast():
                self.conjugated_verbs["third"].append(verb)
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["third"])

        if three_letters_ending_rules == "ger":
                self.get_root = root + "e"
        
        if three_letters_ending_rules == "cer":
                self.get_root = root[:-1] + modified_letter
        # This for loop will check if the verb start with vowel or not
        if is_infinitive == "er" and self.get_root != "all":
            self.conjugated_verbs["first"].append("First group verb")
            for vow in self.get_root[0]:
                if vow in self.vowels:
                    conjugated_verb1 = self.personal_pronouns[0][0] + "'{}{}".format(self.get_root,
                                                                                     self.simple_past_endings_for_first_group_verbs[
                                                                                         0])
                    self.conjugated_verbs["first"].append(conjugated_verb1)
                elif vow not in self.vowels:
                    if three_letters_ending_rules == "cer":
                        self.get_root = root[:-1] + modified_letter
                    conjugated_verb1 = self.personal_pronouns[0] + "{}{}".format(self.get_root,
                                                                                 self.simple_past_endings_for_first_group_verbs[
                                                                                     0])
                    self.conjugated_verbs["first"].append(conjugated_verb1)

            
                

            conjugated_verb2 = self.personal_pronouns[1] + "{}{}".format(self.get_root,
                                                                         self.simple_past_endings_for_first_group_verbs[
                                                                             1])
            self.conjugated_verbs["first"].append(conjugated_verb2)

            conjugated_verb3 = self.personal_pronouns[2] + "{}{}".format(self.get_root,
                                                                         self.simple_past_endings_for_first_group_verbs[
                                                                             2])
            self.conjugated_verbs["first"].append(conjugated_verb3)

            # Handling verbs that end in "cer"
            # if three_letters_ending_rules == "cer":
            #     conjugated_verb4 = self.personal_pronouns[3] + self.get_root[0: -1] + modified_letter + "{}".format(
            #         self.simple_past_endings_for_first_group_verbs[3])
            #     self.conjugated_verbs["first"].append(conjugated_verb4)

            # Handling a verb ending in "ger"
            
            conjugated_verb4 = self.personal_pronouns[3] + "{}{}".format(self.get_root, self.simple_past_endings_for_first_group_verbs[3])
            self.conjugated_verbs["first"].append(conjugated_verb4)

            conjugated_verb5 = self.personal_pronouns[4] + "{}{}".format(self.get_root, self.simple_past_endings_for_first_group_verbs[4])
            self.conjugated_verbs["first"].append(conjugated_verb5)
            if three_letters_ending_rules == "cer" or "ger":
                self.get_root = root
            

            conjugated_verb6 = self.personal_pronouns[5] + "{}{}".format(self.get_root, self.simple_past_endings_for_first_group_verbs[5])
            self.conjugated_verbs["first"].append(conjugated_verb6)
            self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])

        # Condition for second_group verbs
        # elif self.get_root == "all" and self.is_infinitive == "er":
        #     form_infinitive = ("Third group verb")
        #     self.conjugated_verbs["first"].append(form_infinitive)
        #     conjugated_verb1 = self.personal_pronouns[0] + "vais"
        #     self.conjugated_verbs["first"].append(conjugated_verb1)

        #     conjugated_verb2 = self.personal_pronouns[1] + "vas"
        #     self.conjugated_verbs["first"].append(conjugated_verb2)

        #     conjugated_verb3 = self.personal_pronouns[2] + "va"
        #     self.conjugated_verbs["first"].append(conjugated_verb3)

        #     conjugated_verb4 = self.personal_pronouns[3] + "{}{}".format(self.get_root,
        #                                                                  self.simple_past_endings_for_first_group_verbs[
        #                                                                      3])
        #     self.conjugated_verbs["first"].append(conjugated_verb4)

        #     conjugated_verb5 = self.personal_pronouns[4] + "{}{}".format(self.get_root,
        #                                                                  self.simple_past_endings_for_first_group_verbs[
        #                                                                      4])
        #     self.conjugated_verbs["first"].append(conjugated_verb5)

        #     conjugated_verb6 = self.personal_pronouns[5] + "vont"
        #     self.conjugated_verbs["first"].append(conjugated_verb6)
        #     self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])

        elif is_infinitive == "ir" and self.verb != "avoir" and not verb.endswith(string_tuple) or verb.endswith("ouir"):
            conjugated_verb1 = self.personal_pronouns[0] + "{}{}".format(self.get_root,
                                                                         self.simple_past_endings_for_second_group_verbs[
                                                                             0])
            self.conjugated_verbs["second"].append(conjugated_verb1)
            conjugated_verb2 = self.personal_pronouns[1] + "{}{}".format(self.get_root,
                                                                         self.simple_past_endings_for_second_group_verbs[
                                                                             1])
            self.conjugated_verbs["second"].append(conjugated_verb2)
            conjugated_verb3 = self.personal_pronouns[2] + "{}{}".format(self.get_root,
                                                                         self.simple_past_endings_for_second_group_verbs[
                                                                             2])
            self.conjugated_verbs["second"].append(conjugated_verb3)
            conjugated_verb4 = self.personal_pronouns[3] + "{}{}".format(self.get_root,
                                                                         self.simple_past_endings_for_second_group_verbs[
                                                                             3])
            self.conjugated_verbs["second"].append(conjugated_verb4)
            conjugated_verb5 = self.personal_pronouns[4] + "{}{}".format(self.get_root,
                                                                         self.simple_past_endings_for_second_group_verbs[
                                                                             4])
            self.conjugated_verbs["second"].append(conjugated_verb5)
            conjugated_verb6 = self.personal_pronouns[5] + "{}{}".format(self.get_root,
                                                                         self.simple_past_endings_for_second_group_verbs[
                                                                             5])
            self.conjugated_verbs["second"].append(conjugated_verb6)
            self.ids.name_label.text = "\n".join(self.conjugated_verbs["second"])
    

    
    def conjugate_first_group_verbs_in_simple_future(self):
        
        important_elements = self.formating()
        is_infinitive = important_elements[0]
        three_letters_ending_rules = important_elements[1]
        three_letters_ending_rules = important_elements[2]
        four_letters_ending_rules = important_elements[3]
        modified_letter = important_elements[4]
        modified_letter_d_to_n = important_elements[5]
        root = important_elements[8]
        verb = important_elements[7]
        self.verb = verb
        self.personal_pronouns = personal_pronouns
        self.get_root = root
        self.simple_future_endings = simple_future_endings
        self.conjugated_verbs = {"first": [], "second": [], "third": []}
        self.vow = ""
        if self.verb == "avoir":
            for verb in self.avoirInSimpleFuture():
                self.conjugated_verbs["third"].append(verb)
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["third"])

        if self.verb == "être" or self.verb == "etre":
            for verb in self.etreInSimpleFuture():
                self.conjugated_verbs["third"].append(verb)
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["third"])
        # This for loop will check if the verb start with vowel or not

        if is_infinitive == "er" and self.get_root != "alle":
            self.conjugated_verbs["first"].append("First group verb")
            for vow in self.get_root[0]:
                if vow in self.vowels:
                
                    if four_letters_ending_rules == "oyer" or four_letters_ending_rules == "uyer":
                        
                        if self.verb == "envoyer":
                                self.get_root = self.get_root[:-3] + "er"
                                conjugated_verb1 = self.personal_pronouns[0][0] + "'{}{}".format(self.get_root, self.simple_future_endings[0])
                                self.conjugated_verbs["first"].append(conjugated_verb1)

                        elif self.verb != "envoyer":
                            conjugated_verb1 = self.personal_pronouns[0][0] + "'{}{}".format(self.get_root[:-2] + "ie", self.simple_future_endings[0])
                            self.conjugated_verbs["first"].append(conjugated_verb1)


                    else:
                        conjugated_verb1 = self.personal_pronouns[0][0] + "'{}{}".format(self.get_root, self.simple_future_endings[0])
                        self.conjugated_verbs["first"].append(conjugated_verb1)
                
                elif vow not in self.vowels:

                    if four_letters_ending_rules == "oyer" or four_letters_ending_rules == "uyer":

                        if self.verb == "renvoyer":
                            self.get_root = self.get_root[:-3] + "er"
                            conjugated_verb1 = self.personal_pronouns[0] + "{}{}".format(self.get_root, self.simple_future_endings[0])
                            self.conjugated_verbs["first"].append(conjugated_verb1)
                        elif self.verb != "renvoyer":
                            conjugated_verb1 = self.personal_pronouns[0] + "{}{}".format(self.get_root[:-2] + "ie", self.simple_future_endings[0])
                            self.conjugated_verbs["first"].append(conjugated_verb1)

                    else:
                        self.get_root = root
                        conjugated_verb1 = self.personal_pronouns[0] + "{}{}".format(self.get_root, self.simple_future_endings[0])
                        self.conjugated_verbs["first"].append(conjugated_verb1)

            if self.verb == "renvoyer" or self.verb == "envoyer":
                self.get_root = self.get_root[:-2] + "er"
            elif four_letters_ending_rules == "oyer" or four_letters_ending_rules == "uyer" and self.verb != "renvoyer" and self.verb != "envoyer":
                self.get_root = self.get_root[: -2] + "ie"
            else:
                #four_letters_ending_rules != "oyer" or four_letters_ending_rules != "uyer":
                self.get_root = root

            conjugated_verb2 = self.personal_pronouns[1] + "{}{}".format(self.get_root,
                                                                    self.simple_future_endings[
                                                                        1])
            self.conjugated_verbs["first"].append(conjugated_verb2)

            conjugated_verb3 = self.personal_pronouns[2] + "{}{}".format(self.get_root,
                                                                        self.simple_future_endings[
                                                                            2])
            self.conjugated_verbs["first"].append(conjugated_verb3)

            conjugated_verb4 = self.personal_pronouns[3] + "{}{}".format(self.get_root, self.simple_future_endings[3])
            self.conjugated_verbs["first"].append(conjugated_verb4)

            conjugated_verb5 = self.personal_pronouns[4] + "{}{}".format(self.get_root,
                                                                        self.simple_future_endings[
                                                                            4])
            self.conjugated_verbs["first"].append(conjugated_verb5)

            conjugated_verb6 = self.personal_pronouns[5] + "{}{}".format(self.get_root,
                                                                        self.simple_future_endings[
                                                                            5])
            self.conjugated_verbs["first"].append(conjugated_verb6)

            self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
 
        if self.get_root == "alle" and self.is_infinitive == "er":
            form_infinitive = ("Third group verb")
            self.conjugated_verbs["first"].append(form_infinitive)
            conjugated_verb1 = self.personal_pronouns[0][0] + "'" + "irai"
            self.conjugated_verbs["first"].append(conjugated_verb1)

            conjugated_verb2 = self.personal_pronouns[1] + "iras"
            self.conjugated_verbs["first"].append(conjugated_verb2)

            conjugated_verb3 = self.personal_pronouns[2] + "ira"
            self.conjugated_verbs["first"].append(conjugated_verb3)

            conjugated_verb4 = self.personal_pronouns[3] + "{}{}".format("i",
                                                                         self.simple_future_endings[
                                                                             3])
            self.conjugated_verbs["first"].append(conjugated_verb4)

            conjugated_verb5 = self.personal_pronouns[4] + "{}{}".format("i",
                                                                         self.simple_future_endings[
                                                                             4])
            self.conjugated_verbs["first"].append(conjugated_verb5)

            conjugated_verb6 = self.personal_pronouns[5] + "iront"
            self.conjugated_verbs["first"].append(conjugated_verb6)
            self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
    def present_perfect(self):
        important_elements = self.formating()
        is_infinitive = important_elements[0]
        three_letters_ending_rules = important_elements[1]
        three_letters_ending_rules = important_elements[2]
        four_letters_ending_rules = important_elements[3]
        modified_letter = important_elements[4]
        modified_letter_d_to_n = important_elements[5]
        root = important_elements[6]
        verb = important_elements[7]
        self.verb = verb
        self.personal_pronouns = personal_pronouns
        self.get_root = root
        self.present_tense_endings_for_first_group_verbs = present_tense_endings_for_first_group_verbs
        self.conjugated_verbs = {"first": [], "second": [], "third": []}
        self.vow = ""
        self.avoir = self.avoirInPresentTense()
        self.etre = self.etreInPresentTense()


        if  is_infinitive == "er" and self.verb not in tuple(verbs_of_movement) and not self.verb.endswith(tuple_third_group_endings) and not self.verb.endswith(tuple(verbs_of_movement)):      
            for verb in self.avoir:
                self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle))
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
        
        if is_infinitive == "er" and self.verb in verbs_of_movement or self.verb.endswith(tuple(verbs_of_movement)) and not self.verb.endswith(tuple(third_group_endings)):
                for verb in self.etre[0:3]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle))
                for verb in self.etre[3:6]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle) + "s")
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
        if is_infinitive == "ir" and self.verb not in tuple(verbs_of_movement):
            if self.verb.endswith("courir"):
                for verb in self.avoirInPresentTense():
                    self.conjugated_verbs["second"].append("{} {}".format(verb, self.get_root + "u"))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["second"])
            else:
                for verb in self.avoirInPresentTense():
                    self.conjugated_verbs["second"].append("{} {}".format(verb, self.get_root + "i"))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["second"])
        if is_infinitive == "ir" and self.verb in tuple(verbs_of_movement) or self.verb.endswith(tuple(verbs_of_movement)):
            for verb in self.etre[0:3]:
                self.conjugated_verbs["second"].append("{} {}".format(verb, self.get_root + "i"))  
            for verb in self.etre[3:6]:
                self.conjugated_verbs["second"].append("{} {}".format(verb, self.get_root + "is"))
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["second"])
        
        if self.verb == "avoir":
            #if self.verb == "avoir":
            for verb in self.avoirInPresentTense():
                self.conjugated_verbs["third"].append("{} {}".format(verb, "eu"))
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["third"])

        if self.verb == "être":
            #if self.verb == "avoir":
            for verb in self.avoirInPresentTense():
                self.conjugated_verbs["third"].append("{} {}".format(verb, "été"))
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["third"])
        
            
            # if is_infinitive == "ir" and not verb.endswith(string_tuple):  # third_group_verbs_that_end_with_ir:
            #
            #     conjugate_second_group_verbs()
    mode = False
    def mode_indicatif_control(self, widget):
        #widget.state = "down"
        print("state is", widget.state)
        if widget.state == "normal":
            self.infinitive()
        if widget.state == "down":
            return self.conjugate_first_group_verbs_in_simple_present()

    
class TheLabApp(App, Leconjugueur):
    pass


TheLabApp().run()

############################ 


# Function that conjugate second group verbs
# def conjugate_second_group_verbs():
#
# # Function that conjugates third group verb type 2
# def conjugate_third_group_verb_type_2():
#     for vow in verb[0]:
#         if vow in vowels:
#             conjugated_verb1 = personal_pronouns[0][0] + "'{}{}".format(get_root,
#                                                                         present_tense_endings_for_third_group_verbs[0])
#             print(conjugated_verb1)
#         elif vow is not vowels:
#             conjugated_verb1 = personal_pronouns[0] + "{}{}".format(get_root,
#                                                                     present_tense_endings_for_third_group_verbs[0])
#             print(conjugated_verb1)
#
#     conjugated_verb2 = personal_pronouns[1] + "{}{}".format(get_root, present_tense_endings_for_third_group_verbs[1])
#     print(conjugated_verb2)
#
#     conjugated_verb3 = personal_pronouns[2] + "{}{}".format(get_root, present_tense_endings_for_third_group_verbs[2])
#     print(conjugated_verb3)
#
#     if four_letters_ending_rules == "endre":
#         conjugated_verb4 = personal_pronouns[3] + get_root[0: -1] + "{}".format(
#             present_tense_endings_for_third_group_verbs[3])
#         print(conjugated_verb4)
#
#     conjugated_verb5 = personal_pronouns[4] + get_root[0: -1] + "{}".format(
#         present_tense_endings_for_third_group_verbs[4])
#     print(conjugated_verb5)
#
#     conjugated_verb6 = personal_pronouns[5] + get_root[0: -1] + modified_letter_d_to_n + "{}".format(
#         present_tense_endings_for_third_group_verbs[5])
#     print(conjugated_verb6)
#
#
# def conjugate_third_group_verb_type_1():
#     for vow in verb[0]:
#         if vow in vowels:
#             conjugated_verb1 = personal_pronouns[0][0] + "'{}{}".format(get_root,
#                                                                         present_tense_endings_for_third_group_verbs[0])
#             print(conjugated_verb1)
#         elif vow is not vowels:
#             conjugated_verb1 = personal_pronouns[0] + "{}{}".format(get_root,
#                                                                     present_tense_endings_for_third_group_verbs[0])
#             print(conjugated_verb1)
#
#     conjugated_verb2 = personal_pronouns[1] + "{}{}".format(get_root, present_tense_endings_for_third_group_verbs[1])
#     print(conjugated_verb2)
#
#     conjugated_verb3 = personal_pronouns[2] + "{}{}".format(get_root, present_tense_endings_for_third_group_verbs[2])
#     print(conjugated_verb3)
#
#     if four_letters_ending_rules == "endre":
#         conjugated_verb4 = personal_pronouns[3] + "{}{}".format(get_root,
#                                                                 present_tense_endings_for_third_group_verbs[3])
#         print(conjugated_verb4)
#
#     conjugated_verb5 = personal_pronouns[4] + "{}{}".format(get_root, present_tense_endings_for_third_group_verbs[4])
#     print(conjugated_verb5)
#
#     conjugated_verb6 = personal_pronouns[5] + "{}{}".format(get_root, present_tense_endings_for_third_group_verbs[5])
#     print(conjugated_verb6)
#
#
# if is_infinitive == "re" and verb in irregular_endre_verbs_type2:
#     print("This is a third group verb")
#     conjugate_third_group_verb_type_2()
#
# if is_infinitive == "re" and verb in irregular_endre_verbs_type1:
#     print("This is a third group verb")
#     conjugate_third_group_verb_type_1()


# for key, items in self.conjugated_verbs.items():
#     for item in items:
#         print(item)
