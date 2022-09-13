import argparse
import os
import shutil
import subprocess
import sys

SAVE_TOOL = 'Fire.Emblem.Save.Tool.exe'
SEARCH_STR = b'\xAD\x55\x0A\x19\x01'
SEARCH_STR_LEN = len(SEARCH_STR)
SPOTPASS_DATA = b'\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0A\x10\xDE\x34\x01\xFF\x0F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\xD0\x46\xA5\x01\xFF\xFF\x3F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0C\xFB\xFC\x41\x01\x3F\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x57\xC0\x60\x65\x01\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0A\x10\xDE\x34\x01\xFF\x0F'
SPOTPASS_DATA_LEN = len(SPOTPASS_DATA)

def find_insert_pos(contents):
  # Need to find the forth instance of the search string
  pos = contents.find(SEARCH_STR)
  pos = contents.find(SEARCH_STR, pos + SEARCH_STR_LEN)
  pos = contents.find(SEARCH_STR, pos + SEARCH_STR_LEN)
  pos = contents.find(SEARCH_STR, pos + SEARCH_STR_LEN)
  return pos + SEARCH_STR_LEN

def add_spotpass_data(filepath):
  print(f'Backing up {filepath} to {filepath}.bak')
  shutil.copy(filepath, f'{filepath}.bak')

  print(f'Decompressing {filepath}')
  decompress_process = subprocess.Popen(f'{SAVE_TOOL} {filepath}', stdout=subprocess.PIPE)
  decompress_process.wait()

  decompressed_path = f'{filepath}_dec'
  print(f'Modifying {decompressed_path}')
  with open(decompressed_path, 'rb') as decompressed_file:
    contents = decompressed_file.read()
    insert_pos = find_insert_pos(contents)
    new_contents = contents[:insert_pos] + SPOTPASS_DATA + contents[insert_pos + SPOTPASS_DATA_LEN:]

  print(f'Overwriting {decompressed_path}')
  with open(decompressed_path, 'wb') as save_file:
    save_file.write(new_contents)

  print(f'Recompressing {decompressed_path}')
  recompress_process = subprocess.Popen(f'{SAVE_TOOL} {decompressed_path}', stdout=subprocess.PIPE)
  recompress_process.wait()
  os.remove(decompressed_path)

  print(f'Save written to {filepath}')


def main():
  parser = argparse.ArgumentParser(description='Fire Emblem Awakening SpotPass Unlocker')
  parser.add_argument('save', type=str, help='Path to save file')
  args = parser.parse_args()

  # Check if PyInstaller executable to know where to check for SAVE_TOOL
  if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    working_dir = os.getcwd()
    executable_dir = os.path.split(sys.executable)[0]
    if working_dir != executable_dir:
      os.chdir(executable_dir)

  if not os.path.exists(SAVE_TOOL):
    print(f'Please ensure {SAVE_TOOL} is in this directory')
    sys.exit(1)

  if not os.path.exists(args.save):
    print(f'Couldn\'t find {args.save}')
    sys.exit(1)
  else:
    add_spotpass_data(args.save)

if __name__ == '__main__':
  main()
