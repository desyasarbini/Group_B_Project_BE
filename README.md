# Introduction

Website LSTR! (Lestari) adalah final Project yang dirancang untuk memenuhi _final assignment_ dari **RevoU** dengan topic **_Climate Change_**.

Project ini menggunakan **SQL** dan **Supabase** sebagai database, bberikut adalah dokumentasi API yang didapatkan dari database tersebut:

1. [LSTR! Website](https://www.luv2read.site)
2. [API Project](https://groupbprojectbe-production.up.railway.app/project)
3. [Postman Documentation](https://documenter.getpostman.com/view/32144902/2sA3BrWpfa)

| Methods | Endpoint                                                                             |
| ------- | ------------------------------------------------------------------------------------ |
| GET     | `/admin`, `/admin/[admin_id]`, `/admin/logout`, `/project`, `/project/[project_id]`, |
| POST    | `/admin`, `/admin/login`, `/project/create`, `/donation/create`                      |
| PUT     | `/project/update/[project_id]`                                                       |
| DELETE  | `/admin/[admin_id]`, `/project/delete/[project_id]`                                  |

## Block Diagram Database

berikut adalah gambaran bagaimana database dalam project ini bekerja.
![block diagram](./assets/databaseBlockDiagram.png)

### In Project

- Python ver 3.10
- Poetry sebagai library `pip install poetry`
- Flask sebagai framework `poetry install flask`
- FLask_jwt_extended : extension protected route
- bcyript : encrypt password
- pydantic : validation data
- install requirements depedencies `poetry add $(cat requirements.txt)`

### Build Docker Image

1. install gunicorn `poetry add gunicorn`
2. install docker `poetry add docker`
3. create docker file dan .dockerignore, sesuaikan dengan project yang akan kalian buat
4. `sudo docker run hello-world` untuk mengechek apakah docker sudah terinstall
5. `docker build -t namaimage`, maka akan ada proses build image.
6. jika terjadi error seperti **permission denied** coba cara ini:
   - `sudo systemctl restart docker`
   - `sudo chmod666/var/run/docker.sock`
7. `docker run -p 5000:5000 --env-file .env namaimagedocker`

### Railway Deploy

1. login ke railway, saya menggunakan github untuk login sehingga jika ada deployment akan terintegrasi dengan railway
2. pilih repository yang ingin di upload
3. pilih variable, dan setting menggunakan data yang ada pada .env kalian
4. setting FLASK_DEBUG `true` ubah ke `false`
5. setting FLASK_ENV `Development` ke `Production`
6. setting PORT mengikuti dengan localhost yang disetting ke app

### Structure

Connector
: -- SQL_connector

Controller
: -- admin
: -- donation
: -- project

Models
: -- base
: -- admin
: -- donation
: -- project

Routes
: -- admin
: -- donation
: -- project
