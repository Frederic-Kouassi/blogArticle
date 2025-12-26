# Contact Page - Refactoring Documentation

## 1. Components to Extract

### Use Shared Components

- Header from `includes/header.html`
- Footer from `includes/footer.html`
- CSS from `static/css/main.css`
- JavaScript from `static/js/main.js`

### Update Template

- Make contact.html extend base.html
- Remove duplicate header/footer code
- Remove inline CSS and JavaScript

---

## 2. Dynamic Elements to Implement

### 2.1 Contact Information (Lines 437-507)

**Current:** Static contact cards with hardcoded emails and addresses

**Make dynamic:**

- General inquiries email
- Editorial/submissions email
- Partnerships email
- Technical support email
- Office address
- Office phone number

**Database needs:**

- ContactInfo model with all contact fields
- Single record editable from admin

### 2.2 Contact Form (Lines 496-557)

**Current:** Static form with JavaScript alert

**Make dynamic:**

- Form submission saves to database
- Email notification sent to admin
- Success/error messages displayed
- Newsletter subscription checkbox functionality
- Form validation (server-side)
- CSRF protection

**Database needs:**

- ContactMessage model (name, email, subject, message, subscribe_newsletter, ip_address, created_at, is_read, replied_at)
- Subject choices (general, submission, partnership, technical, feedback, other)

**Form needs:**

- Django ModelForm for ContactMessage
- Field validation
- Custom widgets with Tailwind classes

### 2.3 FAQ Section (Lines 560-608)

**Current:** 4 hardcoded FAQ items with accordion

**Make dynamic:**

- Question text
- Answer text
- Display order
- Active/inactive status

**Database needs:**

- FAQ model (question, answer, order, is_active)
- Multiple records ordered by order field

---

## 3. Backend Requirements

### Models to Create

1. **ContactInfo** - All contact details
2. **ContactMessage** - Form submissions
3. **FAQ** - Frequently asked questions

### Form to Create

- **ContactForm** - ModelForm for contact submissions with validation

### View to Create

- **contact()** - Handle GET (display form) and POST (process submission)
- Send email notification on form submission
- Handle newsletter subscription if checkbox checked

### Email Functionality

- Create email template for admin notifications
- Configure email settings (SMTP)
- Send notification when contact form submitted

### URL to Add

- `/contact/` - Contact page

### Admin Interface

- Register all models
- ContactMessage admin: list view with filters (subject, is_read, date)
- Mark messages as read
- View submission details
- FAQ admin: inline ordering

---

## 4. Email Configuration

### Settings to Add

- EMAIL_BACKEND
- EMAIL_HOST (e.g., smtp.gmail.com)
- EMAIL_PORT (587)
- EMAIL_USE_TLS
- EMAIL_HOST_USER
- EMAIL_HOST_PASSWORD
- DEFAULT_FROM_EMAIL
- ADMIN_EMAIL

### Email Template

- Create `templates/email/contact_notification.html`
- Include sender info, subject, message
- Professional formatting

---

## 5. Implementation Steps

1. Update contact.html to extend base.html
2. Use header and footer includes
3. Create all required models
4. Create ContactForm
5. Run migrations
6. Create contact view (GET and POST)
7. Implement email notification function
8. Create email template
9. Configure email settings
10. Update URLs
11. Register models in admin
12. Update template to use dynamic data and form
13. Add Django messages framework for feedback
14. Test form submission and email
15. Test FAQ accordion functionality

---

## 6. Form Handling Flow

1. User fills out contact form
2. Form submitted via POST
3. Server validates form data
4. If valid:
   - Save ContactMessage to database
   - If newsletter checkbox: add/update Newsletter record
   - Send email notification to admin
   - Display success message
   - Redirect to contact page
5. If invalid:
   - Display error messages
   - Re-render form with user's data

---

## 7. Security Considerations

- CSRF token in form
- Email validation
- Rate limiting (prevent spam)
- Sanitize user input
- Store IP address for tracking
- Honeypot field (optional anti-spam)
