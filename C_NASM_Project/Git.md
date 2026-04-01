cd 
git init
git remote add origin <repository_url>
git add .
git commit -m "Initial commit"
git push -u origin main
git pull origin master --allow-unrelated-histories
git push origin main
