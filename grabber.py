import sys
lines = sys.stdin.readlines()
packages = {}
for line in lines:
    line = line.strip()[2:]
    package, file = line.split('/', 1)
    line = '''<li><a id="''' + line + '''" class="file" href="javascript:void(0)">''' + file.split('.html')[0] + '''</a></li>'''
    try:
        packages[package].append(line)
    except:
        packages[package] = [line]
# print packages
for package in packages:
    print '''<li class="dropdown"><a href="javascript:void(0)" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">''' + package + ''' <span class="caret"></span></a><ul class="dropdown-menu">'''
    for l in packages[package]:
        print l
    print '''</ul></li>'''