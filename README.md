# Personal Website

A full-stack personal portfolio website built with Angular and FastAPI, featuring a blog, project showcase, and professional experience timeline.

## 🚀 Features

- **Modern Stack**: Angular 21 frontend + FastAPI backend
- **Blog System**: Write and publish blog posts with tags and featured images
- **Project Showcase**: Display your projects with links to GitHub and live demos
- **Experience Timeline**: Professional work history with responsibilities and technologies
- **Responsive Design**: Mobile-first design that works on all devices
- **RESTful API**: Clean API design with MongoDB database
- **GitHub Pages Ready**: Configured for easy deployment to GitHub Pages

## 📁 Project Structure

```
personal-web/
├── client/                 # Angular frontend
│   ├── src/
│   │   ├── app/
│   │   │   ├── blog/      # Blog components
│   │   │   ├── experience/# Experience component
│   │   │   ├── home/      # Landing page
│   │   │   ├── projects/  # Projects components
│   │   │   ├── navbar/    # Navigation
│   │   │   ├── models/    # TypeScript models
│   │   │   └── services/  # API services
│   │   └── environments/  # Environment configs
│   └── package.json
│
├── server/                # FastAPI backend
│   ├── api/
│   │   └── routes/       # API endpoints
│   ├── config/           # Configuration
│   ├── database/         # Database connection
│   ├── models/           # Database models
│   ├── schemas/          # Pydantic schemas
│   └── main.py
│
└── .github/
    └── workflows/        # GitHub Actions
```

## 🛠️ Tech Stack

### Frontend
- **Framework**: Angular 21
- **Language**: TypeScript
- **Styling**: SCSS
- **HTTP Client**: Angular HttpClient
- **Build Tool**: Angular CLI

### Backend
- **Framework**: FastAPI
- **Language**: Python 3.11+
- **Database**: MongoDB
- **ORM**: Motor (async MongoDB driver)
- **Validation**: Pydantic

## 📋 Prerequisites

- **Node.js** 18+ and npm 9+
- **Python** 3.11+
- **MongoDB** (local or Atlas)

## 🚀 Getting Started

### Backend Setup

1. Navigate to the server directory:
```bash
cd server
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the server directory:
```env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=personal_website
ALLOWED_ORIGINS=http://localhost:4200
```

5. Run the server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the client directory:
```bash
cd client
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

The app will be available at `http://localhost:4200`

## 📝 API Documentation

Once the backend is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### API Endpoints

#### Blogs
- `GET /api/blogs` - List all blogs
- `GET /api/blogs/{id}` - Get single blog
- `POST /api/blogs` - Create blog
- `PUT /api/blogs/{id}` - Update blog
- `DELETE /api/blogs/{id}` - Delete blog

#### Projects
- `GET /api/projects` - List all projects
- `GET /api/projects/{id}` - Get single project
- `POST /api/projects` - Create project
- `PUT /api/projects/{id}` - Update project
- `DELETE /api/projects/{id}` - Delete project

#### Experiences
- `GET /api/experiences` - List all experiences
- `GET /api/experiences/{id}` - Get single experience
- `POST /api/experiences` - Create experience
- `PUT /api/experiences/{id}` - Update experience
- `DELETE /api/experiences/{id}` - Delete experience

## 🌐 Deployment

### Frontend (GitHub Pages)

The repository includes a GitHub Actions workflow that automatically deploys the frontend to GitHub Pages when you push to the main branch.

1. Enable GitHub Pages in repository settings
2. Set source to "GitHub Actions"
3. Push to main branch
4. Your site will be live at `https://yourusername.github.io/personal-web/`

### Backend (Render/Railway/Heroku)

Deploy the FastAPI backend to your preferred platform:

1. Set environment variables (MONGODB_URL, etc.)
2. Update ALLOWED_ORIGINS to include your frontend URL
3. Deploy the server directory

Remember to update the API URL in `client/src/environments/environment.prod.ts` to point to your deployed backend.

## 🎨 Customization

### Update Personal Information

1. **Hero Section**: Edit [client/src/app/home/home.component.html](client/src/app/home/home.component.html)
2. **Navbar Brand**: Edit [client/src/app/navbar/navbar.component.html](client/src/app/navbar/navbar.component.html)
3. **Colors**: Modify SCSS variables in component files
4. **Footer**: Edit [client/src/app/app.html](client/src/app/app.html)

### Add Content

Use the API endpoints (via the Swagger UI at `/docs`) to add:
- Blog posts
- Projects
- Work experiences

## 🧪 Development

### Frontend
```bash
cd client
npm start              # Development server
npm run build          # Production build
npm test               # Run tests
```

### Backend
```bash
cd server
uvicorn main:app --reload     # Development server
pytest                         # Run tests (if configured)
```

## 📄 License

MIT License - feel free to use this project as a template for your own portfolio!

## 🤝 Contributing

This is a personal project, but suggestions and improvements are welcome! Feel free to open an issue or submit a pull request.

## 📧 Contact

For questions or feedback, please open an issue in this repository.

---

Built with ❤️ using Angular and FastAPI
