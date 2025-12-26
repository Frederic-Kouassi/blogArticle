# Blog Refactoring Task List

## Phase 1: Landing Page (home.html) Refactoring

### 1.1 Create Template Structure

- [ ] Create `templates/includes/` folder
- [ ] Extract header to `templates/includes/header.html`
- [ ] Extract footer to `templates/includes/footer.html`
- [ ] Create improved `templates/base.html` with proper structure
- [ ] Update `home.html` to extend base and use includes

### 1.2 Extract Static Assets

- [ ] Move CSS from `home.html` to `static/css/main.css`
- [ ] Move JavaScript from `home.html` to `static/js/main.js`
- [ ] Create `static/js/home.js` for page-specific functionality

### 1.3 Dynamize Landing Page Content

- [ ] Connect hero section to database (title, subtitle, CTA buttons)
- [ ] Make featured posts slider dynamic (fetch from database)
- [ ] Make blog listing section dynamic (fetch latest articles)
- [ ] Make sidebar categories dynamic (fetch from database)
- [ ] Make sidebar recent posts dynamic (fetch from database)
- [ ] Make sidebar popular tags dynamic (fetch from database)
- [ ] Implement newsletter subscription functionality (save to database)
- [ ] Implement "Load More" pagination for blog posts

### 1.4 Backend Development for Landing Page

- [ ] Create/update models for blog posts, categories, tags
- [ ] Create view for home page with context data
- [ ] Create API endpoint for newsletter subscription
- [ ] Create API endpoint for "Load More" functionality
- [ ] Add admin interface for managing homepage content

## Phase 2: About Page Refactoring

### 2.1 Template Refactoring

- [ ] Update `about.html` to extend base template
- [ ] Use header and footer includes
- [ ] Move CSS to shared stylesheet
- [ ] Move JavaScript to shared file

### 2.2 Dynamize About Page Content

- [ ] Make statistics dynamic (monthly readers, articles, countries)
- [ ] Make mission and vision editable from admin
- [ ] Make core values dynamic (fetch from database)
- [ ] Make timeline/journey items dynamic (fetch from database)
- [ ] Make team members dynamic (fetch from database)
- [ ] Add image upload functionality for team members

### 2.3 Backend Development for About Page

- [ ] Create model for About Page content
- [ ] Create model for Team Members
- [ ] Create model for Timeline/Journey items
- [ ] Create model for Core Values
- [ ] Create view for about page
- [ ] Add admin interface for managing about content

## Phase 3: Contact Page Refactoring

### 3.1 Template Refactoring

- [ ] Update `contact.html` to extend base template
- [ ] Use header and footer includes
- [ ] Move CSS to shared stylesheet
- [ ] Move JavaScript to shared file

### 3.2 Implement Contact Form Functionality

- [ ] Create Contact model to store messages
- [ ] Create contact form (Django forms)
- [ ] Implement form validation
- [ ] Implement email notification on form submission
- [ ] Add success/error messages
- [ ] Implement newsletter subscription checkbox functionality
- [ ] Add CSRF protection

### 3.3 Dynamize Contact Page Content

- [ ] Make contact information editable from admin
- [ ] Make FAQ items dynamic (fetch from database)
- [ ] Add ability to add/edit/delete FAQs from admin

### 3.4 Backend Development for Contact Page

- [ ] Create ContactMessage model
- [ ] Create FAQ model
- [ ] Create ContactForm
- [ ] Create view for contact page (GET and POST)
- [ ] Create email template for contact notifications
- [ ] Add admin interface for viewing contact messages
- [ ] Add admin interface for managing FAQs

## Phase 4: Documentation

### 4.1 Landing Page Documentation

- [/] Create detailed documentation for landing page structure
- [/] List all dynamic elements and their data sources
- [/] Document API endpoints
- [/] Document models and relationships

### 4.2 User Dashboard Documentation

- [ ] Create documentation for user dashboard features
- [ ] List all user-specific functionalities
- [ ] Document user permissions and access control

### 4.3 Admin Dashboard Documentation

- [ ] Create documentation for admin dashboard features
- [ ] List all admin-specific functionalities
- [ ] Document admin permissions and access control

## Phase 5: Testing & Verification

### 5.1 Landing Page Testing

- [ ] Test header navigation (all links)
- [ ] Test mobile menu functionality
- [ ] Test featured posts slider
- [ ] Test blog post cards and pagination
- [ ] Test newsletter subscription
- [ ] Test responsive design (mobile, tablet, desktop)

### 5.2 About Page Testing

- [ ] Test all sections display correctly
- [ ] Test responsive design
- [ ] Test team member cards

### 5.3 Contact Page Testing

- [ ] Test contact form submission
- [ ] Test form validation
- [ ] Test email notifications
- [ ] Test FAQ accordion functionality
- [ ] Test responsive design

## Phase 6: Optimization

- [ ] Optimize images (compress, lazy loading)
- [ ] Minify CSS and JavaScript
- [ ] Implement caching for static content
- [ ] Add SEO meta tags
- [ ] Test page load performance
- [ ] Add accessibility features (ARIA labels, etc.)
