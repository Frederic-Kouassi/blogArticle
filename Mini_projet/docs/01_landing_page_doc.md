# Landing Page (home.html) - Refactoring Documentation

## 1. Components to Extract to Includes

### Header Component (`templates/includes/header.html`)

- **Location:** Lines 112-165 in current home.html
- **Contains:** Logo, navigation menu (desktop & mobile), authentication links
- **Dynamic:** User authentication status, active page highlighting
- **Context needed:** `user`, `request.path`

### Footer Component (`templates/includes/footer.html`)

- **Location:** Lines 633-698 in current home.html
- **Contains:** Logo, social links, navigation, categories, newsletter form, copyright
- **Dynamic:** Categories list from database
- **Context needed:** `categories`, `current_year`

### CSS Styles (`static/css/main.css`)

- **Location:** Lines 10-109 in current home.html
- **Extract:** CSS variables, typography, component styles, responsive queries

### JavaScript (`static/js/main.js`)

- **Location:** Lines 700-796 in current home.html
- **Extract:** Mobile menu toggle, sticky header, smooth scrolling, header initialization

### Page-Specific JavaScript (`static/js/home.js`)

- **Extract:** Featured slider, load more button, newsletter form submission

---

## 2. Dynamic Elements to Implement

### 2.1 Hero Section (Lines 167-290)

**Make dynamic:**

- Hero title and subtitle
- CTA buttons based on auth status
- Featured posts slider (3 posts with image, category, date, title, excerpt, author)

**Database needs:**

- HeroSection model (title, subtitle, background_image, is_active)
- BlogPost model with is_featured and featured_order fields

### 2.2 Latest Articles Section (Lines 292-404)

**Make dynamic:**

- Section title and subtitle
- Blog post cards (image, category, date, title, excerpt, author, read time)
- Pagination with "Load More" button

**Database needs:**

- BlogPost model (title, slug, excerpt, content, featured_image, author, category, tags, published_date, read_time, is_published, views_count)

### 2.3 Featured Article Preview (Lines 406-528)

**Make dynamic:**

- Featured image, category, title, author info, date, read time
- Article content preview, tags, social sharing, author bio

**Note:** Display single featured article selected from admin

### 2.4 Sidebar - Newsletter (Lines 533-542)

**Make dynamic:**

- Form submission saves to database
- Email validation and duplicate handling
- Success/error messages

**Database needs:**

- Newsletter model (email, subscribed_date, is_active, ip_address)

### 2.5 Sidebar - Categories (Lines 544-579)

**Make dynamic:**

- Category name, post count, link

**Database needs:**

- Category model (name, slug, description, icon, color, is_active)

### 2.6 Sidebar - Recent Posts (Lines 581-613)

**Make dynamic:**

- Post thumbnail, title, date, link
- Fetch last 3 published posts

### 2.7 Sidebar - Popular Tags (Lines 615-628)

**Make dynamic:**

- Tag name, link, post count

**Database needs:**

- Tag model (name, slug, is_active)

---

## 3. Backend Requirements

### Models to Create

1. **Category** - Blog categories with icon and color
2. **Tag** - Blog tags
3. **BlogPost** - Main blog content with all metadata
4. **HeroSection** - Homepage hero content
5. **Newsletter** - Email subscriptions

### Views to Create

1. **home()** - Main landing page view with all context data
2. **subscribe_newsletter()** - AJAX endpoint for newsletter signup
3. **load_more_posts()** - AJAX endpoint for pagination

### URLs to Add

- `/` - Home page
- `/subscribe/` - Newsletter subscription
- `/load-more/` - Load more posts

---

## 4. JavaScript Functionality

### Newsletter Subscription

- Handle form submission via AJAX
- Display success/error messages
- Clear form on success
- CSRF token handling

### Load More Posts

- Fetch next page of posts via AJAX
- Append new posts to grid
- Update button state (loading, disabled, hidden)
- Update post count display

### Featured Slider

- Scroll functionality with prev/next buttons
- Smooth scrolling behavior

---

## 5. File Structure After Refactoring

```
templates/
├── base.html (NEW - improved)
├── home.html (UPDATED - extends base)
├── includes/ (NEW FOLDER)
│   ├── header.html (NEW)
│   └── footer.html (NEW)

static/
├── css/
│   └── main.css (NEW)
└── js/
    ├── main.js (NEW)
    └── home.js (NEW)

blog/
├── models.py (UPDATED)
├── views.py (UPDATED)
├── urls.py (UPDATED)
└── admin.py (UPDATED)
```

---

## 6. Implementation Steps

1. Create includes folder and extract header/footer
2. Create base.html template
3. Extract CSS to static file
4. Extract JavaScript to static files
5. Create all required models
6. Run migrations
7. Create views with context data
8. Update URLs
9. Register models in admin
10. Update home.html to use dynamic data
11. Test all functionality
