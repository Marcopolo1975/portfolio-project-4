# The Explorer blog

The Explorer Blog App is a web application designed for travel enthusiasts to share their travel experiences, photos, and tips with a community of like-minded adventurers. Users can create and manage their own travel blogs, read and comment on posts from others, and discover new travel destinations. The app provides a platform for users to engage with each other's content through likes and comments, fostering a vibrant and interactive travel community.

The live link can be found here - [The Explorer Blog]()

![Colour Palette](docs/readme_images/site_mockup.png)

## Table of Contents

- [The Explorer Blog](#the-explorer-blog)
  * [User Experience (UX)](#user-experience-ux)
    + [User Stories](#user-stories)
    + [Design](#design)
      - [Colour Scheme](#colour-scheme)
      - [Imagery](#imagery)
      - [Fonts](#fonts)
      - [Wireframes](#wireframes)
  * [Agile Methodology](#agile-methodology)
  * [Data Model](#data-model)
  * [Testing](#testing)
  * [Security Features and Defensive Design](#security-features-and-defensive-design)
    + [User Authentication](#user-authentication)
    + [Form Validation](#form-validation)
    + [Database Security](#database-security)
    + [Custom error pages:](#custom-error-pages-)
  * [Features](#features)
    + [Header](#header)
    + [Footer](#footer)
    + [Home Page](#home-page)
    + [User Account Pages](#user-account-pages)
    + [Browse Posts](#browse-posts)
    + [Post Detail Page](#post-detail-page)
    + [Add Post Form](#add-post-form)
    + [Update Post Form](#update-post-form)
    + [Delete Post](#delete-post)
    + [Comment Post Form](#comment-post-form)
    + [Error Pages](#error-pages)
    + [Future Features](#future-features)
  * [Deployment - Heroku](#deployment---heroku)
  * [Forking this repository](#forking-this-repository)
  * [Cloning this repository](#cloning-this-repository)
  * [Languages](#languages)
  * [Frameworks - Libraries - Programs Used](#frameworks---libraries---programs-used)
  * [Credits](#credits)
  * [Acknowledgments](#acknowledgments)
 
<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>
## User Experience (UX)
Creating a delightful and intuitive user experience for a travel blog app is essential
to engage users and encourage them to share and explore travel content. Here are some 
key UX principles and features that should be incorporated into the app to enhance 
user satisfaction:

### User Stories

#### View paginated list of posts
- As a site user I can view a paginated list of posts so that I can select which post I want to view
- Acceptance criteria
- Given more than one post in the database, these multiple posts are listed.
- When a user opens the main page a list of posts is seen.
  Then the user sees all post titles with pagination to choose what to read.
#### User Navigation
- As a Site User I can immediately understand the purpose of the site so that I can decide if it meets my needs.
- As a Site User, I can intuitively navigate around the site so that I can find content and understand where I am on the site.
- As a Site User, I can view a paginated list of posts so that I can select a post to view.
- As a Site User, I can click on a post so that I can read the full post, view comments left by users.

#### Post Management
- As a Site User, I can add my  post onto the app through an easy to use interface so that I can share them with other users.
- As a Site User, I can edit and delete my posts that I have created so that I can easily make changes without having to start over.

#### Post Interaction
- As a Site User, I can comment on other people's posts so I can give my feedback.
- As a Site User, I can edit and delete comments that I have created so that I can easily make changes if I have made a mistake.
- As a Site User / Admin I can view comments on an individual post so that I can read the conversation

#### Account registration
- As a Site User, i can register an account by giving a user name or email and password.
- As a Site User, I can log in to the app.
- As a Site User, I can  logged in then i can comment on posts, like or unlike the posts and creat my own posts to share with other Users.
- As a Site User, I can Add a new Post so that so that i can share my experience with other users

#### Site Administration
- As a Site Administrator, I can create, read, update and delete posts so that I can manage my blog content.
- As a Site Administrator, i have Given a logged in user, they can create a blog post.
- As a Site Administrator, i have Given a logged in user, they can read a blog post.
- As a Site Administrator, i have Given a logged in user, they can update their blog post.
- As a Site Administrator, i have Given a logged in user, they can delete a blog post.
- As a Site Administrator, I can create or update the about page content so that it is available on the site.
- As a Site Administrator, I can approve or disapprove comments so that I can filter out objectionable comments.
- As a Site Administrator, I can create or update the about page content so that it is available on the site.
- As a Site Administrator, I can create draft posts so that I can finish writing the content later.

#### Read about the site
- As a Site User, I can click on the About link so that I can read about the site.
- As a Site Administrator, I can create or update the about page content so that it is available on the site.

#### Potential Collaboration
- As a Site User, I can fill in a contact form so that I can submit a request for collaboration.
- As a Site Administrator, I can store collaboration requests in the database so that I can review them.
- As a Site Administrator, i can read the collaboration requests and reply to them for further collaboration.

#### User stories not yet implemented

The following user stories were scoped out of the project due to time constraints. It is intended that these user stories will be implemented at a later date. 

- As a Site User, I can bookmark a posts so that i can view my favorite posts later.
- As a Site User, I can share the posts to the outher socialmedia platforms. 
- As a Site User, I can search and filter posts so that I can find the one I want.

### Design

The site has a very simple and clean design which was purposely chosen in order to keep in theme with the site's goal. i.e. invoking a sense of calm in the user and reducing stress. 

#### Colour Scheme
Colour palette from Coolors

![Colour Palette](docs/readme_images/colour_scheme.png)

The colour scheme of the site is mainly pale white , Blue and green . The colours chosen are quite neutral and calming. 

Great care was taken to establish a good contrast between background colours and text at all times to ensure maximum user accessibility. 

#### Imagery
The mostely images are from user posts , uploaded to cloudinary DB. logo and main Banner and i have created myself.
#### Fonts
The Georgia serif and Roboto Slab serif font is the main font used for the body of the website with the Playfair Display font used for the main headings on the home page. These fonts were imported via Google Fonts. Sans Serif is the backup font, in case for any reason the main font isn't being imported into the site correctly.

#### Wireframes

<details>

 <summary>Landing Page</summary>

![Landing Page]()
</details>

<details>

<summary> Posts Pages</summary>

![Posts Pages]()
</details>


<details>

<summary>Add Post</summary>

![Add Post]()
</details>

<details>

<summary>About Page</summary>

![About Page]()
</details>

<details>

<summary>Registration Page</summary>

![Registration Page]()
</details>

<details>
<summary>Login&Logout page</summary>

![Login&Logout page]()
</details>

## Agile Methodology

Github projects was used to manage the development process using an agile approach. Please see link to project board [here]()

The 16 user stories were documented within the Github project as Milestones. A Github Issue was created for each User Story which was then allocated to a milestone. Each User Story has defined acceptance criteria to make it clear when the User Story has been completed. The acceptance criteria are further broken down into tasks to facilitate the User Story's execution.

## Data Model
I used principles of Object-Oriented Programming throughout this project and Django’s Class-Based Generic Views.  

Django AllAuth was used for the user authentication system.

In order for the users to create Post a custom Post model was required. The Post author is a foreign key to the User model given a post can only have one author.

The Comment model allows users to comment on individual Post and the Post is a foreign key in the comment model given a comment can only be linked to one Post. 


The diagram below details the database schema.

![Database Schema](docs/readme_images/database_schema.png)
