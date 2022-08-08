import config
import subprocess
import multiprocessing
def run_themis():
    subprocess.run([config.THEMIS_PATH])

for i in range(5):
    process = multiprocessing.Process(target=run_themis)
    process.start()
