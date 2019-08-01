scrot '%Y%m%d%H%M%S_snip.png' -z --select --quality 80 -e 'mv $f ~/Pictures/ && xclip -selection clipboard -target image/png -i ~/Pictures/$f'
