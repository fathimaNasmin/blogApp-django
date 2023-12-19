# A Blog Web App Using Django Framework


## Introduction

Embark on a journey of expression and exploration with Blog App, a dynamic web application meticulously crafted on the robust Python-Django framework. Tailored for bloggers and content creators, our platform is designed to empower your voice and share your insights effortlessly.

## Features

- **Seamless CRUD Operations:**
  Experience the ease of creating, reading, updating, and deleting your blog posts with a user-friendly interface, making content management a breeze.

- **Authentication and Authorization:**
  Rest easy knowing that your content is secure. Blog App employs robust authentication and authorization mechanisms to ensure that only authorized users have access to their own content.

- **Social Authentication:**
  Connect with a single click! Enjoy the convenience of logging in through Google and GitHub, streamlining the onboarding process for both new and existing users.

- **Django Pagination:**
  Navigate through your blog posts effortlessly with Django's pagination feature, providing a smooth and organized reading experience.

- **Email Notifications with Django Signals:**
  Stay in the loop with our sophisticated email notification system. Receive updates when a new user joins, profiles are updated, and be the first to know about the latest posts through our newsletter.

- **Newsletter Subscription:**
  Never miss a beat! Subscribe to our newsletter and receive curated content directly in your inbox. Stay informed about the latest trends, insightful articles, and exclusive updates from your favorite creators.

- **Engagement Features:**
  Interact with the community through likes and comments on posts. 

- **Scheduled Tasks with Celery:**
  Efficiency at its best! Blog App leverages Celery for scheduling tasks, ensuring timely delivery of emails.

## Getting Started

Dive into a world of creativity, knowledge, and connection with Blog App. Join us as we redefine the art of blogging, providing you with the tools and features you need to bring your ideas to life.

### Installation

Clone the repository and follow installation steps to get started.

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```bash
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```bash
virtualenv env
```

That will create a new folder env in your project directory. Next activate it with this command on mac/linux:

```bash
source env/bin/active
```
Then install the project dependencies with

```bash
pip install -r requirements.txt
```
Now you can run the project with this command

```bash
python manage.py runserver
```

## Contributions

We welcome contributions! If you find a bug or have a feature request, please open an issue. Feel free to fork the repository and submit a pull request.

