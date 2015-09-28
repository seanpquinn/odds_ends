# Odds and ends

A collection of random files and commands preserved for reference and posterity. May or may not be helpful.

# BASH

When sharing files with Windows and Mac colleagues one frequently encounters files with an abundace of spaces in the name. Replace them with underscores in the local directory using

```bash
ls | grep " " | rename 's/ /_/g'
```
