# Creating ssh key in my client machine 
ssh-keygen -t rsa -b 4096 -C "mohamedrufai59@gmail.com" -f ~/.ssh/udemywebscraping

# Copy the SSH public key content to your clipboard.
pbcopy < ~/.ssh/udemywebscraping.pub

# Add the SSH key to your GitHub account:
# Go to your GitHub Settings.
# In my Github I can access through url: github.com/settings
# Click on SSH and GPG keys.
# Click on New SSH key or Add SSH key.
# Paste your ssh public key content into the “Key” field.
# Add a descriptive title for the new key, like “Udemy Webscraping Key”.
# Click Add SSH key.


# Ready to push and pull in ssh connected repo
eval "$(ssh-agent -s)"  # Ensure the ssh agent is running
ssh-add --apple-use-keychain ~/.ssh/udemywebscraping  # Add your SSH private key to the ssh-agent
ssh -T git@github.com  # Test your github SSH connection



