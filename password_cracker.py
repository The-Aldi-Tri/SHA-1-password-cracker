import hashlib

def crack_sha1_hash(hash, use_salts=False):
  passwords = []
  with open('top-10000-passwords.txt', 'r') as file1:
    lines = file1.readlines()
    for password in lines:
      passwords.append(password.strip())

  salts = []
  if use_salts:
    with open('known-salts.txt', 'r') as file2:
      lines = file2.readlines()
      for salt in lines:
        salts.append(salt.strip())

  hashPassDict = {}
  if use_salts:
    for salt in salts:
      for password in passwords:
        hashed_pass_prepend = hashlib.sha1(salt.encode() + password.encode()).hexdigest()
        hashPassDict[hashed_pass_prepend] = password
        hashed_pass_append = hashlib.sha1(password.encode() + salt.encode()).hexdigest()
        hashPassDict[hashed_pass_append] = password
  else:
    for password in passwords:
      hashed_pass = hashlib.sha1(password.encode()).hexdigest()
      hashPassDict[hashed_pass] = password
  
  if hash in hashPassDict:
    return hashPassDict[hash]
    
  return "PASSWORD NOT IN DATABASE"
