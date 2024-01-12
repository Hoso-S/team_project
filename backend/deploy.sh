#!/bin/bash


echo "Do something"

cd ~/team_project/backend
source venv/bin/activate
./gunidaemonctl start guni_conf_prod
./gunidaemonctl ps guni_conf_prod

# sudo systemctl disable gunicorn.service
# sudo rm /etc/systemd/system/gunicorn.service
# sudo ln -s $HOME/team_project/backend/gunicorn.service /etc/systemd/system/gunicorn.service

# sudo systemctl daemon-reload
# sudo systemctl start gunicorn.service
# sudo systemctl enable gunicorn.service
# sudo systemctl status gunicorn.service
