#!/bin/bash
# This script is aim to run transliterate bot. See https://github.com/kuza2010/transliterate-tg-bot
#
# Requirements:
#    1) argv: TG_TOKEN - telegram token
#    2) argv: BOT_FOLDER - absolute path to MAIN_EXECUTABLE_FILE
#    3) argv: MAIN_EXECUTABLE_FILE - main executable file

# The script should return PID number of the started process

export TG_TOKEN=$1
BOT_FOLDER=$2
MAIN_EXECUTABLE_FILE=$3

echo "
                                  S T A R T I N G
                            _ _                                        _
 _                         | (_)_                    _                | |          _
| |_   ____ ____ ____   ___| |_| |_  ____  ____ ____| |_  ____        | | _   ___ | |_
|  _) / ___) _  |  _ \ /___) | |  _)/ _  )/ ___) _  |  _)/ _  )       | || \ / _ \|  _)
| |__| |  ( ( | | | | |___ | | | |_( (/ /| |  ( ( | | |_( (/ / _______| |_) ) |_| | |__
 \___)_|   \_||_|_| |_(___/|_|_|\___)____)_|   \_||_|\___)____|_______)____/ \___/ \___)
"
echo -ne 'navigate to bot dir: '
cd $BOT_FOLDER
pwd

echo 'start the bot...'
$MAIN_EXECUTABLE_FILE &
sleep 5
echo 'MAIN_PID:'$!