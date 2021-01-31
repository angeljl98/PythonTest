// # You must automate a search bar for your browser software. If the user's input contains a dot "." then it's a www site and you redirect it to http://input
// # Else, redirect to ftp://input
// #
// # If the input already contains http://, ftp:// or https:// do not redirect to anything else.

// u=readline()
u="www.google.com"
print(u.match(/[a-z]+:\/\//)?u:u.match(/\./)?'http://'+u:'ftp://'+u)
