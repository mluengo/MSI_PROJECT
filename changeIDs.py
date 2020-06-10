from Bio import PDB
# Change the atom index of pdb files: set the index of each
# chain as unique number. The first atom of the first chain 
# set to 1, following chains will have the fist index '+offset'.

# read pdb file
pdb_io = PDB.PDBIO()
pdb_parser = PDB.PDBParser()
pdbfile = '4bxl.pdb'
structure = pdb_parser.get_structure(" ", pdbfile)

# set the increment of index when changing chain
offset = 100 
# set max lenght of each chain
maxLen = 135

new_resnums = [i +1 for i in range(maxLen)]
aux=0
for model in structure:
    for chain in model:
        for i, residue in enumerate(chain.get_residues()):
            res_id = list(residue.id)
            res_id[1] = new_resnums[i]
            residue.id = tuple(res_id)
        new_resnums = [i + offset +aux for i in range(maxLen)]
        aux=offset

# save new pdb
pdb_io.set_structure(structure)
pdb_io.save(pdbfile + "-new.pdb")   
