"""
Test module for the synonyms module
"""
import unittest
import sys
import os 

PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from Strategies.LanguageChecking.languageCheck import check_if_english, check_if_dutch

class TestLanguage(unittest.TestCase):
    def test_check_lang_english_with_english_text(self):
        self.assertTrue(check_if_english("Electrocatalytic N-functionalisation of olefins towards aziridines and amines"))
    
    def test_check_lang_english_with_dutch_text(self):
        self.assertFalse(check_if_english("Elektrokatalytische N-functionalisatie van olefines ter vorming van aziridines en amines"))

    def test_check_lang_dutch_with_dutch_text(self):
        self.assertTrue(check_if_dutch("Heel wat N-bevattende chemicali\xc3\xabn (aryl- en alkylamines, aziridines)worden door indirecte methodes gemaakt, wat een slechteatoomeconomie en veel afvalproductie meebrengt. In de context vanduurzaamheid en gebruik van hernieuwbare energie zijn nieuwesynthesewegen nodig, vooral voor energierijke molecules zoalsaziridines. Het project combineert elektrokatalyse met eenvoudigestikstofbronnen, zoals ammoniak, om een aantal N-bevattendesleutelchemicali\xc3\xabn te maken.We starten met de 'electrificatie' van de jodide-gemedieerdeaziridinatie van styreen met ammoniak. Voor deze reactie gebruiktenwe eerder een chemische oxidatie, maar nu laten we de reactieopgaan door een 2-elektron anodische oxidatie. We ontwikkelen hetproces zowel voor aromatische als alifatische olefines, startend metcommerci\xc3\xable elektrodes. Vervolgens werken we op Nfunctionalisatiesvan olefines via 1-elektron oxidaties. Dit vraagt datwe de reactiviteit van de N-bron in bedwang houden, en dat wenieuwe elektrodes ontwerpen voor gecontroleerde oxidatie van de Nbron.We werken vooral met Ni-bevattende elektrodes, zoals ze ookvoor ureum oxidatie gebruikt worden. Tenslotte tonen we deopschaling en opwerking van de reacties voor 2 industrieelinteressante molecules. "))
    
    def test_check_lang_dutch_with_english_text(self):
        self.assertFalse(check_if_dutch("Many N-containing key chemicals like aryl- and alkylamines andaziridines are synthesised through indirect methods, which have verypoor atom efficiency and produce a lot of side products. In thecontext of sustainability and using renewable energy sources, newsynthetic approaches are needed, especially for chemicals with highenergy content like aziridines. The proposed research will useelectricity driven catalytic processes together with simple N-sourceslike ammonia to produce N-containing key chemicals.As a start, the iodide-mediated aziridination with NH3 and styrene asthe model olefin will be 'electrified'. As developed by our group, thisprocess used a chemical oxidant, but we will now drive it by a twoelectronanodic oxidation. We will develop the process both foraromatic and for aliphatic olefins, using commercially availableelectrodes to start with. Next, we will also develop Nfunctionalisationsof olefins that proceed via one-electron oxidations.This will require that we harness the reactivity of the N-source, andthat we design new electrode materials for controlled oxidation of theN-source. We focus on Ni-containing electrodes, well known frome.g. urea oxidation. Eventually upscaling and workup of the reactionswill be demonstrated for 2 molecules of industrial interest."))

if __name__ == '__main__':
    unittest.main()
