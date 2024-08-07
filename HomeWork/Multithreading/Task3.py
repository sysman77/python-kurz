import os
import shutil
import threading

# Globální proměnné pro statistiky
total_files = 0
total_size = 0


# Funkce pro kopírování souborů s uchováním struktury adresářů
def copy_directory_structure(src, dest):
    global total_files, total_size

    # Procházíme všechny adresáře a soubory ve zdrojovém adresáři
    for dirpath, dirnames, filenames in os.walk(src):
        # Vytvoříme odpovídající adresář ve výstupním adresáři
        relative_path = os.path.relpath(dirpath, src)
        dest_dir = os.path.join(dest, relative_path)
        os.makedirs(dest_dir, exist_ok=True)

        # Kopírujeme všechny soubory do odpovídajícího adresáře
        for file in filenames:
            src_file = os.path.join(dirpath, file)
            dest_file = os.path.join(dest_dir, file)
            shutil.copy2(src_file, dest_file)

            # Aktualizace statistik
            total_files += 1
            total_size += os.path.getsize(src_file)

    print(f"Operace kopírování dokončena. Celkem zkopírováno souborů: {total_files}, O celkové velikosti: {total_size / 1024:.2f} KB")


# Získání cesty od uživatele
src_dir = input("Zadej cestu ke zdrojovému adresáři: ")
dest_dir = input("Zadej cestu ke cílovému adresáři: ")

# Kontrola existence zadaných adresářů
if not os.path.exists(src_dir):
    print(f"Zdrojový adresář '{src_dir}' neexistuje.")
else:
    # Spuštění kopírovacího vlákna
    copy_thread = threading.Thread(target=copy_directory_structure, args=(src_dir, dest_dir))
    copy_thread.start()
    copy_thread.join()  # Počkáme na dokončení kopírování
