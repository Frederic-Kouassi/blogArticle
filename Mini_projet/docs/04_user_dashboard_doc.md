# User Dashboard - Refactoring Documentation

## Overview

Refactor the user dashboard to use Class-Based Views (CBV), template includes, and dynamic data from the database.

---

## 1. Components to Extract

### Use Shared Components

- Header from `includes/header.html` (if applicable for dashboard)
- Create `includes/dashboard_sidebar.html` for sidebar navigation
- Create `includes/dashboard_header.html` for top header bar
- CSS to `static/css/dashboard.css`
- JavaScript to `static/js/dashboard.js`

### Template Structure

- Create `templates/dashboard/base_dashboard.html` - Base template for all dashboard pages
- Update `user_dashboard.html` to extend base_dashboard
- Extract sidebar (lines 167-232) to include
- Extract top header (lines 236-308) to include

---

## 2. Dashboard Sections (Tabs)

### 2.1 Dashboard Overview (Lines 313-453)

**Current:** Static stats and recent activity

**Make dynamic:**

- Total blogs count (from user's posts)
- Total views count (sum of all post views)
- Comments count (total comments on user's posts)
- Followers count
- Recent activity feed (latest actions)
- Quick action buttons

### 2.2 My Blogs (Lines 456-647)

**Current:** Static table with 4 hardcoded blogs

**Make dynamic:**

- List all user's blog posts
- Show title, category, status, views, date
- Pagination (4 posts per page)
- Actions: Edit, View, Delete
- Filter by status (all, published, draft, pending)
- Search functionality

### 2.3 Create Blog (Lines 650-788)

**Current:** Static form with rich text editor

**Make dynamic:**

- Form submission to create new blog
- Image upload for featured image
- Rich text editor for content
- Category dropdown from database
- Tags input
- Status selection (draft, pending, published)
- Form validation

### 2.4 Profile (Lines 791-800+)

**Make dynamic:**

- User profile information
- Avatar upload
- Bio editing
- Social media links
- Email preferences

### 2.5 Analytics

**Create new section:**

- Views over time (chart)
- Most popular posts
- Traffic sources
- Engagement metrics

### 2.6 Settings

**Create new section:**

- Account settings
- Notification preferences
- Privacy settings
- Password change

---

## 3. Backend Requirements - Class-Based Views (CBV)

### Views to Create

**Use Django's generic CBVs:**

1. **DashboardView** (TemplateView)

   - Display overview statistics
   - Recent activity

2. **BlogListView** (ListView)

   - List user's blogs with pagination
   - Filter and search

3. **BlogCreateView** (CreateView)

   - Create new blog post
   - Handle form submission and image upload

4. **BlogUpdateView** (UpdateView)

   - Edit existing blog post

5. **BlogDeleteView** (DeleteView)

   - Delete blog post with confirmation

6. **ProfileView** (UpdateView)

   - View and update user profile

7. **AnalyticsView** (TemplateView)

   - Display analytics data

8. **SettingsView** (UpdateView)
   - Manage user settings

### Mixins to Use

- **LoginRequiredMixin** - Require authentication for all views
- **UserPassesTestMixin** - Ensure user can only edit their own posts

---

## 4. Models Needed

### User Profile Extension

- Bio, avatar, social links, preferences

### Blog Post

- Already exists (from landing page)
- Ensure user foreign key

### User Activity

- Track user actions (create, edit, publish, delete)
- Timestamp and action type

### User Settings

- Notification preferences
- Privacy settings

---

## 5. URLs Structure

```
/dashboard/ - Dashboard overview
/dashboard/blogs/ - My blogs list
/dashboard/blogs/create/ - Create new blog
/dashboard/blogs/<id>/edit/ - Edit blog
/dashboard/blogs/<id>/delete/ - Delete blog
/dashboard/profile/ - User profile
/dashboard/analytics/ - Analytics
/dashboard/settings/ - Settings
```

---

## 6. Forms to Create

1. **BlogForm** - Create/edit blog posts
2. **ProfileForm** - Update user profile
3. **SettingsForm** - Update user settings

---

## 7. JavaScript Functionality

### Tab Navigation

- Switch between dashboard sections
- Update URL without page reload
- Save active tab in localStorage

### Rich Text Editor

- Implement toolbar functionality
- Format text (bold, italic, headings, lists)
- Insert links and images
- Auto-save drafts

### Image Upload

- Drag and drop functionality
- Preview before upload
- Validate file size and type

### Notifications

- Dropdown toggle
- Mark as read
- Real-time updates (optional - WebSocket)

### Blog Actions

- Edit, view, delete with confirmation
- AJAX for delete action

---

## 8. Implementation Steps

1. Create base_dashboard.html template
2. Extract sidebar to include
3. Extract header to include
4. Create all CBVs (Dashboard, BlogList, BlogCreate, etc.)
5. Create forms (BlogForm, ProfileForm, SettingsForm)
6. Update models (UserProfile, UserActivity, UserSettings)
7. Run migrations
8. Create URL patterns
9. Extract CSS to dashboard.css
10. Extract JavaScript to dashboard.js
11. Implement AJAX functionality
12. Add form validation
13. Test all dashboard features
14. Add permission checks (user can only edit own posts)

---

## 9. Security Considerations

- LoginRequiredMixin on all views
- CSRF protection on all forms
- Validate user owns blog before edit/delete
- Sanitize rich text editor input
- Validate image uploads (type, size)
- Rate limiting on form submissions

---

## 10. Features to Add

- Auto-save drafts (every 30 seconds)
- Blog post preview before publish
- Duplicate blog post
- Bulk actions (delete multiple posts)
- Export blog data
- Schedule posts for future publication
- SEO settings per post
- Reading time calculation
