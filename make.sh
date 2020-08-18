docker build -t smartphone_legio_adjutor .

docker run -p 8050:8050 -v $(pwd)/data:/app/data smartphone_legio_adjutor