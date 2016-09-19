read -p "Choose your admin password? " passwd
sudo pip install virtualenv
virtualenv --no-site-packages env
source env/bin/activate
pip install web2py
pip install psycopg2
pip install gunicorn
pip freeze > requirements.txt
echo "web: python web2py.py -a '$passwd' -i 0.0.0.0 -p \$PORT" > Procfile
git init
git add .
git commit -am "initial"
heroku create
git push heroku master
heroku addons:add heroku-postgresql:dev
heroku ps:scale web=1
heroku open
