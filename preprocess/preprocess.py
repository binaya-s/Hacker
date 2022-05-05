import os

data_root_dir = r"VCTK-Corpus_mini"
h5py_path = r"norm_vctk.h5py"
train_proportion = 0.9
index_path = r"index_path.json"
n_samples = 50000
seg_len = 128
speaker_used_path = r"speaker-used.txt"

cmd = f"make_dataset_vctk.py {data_root_dir} {h5py_path} {train_proportion}"
os.system(cmd)
print("File 1 executed")
cmd = f"python3 make_single_samples.py {h5py_path} {index_path} {n_samples} {seg_len} {speaker_used_path}"
os.system(cmd)
print("File 2 executed")
