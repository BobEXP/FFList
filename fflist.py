from __future__ import print_function
from os import scandir, walk, system
from argparse import ArgumentParser
from pathlib import Path
import asyncio

# saving all the gathered filepaths into list
total_files = []

global arg_pout

# clear screen
def sclear() -> None:
	import platform
	plt = platform.system()
	match plt:
		case "Windows":
			system('cls')
		case "Linux":
			system('clear')
		case "Darwin":
			system('clear')

# convert names to path
async def convert_to_path(dirpath: str):
	dirpath.encode('unicode escape')
	p = Path(dirpath)
	return p


# progress bar
async def pbar(progress, total) -> None:
	percent = 100 * (progress / float(total))
	bar = '+' * int(percent) + '-' * (100 - int(percent))
	print(f"\r|{bar}| {percent:.2f}%", end="\r")


# save the list into file
async def save_files() -> None:
	ffolder = str(Path.cwd()) + "/files.txt"
	filepath = await convert_to_path(ffolder)
	with open(filepath, 'w') as f:
		x = 0
		while x <= len(total_files)-1:
			try:
				f.write(f"{total_files[x]}\n")
			except Exception as e:
				pass
			x += 1


# get the files from folder
async def get_files(dirpath: str) -> []:
	files = []
	f_obj = scandir(path=dirpath)
	for entry in f_obj:
		if entry.is_file() and entry.name != None:
			ffolder = f"{dirpath}\\{entry.name}"
			fpath = await convert_to_path(ffolder)
			files.append(fpath)
	return files


# total appender
async def total_appender(dirpath: str) -> None:
	total_lists = []
	total_lists.append(await get_files(dirpath))
	for lst in total_lists:
		for file in lst:
			total_files.append(file)


# init
async def init(init_dir: str, isDeep: bool) -> None:
	sclear()
	init_dir = await convert_to_path(init_dir)
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
	await pbar(0, len(dirs_raw))
	n = 0
	while n <= len(dirs_raw)-1:
		dirpath = await convert_to_path(dirs_raw[n])
		await total_appender(dirpath)
		n += 1
		await pbar(n, len(dirs_raw))
	print(f"Saving file list...")
	await save_files()
	if arg_pout:
		sclear()
		for file in total_files:
			print(file)


# read config file
async def main() -> None:
	global arg_pout
	
	sclear()
	parser = ArgumentParser(description="FFlist Argument Parser", add_help=True)
	folder_group = parser.add_mutually_exclusive_group()
	folder_group.add_argument('-dir','--directory', type=str, help="User Defined Folder")
	folder_group.add_argument('-full','--full', action="store_true", help="All System Files")
	parser.add_argument('-print','--print', action="store_true", help="Print Output")
	args = parser.parse_args()

	if args.directory:
		if args.directory != None:
			try:
				asyncio.gather(init(args.directory, False))
			except Exception as e:
				raise e
	if args.full:
		try:
			asyncio.gather(init("C:/", True))
		except Exception as e:
			raise e
	if args.print:
		arg_pout = True
	else:
		arg_pout = False


if __name__ == "__main__":
	asyncio.run(main())
