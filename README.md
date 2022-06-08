# Introduction 
This project provides the boilerplate code to implement complex API endpoints easily.

# System requirement

To deploy the abc_webapp repository, you'll need:
- Docker

Add the make utility for Ubuntu:
  ```sh
  $ sudo apt-get install build-essential
  ```

# Installation Instructions
This section is a quick setting on an ubuntu VM.
1.	Pull down the source code from this GitLab repository::
      ```sh
      $ git clone <repo-url>
      $ cd <cloned repo>
      ```
      
3.  Build and run the docker container::
      ```sh
      $ make build
      $ make up
      ```
# Other commands
1. Kill the docker container::
      ```sh
      $ make kill
      ```
2. Go inside the container::
      ```sh
      $ make cli
      ```
Go to the URL : [http://0.0.0.0:8000](http://0.0.0.0:8000)