import sys
import os

#3 lines of code to get the import form other files working
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

import Enricher.enricher as enricher
from Utils.fris_entities import Project 
from Utils.enricher_entities import ProjectResult

project = Project('dfsfda', 'Some title', 'Some title', ['Electrocatalysis', 'Sustainability'], [], """Many N-containing key chemicals like aryl- and alkylamines andaziridines are synthesised through indirect methods, which have verypoor atom efficiency and produce a lot of side products. In thecontext of sustainability and using renewable energy sources, newsynthetic approaches are needed, especially for chemicals with highenergy content like aziridines. The proposed research will useelectricity driven catalytic 
processes together with simple N-sourceslike ammonia to produce N-containing key chemicals.As a start, the iodide-mediated aziridination with NH3 and styrene asthe model olefin will be 'electrified'. As developed by 
our group, thisprocess used a chemical oxidant, but we will now drive it by a twoelectronanodic oxidation. We will develop the process both foraromatic and for aliphatic olefins, using commercially availableelectrodes to start with. Next, we will also develop Nfunctionalisationsof olefins that proceed via one-electron oxidations.This will require that we harness the reactivity of the N-source, andthat we design new electrode materials for controlled oxidation of theN-source. We focus on Ni-containing electrodes, well known frome.g. urea oxidation. Eventually upscaling and workup of the reactionswill be demonstrated for 2 molecules of industrial interest."
""", """Many N-containing key chemicals like aryl- and alkylamines andaziridines are synthesised through indirect methods, which have verypoor atom efficiency and produce a lot of side products. In thecontext of sustainability and using renewable energy sources, newsynthetic approaches are needed, especially for chemicals with highenergy content like aziridines. The proposed research will useelectricity driven catalytic 
processes together with simple N-sourceslike ammonia to produce N-containing key chemicals.As a start, the iodide-mediated aziridination with NH3 and styrene asthe model olefin will be 'electrified'. As developed by 
our group, thisprocess used a chemical oxidant, but we will now drive it by a twoelectronanodic oxidation. We will develop the process both foraromatic and for aliphatic olefins, using commercially availableelectrodes to start with. Next, we will also develop Nfunctionalisationsof olefins that proceed via one-electron oxidations.This will require that we harness the reactivity of the N-source, andthat we design new electrode materials for controlled oxidation of theN-source. We focus on Ni-containing electrodes, well known frome.g. urea oxidation. Eventually upscaling and workup of the reactionswill be demonstrated for 2 molecules of industrial interest.""")
test_result = enricher.enrich_project(project)
print(test_result.alerts)
print(test_result.uuid)
for keyword in test_result.keywords:
    print(keyword.value, " / ",  keyword.score, " / ", keyword.language, "  ////  ")