# Personal Website API

FastAPI backend for a personal website with blogs, projects, and experiences.

## Features

- **Blog Management**: Create, read, update, and delete blog posts
- **Project Showcase**: Manage your portfolio projects
- **Experience Timeline**: Track your professional experiences
- **MongoDB Integration**: NoSQL database with Motor async driver
- **CORS Enabled**: Ready for frontend integration
- **API Documentation**: Auto-generated with FastAPI

## Setup

### 1. Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# or
source .venv/bin/activate  # Linux/Mac
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Copy `.env.example` to `.env` and update values:

```bash
cp .env.example .env
```

Edit `.env`:
```env
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=personal_website
```

For MongoDB Atlas:
```env
MONGODB_URL=mongodb+srv://username:password@cluster.mongodb.net/
```

### 4. Run the Server

```bash
uvicorn main:app --reload
```

The API will be available at:
- API: http://127.0.0.1:8000
- Interactive docs: http://127.0.0.1:8000/docs
- Alternative docs: http://127.0.0.1:8000/redoc

## API Endpoints

### Blogs
- `POST /api/blogs/` - Create a new blog
- `GET /api/blogs/` - Get all blogs
- `GET /api/blogs/{id}` - Get a specific blog
- `PUT /api/blogs/{id}` - Update a blog
- `DELETE /api/blogs/{id}` - Delete a blog

### Projects
- `POST /api/projects/` - Create a new project
- `GET /api/projects/` - Get all projects
- `GET /api/projects/{id}` - Get a specific project
- `PUT /api/projects/{id}` - Update a project
- `DELETE /api/projects/{id}` - Delete a project

### Experiences
- `POST /api/experiences/` - Create a new experience
- `GET /api/experiences/` - Get all experiences
- `GET /api/experiences/{id}` - Get a specific experience
- `PUT /api/experiences/{id}` - Update an experience
- `DELETE /api/experiences/{id}` - Delete an experience

## Project Structure

```
server/
├── api/
│   └── routes/
│       ├── blogs.py
│       ├── projects.py
│       └── experiences.py
├── config/
│   └── settings.py
├── database/
│   └── db.py
├── schemas/
│   ├── blog.py
│   ├── project.py
│   └── experience.py
├── main.py
├── requirements.txt
└── .env
```

## MongoDB Atlas Setup

1. Sign up at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
2. Create a free cluster
3. Create a database user
4. Whitelist your IP address (or use 0.0.0.0/0 for development)
5. Get your connection string
6. Update `.env` with the connection string

## Development

Run with auto-reload:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## License

MIT
