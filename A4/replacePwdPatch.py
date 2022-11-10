from Crypto.Hash import SHA1
from os.path import exists

# Place this script in the same folder as the exe file.
# Make sure this script has permission to read the exe (No firewall / access denied)
ORIGINAL_HASH = "d5ea68d77172b3ee9e858b759ff9190b3304ea2f" # Original hash of Group4.program2.exe
ORIGINAL_PATH = "Group4.program2.exe"

PATCHED_PATH = "Group4.program2patch.exe"
NEW_PASSWORD = "PleaseGiveUsFullMarks" # Change this variable to be whatever new password that you want

def replace_pwd():
    assert exists(ORIGINAL_PATH), "Place this script in the same folder as the original exe"

    h = SHA1.new()
    h.update(NEW_PASSWORD.encode())
    new_hash = h.hexdigest()

    print(f"new password: {NEW_PASSWORD}")
    print(f"hash of new password: {h.hexdigest()}")

    # https://stackoverflow.com/questions/6624453/whats-the-correct-way-to-convert-bytes-to-a-hex-string-in-python-3
    f = open(ORIGINAL_PATH, "rb")
    exe = f.read().hex()
    f.close()

    assert len(exe) != 0, "Script does not have permission to read exe file"

    exe = exe.replace(ORIGINAL_HASH, new_hash)
    exe = bytes.fromhex(exe)

    with open(PATCHED_PATH, "wb") as new_patch:
        new_patch.write(exe)

    print(f"created program with new password: {PATCHED_PATH}")

if __name__ == "__main__":
    replace_pwd()
