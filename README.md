# AMPED Banner Generator
A tool for automating the Banner creation process to help the fine folks over at [Hunt Premier](https://twitter.com/THEHUNTorg)

## Usage
Make sure you have [Python](https://www.python.org/) downloaded. Download the sourcecode and run the following command where the `Banner.py` script is located.
```
pip install Pillow
```

After then running the script, it asks for a path to a JSON file with all streamers that banners should get generated for. The file can have multiple different JSON objects sequentially, as long as they all include the following:
```json
{
  "name": "Streamer's 'actual' name",
  "link": "Streamer's username in their link",
  "platform": "Streamer's platform"
}
```
*Example*
```json
{
  "name": "Cozy",
  "link": "@cozybtw",
  "platform": "Youtube"
}
```
After providing the path, a new folder will be generated in `src` called `out` with all the overlays inside

## Natively supported platforms
- [Kick](https://kick.com)
- [Twitch](https://twitch.tv)
- [Youtube](https://youtube.com)

## Example output
![Example_Kick.png](src%2Fassets%2FExample_Kick.png)

![Example_Twitch.png](src%2Fassets%2FExample_Twitch.png)

![Example_Youtube.png](src%2Fassets%2FExample_Youtube.png)

## Adding platforms
Support for multiple different platforms can be manually added by appending a new JSON object to the data.json file in **src/assets** that includes the following:
```json
{
  "platform": "Platform name",
  "link": "Platforms link",
  "color": "A HEX color code for the desired color",
  "fileName": "NameOfTheLogo.png"
}
```
Afterward a square image of the new platform's logo can be added to the `src/assets/logos` folder that matches the `fileName` String and includes the file extension
