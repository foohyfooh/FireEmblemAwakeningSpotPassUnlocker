# Fire Emblem Awakening SpotPass Unlocker

Script to automate the process of adding SpotPass data to Fire Emblem Awakening documented by [u/heritorofrain](https://www.reddit.com/user/heritorofrain/) on [their Reddit post](https://www.reddit.com/r/fireemblem/comments/u8eyah/spotpass_access_for_awakening_on_citra/).

## Requirements
- [Python](https://www.python.org/) 3.6 or higher
  - [PyInstaller](https://pyinstaller.org/en/stable/): `pip install pyinstaller`
<!-- [SciresM](https://github.com/SciresM)'s [FEAST](https://github.com/SciresM/FEAST) -->
- [RainThunder](https://github.com/RainThunder)'s fork of FEAST: [FEST](https://github.com/RainThunder/FEST)

## Building
```
pyinstaller --onefile --icon=icon.ico --name=FireEmblemAwakeningSpotpassUnlocker main.py
```

## Steps
1. Clone or download this repo for the script OR download *FireEmblemAwakeningSpotpassUnlocker.exe* from the [latest binary release](https://github.com/foohyfooh/FireEmblemAwakeningSpotPassUnlocker/releases/latest).
2. Download the *Fire.Emblem.Save.Tool.exe* file the latest release on [FEST's releases page](https://github.com/RainThunder/FEST/releases) and place it in the folder with this program.
3. Copy the Awakening save file to this folder i.e. Chapter0, Chapter1, or Chapter2.
4. Either
    - run the script using the command `python main.py <Chapter file>` e.g. `python main.py Chapter0` for the first save
    - drag the save file into FireEmblemAwakeningSpotpassUnlocker.exe
5. Copy modified save file back to the game and test.


## Thanks
- [u/heritorofrain](https://www.reddit.com/user/heritorofrain/) for finding the SpotPass data.
- [RainThunder](https://github.com/RainThunder) for the FEST tool.
- [Supreme Ricardo](https://www.steamgriddb.com/profile/76561198428145598) for the icon.
