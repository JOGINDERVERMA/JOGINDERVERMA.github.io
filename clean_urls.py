import os
import re

# 1. Update index.html links
with open('index.html', 'r') as f:
    index_content = f.read()
# Replace blog.html with /blog
index_content = index_content.replace('href="blog.html"', 'href="/blog"')
with open('index.html', 'w') as f:
    f.write(index_content)


# 2. Prepare blog/index.html
with open('blog.html', 'r') as f:
    blog_content = f.read()

# Fix links in blog_content
# CSS/JS/IMG
blog_content = blog_content.replace('href="css/', 'href="/css/')
blog_content = blog_content.replace('src="js/', 'src="/js/')
blog_content = blog_content.replace('src="img/', 'src="/img/')
# Fix navigation
blog_content = blog_content.replace('href="index.html', 'href="/')
blog_content = blog_content.replace('href="blog.html"', 'href="/blog"')

if not os.path.exists('blog'):
    os.makedirs('blog')
with open('blog/index.html', 'w') as f:
    f.write(blog_content)


# 3. Prepare post/index.html
with open('single-blog.html', 'r') as f:
    post_content = f.read()

post_content = post_content.replace('href="css/', 'href="/css/')
post_content = post_content.replace('src="js/', 'src="/js/')
post_content = post_content.replace('src="img/', 'src="/img/')
post_content = post_content.replace('href="index.html', 'href="/')
post_content = post_content.replace('href="blog.html"', 'href="/blog"')

if not os.path.exists('post'):
    os.makedirs('post')
with open('post/index.html', 'w') as f:
    f.write(post_content)


# 4. Update JS files to use new paths
with open('js/blog.js', 'r') as f:
    blog_js = f.read()
blog_js = blog_js.replace('href="single-blog.html?id=', 'href="/post?id=')
with open('js/blog.js', 'w') as f:
    f.write(blog_js)

with open('js/single-blog.js', 'r') as f:
    single_js = f.read()
single_js = single_js.replace('href="blog.html"', 'href="/blog"')
with open('js/single-blog.js', 'w') as f:
    f.write(single_js)

# 5. Remove old HTML files
os.remove('blog.html')
os.remove('single-blog.html')
