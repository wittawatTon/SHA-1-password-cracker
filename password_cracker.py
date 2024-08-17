import hashlib

def crack_sha1_hash(hash, use_salts = False):
    # Load the passwords
    with open('top-10000-passwords.txt', 'r') as f:
        passwords = f.read().splitlines()

    # Load the salts if use_salts is True
    salts = []
    if use_salts:
        with open('known-salts.txt', 'r') as f:
            salts = f.read().splitlines()


    def sha1_hash(text):
        return hashlib.sha1(text.encode()).hexdigest()

    # Check each password
    for password in passwords:
        # Check without salts
        if sha1_hash(password) == hash:
            return password

        # Check with salts if enabled
        if use_salts:
            for salt in salts:
                if sha1_hash(salt + password) == hash or sha1_hash(password + salt) == hash:
                    return password

    return "PASSWORD NOT IN DATABASE"
