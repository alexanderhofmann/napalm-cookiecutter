#!/bin/bash

SOURCE_REPO=napalm-automation/napalm-cookiecutter
TARGET_REPO=napalm-automation/napalm-skeleton


set -e
set -x
ls -al

head_hash=$(git rev-parse --short --verify HEAD)
repo_name=$(basename $TARGET_REPO)

# decrypt key and add to agent
ENCRYPTED_KEY_VAR="encrypted_${GH_KEY_TAG}_key"
ENCRYPTED_IV_VAR="encrypted_${GH_KEY_TAG}_iv"
ENCRYPTED_KEY=${!ENCRYPTED_KEY_VAR}
ENCRYPTED_IV=${!ENCRYPTED_IV_VAR}
#openssl aes-256-cbc -K $ENCRYPTED_KEY -iv $ENCRYPTED_IV -in push_key.enc -out push_key -d

chmod 600 push_key
eval $(ssh-agent -s)
md5sum push_key
ssh-add push_key

# clone generated repo
rm -rf gen
git clone git@github.com:${TARGET_REPO}.git gen

# create new generated repo
rm -rf new_gen
cookiecutter --no-input . -o new_gen -f

# cookiecutter creates a base dir inside
cd new_gen/*

# grab git info
mv ../../gen/.git .

# commit and push
git config user.name "Travis CI"
git config user.email "grizz@20c.com"
git add .
git commit -m "generated from $SOURCE_REPO@$head_hash"

git push origin master

