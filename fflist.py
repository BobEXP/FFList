from __future__ import print_function
from os import scandir, walk, system
from os.path import isfile, join, realpath, dirname
from argparse import ArgumentParser
from pathlib import Path
import asyncio

# saving all the gathered filepaths into list
total_files = []

curpath = dirname(realpath(__file__))

# convert names to path
async def convert_to_path(dirname: str):
	dirname.encode('unicode escape')
	p = Path(dirname)
	return p


# progress bar
async def pbar(progress, total) -> None:
	percent = 100 * (progress / float(total))
	bar = '+' * int(percent) + '-' * (100 - int(percent))
	print(f"\r|{bar}| {percent:.2f}%", end="\r")


# save the list into file
async def save_files() -> None:
	ffolder = curpath + "\\files.txt"
	filepath = await convert_to_path(ffolder)
	with open(filepath, 'w') as f:
		x = 0
		while x <= len(total_files)-1:
			f.write(f"{total_files[x]}\n")
			x += 1


# get the files from folder
async def get_files(dirname: str) -> []:
	files = []
	f_obj = scandir(path=dirname)
	for entry in f_obj:
		if entry.is_file() and entry.name != None:
			ffolder = f"{dirname}\\{entry.name}"
			fpath = await convert_to_path(ffolder)
			files.append(fpath)
	return files


# total appender
async def total_appender(dirname: str) -> None:
	total_lists = []
	total_lists.append(await get_files(dirname))
	for lst in total_lists:
		for file in lst:
			total_files.append(file)


# init
async def init(init_dir: str, isDeep: bool) -> None:
	system('cls')
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
		dirname = await convert_to_path(dirs_raw[n])
		await total_appender(dirname)
		n += 1
		await pbar(n, len(dirs_raw))
	print(f"Saving file list...")
	await save_files()
	system('cls')
	for file in total_files:
		print(file)


# read config file
async def main() -> None:
	system('cls')
	parser = ArgumentParser(description="FFlist Argument Parser", add_help=True)
	folder_group = parser.add_mutually_exclusive_group()
	folder_group.add_argument('-dir','--directory', type=str, help="User Defined Folder")
	folder_group.add_argument('-full','--full', type=str, help="All System Files")
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


if __name__ == "__main__":
	asyncio.run(main())
