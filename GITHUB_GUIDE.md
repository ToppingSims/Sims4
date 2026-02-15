# Guide: Udgiv The Sims 4 Backup på GitHub

## Trin 1: Forbered filerne

### Filer der skal med:
- `sims4_backup_v2.py` (omdøb til `sims4_backup.py`)
- `ToppingSimsBackup.ico`
- `lav_exe_med_ikon.bat`
- `README.md` (se nedenfor)
- `LICENSE` (se nedenfor)

### Mapper struktur:
```
Sims4-Backup/
├── sims4_backup.py
├── ToppingSimsBackup.ico
├── lav_exe_med_ikon.bat
├── README.md
├── LICENSE
└── .gitignore
```

## Trin 2: Opret repository på GitHub

1. Gå til https://github.com
2. Log ind på din konto
3. Klik på **"+"** øverst til højre
4. Vælg **"New repository"**
5. Udfyld:
   - **Repository name**: `Sims4-Backup`
   - **Description**: `Et backup program til The Sims 4 - automatisk backup af Mods, saves og Tray`
   - Vælg **Public** (så andre kan se det)
   - ✅ Sæt flueben i **"Add a README file"**
   - **License**: Vælg "MIT License"
6. Klik **"Create repository"**

## Trin 3: Upload filer via GitHub website

### Metode 1: Drag & Drop (Nemmest)

1. På din nye repository side, klik **"Add file"** → **"Upload files"**
2. Træk alle dine filer ind i browseren
3. Scroll ned og skriv en commit besked: `Initial release`
4. Klik **"Commit changes"**

### Metode 2: Via Git (Avanceret)

Hvis du har Git installeret:

```bash
# Naviger til din mappe med filerne
cd C:\sti\til\din\mappe

# Initialiser git
git init

# Tilføj GitHub repository som remote
git remote add origin https://github.com/DIT-BRUGERNAVN/Sims4-Backup.git

# Tilføj alle filer
git add .

# Commit
git commit -m "Initial release"

# Push til GitHub
git branch -M main
git push -u origin main
```

## Trin 4: Opret en Release med .exe fil

1. Lav først .exe filen lokalt (kør `lav_exe_med_ikon.bat`)
2. Find `Sims4Backup.exe` i `dist` mappen
3. På GitHub repository, klik **"Releases"** (i højre side)
4. Klik **"Create a new release"**
5. Udfyld:
   - **Tag version**: `v1.0.0`
   - **Release title**: `Sims 4 Backup v1.0.0`
   - **Description**: 
     ```
     Første officielle release af The Sims 4 Backup programmet!
     
     ## Features
     - ✅ Automatisk backup af Mods, saves og Tray
     - ✅ Valgbar backup placering
     - ✅ Moderne design med afrundede hjørner
     - ✅ Link til ts4.topping.dk
     
     ## Download
     Download `Sims4Backup.exe` nedenfor og dobbeltklik for at køre.
     Ingen installation nødvendig!
     ```
   - **Attach binaries**: Træk `Sims4Backup.exe` hertil
6. Klik **"Publish release"**

## Trin 5: Opdater README.md

Erstat GitHub's auto-genererede README med en bedre version (se README.md filen jeg har lavet til dig).

1. Klik på `README.md` filen i dit repository
2. Klik på blyant ikonet (Edit)
3. Erstat indholdet med den nye README
4. Scroll ned og klik **"Commit changes"**

## Trin 6: Tilføj Topics (Tags)

For at gøre dit projekt nemmere at finde:

1. På hovedsiden af dit repository
2. Klik på tandhjulet ved "About" (øverst til højre)
3. Tilføj topics:
   - `sims4`
   - `the-sims-4`
   - `backup`
   - `backup-tool`
   - `windows`
   - `python`
   - `tkinter`
4. Klik **"Save changes"**

## Trin 7: Del dit projekt

Nu kan du dele linket:
```
https://github.com/DIT-BRUGERNAVN/Sims4-Backup
```

Folk kan:
- Downloade .exe filen fra Releases
- Se kildekoden
- Rapportere bugs via Issues
- Foreslå forbedringer via Pull Requests

## Vedligeholdelse

### Når du laver opdateringer:

1. Ret i filerne lokalt
2. Upload de nye filer til GitHub (erstat de gamle)
3. Lav en ny Release:
   - Tag: `v1.1.0`, `v1.2.0`, osv.
   - Upload den nye .exe fil
   - Beskriv hvad der er nyt

### Håndter Issues:

Når nogen rapporterer problemer:
1. Gå til **"Issues"** tabben
2. Læs problemet
3. Svar og hjælp
4. Luk issue når det er løst

## Tips

💡 **Add a .gitignore fil** for at undgå at uploade unødvendige filer:
```
*.pyc
__pycache__/
dist/
build/
*.spec
*.json
.vscode/
```

💡 **Shields/Badges** til README (valgfrit):
```markdown
![GitHub release](https://img.shields.io/github/v/release/DIT-BRUGERNAVN/Sims4-Backup)
![GitHub downloads](https://img.shields.io/github/downloads/DIT-BRUGERNAVN/Sims4-Backup/total)
```

💡 **License** - MIT License er perfekt for open source projekter som dette

## Hjælp

Hvis du sidder fast:
- GitHub's guide: https://docs.github.com/en/repositories
- Video tutorial: Søg på YouTube efter "how to upload to github"
- Eller spørg mig! 😊
