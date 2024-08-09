# Table of Contents
- [User Story Testing](#user-story-testing)
- [Validator Testing](#validator-testing)
  * [HTML](#html)
    + [Fixed Errors](#fixed-errors)
    + [Unfixed Errors](#unfixed-errors)
  * [CSS](#css)
  * [Javascript](#javascript)
  * [Python](#python)
  * [Lighthouse](#lighthouse)
- [Browser Testing](#browser-testing)
- [Device Testing](#device-testing)
- [Manual Testing](#manual-testing)
  * [Site Navigation](#site-navigation)
  * [Home Page](#home-page)
  * [Browse Posts Page](#browse-Posts-page)
  * [Post Detail Page](#Post-detail-page)
  * [Add Post Page](#add-Post-page)
  * [Update Post Page](#update-Post-page)
  * [Confirm Delete Post Page](#confirm-delete-Post-page)
  * [My Posts Page](#my-Posts-page)
  * [My Bookmarks Page](#my-bookmarks-page)
  * [My Meal Plan Page](#my-meal-plan-page)
  * [Django All Auth Pages](#django-all-auth-pages)
- [Bugs](#bugs)
  * [Fixed Bugs](#fixed-bugs)
    + [Overwrite Meal Plan Items](#overwrite-meal-plan-items)
    + [Required fields using Summernote extension submit with just whitespace entered](#required-fields-using-summernote-extension-submit-with-just-whitespace-entered)
    + [No Reverse Match Error](#no-reverse-match-error)
    + [Cloudinary Images not Displaying](#cloudinary-images-not-displaying)
    + [Footer not staying at bottom of screen](#footer-not-staying-at-bottom-of-screen)
  * [Unfixed bugs:](#unfixed-bugs-)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## User Story Testing

### EPIC | User Profile
*As a Site User I can register an account so that I can add/edit/delete my Posts and comment on and like or dislike other people's Posts and add Posts to my Explorer Blog.*

![header](docs/images/navbar.png)

- A registration up button is immediately visible on the navigation Bar for the user to sign up to get started. When the user clicks the button they are taken to the sign up page.

![header](docs/images/signup.png)

- Once the user has registered an account they can perform all the actions listed above.

*As a Site User, I can login or logout of my account so that I can keep my account secure.*
- If the user has registered an account they can access the login and logout buttons in the My Account section of the Navbar. 
![header](docs/images/navbar.png)
![header](docs/images/signin.png)
![header](docs/images/signout.png)

*As a Site User I can see my login status so that I know if I'm logged in or out.*
- Once the user has logged into their account their username displays on the Navbar beside a profile icon.

![header](docs/images/navbar2.png)

### EPIC | User Navigation
 *As a User I can immediately understand the purpose of the site so that I can decide if it meets my needs*

![header](docs/images/home.png)

*As a user, I can intuitively navigate around the site so that I can find content*
- A navigation bar is visible on every page of the site which is fully responsive on different screen sizes.

![header](docs/images/navbar2.png)

*As a Site User, I can view a paginated list of Posts so that I can select a Post to view.*
- The Browse Posts page displays a paginated list of all Posts in the database with a status of published. 

![header](docs/images/posts.png)
![header](docs/images/posts2.png)

*As a Site User, I can click on a post so that I can read the full Post, and view comments left by users.*
- Clicking anywhere inside the Post card will take you directly to that Post's detailed page which displays the full Post details. 

![header](docs/images/postdetail.png)

![header](docs/images/postdetail2.png)

- A list of comments is displayed underneath the Post details.

![header](docs/images/comments.png)

- Like or dislike icons are displayed underneath the Post details.

![header](docs/images/likes.png)

### EPIC | Post Management
*As a Site User, I can view the posts and write a comment on Posts and like or dislike the Posts onto the app through an easy to use interface so that I can share my opinion  with other users.*
- Once the user has logged in, an Add Post Option is immediately available on the Navbar as a call to action for the user to add a Post. When the user clicks the button they are taken to the add Post form.

![header](docs/images/navbar2.png)

![header](docs/images/addpost.png)


- The 'Add Post' button on the Nav bar is visible on every page.

![header](docs/images/navbar2.png)

- Once the user has filled out the form details they can choose to 'Submit Button' which adds the Post to the Posts page.

*As a Site User, I can edit and delete my  Posts that I have created so that I can easily make changes without having to start over.*
- If the logged in user is the Post author, edit and delete Post icon buttons will display on the Post detail page for each Post allowing the user to edit and delete their Posts.

![header](docs/images/createpostbutton.png)

![header](docs/images/postcreated.png)

![header](docs/images/postdelete.png)
![header](docs/images/postdeleted.png)


*As a Site User, I can view my Posts so that I can see and manage all Posts I have created in the one location.*
- All the user's created Posts are available to see on the 'My Posts' page.

![header](docs/images/myposts.png)


### EPIC | Post Interaction
*As a Site User, I can like or dislike  users' Posts, so can show my view about the Post.
- Each Post has like or dislike buttons right below the Post details, it show also number of likes or dislikes.

![header](docs/images/likedislikebuttons.png)

*As a Site User, I can comment on other people's Posts so I can give my feedback.*
- Each Post has a comment section where logged in users can leave comments on the Post.

![header](docs/images/comments.png)

![header](docs/images/commentaprovel.png)


### EPIC | Posts Management
*As a Site User, I can edit and delete comments that I have created so that I can easily make changes if I have made a mistake.*
- If the logged in user is the comment author, edit and delete icon buttons will display bellow the comment  allowing the user to edit or delete their comments.

![header](docs/images/editcommnet.png)

![header](docs/images/deletecomment.png)

![header](docs/images/commentdeleted.png)

### EPIC | Site Administration
*As a Site Administrator, I can create, read, update and delete Posts, and comments so that I can manage the app content*
-  Admins have full access to CRUD functionality for all Posts,and comments in the admin panel.

![header](docs/images/adminpage.png)
![header](docs/images/adminpage2.png)



## Code Validation
The code on the 'Explorer blog' site has been tested through W3C Markup Validation Service, W3C CSS Validation Service and JSHint. Errors were at first found on the site in the W3C Markup Validation Service but could quite easily be fixed.

### Markup Validation
After fixing the inital errors that W3C Markup Validation Service reported, no errors were returned.

### Html Validation
<details><summary><b>HTML Validation Result</b></summary>

![HTML Result Home Page](docs/images/htmlvalidation.png)

![HTML Result Add Post Page](docs/images/addposttest.png)

![HTML Result Login Page](docs/images/login.png)

![HTML Result Logout Page](docs/images/logout.png)
</details><br/>

### Summernote Errors
When validating the About Page I received a number of errors which were caused by the installed Summernote library which runs when using the form on these pages. I could not rectify these errors given that they weren't in my own code therefore they are unresolved. 

 <details>

 <summary>Summernote Errors</summary>

![Summernote Errors](docs/images/summernote1.png)
 </details>

### CSS Validaton
When validating my own code the W3C CSS Validator reports no errors.

<details><summary><b>CSS Validation Result</b></summary>

![CSS Result](docs/images/cssvalidation.png)
</details><br/>


### PEP Validation

All Python files were run through Pep8 with no errors found.


### Responsiveness Test
The responsive design tests were carried out manually with [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) and [Responsive Design Checker](https://techsini.com/multi-mockup/index.php).

| Desktop    | Display <1280px       | Display >1280px    |
|------------|-----------------------|--------------------|
| Render     | pass                  | pass               |
| Images     | pass                  | pass               |
| Links      | pass                  | pass               |

| Tablet     | Samsung Galaxy Tab 10 | Amazon Kindle Fire | iPad Mini | iPad Pro |
|------------|-----------------------|--------------------|-----------|----------|
| Render     | pass                  | pass               | pass      | pass     |
| Images     | pass                  | pass               | pass      | pass     |
| Links      | pass                  | pass               | pass      | pass     |

| Phone      | Galaxy S5/S6/S7       | iPhone 6/7/8       | iPhone 12pro         |
|------------|-----------------------|--------------------|----------------------|
| Render     | pass                  | pass               | pass      | pass     |
| Images     | pass                  | pass               | pass      | pass     |
| Links      | pass                  | pass               | pass      | pass     |

### Pagespeed insights
Google Pagespeed insights Chrome Developer Tools was used to test the application within the areas of *Performance*, *Accessibility*, *Best Practices* and *SEO*. I tested the 
* Overall site performance for desktop - Performance: 99, Accessibility: 91, Best Practises: 96, SEO: 91
![pagespeed](docs/images/pagespeed.png)
* Overall site performance for mobiles - Performance: 80, Accessibility: 92, Best Practises: 96, SEO: 91
![pagespeed](docs/images/pagespeed2.png)


In general this is OK results. The performance is affected in a negative way by external scripts (connected to i.e. Bootstrap) and the lower result on SEO on the Index page and Admin Area Page is i.e. connected to the 'read more' links that is not a 100% optimal description from a SEO point of view. The lower accessibility result on the review details page is connected to the heading elements not being in sequentially-descending order, but this is an active design choice and not a big issue (but I thought it would be proper to highlight it here so that it's clear I'm aware of it).


## Fixed Errors
When validating Html I received an error there were  extra </p> tags in the 'post detail' and in base.html files, field which had been created using the summernote editor. The issue was due to Summernote including < /p> tags around the form field. I resolved the error by removing the surrounding < /p> tags in my HTML when rendering a summernote field in my post Detail page.



[Back to top](<#table-of-content>)

## Fixed Bugs
 - #### No Reverse Match Error
     - **Bug**: When I first implemented the Add Post form I kept getting a no reverse match error
                when trying to submit a new post due to the slug field not populating properly. 
     - **Fix**: with help of my Mentor I learned about AutoSlugField which is a Django Model Field extension
                which will automatically create a unique slug and you can choose which field to 
                populate the slug from. Utilising this extension I was able to create a unique slug populated from the post title.

- #### Cloudinary Images not Displaying
     - **Bug**: Cloudinary images not displaying after uploading. 
     - **Fix**: with help of my Mentor and  discussed the issue on slack I realised that I needed to include
                enctype="multipart/form-data in the opening form HTML tag and this solved the problems 

- #### Footer not staying at bottom of screen
     - **Bug**: Footer not staying at the bottom of the screen when displaying on pages
                without fullscreen content and didn't want to use a sticky footer. 
     - **Fix**: page hight was set for smaller pages and make the page content 100% of the
                viewport height less the height of the footer and this solved the problem.
 
 - #### Edit or Delete Comments not working
     - **Bug**: edit or delete comments function was throwing error, 
     - **fix**: there was a typo in blog url for the delete or edit views. correction the view name solved the problem.
     
  - #### Responsiveness testing sites wrere unable to connect to Heroku App
     - **Bug**: for testing the site responsiveness, while testing occurred an error that Heroku app refused to connect.
     - **Fix**: I asked Help on slack community, i needed to add a chrome extension "Ignore X-Frame headers" that solved the problem.
     

### Unfixed bugs:
There are no known unfixed bugs.

### Browser Compatibility
* Google Chrome Version (106.0.5249.119)
* Mozilla Firefox (version 105.0.3)
* Min (version 1.26.0)
* Apple Safari (version 16.0)
* Microsoft Edge (version 106.0.1370.47)


