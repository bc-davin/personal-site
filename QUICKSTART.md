# Quick Start Guide

## 🚀 Get Your Site Running in 5 Minutes

### Step 1: Install Frontend Dependencies

```bash
cd client
npm install
```

### Step 2: Start Frontend Development Server

```bash
npm start
```

Your Angular app will be running at http://localhost:4200

### Step 3: Install Backend Dependencies

Open a new terminal:

```bash
cd server
python -m venv venv

# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### Step 4: Configure MongoDB

Create a `.env` file in the `server` directory:

```env
MONGODB_URL=mongodb://localhost:27017
# OR use MongoDB Atlas:
# MONGODB_URL=mongodb+srv://username:password@cluster.mongodb.net/

DATABASE_NAME=personal_website
ALLOWED_ORIGINS=http://localhost:4200
```

### Step 5: Start Backend Server

```bash
cd server
uvicorn main:app --reload
```

Your API will be running at http://localhost:8000

### Step 6: View Your Site

Open http://localhost:4200 in your browser!

### Step 7: Add Content (Optional)

1. Go to http://localhost:8000/docs (Swagger UI)
2. Use the API endpoints to add:
   - Blog posts
   - Projects
   - Work experiences

## 📝 Example Data

### Create a Project

POST to `/api/projects`:

```json
{
  "title": "Personal Website",
  "description": "A full-stack portfolio site built with Angular and FastAPI",
  "technologies": ["Angular", "FastAPI", "MongoDB", "TypeScript", "Python"],
  "github_url": "https://github.com/yourusername/personal-web",
  "featured": true
}
```

### Create a Blog Post

POST to `/api/blogs`:

```json
{
  "title": "Getting Started with Angular",
  "content": "Angular is a powerful framework for building web applications...",
  "excerpt": "Learn the basics of Angular in this introductory post",
  "tags": ["Angular", "TypeScript", "Web Development"],
  "published": true,
  "author": "Your Name"
}
```

### Create an Experience

POST to `/api/experiences`:

```json
{
  "title": "Software Engineer",
  "company": "Tech Company Inc.",
  "location": "San Francisco, CA",
  "description": "Built scalable web applications",
  "responsibilities": [
    "Developed features using Angular and Node.js",
    "Collaborated with cross-functional teams",
    "Mentored junior developers"
  ],
  "technologies": ["Angular", "Node.js", "MongoDB", "AWS"],
  "start_date": "2022-01-01T00:00:00Z",
  "employment_type": "Full-time",
  "is_current": true
}
```

## 🎉 Next Steps

- Customize the hero section in `client/src/app/home/home.component.html`
- Update colors in the SCSS files
- Add your own projects, blog posts, and experiences via the API
- Deploy to GitHub Pages (see main README.md)

## 🆘 Troubleshooting

**Frontend won't start?**
- Make sure you ran `npm install` in the client directory
- Check that Node.js version is 18 or higher: `node --version`

**Backend won't start?**
- Verify MongoDB is running (if using local MongoDB)
- Check Python version is 3.11+: `python --version`
- Make sure virtual environment is activated

**Can't see any data?**
- The site starts empty - use the API to add content
- Go to http://localhost:8000/docs to use the interactive API

**CORS errors?**
- Check that ALLOWED_ORIGINS in `.env` includes `http://localhost:4200`
- Restart the backend server after changing `.env`

---

Happy coding! 🚀
