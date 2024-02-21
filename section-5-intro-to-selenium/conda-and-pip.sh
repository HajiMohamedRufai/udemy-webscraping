# create conda environment
conda create --name webscraping  # conda create -n webscraping

# list conda environments
conda env list 

# delete/remove an envt
conda remove --name webscraping --all

# create envt with python
conda create --name webscraping python=3.8

# activate environment
conda activate webscraping

# path of envt exucutable commands
# /Users/hajirufai/anaconda3/envs/webscraping/bin/

#================================================================================================

# check conda version
conda --version

# check pip version
pip --version

# update conda version
conda update conda

# update pip version
pip install --upgrade pip

# list conda installed packages
conda list

# list pip installed packages
pip list

# check package version in conda
conda list pandas

# check package version in pip
pip show pandas | grep -i version


# Better use conda, and if you install packages in conda, they will be already assumed in pip


