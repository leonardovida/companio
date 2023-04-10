source vars.sh

ssh-add $SSH_KEY_PATH

# companio-backend
rsync -av ../companio-backend $USER@$HOST: --exclude=venv
cp ../companio-backend/.env.example .env.companio-backend
sed -i '' "s/DATABASE_URL=.*/DATABASE_URL=postgresql:\/\/$DB_USER:$DB_PASSWORD@localhost\/$DB_NAME/g" .env.companio-backend
scp .env.companio-backend $USER@$HOST:~/companio-backend/.env
ssh $USER@$HOST "
    cd companio-backend
    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt
    alembic upgrade head
    pm2 delete companio-backend
    pm2 start 'gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app' --name companio-backend
"

# companio-frontend
rsync -av ../companio-frontend $USER@$HOST: --exclude=node_modules --exclude=.next
cp ../companio-frontend/.env.development .env.companio-frontend
sed -i '' "s/NEXT_PUBLIC_API_URL=.*/NEXT_PUBLIC_API_URL=http:\/\/$HOST\/api/g" .env.companio-frontend
scp .env.companio-frontend $USER@$HOST:~/companio-frontend/.env.local
ssh $USER@$HOST "
    cd companio-frontend
    npm install
    npm run build
    pm2 delete companio-frontend
    pm2 start 'npm start' --name companio-frontend
"

# nginx
cp default.template.conf default.conf
sed -i '' "s/{HOST}/$HOST/g" default.conf
sed -i '' "s/{DOMAIN}/$DOMAIN/g" default.conf
scp default.conf $USER@$HOST:
ssh $USER@$HOST "
    sudo cp default.conf /etc/nginx/conf.d
    sudo service nginx restart
"