# The Sims 4 Backup Tool

Et professionelt backup program til The Sims 4, der automatisk sikkerhedskopierer dine Mods, saves og Tray mapper.

![The Sims 4 Backup](https://img.shields.io/badge/Sims%204-Backup%20Tool-3caad6)
![Platform](https://img.shields.io/badge/platform-Windows-blue)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## ✨ Features

- 🎮 **Automatisk backup** af Mods, saves og Tray mapper
- 📁 **Valgbar placering** - Vælg selv hvor dine backups skal gemmes
- 💾 **Husker indstillinger** - Bruger Windows Registry til at gemme præferencer
- ⏰ **Tidsstempler** - Hver backup får automatisk dato og tid i navnet
- 🎨 **Moderne design** - Pænt interface med afrundede hjørner
- 🔗 **Direkte link** - Klik på ts4.topping.dk for mere info
- 🚀 **Ingen installation** - Kør direkte fra .exe filen

## 📥 Download

**[Download seneste version](https://github.com/DIT-BRUGERNAVN/Sims4-Backup/releases/latest)**

Download `Sims4Backup.exe` og dobbeltklik for at køre - det er så simpelt!

## 🚀 Sådan bruger du det

1. **Første gang:**
   - Dobbeltklik på `Sims4Backup.exe`
   - Klik på "Skift placering" og vælg hvor dine backups skal gemmes
   
2. **Hver gang du vil lave backup:**
   - Åbn programmet
   - Klik "Start Backup"
   - Vent mens filerne kopieres
   - Færdig! ✅

## 📋 Hvad bliver backup'et?

Programmet laver en komplet kopi af disse tre vigtige mapper fra The Sims 4:

- **📦 Mods** - Alle dine custom content og mods
- **💾 saves** - Alle dine gemte spil
- **👥 Tray** - Dine gemte Sims, huse og lots

Filerne kopieres fra:
```
C:\Users\[BRUGERNAVN]\Documents\Electronic Arts\The Sims 4\
```

## 🛠️ Byg selv fra kildekode

Hvis du vil bygge .exe filen selv:

### Krav:
- Python 3.8 eller nyere
- PyInstaller

### Trin:

1. **Klon repository:**
   ```bash
   git clone https://github.com/DIT-BRUGERNAVN/Sims4-Backup.git
   cd Sims4-Backup
   ```

2. **Installer PyInstaller:**
   ```bash
   pip install pyinstaller
   ```

3. **Byg .exe filen:**
   ```bash
   python -m PyInstaller --onefile --windowed --icon="ToppingSimsBackup.ico" --add-data "ToppingSimsBackup.ico;." --name="Sims4Backup" sims4_backup.py
   ```

4. **Find .exe filen:**
   ```
   dist\Sims4Backup.exe
   ```

Eller brug den medfølgende `lav_exe_med_ikon.bat` fil.

## 💡 Tips

- 🎮 **Luk The Sims 4** før du kører backup (ellers kan nogle filer være låste)
- 📅 **Lav backup regelmæssigt:**
  - Før du installerer nye mods
  - Før spil-opdateringer
  - Efter vigtige gameplay sessions
- 🗑️ **Slet gamle backups** når du vil spare plads (behold gerne de 2-3 nyeste)
- 🖥️ **Genvej på skrivebordet** - Flyt .exe filen til dit skrivebord for nem adgang

## 🔧 Tekniske detaljer

- **Sprog:** Python 3
- **GUI:** Tkinter
- **Indstillinger:** Windows Registry (`HKEY_CURRENT_USER\Software\ToppingSims4Backup`)
- **Platform:** Windows 10/11

## 📝 Changelog

### v1.0.0 (2025-02-15)
- 🎉 Første officielle release
- ✅ Automatisk backup af Mods, saves, Tray
- ✅ Valgbar backup placering
- ✅ Moderne UI med afrundede hjørner
- ✅ Windows Registry integration
- ✅ Link til ts4.topping.dk

## 🐛 Rapporter problemer

Fandt du en fejl eller har et forslag? [Opret et issue](https://github.com/DIT-BRUGERNAVN/Sims4-Backup/issues)

## 🤝 Bidrag

Pull requests er velkomne! Hvis du vil bidrage:

1. Fork projektet
2. Opret en feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit dine ændringer (`git commit -m 'Add some AmazingFeature'`)
4. Push til branchen (`git push origin feature/AmazingFeature`)
5. Åbn en Pull Request

## 📄 Licens

Dette projekt er licenseret under MIT License - se [LICENSE](LICENSE) filen for detaljer.

## 👤 Forfatter

**Topping**

- Website: [ts4.topping.dk](https://ts4.topping.dk)
- GitHub: [@DIT-BRUGERNAVN](https://github.com/DIT-BRUGERNAVN)

## ⭐ Support

Hvis du finder dette program nyttigt, giv det gerne en stjerne ⭐ på GitHub!

---

Lavet med ❤️ til The Sims 4 fællesskabet
