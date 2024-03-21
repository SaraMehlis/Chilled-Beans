# Validation Testing

## HTML and CSS

I used the W3c validator on my HTML and CSS files.  Please see results below:


### HTML

| File | URL | Screenshot | Notes |
|--------|--------|--------|--------|
| Home | https://validator.w3.org/nu/?doc=https%3A%2F%2Fchilled-beans-b5ddfca96935.herokuapp.com%2F | ![Screenshot](static/images/home-w3c.PNG) | Document checking completed. No errors or warnings to show |
| About | https://validator.w3.org/nu/?doc=https%3A%2F%2Fchilled-beans-b5ddfca96935.herokuapp.com%2Fabout%2F | ![Screenshot](static/images/about-w3c.PNG) | Document checking completed. No errors or warnings to show |
| Add Recipe | https://validator.w3.org/nu/?doc=https%3A%2F%2Fchilled-beans-b5ddfca96935.herokuapp.com%2Fform%2F | ![Screenshot](static/images/add_recipe-w3c.PNG) | Document checking completed. No errors or warnings to show |
| Edit page | https://validator.w3.org/nu/?doc=https%3A%2F%2Fchilled-beans-b5ddfca96935.herokuapp.com%2Frecipe%2Fedit%2Ficed-honey-oat-milk-latte%2F | ![Screenshot](static/images/edit-w3c.PNG) | The form will be submitted to the same view that renders it, leaving the action attribute empty (action="") is a common practice in Django |
| Confirm adding recipe page | https://validator.w3.org/nu/?doc=https%3A%2F%2Fchilled-beans-b5ddfca96935.herokuapp.com%2Fform%2F | ![Screenshot](static/images/confirm-add-w3c.PNG) | Document checking completed. No errors or warnings to show |
| Confirm adding recipe page | https://validator.w3.org/nu/?doc=https%3A%2F%2Fchilled-beans-b5ddfca96935.herokuapp.com%2Frecipe%2Fdelete%2Fgggg32%2F | ![Screenshot](static/images/confirm-delete-w3c.PNG) | Document checking completed. No errors or warnings to show |
| Search Page | https://validator.w3.org/nu/?doc=https%3A%2F%2Fchilled-beans-b5ddfca96935.herokuapp.com%2Fsearch%2F%3Fq%3Dlatte | ![Screenshot](static/images/search-w3c.PNG) | Document checking completed. No errors or warnings to show |
| Register | https://validator.w3.org/nu/?doc=https%3A%2F%2Fchilled-beans-b5ddfca96935.herokuapp.com%2Faccounts%2Fsignup%2F | ![Screenshot](static/images/register-w3c.PNG) | Error within AllAuth |
| Sign In | https://validator.w3.org/nu/?doc=https%3A%2F%2Fchilled-beans-b5ddfca96935.herokuapp.com%2Faccounts%2Flogin%2F | ![Screenshot](static/images/signin-w3c.PNG) | Document checking completed. No errors or warnings to show |
| sign Out | https://validator.w3.org/nu/?doc=https%3A%2F%2Fchilled-beans-b5ddfca96935.herokuapp.com%2Faccounts%2Flogout%2F | ![Screenshot](static/images/signout-w3c.PNG) | Document checking completed. No errors or warnings to show |   


### CSS

| File |  URL | Screenshot | Notes |
|--------|--------|--------|--------|
| style.css | https://jigsaw.w3.org/css-validator/validator | ![Screenshot](static/images/css-w3c.PNG) | No Error Found |


### PYTHON

I used the CI Python Linter https://pep8ci.herokuapp.com/# on all my .py files. Please see results below.
| File | Screenshot |
|--------|--------|
| my_project urls.py | ![Screenshot](static/images/project-url.py-validator.PNG) |
| my_project setting.py | ![Screenshot](static/images/setting.py-validator.PNG) |
| admin.py | ![Screenshot](static/images/admin.py-validate.PNG) |
| forms.py | ![Screenshot](static/images/forms.py-validate.PNG) |
| models.py | ![Screenshot](static/images/models.py-validator.PNG) |
| blog urls.py | ![Screenshot](static/images/recipe-url-validator.PNG) |
| views.py | ![Screenshot](static/images/views.py-validator.PNG) |

Due to the nature of the code and the need to accommodate complex expressions, I encountered difficulties in complying with the PEP8 standards, particularly regarding line length. While adhering to the guidelines is important, in certain cases, maintaining readability and clarity took precedence.


### Manual Testing


