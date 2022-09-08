import pandas as pd
import numpy
data = pd.read_csv('~/Nextcloud/Documents/Pol/Quimica_elena/Genetic_TRY2.csv', encoding='unicode_escape', sep=';', on_bad_lines='skip')
data['TraitID'] = data['TraitID'].astype('Int64')
data['1Cpg'] = data['1Cpg'].str.replace(',', '.')
data['1Cpg'] = pd.to_numeric(data['1Cpg'])
Traits = data['TraitID'].unique()
Traits = Traits[~numpy.isnan(Traits)]

for trait in Traits:
    globals()["mask"+str(trait)] = data['TraitID'] == trait
    globals()[f"Trait{trait}"] = pd.DataFrame(data[globals()["mask"+str(trait)]])
    species = len(globals()[f"Trait{trait}"]["AccSpeciesName"].unique())
    max_genome = globals()[f"Trait{trait}"]["1Cpg"].max()
    min_genome = globals()[f"Trait{trait}"]["1Cpg"].min()
    print(f"For trait {trait} we have {species} species with max genome size of {max_genome} and minimum genome size of {min_genome}")
    #globals()[f"Trait{trait}"].to_csv(f'~/Nextcloud/Documents/Pol/Quimica_elena/Trait{trait}.csv', index=False)
for trait in Traits:
    globals()[f"Trait{trait}_3_or_more"] = pd.DataFrame(globals()[f"Trait{trait}"][globals()[f"Trait{trait}"].groupby(["AccSpeciesName"])["AccSpeciesName"].transform("size") > 2])
    #globals()[f"Trait{trait}_3_or_more"].to_csv(f'~/Nextcloud/Documents/Pol/Quimica_elena/Trait{trait}_3_or_more.csv', index = False)
    species = len(globals()[f"Trait{trait}_3_or_more"]["AccSpeciesName"].unique())
    globals()[f"species{trait}"] = globals()[f"Trait{trait}_3_or_more"]["AccSpeciesName"].unique()
    max_genome = globals()[f"Trait{trait}_3_or_more"]["1Cpg"].max()
    min_genome = globals()[f"Trait{trait}_3_or_more"]["1Cpg"].min()
    print(f"For trait {trait} we have {species} species with max genome size of {max_genome} and minimum genome size of {min_genome}")
from functools import reduce
int1 = numpy.intersect1d(species335,species343)
int2 = numpy.intersect1d(species15,int1)
int3 = numpy.intersect1d(species8,int2)
int4 = numpy.intersect1d(species22,int3)
int5 = numpy.intersect1d(species14,int4)
len(int5)
