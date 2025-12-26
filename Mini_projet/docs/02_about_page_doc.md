# About Page - Refactoring Documentation

## 1. Components to Extract

### Use Shared Components
- Header from `includes/header.html`
- Footer from `includes/footer.html`
- CSS from `static/css/main.css`
- JavaScript from `static/js/main.js`

### Update Template
- Make about.html extend base.html
- Remove duplicate header/footer code
- Remove inline CSS and JavaScript

---

## 2. Dynamic Elements to Implement

### 2.1 Statistics Section (Lines 171-198)
**Current:** Static numbers (10,000+ readers, 250+ articles, 150+ countries)

**Make dynamic:**
- Monthly readers count
- Published articles count
- Countries reached count

**Database needs:**
- AboutPageStats model with these three integer fields
- Single record updated from admin

### 2.2 Mission & Vision (Lines 202-214)
**Current:** Static text blocks

**Make dynamic:**
- Mission title and text
- Vision title and text

**Database needs:**
- AboutPageContent model with mission and vision fields
- Editable from admin panel

### 2.3 Core Values (Lines 216-244)
**Current:** 3 hardcoded values

**Make dynamic:**
- Value icon (FontAwesome class)
- Value title
- Value description
- Display order

**Database needs:**
- CoreValue model with icon, title, description, order, is_active
- Multiple records, ordered by order field

### 2.4 Timeline/Journey (Lines 246-308)
**Current:** 4 hardcoded timeline items

**Make dynamic:**
- Year/period
- Title
- Description
- Display order

**Database needs:**
- TimelineItem model with year, title, description, order, is_active
- Multiple records showing company history

### 2.5 Team Members (Lines 310-422)
**Current:** 4 hardcoded team cards

**Make dynamic:**
- Profile photo (with image upload)
- Name
- Position/title
- Bio
- Social media links (Twitter, LinkedIn, Email)
- Display order

**Database needs:**
- TeamMember model with all profile fields
- Image upload for photos
- Optional social media URLs

---

## 3. Backend Requirements

### Models to Create
1. **AboutPageStats** - Statistics numbers
2. **AboutPageContent** - Mission/vision text
3. **CoreValue** - Company values
4. **TimelineItem** - Company history
5. **TeamMember** - Team profiles

### View to Create
- **about()** - Fetch all about page data and render template

### URL to Add
- `/about/` - About page

### Admin Interface
- Register all models
- Make stats and content editable (single record)
- Allow adding/editing/ordering values, timeline, team members

---

## 4. Implementation Steps

1. Update about.html to extend base.html
2. Use header and footer includes
3. Create all required models
4. Run migrations
5. Create about view with context
6. Update URLs
7. Register models in admin
8. Update template to use dynamic data
9. Add sample data via admin
10. Test responsive design
