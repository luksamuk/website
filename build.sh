#!/bin/sh
# Create project tree
echo "Creating project tree"
sh ./scripts/make_tree.sh

# Copy static assets
echo "Copying static assets"
sh ./scripts/copy_static.sh

# Export index and pages
echo "Exporting index"
sh ./scripts/export_index.sh

echo "Exporting pages"
sh ./scripts/export_pages.sh

# Export posts
echo "Exporting posts"
sh ./scripts/export_posts.sh

# Export talks
echo "Exporting presentations"
sh ./scripts/export_talks.sh
