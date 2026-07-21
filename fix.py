import os

for r, d, files in os.walk('.'):
    if '.git' in r:
        continue
    for f in files:
        if f.endswith(('.html', '.mjs', '.css', '.js')):
            path = os.path.join(r, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # replace absolute path to relative path
            new_content = content.replace('"/assets/', '"./assets/')
            new_content = new_content.replace("'/assets/", "'./assets/")
            new_content = new_content.replace("url(/assets/", "url(./assets/")
            new_content = new_content.replace('href="/assets/', 'href="./assets/')
            new_content = new_content.replace('src="/assets/', 'src="./assets/')
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                print(f"Fixed {path}")
