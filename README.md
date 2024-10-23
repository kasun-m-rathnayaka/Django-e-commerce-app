# 🛒 E-Commerce Django Application

An e-commerce web application built with **Django** that features a fully functional website header with a logo, navigation menu, and cart button. The goal of this project is to build a scalable and customizable platform for online shopping.

## 🌟 Features
- Responsive **Header** with:
  - Logo Icon
  - Navigation Menu (Home, About, Services, Contact)
  - Cart Button with **Badge Count**
- User Authentication (Signup, Login, Logout)
- Product Management System (CRUD Operations)
- Integrated Cart & Checkout functionality

---

## 🛠️ Tech Stack

- **Backend**: Django 4.x
- **Frontend**: HTML, CSS and Bootstrap
- **Database**: SQLite
- **Icons**: FontAwesome
- **Version Control**: Git

---

## 🚀 How to Run the Project

1. Clone the Repository
```bash
git clone https://github.com/your-username/your-django-project.git
cd your-django-project
```
2. Create and Activate a Virtual Environment
```bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install Dependencies
```bash
Copy code
pip install -r requirements.txt
```
5. Apply Migrations
```bash
Copy code
python manage.py migrate
```
6. Run the Development Server
```bash
Copy code
python manage.py runserver
Open your browser and go to: http://127.0.0.1:8000/
```

📁 Project Structure
```bash
your-django-project/
│
├── manage.py               # Django project management file
├── your_app/               # Main Django application folder
│   ├── migrations/         # Database migration files
│   ├── templates/          # HTML templates folder
│   ├── static/             # CSS, JS, and image assets
│   ├── views.py            # View functions
│   └── models.py           # Django models
│
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .gitignore              # Files to ignore in version control
```

📦 Dependencies
Make sure you have the following installed:

Python 3.8+
Django 4.x
Install all dependencies via:
```bash
pip install -r requirements.txt
```

🛠️ Header Code
HTML (Header Component)
```bash
<header class="header">
  <div class="logo">
    <img src="https://via.placeholder.com/40" alt="Logo Icon">
    <h1>MySite</h1>
  </div>
  
  <nav class="nav-menu">
    <ul>
      <li><a href="#">Home</a></li>
      <li><a href="#">About</a></li>
      <li><a href="#">Services</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
  </nav>

  <div class="header-icons">
    <a href="#" class="cart-btn">
      <i class="fas fa-shopping-cart"></i>
      <span class="cart-count">2</span>
    </a>
  </div>
</header>
```

CSS (styles.css)
```bash
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  background-color: #333;
  color: #fff;
}

.logo {
  display: flex;
  align-items: center;
  gap: 10px;
}

.nav-menu ul {
  display: flex;
  list-style: none;
  gap: 20px;
}

.nav-menu a {
  text-decoration: none;
  color: #fff;
  transition: color 0.3s;
}

.nav-menu a:hover {
  color: #f0c14b;
}

.header-icons .cart-btn {
  position: relative;
  color: #fff;
}

.cart-count {
  position: absolute;
  top: -5px;
  right: -10px;
  background-color: red;
  border-radius: 50%;
  padding: 2px 6px;
  font-size: 0.8rem;
}
```

🤝 Contributing
We welcome contributions! Follow these steps to contribute:

Fork the repository
Create a new branch: git checkout -b feature/your-feature
Commit your changes: git commit -m 'Add some feature'
Push to the branch: git push origin feature/your-feature

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
