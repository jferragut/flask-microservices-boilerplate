#!/bin/bash

# exit when any command fails
set -e

# keep track of the last executed command
trap 'last_command=$current_command; current_command=$BASH_COMMAND' DEBUG
# echo an error message before exiting
trap 'echo "\"${last_command}\" command filed with exit code $?."' EXIT


clear

printf "Using Homebrew to Install Heroku CLI\n"
brew install heroku/brew/heroku 
printf "Success! \n\n"

printf "Using Homebrew to Install Zeit Now CLI\n"
brew cask install now
printf "Success! \n\n"

printf "Using Homebrew to Install Pipenv CLI\n"
brew install pipenv
printf "Success! \n\n"

printf "Dependencies installed successfully.\n\n"

printf "Installing pip packages\n"
pipenv install
printf "Packages installed successfully.\n\n"


printf "Running database migrations\n"
pipenv run migrate
printf "Migrations were performed successfully.\n\n"

echo "Installation was successful. type `pipenv run start` to begin the dev server."