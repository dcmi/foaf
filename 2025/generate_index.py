#!/usr/bin/env python3
"""
FOAF Project - Site Generator

This script generates the GitHub Pages site into the _site/ directory.
It runs as part of the GitHub Actions workflow on each push to main/master.

IMPORTANT: This script only writes to _site/ to avoid overwriting any
existing files in the repository.
"""

import os
import shutil
from datetime import datetime, timezone

# Output directory - isolated from repo source files
SITE_DIR = "_site"


def generate_index_html():
    """Generate the main index.html page for the FOAF project."""

    now = datetime.now(timezone.utc)
    build_timestamp = now.strftime("%Y-%m-%d %H:%M:%S UTC")

    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Friend of a Friend (FOAF) Project</title>
    <link rel="shortcut icon" href="favicon.ico" />
    <style>
        :root {{
            --bg-color: #ffffff;
            --text-color: #333333;
            --link-color: #0066cc;
            --accent-bg: #f5f5f5;
            --border-color: #cccccc;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
                         Helvetica, Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
        }}

        h1 {{
            color: var(--text-color);
            border-bottom: 2px solid var(--border-color);
            padding-bottom: 0.5rem;
        }}

        .intro {{
            font-size: 1.1rem;
            margin: 1.5rem 0;
        }}

        .foaf-image {{
            text-align: center;
            margin: 2rem 0;
        }}

        .foaf-image img {{
            max-width: 100%;
            height: auto;
        }}

        .quick-links {{
            background: var(--accent-bg);
            border: 1px dashed var(--border-color);
            padding: 1.5rem;
            margin: 1.5rem 0;
            border-radius: 4px;
        }}

        .quick-links h2 {{
            margin-top: 0;
            font-size: 1rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}

        .link-section {{
            margin: 1rem 0;
        }}

        .link-section strong {{
            display: inline-block;
            min-width: 100px;
        }}

        a {{
            color: var(--link-color);
            text-decoration: none;
        }}

        a:hover {{
            text-decoration: underline;
        }}

        footer {{
            margin-top: 3rem;
            padding-top: 1rem;
            border-top: 1px solid var(--border-color);
            font-size: 0.9rem;
            color: #666;
            text-align: center;
        }}

        .build-info {{
            font-size: 0.8rem;
            color: #999;
        }}
    </style>
</head>
<body>
    <h1>The FOAF Project</h1>

    <div class="intro">
        <p>
            The <em>Friend of a Friend</em> (FOAF) project is about creating a Web
            of machine-readable homepages describing people, the links between them,
            and the things they create and do.
        </p>
    </div>

    <div class="foaf-image">
        <img alt="FOAF - connecting people" src="images/foaflets.jpg" />
    </div>

    <div class="quick-links">
        <h2>Quick Start</h2>
        <div class="link-section">
            <a href="http://xmlns.com/foaf/0.1/">FOAF Vocabulary Spec</a> |
            <a href="https://github.com/danbri/foaf">GitHub Repository</a>
        </div>

        <h2>Historical Resources</h2>
        <div class="link-section">
            <a href="https://github.com/danbri/foaf/tree/master/foafproject">FOAF Project Files</a> |
            <a href="https://github.com/danbri/foaf/tree/master/rdfweb.org">RDFWeb Archive</a>
        </div>
    </div>

    <footer>
        <p>
            The FOAF Project - Semantic Web since 2000
        </p>
        <p class="build-info">
            Page generated: {build_timestamp}<br>
            <a href="https://github.com/danbri/foaf">View source on GitHub</a>
        </p>
    </footer>
</body>
</html>
'''

    return html_content


def main():
    """Main entry point for the script."""

    # Determine paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    site_dir = os.path.join(repo_root, SITE_DIR)

    print(f"Building site into: {site_dir}")

    # Clean and create _site directory
    if os.path.exists(site_dir):
        shutil.rmtree(site_dir)
    os.makedirs(site_dir)

    # Generate index.html
    index_path = os.path.join(site_dir, "index.html")
    html_content = generate_index_html()
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"Generated: index.html ({len(html_content)} bytes)")

    # Copy images directory
    src_images = os.path.join(repo_root, "foafproject", "htdocs", "images")
    dst_images = os.path.join(site_dir, "images")
    if os.path.exists(src_images):
        shutil.copytree(src_images, dst_images)
        print(f"Copied: images/")

    print(f"Site build complete!")


if __name__ == "__main__":
    main()
