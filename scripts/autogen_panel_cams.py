import copy

ref_data_file = "../data/BottomSilkScreen_altium.gbo"

big_sn_list = [[j for j in range(i,i+15)] for i in range(42061,42420,15)]

ref_sn_list = [i for i in range(42031,42046)]

with open(ref_data_file, "rb") as f:
  ref_data = f.read()

# Main loop
for bigi, bigsn in enumerate(big_sn_list):
  # print(big_sn_list[:1])
  tmp_data = copy.copy(ref_data)
  for lk, lsn in enumerate(ref_sn_list):
    tmp_data = tmp_data.replace(b"S/N %d" %lsn, b"S/N %d" %bigsn[lk])
    # print(lsn, bigi)
  with open("BottomSilkScreen_altium_cam_panel_%d.gbo" %bigi, "wb") as ff:
    ff.write(tmp_data)
