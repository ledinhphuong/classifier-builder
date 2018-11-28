import glob
import os
import subprocess
import sys
import datetime


if __name__ == "__main__":
  start_date = datetime.datetime.now()
  print(">>> Start at {}\n".format(start_date))

  model_dir = "./testai_model"
  for file in glob.glob(os.path.join(model_dir, '*.pb')):
    file_name = os.path.basename(file)
    model_name = os.path.splitext(file_name)[0]

    print('\n* Model name: ' + model_name)
    graph_file = os.path.join(model_dir, '{}.pb'.format(model_name))
    label_file = os.path.join(model_dir, '{}.pbtxt'.format(model_name))

    p = subprocess.Popen([sys.executable, "run_model.py", "--graph", graph_file, "--label", label_file, "--image", "./cart.png"])
    p.wait()

  end_date = datetime.datetime.now()
  print("\n>>> End at {}".format(end_date))

  diff = end_date - start_date
  print("Duration: {}".format(diff))
