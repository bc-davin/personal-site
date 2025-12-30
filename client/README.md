# Personal Website - Frontend

This is the Angular frontend for my personal portfolio website, featuring my projects, blog posts, and professional experience.

## Features

- 🏠 Home page with featured projects and recent blog posts
- 💼 Projects showcase with detailed information
- 📝 Blog with article listings and individual post pages
- 👔 Professional experience timeline
- 📱 Responsive design for all devices
- 🎨 Modern UI with smooth animations

## Tech Stack

- **Framework**: Angular 21
- **Language**: TypeScript
- **Styling**: SCSS
- **HTTP Client**: Angular HttpClient
- **Routing**: Angular Router

## Prerequisites

- Node.js (v18 or higher)
- npm (v9 or higher)

## Installation

1. Install dependencies:
```bash
npm install
```

## Development

Run the development server:
```bash
npm start
```

Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.

## Backend Connection

The app connects to a FastAPI backend running at `http://localhost:8000/api` by default (development mode).

Make sure your backend server is running before starting the frontend.

## Building for Production

Build the project:
```bash
npm run build
```

The build artifacts will be stored in the `dist/` directory.

## Project Structure

```
client/
├── src/
│   ├── app/
│   │   ├── blog/              # Blog components
│   │   ├── experience/        # Experience/resume component
│   │   ├── home/              # Landing page
│   │   ├── models/            # TypeScript interfaces
│   │   ├── navbar/            # Navigation component
│   │   ├── projects/          # Projects components
│   │   ├── services/          # API services
│   │   ├── app.config.ts      # App configuration
│   │   ├── app.routes.ts      # Route definitions
│   │   └── app.ts             # Root component
│   ├── environments/          # Environment configurations
│   └── styles.scss            # Global styles
└── package.json
```

## Deployment to GitHub Pages

1. Install the Angular GitHub Pages deployer:
```bash
npm install -g angular-cli-ghpages
```

2. Build for production with base href:
```bash
npm run build -- --base-href /personal-web/
```

3. Deploy to GitHub Pages:
```bash
npx angular-cli-ghpages --dir=dist/client-app/browser
```

Note: Make sure to update the API URL in the production environment file to point to your hosted backend.

## API Endpoints

The app consumes the following API endpoints:

- `GET /api/blogs` - List all blog posts
- `GET /api/blogs/:id` - Get single blog post
- `GET /api/projects` - List all projects
- `GET /api/projects/:id` - Get single project
- `GET /api/experiences` - List all experiences
- `GET /api/experiences/:id` - Get single experience

## Customization

To customize the site for your own use:

1. Update the hero text in `src/app/home/home.component.html`
2. Modify colors and styles in component SCSS files
3. Update the navbar brand name in `src/app/navbar/navbar.component.html`
4. Configure your API URL in `src/environments/` files

## License

MIT
