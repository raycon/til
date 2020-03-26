import os
from datetime import datetime

# Directory
root = os.getcwd()

# Exclude
excludes = (root, "drafts", "archive")

def relative(root, path):
    return '/'.join(path.replace(root, '').split(os.path.sep)[1:])

def tils(root):
    for (path, dirs, files) in os.walk(root):
        dirs[:] = [d for d in dirs if d not in excludes and not d.startswith(".")]
        paths = [os.path.join(path, f) for f in files if f.endswith(".md")]
        if path != root:
            yield relative(root, path), paths

def flat(tils):
    for (relative, paths) in tils:
        for path in paths:
            yield relative, path

def recent(tils, limit):
    modified = []
    for relative, filename in tils:
        date = os.path.getmtime(filename)
        modified.append((date, filename))
    modified.sort(key=lambda data: data[0], reverse=True)
    return modified[:limit]

def link(root, path):
    path = relative(root, path)
    directory = path.split('/')[-2]
    filename = path.split('/')[-1]
    filename = filename.replace(directory+"-", '', 1)
    title = ' '.join(n.capitalize() for n in os.path.splitext(filename)[0].split('-'))
    return f"[{title}]({path})"

def total(root):
    return len(list(flat(tils(root))))

def readme():
    lines = []
    lines.append("# TIL\n")
    lines.append("> Today I Learned\n")

    # Recents
    lines.append("## Recently Modified\n")
    for date, filename in recent(flat(tils(root)), 15):
        date = datetime.utcfromtimestamp(date).strftime("%Y-%m-%d")
        l = link(root, filename)
        lines.append(f"- *{date}* : {l}")

    # Categories
    lines.append("\n## Categories\n")
    lines.append("Total `%s` TILs\n" % total(root))
    for relative, paths in tils(root):
        count = len(paths)
        lines.append(f"- [{relative}](#{relative}) *({count})*")

    # Links
    for relative, paths in tils(root):
        lines.append(f"\n### {relative}\n")
        for path in paths:
            l = link(root, path)
            lines.append(f"- {l}")

    return lines

output = open(os.path.join(root, "README.md"), 'w')
for line in readme():
    output.write(line)
    output.write('\n')
output.close()
