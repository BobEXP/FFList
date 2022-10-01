<h1 align="center">
    <br>
    <img src="https://raw.githubusercontent.com/BobEXP/FFList/main/FFList.png" alt="FFList">
    <br>
    FFList
</h1>

<p align="center">
    A Fast System File Lister written in Python
</p>


## Features v1.0.0.1
- [x] Completely Asynchronous
- [x] Gather All System Files
- [x] Gather Files From Specified Directory
- [x] Recursive File Collection

## System Requirements

- [x] Windows 7 / 10 / 11
- [x] Python 3.11

## Usage

```python
git clone --depth=1 https://github.com/BobEXP/FFList
```

```python
cd FFList
```

```python
python -m pip install requirements.txt
```

```python
python fflist.py --help
```

### Examples Use

#### Gather All System Files

```python
python fflist.py -f "*" -full
```

#### Gather files from specific directory recursive

```python
python fflist.py -f "C:/Program Files/"
```

## License

<a href="https://github.com/BobEXP/FFList/LICENSE" title="License">MIT License</a>

