from __future__ import print_function
from os import listdir, walk, system
from os.path import isfile, join, realpath, dirname
from argparse import ArgumentParser
import asyncio

# saving all the gathered filepaths into list
total_files = []

curpath = dirname(realpath(__file__))

# progress bar
def pbar(progress, total) -> None:
	percent = 100 * (progress / float(total))
	bar = '+' * int(percent) + '-' * (100 - int(percent))
	print(f"\r|{bar}| {percent:.2f}%", end="\r")


# save the list into file
async def save_files() -> None:
	filepath = curpath + "/files.txt"
	with open(filepath, 'w') as f:
		x = 0
		while x <= len(total_files)-1:
			f.write(f"{total_files[x]}\n")
			x += 1


# get the files from folder
def get_files(dir: str) -> []:
	tempfiles = [f for f in listdir(dir) if isfile(join(dir, f))]
	temptotal = dir + "/".join([temp_file for temp_file in tempfiles])[1:]
	return temptotal


# replace with slash
async def replace_slash(rwith: str) -> str:
	replaced = rwith.replace("\\", "/")
	return replaced


# append total files
async def total_appender(dirname: str) -> None:
	total_files.append(get_files(dirname))


# init
async def init(init_dir: str, isDeep: bool) -> None:
	system('cls')
	print(f"Gathering FileSystem Directories from {init_dir}..")
	dirs_raw = []
	match isDeep:
		case True:
			filenum = 0
			for x in walk(init_dir):
				dirs_raw.append(x[0])
				filenum	+= 1
				if filenum % 100 == 0:
					print(f"Folders Gathered: {filenum}")
		case False:
			dirs_raw = [x[0] for x in walk(init_dir)]
	
	print(f"Gathering files in {len(dirs_raw)} directories..")
	pbar(0, len(dirs_raw))
	n = 0
	while n <= len(dirs_raw)-1:
		await replace_slash(dirs_raw[n])
		await total_appender(dirs_raw[n])
		n += 1
		pbar(n, len(dirs_raw))
	print(f"Saving file list...")
	await save_files()


# read config file
async def main() -> None:
	parser = ArgumentParser(description="FFlist Argument Parser", add_help=True)
	parser.add_argument('-f','--folder', type=str, help="Use '*' for --full & 'FOLDER_PATH' for --folder")
	parser.add_argument('-full','--full', action='store_true', help="All System Files")
	args = parser.parse_args()

	if args.full:
		asyncio.gather(init("C:/", True))
	
	if args.folder != "*":
		if args.folder != None:
			folder = await replace_slash(args.folder)
			asyncio.gather(init(folder, False))
		else:
			print("Please read --help")


if __name__ == "__main__":
	asyncio.run(main())
