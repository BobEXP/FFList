<h1 align="center">
    <br>
    <img src="https://raw.githubusercontent.com/BobEXP/FFList/main/FFList.png" alt="FFList">
    <br>
    FFList
</h1>

<p align="center">
    A Fast Asynchronous System File Lister
</p>


## Features v1.0.0.4
- [x] Completely Asynchronous
- [x] Gather All System Files
- [x] Gather Files From Specified Directory
- [x] Cross Platform
- [x] Print Standard Output

## System Requirements

- [x] Windows / Linux / Mac
- [x] Python 3.10+ (Preferred Python 3.11 for performance)

## Usage

```bash
git clone --depth=1 https://github.com/BobEXP/FFList
```

```bash
cd FFList
```

```bash
python -m pip install requirements.txt
```

```bash
python fflist.py --help
```

### Examples Use

#### Gather All System Files

```bash
python fflist.py -full
```

#### Gather files from specific directory recursive

```bash
python fflist.py -dir "C:/Program Files/"
```

#### Gather files & Print output

```bash
python fflist.py -dir "C:/Program Files/" -print
```

## License

<a href="https://github.com/BobEXP/FFList/LICENSE" title="License">MIT License</a>

