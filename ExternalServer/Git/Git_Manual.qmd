---
title: "Banco de Portugal's Microdata Research Laboratory: Using Git"
author: "[BPLIM](https://bplim.bportugal.pt/)"
date: "April 1, 2023"
format:
  html:
    theme: cosmo
    embed-resources: true
    toc: true
    toc-location: left
    html-math-method: katex
    code-copy: true
    number-sections: true
bibliography: references.bib
csl: apa-6th-edition
output:
  html_document:
    citation_package: citeproc
---


## Using Git in the external server

Whenever a user wants to use Git on the external server, it is necessary to add their project to the internal GIT server. This procedure is carried out by DSI.

Please run the following test:

1.	Login to the external server


2. Config file

To use git, it is necessary to modify or create the .gitconfig file in your user's home directory. You can use KWrite to edit/create the file. The file should have the following format and should be created for each user who has access to GitLab. In this file, you can adapt the name and replace 'investa' with your own user.


  [cola]
  
          spellcheck = false
          
  [user]
  
          name = Investigador A
          
          email = investa@sxpe-bplim01.bplim.local
          
  [gui]
  
          editor = kwrite



2.	Authenticate by `ssh-key`. Open a `Terminal` in your home folder and type:

    - `ssh-keygen -t rsa -C “BPLIM git”`

    - `cat ~/.ssh/id_rsa.pub`

3.	Copy the resulting key to the clipboard

4.	Open Firefox and navigate to [https://vxpp-bplimgit.bplim.local/](https://vxpp-bplimgit.bplim.local/)

![](images/fig1.png)

> Confirm that you have a secure connection and use your credentials for the external server to login. 

5.	In your profile go to settings and on the left-side bar click in SSH Keys and paste the contents of the clipboard in the text box on the top right corner under "Key"

![](images/fig2.png)

![](images/fig3.png)

![](images/fig4.png)

> Give a title, e.g., "BPLIM git", and click in "Add key"


6. Go to `Projects` and create a `New project`, e.g., myfirst


![](images/fig5.png)


![](images/fig7.png)


7. Now you can clone the project


![](images/fig6.png)

Open a `Terminal` in your `work_area` and type

`git clone git@vxpp-bplimgit.bplim.local:investa/myfirst.git`


![](images/fig8.png)


You have now a new folder corresponding to your project

![](images/fig9.png)

9. You should now create a `.gitignore` file following the instructions available at [https://git-scm.com/docs/gitignore](https://git-scm.com/docs/gitignore)

8. You are now ready to work with Git on your project

You can find here a Git tutorial

[https://git-scm.com/docs/gittutorial](https://git-scm.com/docs/gittutorial)


