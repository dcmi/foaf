#!/usr/bin/env python3
"""
FOAF Project - Index Page Generator

This script generates the index.html for the FOAF project GitHub Pages site.
It runs as part of the GitHub Actions workflow on each push to main/master.
"""

import os
from datetime import datetime, timezone

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
        <img alt="FOAF - connecting people" src="foafproject/htdocs/images/foaflets.jpg" />
    </div>

    <div class="quick-links">
        <h2>Quick Start</h2>
        <div class="link-section">
            <a href="http://xmlns.com/foaf/0.1/">FOAF Vocabulary Spec</a> |
            <a href="foafproject/htdocs/index.html">Original FOAF Site</a> |
            <a href="https://github.com/danbri/foaf">GitHub Repository</a>
        </div>

        <h2>Historical Resources</h2>
        <div class="link-section">
            <strong>Sites:</strong>
            <a href="rdfweb.org/htdocs/index.html">RDFWeb</a> |
            <a href="foafnaut.org/index.html">FOAFnaut</a> |
            <a href="xmlns.com/index.html">xmlns.com</a>
        </div>

        <div class="link-section">
            <strong>Tools:</strong>
            <a href="foafproject/htdocs/foaf-a-matic/index.html">FOAF-a-matic</a>
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

    # Determine output directory (root of repo for GitHub Pages)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    output_path = os.path.join(repo_root, "index.html")

    print(f"Generating index.html...")
    print(f"Output path: {output_path}")

    html_content = generate_index_html()

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"Successfully generated index.html")
    print(f"File size: {len(html_content)} bytes")


if __name__ == "__main__":
    main()
