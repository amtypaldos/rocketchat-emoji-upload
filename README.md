# rocketchat-emoji-upload
> CLI to bulk upload emojis to Rocketchat

## Install

All required pip packages are in the requirements.txt file, install like so:

```bash
pip install -r requirements.txt
```


## Usage

In order to work you will need access to your rockechat mongo instance

```bash
$ python emoji-upload.py
URL for YAML file?https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/futurama.yaml
MongoDB URI for your rocketchat deployment?mongo://<mongoserver>
```


Note that the emoji pack to upload  must be a **URL**, like [http://www.emojipacks.com/packs/food.yaml](http://www.emojipacks.com/packs/food.yaml).

## Emoji Yaml File

Also note that the yaml file must be indented properly and formatted as such:

```yaml
title: food
emojis:
  - name: apple
    src: http://i.imgur.com/Rw0Vlda.png
  - name: applepie
    src: http://i.imgur.com/g4RU1fM.png
```

..with the `src` pointing to an image file.


## Emoji packs

- [animals](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/animals.yaml)
- [clippy](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/clippy.yaml)
- [fika](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/fika.yaml)
- [frontend](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/frontend.yaml)
- [harrypotter](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/harrypotterhouses.yaml)
- [mario](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/mario-8bit.yaml)
- [occupy](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/occupy.yaml)
- [officespace](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/officespace.yaml)
- [omnom](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/omnom.yaml)
- [futurama](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/futurama.yaml)
- [food](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/food.yaml)
- [skype](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/skype.yaml)
- [starwars](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/starwars.yaml)
- [startups](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/startups.yaml)
- [businessfish](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/businessfish.yaml)
- [hipchat](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/hipchat.yaml)
- [twitch](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/twitch.yaml)
- [parrotparty](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/parrotparty.yaml) ([Parrot](http://cultofthepartyparrot.com/) [Paint](http://cultofthepartyparrot.com/paint/))
- [Finland](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/finland.yaml)
- [pokemongo: items](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/pokemongo.yaml)
- [Pokémon Go: Pokémon](https://raw.githubusercontent.com/Templarian/slack-emoji-pokemon/master/pokemon.yaml) ([Prefixed `pokemon-*`](https://raw.githubusercontent.com/Templarian/slack-emoji-pokemon/master/pokemon-prefix.yaml))
- [politipack](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/politipack.yaml)
- [nekoatsume](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/nekoatsume.yaml)
- [octicons](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/octicons.yaml)
- [pokemon](https://raw.githubusercontent.com/jaylynch/pokemoji/master/pokemon-by-name.yaml)
- [devicon](https://raw.githubusercontent.com/izumin5210/emojipack-for-devicon/master/png/devicon.yaml) ([Devicon](http://devicon.fr/))
- [hamsterdance](https://raw.githubusercontent.com/snipe/hamsterdance-emojipack/master/hamsterdance.yaml) ([snipe/emojipacks](https://github.com/snipe/hamsterdance-emojipack))
- [avengers](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/avengers.yaml)
- [Shiba Stickers](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/shiba.yaml) (from Messenger)
- [gamedevmoji](https://raw.githubusercontent.com/niksudan/gamedevmoji/master/gamedevicons.yaml)
- [AWS simple icons](https://raw.githubusercontent.com/Surgo/aws_emojipacks/master/noprefix-emojipacks.yml)

### Emoji packs from [slackmojis.com](http://www.slackmojis.com)

- [Uncategorized](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-uncategorized.yaml)
- [Facebook Reaction](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-facebook-reaction.yaml)
- [Logo](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-logo.yaml)
- [Meme](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-meme.yaml)
- [MLB](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-mlb.yaml)
- [NBA](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-nba.yaml)
- [NFL](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-nfl.yaml)
- [NHL](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-nhl.yaml)
- [NYC Subway](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-nyc-subway.yaml)
- [Party Parrot](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-party-parrot.yaml)
- [Pokemon](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-pokemon.yaml)
- [Retro Game](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-retro-game.yaml)
- [Scrabble Letters](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-scrabble-letters.yaml)
- [Skype](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-skype.yaml)
- [Star Wars](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-star-wars.yaml)
- [Turntable.fm](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-turntable.fm.yaml)
- [Yoyo](https://raw.githubusercontent.com/lambtron/emojipacks/master/packs/slackmojis-yoyo.yaml)

## Credits

This is based on [lambtron's emojipacks](https://github.com/lambtron/emojipacks/issues/new)
