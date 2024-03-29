# from kivy import Config
# Config.set('graphics', 'multisamples', '0')
#import os
# os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
##os.environ['KIVY_GRAPHICS'] = 'angle_sdl2'
from first_group_verbs import list_1 as f
from second_group_verbs import list_2 as s
from third_group_verbs import list_3 as t
from verb_list import verb_list as v
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
from kivy.properties import StringProperty, BooleanProperty, ListProperty, ObjectProperty, NumericProperty
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.lang import Builder

#-- maximize first, to get the screen size, minus any OS toolbars
# Window.maximize()
# maxSize = Window.system_size

#-- set the actual window size, to be slightly smaller than full screen
# desiredSize = (maxSize[0]*0.9, maxSize[1]*0.9)
# Window.size = desiredSize

# set App size

#Window.size = (804, 800)
#Builder.load_file('thelab.kv')
reflexive_1 = ["me", "te", "se", "nous", "vous", "se"]
past_reflexive = ["me ", "te ", "se ", "nous ", "vous ", "se "]
reflexive_2 = ["m'", "t'", "s'", "nous ", "vous ", "s'"]
personal_pronouns = ["Je ", "Tu ", "Il ", "Nous ", "Vous ", "Ils "]
personal_pronouns_2 = ["J'", "Tu ", "Il ", "Nous ", "Vous ", "Ils "]
present_tense_endings_for_first_group_verbs = ["e", "es", "e", "ons", "ez", "ent"]
simple_future_endings = ["rai", "ras", "ra", "rons", "rez", "ront"]
imparfait_endings = ["ais", "ais", "ait", "ions", "iez", "aient"]
etre_in_present_tense = ["suis", "es", "est", "sommes", "êtes", "sont"]
etre_in_imparfait = ["étais", "étais", "était", "étions", "étiez", "étaient"]
etre_in_simple_past_tense = ["fus", "fus", "fut", "fûmes", "fûtes", "furent"]
etre_in_simple_future = ["serai", "seras", "sera", "serons", "serez", "seront"]
avoir_in_present_tense = ["ai", "as", "a", "avons", "avez", "ont"]
avoir_in_imparfait = ["avais", "avais", "avait", "avions", "aviez", "avaient"]
avoir_in_simple_past = ["eus", "eus", "eut", "eûmes", "eûtes", "eurent"]
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
peser_family = ["ecer", "emer", "ener", "eper", "eser", "ever", "evrer"]
ceder_family = ["ébrer", "écher", "écrer", "égler", "égner", "égrer", "éguer", "équer", "étrer", "évrer", "écer", "éder", "éler", "émer", "éner", "éper",  "érer", "éser", "éter", "éyer"]
exceptions_of_eler_and_eter_family = ["celer", "déceler", "se déceler", "se receler", "receler", "se ciseler", "ciseler", "se démanteler", "démanteler", "s'écarteler", "écarteler", "s'encasteler", "encasteler", "se geler", "geler", "se dégeler", "dégeler", "se congeler", "congeler", "se surgeler", "surgeler", "se marteler", "marteler", "se modeler", "modeler", "se peler", "peler", "s'acheter", "acheter", "se racheter", "racheter", "se bégueter", "bégueter", "se corseter", "corseter", "se crocheter", "crocheter", "se fileter", "fileter", "fureter", "haleter"]
irregular_endre_verbs_type1 = ["descendre", "défendre"]
irregular_endre_verbs_type2 = ["prendre", "apprendre", "comprendre"]
verbs_of_movement = ["aller", "arriver", "descendre", "entrer", "monter", "mourir", "naître", "partir", "passer", "rester", "sortir", "tomber", "venir"]
# print(tuple_third_group_endings)


class Leconjugueur(BoxLayout):

    infinitif = ""

    indicatif_enabled = BooleanProperty(False)


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.modified_letter = "ç"
        self.vowels = vowels
        self.modified_letter_d_to_n = "n"
        #self.personal_pronouns = personal_pronouns

    def special_characters(self, button):
        # Create variable for whatever was in text input
        prior = self.ids.name_input.text

        # adding letter to prior
        self.ids.name_input.text = f'{prior}{button}'
        return self.ids.e_acute_accent.text

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
        self.my_verb = []

        for personal_pronoun, etre_in_present_tense_ending in zip(self.personal_pronouns, etre_in_present_tense):
            self.conjugated_verbs["third"].append(personal_pronoun + etre_in_present_tense_ending)
        return self.conjugated_verbs["third"]

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

        for personal_pronoun, etre_in_simple_future_tense_ending in zip(self.personal_pronouns, simple_future_endings):
            self.conjugated_verbs["third"].append(personal_pronoun + "se" + etre_in_simple_future_tense_ending)
        return self.conjugated_verbs["third"]

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
        for personal_pronoun, etre_in_simple_past_tense_ending in zip(self.personal_pronouns, etre_in_simple_past_tense):
            self.conjugated_verbs["third"].append(personal_pronoun + etre_in_simple_past_tense_ending)
        return self.conjugated_verbs["third"]

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
    
        for personal_pronoun, imparfait_ending in zip(self.personal_pronouns, imparfait_endings):
            self.conjugated_verbs["third"].append(personal_pronoun + "ét" + imparfait_ending)
            self.conjugated_verbs["third"][0] = personal_pronouns[0][0] + "'ét" + imparfait_endings[0]
        return self.conjugated_verbs["third"]


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

        for personal_pronoun, avoir_in_present_tense_ending in zip(self.personal_pronouns, avoir_in_present_tense):
            self.conjugated_verbs["third"].append(personal_pronoun + avoir_in_present_tense_ending)
            self.conjugated_verbs["third"][0] = personal_pronouns[0][0] + "'" + avoir_in_present_tense[0]
        return self.conjugated_verbs["third"]
        
    

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
        
        for personal_pronoun, imparfait_ending in zip(self.personal_pronouns, imparfait_endings):
            self.conjugated_verbs["third"].append(personal_pronoun + "av" + imparfait_ending)
            self.conjugated_verbs["third"][0] = personal_pronouns[0][0] + "'" + "av" + imparfait_endings[0]
        return self.conjugated_verbs["third"]        

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
        for personal_pronoun, avoir_in_simple_past_tense_ending in zip(self.personal_pronouns, avoir_in_simple_past):
            self.conjugated_verbs["third"].append(personal_pronoun + avoir_in_simple_past_tense_ending)
            self.conjugated_verbs["third"][0] = personal_pronouns[0][0] + "'" + avoir_in_simple_past[0]
        return self.conjugated_verbs["third"]
    
    
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
        for personal_pronoun, avoir_in_simple_future_tense_ending in zip(self.personal_pronouns, simple_future_endings):
            self.conjugated_verbs["third"].append(personal_pronoun + "au" + avoir_in_simple_future_tense_ending)
            self.conjugated_verbs["third"][0] = personal_pronouns[0][0] + "'au" + simple_future_endings[0]
        return self.conjugated_verbs["third"]

    

    def conjugate_first_group_verbs_in_simple_present(self):
        important_elements = self.formating()
        is_infinitive = important_elements[0]
        three_letters_ending_rules = important_elements[1]
        three_letters_ending_rules = important_elements[2]
        four_letters_ending_rules = important_elements[3]
        modified_letter = important_elements[4]
        modified_letter_d_to_n = important_elements[5]
        root = important_elements[6]
        verb = important_elements[7]
        if verb == "avérer":
            self.verb = ""
        # else:
        #     self.verb = verb
        self.personal_pronouns = personal_pronouns
        # if self.verb[0] in tuple(vowels):
        #     self.personal_pronouns[0] = self.personal_pronouns[0][0] + "'"
        self.get_root = root
        self.present_tense_endings_for_first_group_verbs = present_tense_endings_for_first_group_verbs
        self.conjugated_verbs = {"first": [], "second": [], "third": []}
        self.vow = ""
        new_pronouns = []
            
        if self.verb.startswith("se "):
            self.get_root = self.get_root[2:]
            for personal_pronoun, reflexive in zip(personal_pronouns, reflexive_1): 
                personal_pronouns.append(personal_pronoun + reflexive)
            self.personal_pronouns = personal_pronouns[6:]

        if self.verb.startswith("s'"):
            self.get_root = self.get_root
            for personal_pronoun, reflexive2 in zip(personal_pronouns, reflexive_2): 
                if personal_pronoun not in tuple(new_pronouns):
                    new_pronouns.append(personal_pronoun + reflexive2)
                self.personal_pronouns = new_pronouns
              
            #self.personal_pronouns = personal_pronouns[6:]
            #self.personal_pronouns = dict.fromkeys(self.personal_pronouns)
            
        for ending in tuple(peser_family[:-1]):
            if self.verb.endswith(ending):
                # print(ending)
                # print(self.get_root)
                self.get_root = root[:-2] + "è" + root[-1]
            if self.verb[0:3] == "se " and self.verb.endswith(ending):
                self.get_root = root[2:-2] + "è" + root[-1]
            if self.verb[0:2] == "s'" and self.verb.endswith(ending):
                self.get_root = root[:-2] + "è" + root[-1]

        for ending in ceder_family:
            if self.verb.endswith(ending) and len(ending) == 5:
                self.get_root = root[:-3] + "è" + self.verb[-4:-2]
            if self.verb.endswith(ending) and len(ending) == 4:
                self.get_root = root[:-2] + "è" + self.verb[-3:-2]
            if self.verb.startswith("se ") and self.verb.endswith(ending) and len(ending) == 5:
                self.get_root = root[2:-3] + "è" + self.verb[-4:-2]
            if self.verb.startswith("s'") and self.verb.endswith(ending) and len(ending) == 4:
                self.get_root = root[:-2] + "è" + self.verb[-3:-2]

        
        for ending in tuple(peser_family):
            if self.verb.endswith(ending) and ending not in tuple(peser_family[:-1]):
                self.get_root = root[:-3] + "è" + self.verb[-4:-2] 


        
        if self.verb == "avoir":            
            for verb in self.avoirInPresentTense():
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["third"])
        if self.verb == "être" or self.verb == "etre":
            for verb in self.etreInPresentTense():
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["third"])
        
        if four_letters_ending_rules == "oyer" or four_letters_ending_rules == "uyer":
            self.get_root = root[:-1] + "i"

        if self.verb[0:2] ==("s'"):#and four_letters_ending_rules != "oyer :
            self.get_root = self.get_root[2:]
        if self.verb[0:3] == ("se "):
            if four_letters_ending_rules == "oyer" or four_letters_ending_rules == "uyer":
                self.get_root = self.get_root[2:]
        
        if self.verb not in tuple(exceptions_of_eler_and_eter_family):
            if self.verb.endswith("eler") or self.verb.endswith("eter"):
                if self.verb[:3] != "se ":
                    self.get_root = self.verb[:-2] + self.verb[-3]
                if self.verb[0:2] != "s'":
                    self.get_root = self.verb[:-2] + self.verb[-3]
                if self.verb.startswith("se ") or self.verb.startswith("s'"):
                    self.get_root = self.verb[2:-2] + self.verb[-3]
        if self.verb in tuple(exceptions_of_eler_and_eter_family):
            if not self.verb.startswith("se ") or not self.verb.startswith("s'"):
                self.get_root = self.verb[:-4] + "è" + self.verb[-3]
            if self.verb.startswith("se ") or self.verb.startswith("s'"):
                self.get_root = self.verb[2:-4] + "è" + self.verb[-3]
        if self.verb.endswith("éger"):
            if not self.verb.startswith("se ") or not self.verb.startswith("s'"):
                self.get_root = self.verb[:-4] + "è" + self.verb[-3:-2]
            if self.verb.startswith("se ") or self.verb.startswith("s'"):
                self.get_root = self.verb[2:-4] + "è" + self.verb[-3:-2]
        if self.verb.endswith("ayer"):
            if not self.verb.startswith("se ") or not self.verb.startswith("s'"):
                self.get_root = self.verb[:-3] + "i"
            if self.verb.startswith("se ") or self.verb.startswith("s'"):
                self.get_root = self.verb[2:-3] + "i"

        if self.verb in tuple(f):#is_infinitive == "er" and self.get_root != "all" and self.verb != "être" and self.verb != "etre":
            # self.conjugated_verbs["first"].append("First group verb")
        
            if self.verb[0:2] != "s'" and self.verb[0] in tuple(vowels):
                conjugated_verb1 = self.personal_pronouns[0][0] + "'{}{}".format(self.get_root, self.present_tense_endings_for_first_group_verbs[0])
                self.conjugated_verbs["first"].append(conjugated_verb1)

            if self.verb[0] not in tuple(vowels):
        
                    conjugated_verb1 = self.personal_pronouns[0] + "{}{}".format(self.get_root, self.present_tense_endings_for_first_group_verbs[0])
                    self.conjugated_verbs["first"].append(conjugated_verb1)
            
            conjugated_verb2 = self.personal_pronouns[1] + "{}{}".format(self.get_root, self.present_tense_endings_for_first_group_verbs[1])
            self.conjugated_verbs["first"].append(conjugated_verb2)

            conjugated_verb3 = self.personal_pronouns[2] + "{}{}".format(self.get_root, self.present_tense_endings_for_first_group_verbs[2])
            self.conjugated_verbs["first"].append(conjugated_verb3)

            # Handling verbs that end in "cer"
            if three_letters_ending_rules == "cer":
                conjugated_verb4 = self.personal_pronouns[3] + self.get_root[0: -1] + modified_letter + "{}".format(
                    self.present_tense_endings_for_first_group_verbs[3])
                self.conjugated_verbs["first"].append(conjugated_verb4)
            
            elif self.three_letters_ending_rules == "ger":
                conjugated_verb4 = self.personal_pronouns[3] + "{}e{}".format(self.get_root,
                                                                            self.present_tense_endings_for_first_group_verbs[
                                                                                3])
                self.conjugated_verbs["first"].append(conjugated_verb4)

            else:
                conjugated_verb4 = self.personal_pronouns[3] + "{}{}".format(self.get_root, self.present_tense_endings_for_first_group_verbs[3])
                self.conjugated_verbs["first"].append(conjugated_verb4)
            
            conjugated_verb5 = self.personal_pronouns[4] + "{}{}".format(self.get_root, self.present_tense_endings_for_first_group_verbs[4])
            self.conjugated_verbs["first"].append(conjugated_verb5)

            conjugated_verb6 = self.personal_pronouns[5] + "{}{}".format(self.get_root, self.present_tense_endings_for_first_group_verbs[5])
            self.conjugated_verbs["first"].append(conjugated_verb6)
            if self.verb[0:2] == "s'" or self.verb[0:3] == "se ":
                if four_letters_ending_rules == "oyer" or four_letters_ending_rules == "uyer":
                    self.conjugated_verbs["first"][3] = self.conjugated_verbs["first"][3][:9] + " " + self.get_root[:-1] + "y" + "ons"
                    self.conjugated_verbs["first"][4] = self.conjugated_verbs["first"][4][:9] + " " +  self.get_root[:-1] + "y" + "ez"
                for ending in tuple(peser_family[:-1]):
                    if self.verb.endswith(ending):
                        self.conjugated_verbs["first"][3] = self.conjugated_verbs["first"][3][:-5] + "e" + self.conjugated_verbs["first"][3][-4:]
                        self.conjugated_verbs["first"][4] = self.conjugated_verbs["first"][4][:-4] + "e" + self.conjugated_verbs["first"][4][-3:]
            if self.verb[0:2] != "s'" or self.verb[0:3] != "se ":
                if four_letters_ending_rules == "oyer" or four_letters_ending_rules == "uyer":
                    self.conjugated_verbs["first"][3] = self.conjugated_verbs["first"][3][:-4] + "y" + "ons"
                    self.conjugated_verbs["first"][4] = self.conjugated_verbs["first"][4][:-3] + "y" + "ez"
                for ending in tuple(peser_family[:-1]):
                    if self.verb.endswith(ending):
                        self.conjugated_verbs["first"][3] = self.conjugated_verbs["first"][3][:-5] + "e" + self.conjugated_verbs["first"][3][-4:]
                        self.conjugated_verbs["first"][4] = self.conjugated_verbs["first"][4][:-4] + "e" + self.conjugated_verbs["first"][4][-3:]
            
            for ending in tuple(peser_family):
                if self.verb.endswith(ending) and ending not in tuple(peser_family[:-1]):
                    self.conjugated_verbs["first"][3] = self.conjugated_verbs["first"][3][:-6] + "e" + self.conjugated_verbs["first"][3][-5:]
                    self.conjugated_verbs["first"][4] = self.conjugated_verbs["first"][4][:-5] + "e" + self.conjugated_verbs["first"][4][-4:]
            
            for ending in ceder_family:
                if self.verb.endswith(ending) and len(ending) == 5:
                    self.conjugated_verbs["first"][3] = self.conjugated_verbs["first"][3][:-6] + "é" + self.conjugated_verbs["first"][3][-5:]
                    self.conjugated_verbs["first"][4] = self.conjugated_verbs["first"][4][:-5] + "é" + self.conjugated_verbs["first"][4][-4:]
                if self.verb.endswith(ending) and len(ending) == 4:
                    self.conjugated_verbs["first"][3] = self.conjugated_verbs["first"][3][:-5] + "é" + self.conjugated_verbs["first"][3][-4:]
                    self.conjugated_verbs["first"][4] = self.conjugated_verbs["first"][4][:-4] + "é" + self.conjugated_verbs["first"][4][-3:]
            
            if self.verb not in tuple(exceptions_of_eler_and_eter_family):
                if self.verb.endswith("eler") or self.verb.endswith("eter"):
                    self.conjugated_verbs["first"][3] = self.conjugated_verbs["first"][3][:-4] + self.conjugated_verbs["first"][3][-3:]
                    self.conjugated_verbs["first"][4] = self.conjugated_verbs["first"][4][:-4] + self.conjugated_verbs["first"][4][-3:]
            
            if self.verb in tuple(exceptions_of_eler_and_eter_family):
                self.conjugated_verbs["first"][3] = self.conjugated_verbs["first"][3][:-5] + "e" + self.conjugated_verbs["first"][3][-4:]
                self.conjugated_verbs["first"][4] = self.conjugated_verbs["first"][4][:-4] + "e" + self.conjugated_verbs["first"][4][-3:]
           
            if self.verb.endswith("éger"):
                self.conjugated_verbs["first"][3] = self.conjugated_verbs["first"][3][:-6] + "é" + self.conjugated_verbs["first"][3][-5:]
                self.conjugated_verbs["first"][4] = self.conjugated_verbs["first"][4][:-4] + "é" + self.conjugated_verbs["first"][4][-3:]
            
            if self.verb.endswith("ayer"):
                self.conjugated_verbs["first"][3] = self.conjugated_verbs["first"][3][:-4] + "y" + self.conjugated_verbs["first"][3][-3:]
                self.conjugated_verbs["first"][4] = self.conjugated_verbs["first"][4][:-3] + "y" + self.conjugated_verbs["first"][4][-2:]
            #       else:
            #     conjugated_verb6 = self.personal_pronouns[5] + "{}{}".format(self.get_root, self.present_tense_endings_for_first_group_verbs[5])
            #     self.conjugated_verbs["first"].append(conjugated_verb6)
            self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])

        # Condition for second_group verbs
        elif self.get_root == "all" and self.is_infinitive == "er":
            form_infinitive = ("Third group verb")
            # self.conjugated_verbs["first"].append(form_infinitive)
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
        
        if self.verb in tuple(s):#is_infinitive == "ir" and self.verb != "avoir" and not verb.endswith(string_tuple) or verb.endswith("ouir"):# and verb.endswith(string_tuple):# and verb.endswith("ouir"):
            if self.verb.startswith(tuple(vowels)):
                self.personal_pronouns = personal_pronouns_2
            if not self.verb.endswith("haïr"):    
                for personal_pronoun, ending in zip(self.personal_pronouns, present_tense_endings_for_second_group_verbs):
                    self.conjugated_verbs["second"].append(personal_pronoun + self.get_root + ending)
            if self.verb.endswith("haïr"):
                if not self.verb.startswith("se " or "s'"):
                    for personal_pronoun, ending in zip(self.personal_pronouns[:3], present_tense_endings_for_second_group_verbs[:3]):
                        self.conjugated_verbs["second"].append(personal_pronoun + self.verb[:-2] + ending)
                    for personal_pronoun, ending in zip(self.personal_pronouns[3:], present_tense_endings_for_second_group_verbs[3:]):
                        self.conjugated_verbs["second"].append(personal_pronoun + self.verb[:-2] + "ï" + ending[1:])

            if self.verb.endswith("haïr"):    
                if self.verb.startswith("se " or "s'"):
                    for personal_pronoun, ending in zip(self.personal_pronouns[:3], present_tense_endings_for_second_group_verbs[:3]):
                        self.conjugated_verbs["second"].append(personal_pronoun + self.verb[2:-2] + ending)
                    for personal_pronoun, ending in zip(self.personal_pronouns[3:], present_tense_endings_for_second_group_verbs[3:]):
                        self.conjugated_verbs["second"].append(personal_pronoun + self.verb[2:-2] + "ï" + ending[1:])
           
            self.ids.name_label.text = "\n".join(self.conjugated_verbs["second"])
        if self.verb.endswith(tuple(string_tuple)):
            self.ids.name_label.text = "It's coming soon!"
            
    
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
        if verb == "avérer":
            self.verb = ""
        else:
            self.verb = verb
        self.personal_pronouns = personal_pronouns
        self.get_root = root[:-1]
        self.imparfait_endings = imparfait_endings
        self.conjugated_verbs = {"first": [], "second": [], "third": []}

        new_pronouns = []
        if self.verb.startswith("se "):
            self.get_root = self.get_root[2:]
            for personal_pronoun, reflexive in zip(personal_pronouns, reflexive_1): 
                personal_pronouns.append(personal_pronoun + reflexive)
            self.personal_pronouns = personal_pronouns[6:]

        if self.verb.startswith("s'"):
            self.get_root = self.get_root
            for personal_pronoun, reflexive2 in zip(personal_pronouns, reflexive_2): 
                if personal_pronoun not in tuple(new_pronouns):
                    new_pronouns.append(personal_pronoun + reflexive2)
                self.personal_pronouns = new_pronouns

        if self.verb == "avoir":
            for verb in self.avoirInImparfait():
                # self.conjugated_verbs["third"].append(verb)
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["third"])

        if self.verb == "être" or self.verb == "etre":
            for verb in self.etreInImparfait():
                #self.conjugated_verbs["third"].append(verb)
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["third"])

        if self.verb == "aller":
            for personal_pronoun, ending in zip(personal_pronouns_2, imparfait_endings):
                self.conjugated_verbs["first"].append(personal_pronoun + self.verb[:-2] + ending)
            self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
            
        if four_letters_ending_rules == "oyer" or four_letters_ending_rules == "uyer":
            self.get_root = root[:-1]

        if self.verb[0:2] ==("s'"):#and four_letters_ending_rules != "oyer :
            self.get_root = self.get_root[2:]
        if self.verb[0:3] == ("se "):
            if four_letters_ending_rules == "oyer" or four_letters_ending_rules == "uyer":
                self.get_root = self.get_root[2:]
        
         # This for loop will check if the verb start with vowel or not
        if self.verb in tuple(f) and three_letters_ending_rules != "cer" and three_letters_ending_rules != "ger":
            # self.conjugated_verbs["first"].append("First group verb")
            if self.verb[0:2] != "s'" and self.verb[0] in tuple(vowels):
                conjugated_verb1 = self.personal_pronouns[0][0] + "'{}{}".format(self.get_root, self.imparfait_endings[0])
                self.conjugated_verbs["first"].append(conjugated_verb1)
            
            if self.verb[0] not in tuple(vowels):
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

            # self.conjugated_verbs["first"].append("First group verb")
            vow = self.verb[0]
            if vow in tuple(self.vowels):
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

 
            self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
                    # for personal_pronoun, ending in zip(self.personal_pronouns[3:], imparfait_endings_for_second_group_verbs[3:]):
                    #     self.conjugated_verbs["second"].append(personal_pronoun + self.verb[:-2] + "ï" + ending[1:])

        if self.verb in tuple(s):
            if self.verb.startswith(tuple(vowels)):
                self.personal_pronouns = personal_pronouns_2
            if not self.verb.endswith("haïr"):
                for personal_pronoun, ending in zip(self.personal_pronouns,
                                                    imparfait_endings_for_second_group_verbs):
                    self.conjugated_verbs["second"].append(personal_pronoun + self.get_root + ending)
            if self.verb.endswith("haïr"):
                if not self.verb.startswith("se " or "s'"):
                    for personal_pronoun, ending in zip(self.personal_pronouns[:3],
                                                        imparfait_endings_for_second_group_verbs[:3]):
                        self.conjugated_verbs["second"].append(personal_pronoun + self.verb[:-2] + "ï" + ending[1:])
                    for personal_pronoun, ending in zip(self.personal_pronouns[3:],
                                                        imparfait_endings_for_second_group_verbs[3:]):
                        self.conjugated_verbs["second"].append(personal_pronoun + self.verb[:-2] + "ï" + ending[1:])

            if self.verb.endswith("haïr"):
                if self.verb.startswith("se " or "s'"):
                    for personal_pronoun, ending in zip(self.personal_pronouns[:3],
                                                        imparfait_endings_for_second_group_verbs[:3]):
                        self.conjugated_verbs["second"].append(personal_pronoun + self.verb[2:-2] + "ï" + ending[1:])
                    for personal_pronoun, ending in zip(self.personal_pronouns[3:],
                                                        imparfait_endings_for_second_group_verbs[3:]):
                        self.conjugated_verbs["second"].append(personal_pronoun + self.verb[2:-2] + "ï" + ending[1:])

            self.ids.name_label.text = "\n".join(self.conjugated_verbs["second"])

        if self.verb.endswith(tuple(string_tuple)):
            self.ids.name_label.text = "It's coming soon!"

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
        self.get_root = root
        if verb == "avérer":
            self.verb = ""
        
        
        self.simple_past_endings_for_first_group_verbs = simple_past_endings_for_first_group_verbs
        self.simple_past_endings_for_second_group_verbs = simple_past_endings_for_second_group_verbs
        
        self.conjugated_verbs = {"first": [], "second": [], "third": []}
        # self.vow = ""
        new_pronouns = []
        new_pronouns_2 = []
        if self.verb[0:3] == "se ":
            # self.get_root = root[2:]
            self.verb = self.verb[3:]
            for personal_pronoun, reflexive in zip(personal_pronouns, past_reflexive): 
                new_pronouns_2.append(personal_pronoun + reflexive)
            self.personal_pronouns = new_pronouns_2


        if self.verb.startswith("s'"):
            # self.get_root = root[2:]
            self.verb = self.verb[2:]
            # print(self.get_root)
            for personal_pronoun, reflexive2 in zip(personal_pronouns, reflexive_2): 
                if personal_pronoun not in tuple(new_pronouns):
                    new_pronouns.append(personal_pronoun + reflexive2)
                self.personal_pronouns = new_pronouns

        if self.verb == "avoir":
            for verb in self.avoirInSimplePast():
                #self.conjugated_verbs["third"].append(verb)
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["third"])

        if self.verb == "être" or self.verb == "etre":
            for verb in self.etreInSimplePast():
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["third"])    

        if self.verb == "aller":
            for personal_pronoun, ending in zip(personal_pronouns_2, simple_past_endings_for_first_group_verbs):
                self.conjugated_verbs["first"].append(personal_pronoun + self.verb[:-2] + ending)
            self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
                
        
        if self.verb in tuple(f):
                
            for personal_pronoun, ending in zip(self.personal_pronouns, simple_past_endings_for_first_group_verbs):
               
                if not self.verb.endswith("ger") and not self.verb.endswith("cer"):    
                    self.conjugated_verbs["first"].append(personal_pronoun + self.verb[:-2] + ending)
                if self.verb.endswith("ger"):
                    self.conjugated_verbs["first"].append(personal_pronoun + self.verb[:-1] + ending)
                if self.verb.endswith("cer"):
                    self.conjugated_verbs["first"].append(personal_pronoun + self.verb[:-3] + "ç" + ending)
                
                # Handle ger, cer...,verbs
            if self.verb.endswith("ger"):
                self.conjugated_verbs["first"][5] = self.conjugated_verbs["first"][5][:-6] + "èrent"
            if self.verb.endswith("cer"):
                self.conjugated_verbs["first"][5] = self.conjugated_verbs["first"][5][:-6] + "cèrent"
            
            if self.get_root[0] in tuple(vowels):
                self.conjugated_verbs["first"][0] = self.conjugated_verbs["first"][0][0] + "'" + self.conjugated_verbs["first"][0][2:]
            self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
 
        
        if self.verb in tuple(s):
            if self.verb.startswith(tuple(vowels)):
                self.personal_pronouns = personal_pronouns_2            
            if not self.verb.endswith("haïr"):    
                for personal_pronoun, ending in zip(self.personal_pronouns, simple_past_endings_for_second_group_verbs):
                    self.conjugated_verbs["second"].append(personal_pronoun + self.get_root + ending)
            if self.verb.endswith("haïr"):
                if not self.verb.startswith("se " or "s'"):
                    for personal_pronoun, ending in zip(self.personal_pronouns, simple_past_endings_for_second_group_verbs):
                        self.conjugated_verbs["second"].append(personal_pronoun + self.verb[:-2] + "ï" + ending[1:])
                    
            if self.verb.endswith("haïr"):    
                if self.verb.startswith("se " or "s'"):
                    for personal_pronoun, ending in zip(self.personal_pronouns, simple_past_endings_for_second_group_verbs):
                        self.conjugated_verbs["second"].append(personal_pronoun + self.verb[2:-2] + "ï" + ending[1:])
                    
            self.ids.name_label.text = "\n".join(self.conjugated_verbs["second"])

        if self.verb.endswith(tuple(string_tuple)):
            self.ids.name_label.text = "It's coming soon!"            


    
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
        if verb == "avérer":
            self.verb = ""
        else:
            self.verb = verb
        self.personal_pronouns = personal_pronouns
        self.get_root = root
        self.simple_future_endings = simple_future_endings
        self.conjugated_verbs = {"first": [], "second": [], "third": []}
        self.vow = ""
        new_pronouns = []
        # if self.verb.startswith("se "):
        #     self.get_root = root[2:]
        if self.verb.startswith("se "):
            self.get_root = root[2:]
            for personal_pronoun, reflexive in zip(personal_pronouns, reflexive_1): 
                personal_pronouns.append(personal_pronoun + reflexive)
            self.personal_pronouns = personal_pronouns[6:]

        if self.verb.startswith("s'"):
            self.get_root = root[2:]

            for personal_pronoun, reflexive2 in zip(personal_pronouns, reflexive_2): 
                if personal_pronoun not in tuple(new_pronouns):
                    new_pronouns.append(personal_pronoun + reflexive2)
                self.personal_pronouns = new_pronouns

        for ending in tuple(peser_family[:-1]):
            if self.verb.endswith(ending):

                self.get_root = root[:-3] + "è" + self.verb[-3:-1] #root[-1]
            if self.verb[0:3] == "se " and self.verb.endswith(ending):
                self.get_root = root[2:-3] + "è" + self.verb[-3:-1]#root[-1]
            if self.verb[0:2] == "s'" and self.verb.endswith(ending):
                self.get_root = root[2:-3] + "è" + self.verb[-3:-1]#root[-1]
        
        for ending in tuple(peser_family):
            if self.verb.endswith(ending) and ending not in tuple(peser_family[:-1]):
                self.get_root = root[:-4] + "è" + self.verb[-4:-1]

        if self.verb not in tuple(exceptions_of_eler_and_eter_family):
            if self.verb.endswith("eler") or self.verb.endswith("eter"):
                if self.verb[:3] != "se ":
                    self.get_root = self.verb[:-1] + self.verb[-3:-1]
                if self.verb[0:2] != "s'":
                    self.get_root = self.verb[:-2] + self.verb[-3:-1]
                if self.verb.startswith("se ") or self.verb.startswith("s'"):
                    self.get_root = self.verb[2:-2] + self.verb[-3:-1]
        if self.verb in tuple(exceptions_of_eler_and_eter_family):
            if not self.verb.startswith("se ") or not self.verb.startswith("s'"):
                self.get_root = self.verb[:-4] + "è" + self.verb[-3:-1]
            if self.verb.startswith("se ") or self.verb.startswith("s'"):
                self.get_root = self.verb[2:-4] + "è" + self.verb[-3:-1]

        if self.verb.endswith("ayer"):
            self.get_root = self.verb[:-3] + "i" + self.verb[-2] 
        if self.verb == "avoir":
            for verb in self.avoirInSimpleFuture():
                #self.conjugated_verbs["third"].append(verb)
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["third"])

        if self.verb == "être" or self.verb == "etre":
            for verb in self.etreInSimpleFuture():
                #self.conjugated_verbs["third"].append(verb)
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["third"])
        # This for loop will check if the verb start with vowel or not
        
        # if self.verb == "renvoyer" or self.verb == "envoyer":
        #     self.get_root = self.get_root[:-3] + "er"
        if self.verb in tuple(f):#is_infinitive == "er" and self.get_root != "alle":
            if self.verb == "renvoyer" or self.verb == "envoyer" or self.verb == "se renvoyer" or self.verb == "s'envoyer":
                self.get_root = self.get_root[:-3] + "er"
            if self.verb != "renvoyer" and self.verb != "envoyer" and self.verb != "se renvoyer" and self.verb != "s'envoyer":
                if four_letters_ending_rules == "oyer" or four_letters_ending_rules == "uyer":
                    self.get_root = self.get_root[: -2] + "ie"
            # self.conjugated_verbs["first"].append("First group verb")
            if self.verb[0] in tuple(vowels):
                conjugated_verb1 = self.personal_pronouns[0][0] + "'{}{}".format(self.get_root, self.simple_future_endings[0])
                self.conjugated_verbs["first"].append(conjugated_verb1)
            
            if self.verb[0] not in tuple(vowels):
                conjugated_verb1 = self.personal_pronouns[0] + "{}{}".format(self.get_root, self.simple_future_endings[0])
                self.conjugated_verbs["first"].append(conjugated_verb1)


            conjugated_verb2 = self.personal_pronouns[1] + "{}{}".format(self.get_root, self.simple_future_endings[1])
            self.conjugated_verbs["first"].append(conjugated_verb2)

            conjugated_verb3 = self.personal_pronouns[2] + "{}{}".format(self.get_root, self.simple_future_endings[2])
            self.conjugated_verbs["first"].append(conjugated_verb3)

            conjugated_verb4 = self.personal_pronouns[3] + "{}{}".format(self.get_root, self.simple_future_endings[3])
            self.conjugated_verbs["first"].append(conjugated_verb4)

            conjugated_verb5 = self.personal_pronouns[4] + "{}{}".format(self.get_root, self.simple_future_endings[4])
            self.conjugated_verbs["first"].append(conjugated_verb5)

            conjugated_verb6 = self.personal_pronouns[5] + "{}{}".format(self.get_root, self.simple_future_endings[5])
            self.conjugated_verbs["first"].append(conjugated_verb6)

            self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
 
        if self.get_root == "alle" and self.is_infinitive == "er":
            #form_infinitive = "Third group verb"
            #self.conjugated_verbs["first"].append(form_infinitive)
            conjugated_verb1 = self.personal_pronouns[0][0] + "'" + "irai"
            self.conjugated_verbs["first"].append(conjugated_verb1)

            conjugated_verb2 = self.personal_pronouns[1] + "iras"
            self.conjugated_verbs["first"].append(conjugated_verb2)

            conjugated_verb3 = self.personal_pronouns[2] + "ira"
            self.conjugated_verbs["first"].append(conjugated_verb3)

            conjugated_verb4 = self.personal_pronouns[3] + "{}{}".format("i",self.simple_future_endings[3])
            self.conjugated_verbs["first"].append(conjugated_verb4)

            conjugated_verb5 = self.personal_pronouns[4] + "{}{}".format("i",self.simple_future_endings[4])
            self.conjugated_verbs["first"].append(conjugated_verb5)

            conjugated_verb6 = self.personal_pronouns[5] + "iront"
            self.conjugated_verbs["first"].append(conjugated_verb6)
            self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])

    # Handling second group verb

        if self.verb in tuple(s):
            if self.verb.startswith(tuple(vowels)):
                self.personal_pronouns = personal_pronouns_2            
            if not self.verb.endswith("haïr"):
                for personal_pronoun, ending in zip(self.personal_pronouns, simple_future_endings):
                    self.conjugated_verbs["second"].append(personal_pronoun + self.get_root + ending)
            if self.verb.endswith("haïr"):
                if not self.verb.startswith("se " or "s'"):
                    for personal_pronoun, ending in zip(self.personal_pronouns[:3], simple_future_endings[:3]):
                        self.conjugated_verbs["second"].append(personal_pronoun + self.verb[:-2] + "ï" + ending)
                    for personal_pronoun, ending in zip(self.personal_pronouns[3:], simple_future_endings[3:]):
                        self.conjugated_verbs["second"].append(personal_pronoun + self.verb[:-2] + "ï" + ending)

            if self.verb.endswith("haïr"):
                if self.verb.startswith("se " or "s'"):
                    for personal_pronoun, ending in zip(self.personal_pronouns[:3], simple_future_endings[:3]):
                        self.conjugated_verbs["second"].append(personal_pronoun + self.verb[2:-2] + "ï" + ending)
                    for personal_pronoun, ending in zip(self.personal_pronouns[3:], simple_future_endings[3:]):
                        self.conjugated_verbs["second"].append(personal_pronoun + self.verb[2:-2] + "ï" + ending)

            self.ids.name_label.text = "\n".join(self.conjugated_verbs["second"])

        if self.verb.endswith(tuple(string_tuple)):
            self.ids.name_label.text = "It's coming soon!"            

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
        conjugated_verbs =[]
        self.vow = ""
        self.avoir = self.avoirInPresentTense()
        self.etre = self.etreInPresentTense()
        new_pronouns = []
        reflexive_verbs =[]
        modified_personal_pronouns = []
        if self.verb.startswith("se "):
            self.get_root = self.get_root[2:]
            for personal_pronoun, reflexive in zip(personal_pronouns, reflexive_1): 
                personal_pronouns.append(personal_pronoun + reflexive)
            self.personal_pronouns = personal_pronouns[-6:]
            for personal_pronoun in self.personal_pronouns[0:1]:
                modified_personal_pronouns.append(personal_pronoun)
            for personal_pronoun in self.personal_pronouns[1:3]:
                modified_personal_pronouns.append(personal_pronoun[:4] + "'")
            for personal_pronoun in self.personal_pronouns[3:]:
                modified_personal_pronouns.append(personal_pronoun)
            self.personal_pronouns = modified_personal_pronouns

            if  is_infinitive == "er" and not self.verb.endswith(tuple_third_group_endings) and not self.verb.endswith(tuple(verbs_of_movement)):      
                for pronoun, conjugated_etre in zip(self.personal_pronouns,etre_in_present_tense):
                    reflexive_verbs.append(pronoun + " " + conjugated_etre)
                for verb in reflexive_verbs[:3]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
                for verb in reflexive_verbs[3:]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle + "s"))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
       

        if self.verb.startswith("s'"):
            self.get_root = self.get_root[2:]
            for personal_pronoun, reflexive in zip(personal_pronouns, reflexive_1): 
                personal_pronouns.append(personal_pronoun + reflexive)
            self.personal_pronouns = personal_pronouns[-6:]
            for personal_pronoun in self.personal_pronouns[0:1]:
                modified_personal_pronouns.append(personal_pronoun)
            for personal_pronoun in self.personal_pronouns[1:3]:
                modified_personal_pronouns.append(personal_pronoun[:4] + "'")
            for personal_pronoun in self.personal_pronouns[3:]:
                modified_personal_pronouns.append(personal_pronoun)
            self.personal_pronouns = modified_personal_pronouns

            if  is_infinitive == "er" and not self.verb.endswith(tuple_third_group_endings) and not self.verb.endswith(tuple(verbs_of_movement)):      
                for pronoun, conjugated_etre in zip(self.personal_pronouns,etre_in_present_tense):
                    reflexive_verbs.append(pronoun + " " + conjugated_etre)
                for verb in reflexive_verbs[:3]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
                for verb in reflexive_verbs[3:]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle + "s"))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
       
        if  is_infinitive == "er" and not self.verb.startswith("se ") and not self.verb.startswith("s'") and not self.verb.endswith(tuple_third_group_endings) and not self.verb.endswith(tuple(verbs_of_movement)):      
            for verb in self.avoir:
                self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle))
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
        
        if is_infinitive == "er" and not self.verb.startswith("se ") and not self.verb.startswith("s'") and self.verb.endswith(tuple(verbs_of_movement)) and not self.verb.endswith(tuple(third_group_endings)):
                for verb in self.etre[0:3]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle))
                for verb in self.etre[3:6]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle) + "s")
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
        if is_infinitive == "ir" and not self.verb.startswith("se ") and not self.verb.startswith("s'") and self.verb and not self.verb.endswith(tuple(verbs_of_movement)):
            if self.verb.endswith("courir"):
                for verb in self.avoirInPresentTense():
                    self.conjugated_verbs["second"].append("{} {}".format(verb, self.get_root + "u"))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["second"])

            elif self.verb == "avoir":
                for verb in self.avoirInPresentTense():
                    conjugated_verbs.append("{} {}".format(verb, "eu"))
                    self.ids.name_label.text = "\n".join(conjugated_verbs)
            
            else:
                for verb in self.avoirInPresentTense():
                    self.conjugated_verbs["second"].append("{} {}".format(verb, self.get_root + "i"))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["second"])
        if is_infinitive == "ir" and not self.verb.startswith("se ") and not self.verb.startswith("s'") and self.verb.endswith(tuple(verbs_of_movement)):
            for verb in self.etre[0:3]:
                self.conjugated_verbs["second"].append("{} {}".format(verb, self.get_root + "i"))  
            for verb in self.etre[3:6]:
                self.conjugated_verbs["second"].append("{} {}".format(verb, self.get_root + "is"))
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["second"])
        
        if self.verb == "être":
            for verb in self.avoirInPresentTense():
                conjugated_verbs.append("{} {}".format(verb, "été"))
                self.ids.name_label.text = "\n".join(conjugated_verbs)

        if self.verb.endswith(tuple(string_tuple)):
            self.ids.name_label.text = "It's coming soon!"                

    def past_perfect(self):
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
        conjugated_verbs =[]
        self.vow = ""
        self.avoir = self.avoirInImparfait()
        self.etre = self.etreInImparfait()

        new_pronouns = []
        reflexive_verbs =[]
        modified_personal_pronouns = []
        if self.verb.startswith("se "):
            self.get_root = self.get_root[2:]
            for personal_pronoun, reflexive in zip(personal_pronouns, reflexive_1): 
                personal_pronouns.append(personal_pronoun + reflexive)
            self.personal_pronouns = personal_pronouns[-6:]
            for personal_pronoun in self.personal_pronouns[0:1]:
                modified_personal_pronouns.append(personal_pronoun[:4] + "'")
            for personal_pronoun in self.personal_pronouns[1:3]:
                modified_personal_pronouns.append(personal_pronoun[:4] + "'")
            for personal_pronoun in self.personal_pronouns[3:5]:
                modified_personal_pronouns.append(personal_pronoun)
            for personal_pronoun in self.personal_pronouns[5:]:
                modified_personal_pronouns.append(personal_pronoun[:5] + "'")
            self.personal_pronouns = modified_personal_pronouns
            
            if  is_infinitive == "er" and not self.verb.endswith(tuple_third_group_endings) and not self.verb.endswith(tuple(verbs_of_movement)):      
                for pronoun, conjugated_etre in zip(self.personal_pronouns,etre_in_imparfait):
                    reflexive_verbs.append(pronoun + " " + conjugated_etre)
                for verb in reflexive_verbs[:3]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
                for verb in reflexive_verbs[3:]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle + "s"))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
       

        if self.verb.startswith("s'"):
            self.get_root = self.get_root[2:]
            for personal_pronoun, reflexive in zip(personal_pronouns, reflexive_1): 
                personal_pronouns.append(personal_pronoun + reflexive)
            self.personal_pronouns = personal_pronouns[-6:]
            for personal_pronoun in self.personal_pronouns[0:1]:
                modified_personal_pronouns.append(personal_pronoun[:4] + "'")
            for personal_pronoun in self.personal_pronouns[1:3]:
                modified_personal_pronouns.append(personal_pronoun[:4] + "'")
            for personal_pronoun in self.personal_pronouns[3:5]:
                modified_personal_pronouns.append(personal_pronoun)
            for personal_pronoun in self.personal_pronouns[5:]:
                modified_personal_pronouns.append(personal_pronoun[:5] + "'")
            self.personal_pronouns = modified_personal_pronouns
        
            if  is_infinitive == "er" and not self.verb.endswith(tuple_third_group_endings) and not self.verb.endswith(tuple(verbs_of_movement)):      
                for pronoun, conjugated_etre in zip(self.personal_pronouns,etre_in_imparfait):
                    reflexive_verbs.append(pronoun + " " + conjugated_etre)
                for verb in reflexive_verbs[:3]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
                for verb in reflexive_verbs[3:]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle + "s"))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
       
        
        if  is_infinitive == "er" and not self.verb.startswith("se ") and not self.verb.startswith("s'") and not self.verb.endswith(tuple_third_group_endings) and not self.verb.endswith(tuple(verbs_of_movement)):      
                for verb in self.avoir:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
            
        if is_infinitive == "er" and not self.verb.startswith("se ") and not self.verb.startswith("s'") and self.verb.endswith(tuple(verbs_of_movement)) and not self.verb.endswith(tuple(third_group_endings)):
                for verb in self.etre[0:3]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle))
                for verb in self.etre[3:6]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle) + "s")
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
        if is_infinitive == "ir" and not self.verb.startswith("se ") and not self.verb.startswith("s'") and self.verb and not self.verb.endswith(tuple(verbs_of_movement)):
            if self.verb.endswith("courir"):
                for verb in self.avoir:
                    self.conjugated_verbs["second"].append("{} {}".format(verb, self.get_root + "u"))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["second"])

            elif self.verb == "avoir":
                for verb in self.avoir:
                    conjugated_verbs.append("{} {}".format(verb, "eu"))
                    self.ids.name_label.text = "\n".join(conjugated_verbs)
            
            else:
                for verb in self.avoir:
                    self.conjugated_verbs["second"].append("{} {}".format(verb, self.get_root + "i"))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["second"])
        if is_infinitive == "ir" and not self.verb.startswith("se ") and not self.verb.startswith("s'") and self.verb.endswith(tuple(verbs_of_movement)):
            for verb in self.etre[0:3]:
                self.conjugated_verbs["second"].append("{} {}".format(verb, self.get_root + "i"))  
            for verb in self.etre[3:6]:
                self.conjugated_verbs["second"].append("{} {}".format(verb, self.get_root + "is"))
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["second"])
        
        if self.verb == "être":
            for verb in self.avoir:
                conjugated_verbs.append("{} {}".format(verb, "été"))
                self.ids.name_label.text = "\n".join(conjugated_verbs)

        if self.verb.endswith(tuple(string_tuple)):
            self.ids.name_label.text = "It's coming soon!"                

    
    def passeAnterieur(self):
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
        conjugated_verbs =[]
        self.vow = ""
        self.avoir = self.avoirInSimplePast()
        self.etre = self.etreInSimplePast()

        new_pronouns = []
        reflexive_verbs =[]
        modified_personal_pronouns = []
        if self.verb.startswith("se "):
            self.get_root = self.get_root[2:]
            for personal_pronoun, reflexive in zip(personal_pronouns, reflexive_1): 
                personal_pronouns.append(personal_pronoun + reflexive)
            self.personal_pronouns = personal_pronouns[-6:]
            
            if  is_infinitive == "er" and not self.verb.endswith(tuple_third_group_endings) and not self.verb.endswith(tuple(verbs_of_movement)):      
                for pronoun, conjugated_etre in zip(self.personal_pronouns,etre_in_simple_past_tense):
                    reflexive_verbs.append(pronoun + " " + conjugated_etre)
                for verb in reflexive_verbs[:3]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
                for verb in reflexive_verbs[3:]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle + "s"))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
       

        if self.verb.startswith("s'"):
            self.get_root = self.get_root[2:]
            for personal_pronoun, reflexive in zip(personal_pronouns, reflexive_1): 
                personal_pronouns.append(personal_pronoun + reflexive)
            self.personal_pronouns = personal_pronouns[-6:]
        
            if  is_infinitive == "er" and not self.verb.endswith(tuple_third_group_endings) and not self.verb.endswith(tuple(verbs_of_movement)):      
                for pronoun, conjugated_etre in zip(self.personal_pronouns,etre_in_simple_past_tense):
                    reflexive_verbs.append(pronoun + " " + conjugated_etre)
                for verb in reflexive_verbs[:3]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
                for verb in reflexive_verbs[3:]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle + "s"))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
       
        
        if  is_infinitive == "er" and not self.verb.startswith("se ") and not self.verb.startswith("s'") and not self.verb.endswith(tuple_third_group_endings) and not self.verb.endswith(tuple(verbs_of_movement)):      
                for verb in self.avoir:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
            
        if is_infinitive == "er" and not self.verb.startswith("se ") and not self.verb.startswith("s'") and self.verb.endswith(tuple(verbs_of_movement)) and not self.verb.endswith(tuple(third_group_endings)):
                for verb in self.etre[0:3]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle))
                for verb in self.etre[3:6]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle) + "s")
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
        if is_infinitive == "ir" and not self.verb.startswith("se ") and not self.verb.startswith("s'") and self.verb and not self.verb.endswith(tuple(verbs_of_movement)):
            if self.verb.endswith("courir"):
                for verb in self.avoir:
                    self.conjugated_verbs["second"].append("{} {}".format(verb, self.get_root + "u"))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["second"])

            elif self.verb == "avoir":
                for verb in self.avoir:
                    conjugated_verbs.append("{} {}".format(verb, "eu"))
                    self.ids.name_label.text = "\n".join(conjugated_verbs)
            
            else:
                for verb in self.avoir:
                    self.conjugated_verbs["second"].append("{} {}".format(verb, self.get_root + "i"))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["second"])
        if is_infinitive == "ir" and not self.verb.startswith("se ") and not self.verb.startswith("s'") and self.verb.endswith(tuple(verbs_of_movement)):
            for verb in self.etre[0:3]:
                self.conjugated_verbs["second"].append("{} {}".format(verb, self.get_root + "i"))  
            for verb in self.etre[3:6]:
                self.conjugated_verbs["second"].append("{} {}".format(verb, self.get_root + "is"))
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["second"])
        
        if self.verb == "être":
            for verb in self.avoir:
                conjugated_verbs.append("{} {}".format(verb, "été"))
                self.ids.name_label.text = "\n".join(conjugated_verbs)

        if self.verb.endswith(tuple(string_tuple)):
            self.ids.name_label.text = "It's coming soon!"                

    
    def futurePerfect(self):
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
        conjugated_verbs =[]
        self.vow = ""
        self.avoir = self.avoirInSimpleFuture()
        self.etre = self.etreInSimpleFuture()

        new_pronouns = []
        reflexive_verbs =[]
        modified_personal_pronouns = []
        if self.verb.startswith("se "):
            self.get_root = self.get_root[2:]
            for personal_pronoun, reflexive in zip(personal_pronouns, reflexive_1): 
                personal_pronouns.append(personal_pronoun + reflexive)
            self.personal_pronouns = personal_pronouns[-6:]
            
            
            if  is_infinitive == "er" and not self.verb.endswith(tuple_third_group_endings) and not self.verb.endswith(tuple(verbs_of_movement)):      
                for pronoun, conjugated_etre in zip(self.personal_pronouns,etre_in_simple_future):
                    reflexive_verbs.append(pronoun + " " + conjugated_etre)
                for verb in reflexive_verbs[:3]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
                for verb in reflexive_verbs[3:]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle + "s"))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
       

        if self.verb.startswith("s'"):
            self.get_root = self.get_root[2:]
            for personal_pronoun, reflexive in zip(personal_pronouns, reflexive_1): 
                personal_pronouns.append(personal_pronoun + reflexive)
            self.personal_pronouns = personal_pronouns[-6:]
        
            if  is_infinitive == "er" and not self.verb.endswith(tuple_third_group_endings) and not self.verb.endswith(tuple(verbs_of_movement)):      
                for pronoun, conjugated_etre in zip(self.personal_pronouns,etre_in_simple_future):
                    reflexive_verbs.append(pronoun + " " + conjugated_etre)
                for verb in reflexive_verbs[:3]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
                for verb in reflexive_verbs[3:]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle + "s"))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
       
        
        if  is_infinitive == "er" and not self.verb.startswith("se ") and not self.verb.startswith("s'") and not self.verb.endswith(tuple_third_group_endings) and not self.verb.endswith(tuple(verbs_of_movement)):      
                for verb in self.avoir:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
            
        if is_infinitive == "er" and not self.verb.startswith("se ") and not self.verb.startswith("s'") and self.verb.endswith(tuple(verbs_of_movement)) and not self.verb.endswith(tuple(third_group_endings)):
                for verb in self.etre[0:3]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle))
                for verb in self.etre[3:6]:
                    self.conjugated_verbs["first"].append("{} {}".format(verb, self.get_root + first_group_verbs_past_participle) + "s")
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["first"])
        if is_infinitive == "ir" and not self.verb.startswith("se ") and not self.verb.startswith("s'") and self.verb and not self.verb.endswith(tuple(verbs_of_movement)):
            if self.verb.endswith("courir"):
                for verb in self.avoir:
                    self.conjugated_verbs["second"].append("{} {}".format(verb, self.get_root + "u"))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["second"])

            elif self.verb == "avoir":
                for verb in self.avoir:
                    conjugated_verbs.append("{} {}".format(verb, "eu"))
                    self.ids.name_label.text = "\n".join(conjugated_verbs)
            
            else:
                for verb in self.avoir:
                    self.conjugated_verbs["second"].append("{} {}".format(verb, self.get_root + "i"))
                    self.ids.name_label.text = "\n".join(self.conjugated_verbs["second"])
        if is_infinitive == "ir" and not self.verb.startswith("se ") and not self.verb.startswith("s'") and self.verb.endswith(tuple(verbs_of_movement)):
            for verb in self.etre[0:3]:
                self.conjugated_verbs["second"].append("{} {}".format(verb, self.get_root + "i"))  
            for verb in self.etre[3:6]:
                self.conjugated_verbs["second"].append("{} {}".format(verb, self.get_root + "is"))
                self.ids.name_label.text = "\n".join(self.conjugated_verbs["second"])
        
        if self.verb == "être":
            for verb in self.avoir:
                conjugated_verbs.append("{} {}".format(verb, "été"))
                self.ids.name_label.text = "\n".join(conjugated_verbs)

        if self.verb.endswith(tuple(string_tuple)):
            self.ids.name_label.text = "It's coming soon!"                


    mode = False
    def mode_indicatif_control(self, widget):
        #widget.state = "down"
        #print("state is", widget.state)
        if widget.state == "normal":
            self.infinitive()
        if widget.state == "down":
            return self.conjugate_first_group_verbs_in_simple_present()

    
class TheLabApp(App, Leconjugueur):
    pass


TheLabApp().run()

############################ 
