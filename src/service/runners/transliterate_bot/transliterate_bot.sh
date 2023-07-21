#!/bin/bash
# This script is aim to run transliterate bot. See https://github.com/kuza2010/transliterate-tg-bot
#
# Requirements:
#    1) env: TG_TOKEN
# The script should return PID of the started process

BOT_FOLDER=/home/kyza2010/Downloads/tg_bot/dist
MAIN_EXECUTABLE_FILE=main
export TG_TOKEN=6244212005:AAFsrfsWRXI_0IgzhlQILsNhErSmOaMrNrc

echo "
                            _ _                                        _
 _                         | (_)_                    _                | |          _
| |_   ____ ____ ____   ___| |_| |_  ____  ____ ____| |_  ____        | | _   ___ | |_
|  _) / ___) _  |  _ \ /___) | |  _)/ _  )/ ___) _  |  _)/ _  )       | || \ / _ \|  _)
| |__| |  ( ( | | | | |___ | | | |_( (/ /| |  ( ( | | |_( (/ / _______| |_) ) |_| | |__
 \___)_|   \_||_|_| |_(___/|_|_|\___)____)_|   \_||_|\___)____|_______)____/ \___/ \___)
"
echo -ne 'navigate to bot dir...'
cd $BOT_FOLDER

echo -ne 'working dir now: '
pwd

echo -ne "check if $MAIN_EXECUTABLE_FILE exists ---> "
if test -f "$MAIN_EXECUTABLE_FILE";
then
  echo 'YES'
else
  echo 'NO'
  exit 1
fi

echo 'start the bot...'
main &
echo 'MAIN_PID:'$!