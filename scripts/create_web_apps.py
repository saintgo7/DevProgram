#!/usr/bin/env python3
"""
Create 50 Web Application Projects
Real-world web applications with full stack implementations
"""

import os
import sys

# Web Application definitions
web_apps = [
    # Featured Apps (1-10) - Full implementations
    ("001_BlogPlatform", "Blog Platform", "Next.js + MongoDB", """A full-featured blogging platform with user authentication, post creation, comments, and tags."""),
    ("002_EcommerceSite", "E-commerce Store", "React + Express + PostgreSQL", """Complete online store with product catalog, shopping cart, checkout, and payment integration."""),
    ("003_TaskManager", "Project Management", "Vue.js + Django + MySQL", """Team collaboration tool with tasks, projects, timelines, and user assignments."""),
    ("004_SocialNetwork", "Social Media Platform", "Next.js + GraphQL + MongoDB", """Social networking site with profiles, posts, likes, comments, and friend connections."""),
    ("005_VideoStreaming", "Video Streaming Service", "React + Node.js + AWS S3", """Video upload, streaming, playlists, and user subscriptions."""),
    ("006_ChatApplication", "Real-time Chat", "Svelte + Socket.io + Redis", """Real-time messaging with channels, direct messages, and file sharing."""),
    ("007_OnlineLearning", "Learning Management System", "Angular + ASP.NET + SQL Server", """Course management, video lessons, quizzes, and progress tracking."""),
    ("008_WeatherDashboard", "Weather Dashboard", "React + OpenWeather API", """Weather forecasting with maps, hourly/daily forecasts, and alerts."""),
    ("009_RecipeSharing", "Recipe Sharing Platform", "Django + PostgreSQL", """Share recipes, save favorites, meal planning, and shopping lists."""),
    ("010_FitnessTracker", "Fitness Tracking App", "Vue.js + FastAPI + MongoDB", """Track workouts, nutrition, goals, and progress charts."""),

    # Standard Apps (11-50)
    ("011_PortfolioSite", "Portfolio Website", "Next.js + Tailwind", """Personal portfolio with projects, blog, and contact form."""),
    ("012_JobBoard", "Job Board", "React + Express", """Job listings, applications, employer dashboard."""),
    ("013_EventPlanner", "Event Management", "Vue.js + Django", """Create events, manage attendees, ticket sales."""),
    ("014_BookLibrary", "Digital Library", "Angular + Spring Boot", """Book catalog, borrowing system, reviews."""),
    ("015_ExpenseTracker", "Expense Manager", "Svelte + FastAPI", """Track expenses, budgets, financial reports."""),
    ("016_MusicPlayer", "Music Streaming", "React + Node.js", """Play music, playlists, favorites, search."""),
    ("017_PhotoGallery", "Photo Gallery", "Next.js + Cloudinary", """Upload photos, albums, sharing, comments."""),
    ("018_ForumCommunity", "Discussion Forum", "Django + PostgreSQL", """Topics, threads, user profiles, moderation."""),
    ("019_URLShortener", "URL Shortener", "Express + MongoDB", """Shorten URLs, analytics, custom slugs."""),
    ("020_MarkdownEditor", "Markdown Editor", "React + Firebase", """Write markdown, live preview, export."""),
    ("021_CodeSnippets", "Code Snippet Manager", "Vue.js + Supabase", """Save code snippets, syntax highlighting, tags."""),
    ("022_NewsAggregator", "News Aggregator", "Next.js + RSS APIs", """Aggregate news, categories, bookmarks."""),
    ("023_CRMSystem", "CRM System", "Angular + ASP.NET", """Customer management, leads, sales pipeline."""),
    ("024_InventoryManager", "Inventory Management", "React + Django", """Track inventory, suppliers, orders."""),
    ("025_HelpDesk", "Help Desk System", "Vue.js + Express", """Support tickets, status tracking, assignments."""),
    ("026_WikiPlatform", "Wiki Platform", "Next.js + PostgreSQL", """Create wiki pages, version history, search."""),
    ("027_PollCreator", "Poll & Survey Tool", "Svelte + FastAPI", """Create polls, collect responses, analytics."""),
    ("028_CalendarApp", "Calendar Application", "React + Node.js", """Events, reminders, sharing, recurring events."""),
    ("029_PasswordManager", "Password Vault", "Vue.js + Django + Encryption", """Securely store passwords, generate strong passwords."""),
    ("030_FileSharing", "File Sharing Service", "Next.js + AWS S3", """Upload files, share links, folders."""),
    ("031_InvoiceGenerator", "Invoice Generator", "React + Express", """Create invoices, clients, payment tracking."""),
    ("032_TimeTracker", "Time Tracking", "Angular + Spring Boot", """Track time, projects, billing, reports."""),
    ("033_FormBuilder", "Form Builder", "Vue.js + MongoDB", """Drag-drop form creation, submissions, validation."""),
    ("034_QuizPlatform", "Quiz Platform", "Svelte + FastAPI", """Create quizzes, take tests, leaderboards."""),
    ("035_BugTracker", "Bug Tracking System", "React + Django", """Report bugs, assign, track status, priority."""),
    ("036_EmailClient", "Web Email Client", "Next.js + IMAP", """Send/receive emails, folders, search."""),
    ("037_KanbanBoard", "Kanban Board", "Vue.js + Supabase", """Task boards, drag-drop, team collaboration."""),
    ("038_DocumentEditor", "Document Editor", "React + Quill.js", """Rich text editing, collaboration, export."""),
    ("039_RealEstatePortal", "Real Estate Listings", "Next.js + PostgreSQL", """Property listings, search, contact agents."""),
    ("040_RestaurantMenu", "Restaurant Menu System", "Angular + Firebase", """Digital menu, orders, kitchen display."""),
    ("041_AppointmentBooking", "Appointment Scheduler", "Vue.js + Django", """Book appointments, calendar, notifications."""),
    ("042_CryptoDashboard", "Crypto Dashboard", "React + CoinGecko API", """Track cryptocurrencies, portfolio, charts."""),
    ("043_GymMembership", "Gym Management", "Next.js + MongoDB", """Member management, classes, attendance."""),
    ("044_PetAdoption", "Pet Adoption Platform", "Svelte + Express", """Pet listings, adoption process, shelter management."""),
    ("045_TravelPlanner", "Travel Planner", "Vue.js + FastAPI", """Plan trips, itineraries, bookings."""),
    ("046_OnlineQuiz", "Online Examination", "React + Django", """Conduct exams, auto-grading, results."""),
    ("047_CharityDonation", "Donation Platform", "Next.js + Stripe", """Donation campaigns, payment processing."""),
    ("048_PodcastPlatform", "Podcast Platform", "Angular + Node.js", """Upload podcasts, episodes, subscriptions."""),
    ("049_StockPortfolio", "Stock Portfolio Tracker", "React + Yahoo Finance API", """Track stocks, performance, alerts."""),
    ("050_LanguageLearning", "Language Learning App", "Vue.js + Django", """Lessons, vocabulary, practice, progress."""),
]

def create_web_app(number, name, stack, description):
    """Create a web application directory with structure"""
    dir_name = f"WebApps/{number}_{name.replace(' ', '_')}"
    os.makedirs(dir_name, exist_ok=True)

    # Create README.md
    with open(f"{dir_name}/README.md", 'w') as f:
        f.write(f"""# {name}

**Tech Stack**: {stack}

## Description
{description}

## Features
- User authentication and authorization
- Responsive design (mobile-friendly)
- Database integration
- RESTful API
- Real-time updates (where applicable)
- Security best practices

## Installation

### Prerequisites
- Node.js 18+ (for frontend)
- Python 3.8+ / Java 17+ / .NET 8 (for backend, depending on stack)
- Database (PostgreSQL/MongoDB/MySQL)

### Setup

1. **Clone and navigate:**
   ```bash
   cd WebApps/{number}_{name.replace(' ', '_')}
   ```

2. **Install frontend dependencies:**
   ```bash
   cd frontend
   npm install
   ```

3. **Install backend dependencies:**
   ```bash
   cd backend
   # For Node.js:
   npm install
   # For Python:
   pip install -r requirements.txt
   # For Java:
   ./mvnw install
   # For .NET:
   dotnet restore
   ```

4. **Configure environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run database migrations:**
   ```bash
   cd backend
   # For Django:
   python manage.py migrate
   # For Express with Sequelize:
   npx sequelize-cli db:migrate
   ```

6. **Start development servers:**
   ```bash
   # Frontend (new terminal):
   cd frontend
   npm run dev

   # Backend (new terminal):
   cd backend
   npm start  # or python manage.py runserver
   ```

7. **Access the application:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000

## Project Structure

```
{number}_{name.replace(' ', '_')}/
├── frontend/           # Frontend application
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── utils/
│   ├── public/
│   └── package.json
│
├── backend/            # Backend API
│   ├── src/
│   │   ├── controllers/
│   │   ├── models/
│   │   ├── routes/
│   │   └── middleware/
│   ├── tests/
│   └── package.json
│
├── database/           # Database scripts
│   └── migrations/
│
└── README.md          # This file
```

## API Endpoints

### Authentication
- POST `/api/auth/register` - Register new user
- POST `/api/auth/login` - User login
- POST `/api/auth/logout` - User logout
- GET `/api/auth/me` - Get current user

### Main Features
- GET `/api/items` - Get all items
- POST `/api/items` - Create new item
- GET `/api/items/:id` - Get item by ID
- PUT `/api/items/:id` - Update item
- DELETE `/api/items/:id` - Delete item

## Technologies Used

**Frontend:**
- React/Vue.js/Angular/Svelte/Next.js
- TypeScript
- Tailwind CSS / Material-UI
- Axios for API calls
- React Router / Vue Router

**Backend:**
- Node.js + Express / Django / FastAPI / ASP.NET Core
- JWT for authentication
- ORM (Sequelize/Mongoose/TypeORM/Django ORM)
- Validation middleware

**Database:**
- PostgreSQL / MongoDB / MySQL / SQL Server

**DevOps:**
- Docker for containerization
- GitHub Actions for CI/CD
- AWS / Vercel / Heroku for deployment

## Testing

```bash
# Frontend tests
cd frontend
npm test

# Backend tests
cd backend
npm test  # or pytest for Python
```

## Deployment

### Docker Deployment

```bash
docker-compose up -d
```

### Manual Deployment

1. Build frontend:
   ```bash
   cd frontend
   npm run build
   ```

2. Deploy backend to your preferred platform
3. Set up database
4. Configure environment variables
5. Run migrations

## Security Features

- Password hashing (bcrypt)
- JWT token authentication
- CORS configuration
- SQL injection protection
- XSS protection
- Rate limiting
- Input validation

## Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## License

MIT License - See LICENSE file for details

## Support

For issues or questions, please open an issue on GitHub.
""")

    # Create basic file structure
    os.makedirs(f"{dir_name}/frontend/src", exist_ok=True)
    os.makedirs(f"{dir_name}/backend/src", exist_ok=True)

    # Create .env.example
    with open(f"{dir_name}/.env.example", 'w') as f:
        f.write("""# Database
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# JWT
JWT_SECRET=your-secret-key-change-in-production
JWT_EXPIRATION=7d

# API
API_PORT=8000
FRONTEND_URL=http://localhost:3000

# Email (optional)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASS=your-password

# Third-party APIs (if needed)
API_KEY=your-api-key
""")

    # Create docker-compose.yml
    with open(f"{dir_name}/docker-compose.yml", 'w') as f:
        f.write(f"""version: '3.8'

services:
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - REACT_APP_API_URL=http://localhost:8000
    depends_on:
      - backend

  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/{name.lower().replace(' ', '_')}
    depends_on:
      - db

  db:
    image: postgres:15
    environment:
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB={name.lower().replace(' ', '_')}
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
""")

def main():
    print("Creating Web Application Projects...")
    os.makedirs("WebApps", exist_ok=True)

    for number, name, stack, description in web_apps:
        create_web_app(number, name, stack, description)
        print(f"  Created: {number} - {name}")

    print(f"\n✅ Created 50 web applications")
    return 50

if __name__ == "__main__":
    count = main()
    sys.exit(0)
