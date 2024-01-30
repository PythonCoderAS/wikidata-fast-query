from collections import defaultdict

mylang = "wikidata"
family = "wikidata"
usernames: defaultdict[str, defaultdict[str, str]] = defaultdict(defaultdict)

usernames[family][mylang] = "RPI2026F1Bot"

simulate = True

password_file = "user-password.py"

put_throttle = 1

del defaultdict
