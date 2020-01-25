# zipdir

Convenience utility for recursively zipping up a directory (or "folder").


## Features

- Can filter some revision control files out of resulting zipfile.
- Can use `.gitignore` file for filtering.
- Can zip up a git workspace including the `.git` folder.
- Can make a fresh zipfile or reuse an existing one.
- Can pass options to **zip**.
- Dry run.


## Requirements

- A [Python](https://www.python.org/) interpreter, version 3.6 or later
- The Python packages listed in [requirements.txt][]
- [zip][] installed somewhere on your path


## Installing

1. Create and activate your Python virtual environment.
2.  Install requirements via `pip`:

        pip install -r requirements.txt

3.  Install **zipdir** via `setup.py`:

        python setup.py install


## References

- [zip][]
- [gitignore-parser][]


 [gitignore-parser]: https://github.com/mherrmann/gitignore_parser
 [python]: https://www.python.org/
 [requirements.txt]: requirements.txt
 [zip]: https://infozip.sourceforge.io/Zip.html
