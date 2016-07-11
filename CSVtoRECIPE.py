# -*- coding: utf-8 -*-
"""
Created on Friday, July 8, 2016
@author: brettbarbaro
"""

import csv
import math
import numpy
import json

# import data from csv file - Brett
f = "/Users/Brett/FELLOWSHIP/Syn1.0_proteome_spreadsheet_cut.csv"
all_data = []
cell_radius = 0.15  # um
cell_density = 1.07  # g/cc
protein_content_fraction = 0.163  # 155.0/950.0#0.163#by weight
cell_volume = 4.0 * math.pi * (math.pow(cell_radius, 3.0) / 3.0)  # cu um
cell_mass = cell_volume * cell_density * math.pow(10, -12)  # g
protein_mass = cell_mass * protein_content_fraction  # g
total_I = [0, 0, 0, 0]
total_IBAQ = [0, 0, 0, 0]
total_LFQ = [0, 0, 0, 0]
col_id = [42, 47, 51]
total = [total_I, total_IBAQ, total_LFQ]
oneMol = [total_I, total_IBAQ, total_LFQ]
with open(f, 'r') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        all_data.append(row)
        if len(all_data) == 1: continue
        for i in range(3):
            for j in range(4):
                intensity = row[col_id[i] + j]
                if intensity == "NaN":
                    intensity = 0
                else:
                    intensity = intensity.replace(",", ".")
                total[i][j] += float(intensity)
nbMol = []
avgMols = []
mWeight = []
names = []

# fill in missing data
#   Ingredients from proteomics:
#     Needs name (the name in the data you have)
#     Needs unique ID e.g. uniprot or ncbi (synthetic cell or http://wholecelldb.stanford.edu)
#     Needs the copy number of concentration (e.g. from mass spec, or http://wholecelldb.stanford.edu/ or david estimation from his painting...)
#     Fetch the sequence
#     Fetch or calculate  the molecular weight
#     From sequence retrieve a template from the PDB. Keep e-value and score…
#     Retrieve the multimer states for the structure using the PDB (biological assembly).
#     From sequence retrieve the localisation if unknow (e.g. cytoplasm, membrane etc,...)
#       http://www.ncbi.nlm.nih.gov/CBBresearch/Lu/subcellular/
#       http://www.imtech.res.in/raghava/pslpred/
#
#     From sequence and template from the PDB build an homology model (e.g. MODELLER or server license for MODELLER is MODELAJE in upper case)
#     If localisation is inner/outer membrane predict/retrieve the orientation of the structure  using http://opm.phar.umich.edu
#     Once a structure is known,
#       Load and center the atoms to the origin
#       apply k-means clustering based on number of atoms.
#       Generate a coarse molecular surface and save it as collada 1.4
#     Generate a recipe file in json.
#
#     Note:
#     http://wholecellkb.stanford.edu/list/Mgenitalium/ProteinComplex contains the mutlimeric states off all  proteins from mycoplasma genitalium. All entry are defined according the gene name (MG_001->MG_526). However for each gene there is a link to the uniprort.
#     Example code are in the github repo of autopack in the script folder
#     For ncbi access the fasta sequence can be done with
#     http://www.ncbi.nlm.nih.gov/protein/296456015?report=fasta&log$=seqview&format=text#

#   export results as json

print"done"

