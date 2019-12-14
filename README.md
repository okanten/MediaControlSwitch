# MediaControl
Small and ugly script to alternate between spotify and vlc for my media keys.

## Usage
This script reads from player.txt to extract the player name used by dbus-send

Run with arguments:

```
    pause - pause current track
    next - next track
    prev - previous track

    spotify - change player.txt to spotify
    vlc - change player.txt to vlc
```

Running with no arguments will alternate between. If current player selected is spotify it will change to vlc and vice versa.

## How I use it with i3

My config looks like this:

```
# Media player controls - My pause button is broken, hence the use of XF86AudioStop over XF86AudioPause. Switch if you prefer pause button to pause.
bindsym XF86AudioStop exec python /path/to/scripts/MediaControl/mediacontrol.py pause
bindsym XF86AudioNext exec python /path/to/scripts/MediaControl/mediacontrol.py next
bindsym XF86AudioPrev exec python /path/to/scripts/MediaControl/mediacontrol.py prev

# Alternate between spotify and vlc
bindsym $mod+XF86AudioStop exec python /path/to/scripts/MediaControl/mediacontrol.py

```
