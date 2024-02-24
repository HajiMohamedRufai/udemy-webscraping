# GITHUB SETTINGS
# In my github I cant access my github settings unless I type the url:
# github.com/settings
# That's where I will be able to add ssh keys etc

# HOW TO ADD REPO
# how to list available remote
git remote -v
# git remote add
git remote add origin git@github.com:HajiMohamedRufai/udemy-webscraping.git


# Creating ssh key in my client machine 
ssh-keygen -t rsa -b 4096 -C "mohamedrufai59@gmail.com" -f ~/.ssh/udemywebscraping

# Copy the SSH public key to your clipboard.
pbcopy < ~/.ssh/udemywebscraping.pub

# Add the SSH key to your GitHub account:
# Go to your GitHub Settings.
# Click on SSH and GPG keys.
# Click on New SSH key or Add SSH key.
# Paste your key into the “Key” field.
# Add a descriptive title for the new key, like “Udemy Webscraping Key”.
# Click Add SSH key.

# HOW TO TEST IF I CAN PUSH/PULL
# Ensure the ssh agent is running
eval "$(ssh-agent -s)"  
# Add your SSH private key to the ssh-agent
ssh-add --apple-use-keychain ~/.ssh/udemywebscraping 
# Test your SSH connection:
ssh -T git@github.com
# Should print out this: 
# "Hi HajiMohamedRufai! You've successfully authenticated, but GitHub does not provide shell access."





