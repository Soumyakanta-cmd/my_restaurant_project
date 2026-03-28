# 🍽️ My Restaurant Booking System (Django)

A web-based restaurant booking system built with Django where users can book places and admin can manage and approve bookings.

---

## 🚀 Features


- Book restaurant/place
- Admin approval system
- Booking status (Pending / Confirmed / Cancelled)
- Admin dashboard
- Responsive UI

---

## 🛠️ Tech Stack

- Backend: Django
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite (default)

---

## 📂 Project Structure


my_restaurant/
│── manage.py
│── db.sqlite3
│── my_restaurant/ # main project
│── base_app/ # my app
│── templates/
│── static/
│── media/


---

## ⚙️ Setup Instructions

 1️⃣ Clone the repository:
```bash
git clone https://github.com/Soumyakanta-cmd/my-restaurant-project.git
cd my-restaurant-project

2️⃣ Create virtual environment:python -m venv venv
Windows:venv\Scripts\activate
Mac/Linux:source venv/bin/activate
3️⃣ Install dependencies:pip install -r requirements.txt
4️⃣ Apply migrations:python manage.py migrate
5️⃣ Create superuser:python manage.py createsuperuser
6️⃣ Run server:python manage.py runserver
  👉 Open in browser:http://127.0.0.1:8000/
  🔐 Admin Panel:http://127.0.0.1:8000/admin/

📌 Future Improvements
Payment integration
REST API
Deployment
## 📸 Screenshots

### 🏠 Home Page
![Home](https://raw.githubusercontent.com/Soumyakanta-cmd/my_restaurant_project/main/screenshot/home.png)

###  📅 Book Table
![Book table](https://raw.githubusercontent.com/Soumyakanta-cmd/my_restaurant_project/main/screenshot/bookingview.png)

### 📅 Booking Page
![Booking](https://raw.githubusercontent.com/Soumyakanta-cmd/my_restaurant_project/main/screenshot/booktable.png)

### ⚙️ Admin Dashboard
![Admin]([screenshot/admindashboard.png](https://raw.githubusercontent.com/Soumyakanta-cmd/my_restaurant_project/main/screenshot/admindashboard.png))
