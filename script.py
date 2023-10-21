import os
import shutil

dest = os.getcwd()
os.chdir("../PDB_SETS")
# print(os.getcwd())

for i in range(1, 2):
	os.chdir(f"SET_{i}")
	PDBS = [file for file in os.listdir()]
	print(os.getcwd())
	for pdb in PDBS:
		os.chdir(pdb)
		src = os.path.join(os.getcwd(), f'{pdb}.pickle')
		# print(src)
		shutil.copy(src, dest)
		os.chdir("../")
	os.chdir("../")

# os.chdir("../")




	


