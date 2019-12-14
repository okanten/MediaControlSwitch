import subprocess, sys

p_txt = '{}/player.txt'.format(sys.path[0])

#player_array = ['spotify', 'vlc']

player = ''
with open(p_txt) as f:
    player = f.read().rstrip()

command_play_pause = 'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.{} /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause'.format(player).split(' ')
command_next = 'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.{} /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next'.format(player).split(' ')
command_prev = 'dbus-send --print-reply --dest=org.mpris.MediaPlayer2.{} /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous'.format(player).split(' ')

control_dict = {
    "pause": command_play_pause,
    "next": command_next,
    "prev": command_prev,
}
try:

    if sys.argv[1] in control_dict:
        s = subprocess.Popen(control_dict[sys.argv[1]], stdout=subprocess.PIPE)
    else:
        with open(p_txt, 'w') as f:
            f.write(sys.argv[1])

except IndexError:
    if player == 'spotify':
        player = 'vlc'
    else:
        player = 'spotify'

    with open(p_txt, 'w') as f:
        f.write(player)
